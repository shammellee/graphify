"""Tests for semantic-extraction backend selection and retry logic."""

from pathlib import Path
from unittest.mock import patch

import pytest

from graphify import llm


def _clear_backend_env(monkeypatch):
    for env_key in ("ANTHROPIC_API_KEY", "AWS_PROFILE", "AWS_REGION", "AWS_DEFAULT_REGION"):
        monkeypatch.delenv(env_key, raising=False)


def test_claude_backend_detected(monkeypatch):
    _clear_backend_env(monkeypatch)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    assert llm.detect_backend() == "claude"
    assert llm._get_backend_api_key("claude") == "test-key"


def test_bedrock_backend_detected_via_aws_region(monkeypatch):
    _clear_backend_env(monkeypatch)
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    assert llm.detect_backend() == "bedrock"


def test_bedrock_backend_detected_via_aws_profile(monkeypatch):
    _clear_backend_env(monkeypatch)
    monkeypatch.setenv("AWS_PROFILE", "my-profile")
    assert llm.detect_backend() == "bedrock"


def test_claude_beats_bedrock(monkeypatch):
    _clear_backend_env(monkeypatch)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    monkeypatch.setenv("AWS_REGION", "us-east-1")
    assert llm.detect_backend() == "claude"


def test_detect_backend_returns_none_when_no_credentials(monkeypatch):
    _clear_backend_env(monkeypatch)
    assert llm.detect_backend() is None


# ---------------------------------------------------------------------------
# Adaptive retry: context-window overflow recovery
# ---------------------------------------------------------------------------


def _ok(nodes=None, edges=None, model="m"):
    return {
        "nodes": nodes or [],
        "edges": edges or [],
        "hyperedges": [],
        "input_tokens": 1,
        "output_tokens": 1,
        "model": model,
        "finish_reason": "stop",
    }


def test_looks_like_context_exceeded_matches_common_messages():
    msgs = [
        "Error code: 400 - {'error': 'Context size has been exceeded.'}",
        "n_keep: 22374 >= n_ctx: 4096",
        "context_length_exceeded: This model's maximum context length is 8192 tokens",
        "exceeds the available context size",
        "The prompt is too long for this model.",
    ]
    for m in msgs:
        assert llm._looks_like_context_exceeded(RuntimeError(m)), m


def test_looks_like_context_exceeded_ignores_unrelated_errors():
    for m in ["timeout", "rate limit", "401 unauthorized", "connection refused"]:
        assert not llm._looks_like_context_exceeded(RuntimeError(m)), m


def test_adaptive_retry_splits_on_context_exceeded(tmp_path):
    files = [tmp_path / f"f{i}.md" for i in range(4)]
    for f in files:
        f.write_text("hello")

    calls = {"n": 0}

    def fake_extract(chunk, *_, **__):
        calls["n"] += 1
        if len(chunk) == 4:
            raise RuntimeError("Error 400: Context size has been exceeded.")
        return _ok(nodes=[{"id": f.stem} for f in chunk])

    with patch("graphify.llm.extract_files_direct", side_effect=fake_extract):
        result = llm._extract_with_adaptive_retry(
            files, backend="claude", api_key="k", model="m", root=tmp_path, max_depth=3
        )

    assert len(result["nodes"]) == 4
    assert calls["n"] == 3  # 1 failure + 2 halves


def test_adaptive_retry_gives_up_on_single_file_overflow(tmp_path):
    f = tmp_path / "huge.md"
    f.write_text("x")

    def fake_extract(*_, **__):
        raise RuntimeError("context_length_exceeded")

    with patch("graphify.llm.extract_files_direct", side_effect=fake_extract):
        result = llm._extract_with_adaptive_retry(
            [f], backend="claude", api_key="k", model="m", root=tmp_path, max_depth=3
        )

    assert result["nodes"] == []
    assert result["edges"] == []
    assert result["finish_reason"] == "stop"


def test_adaptive_retry_re_raises_unrelated_errors(tmp_path):
    f = tmp_path / "f.md"
    f.write_text("x")

    def fake_extract(*_, **__):
        raise RuntimeError("rate limit hit")

    with patch("graphify.llm.extract_files_direct", side_effect=fake_extract):
        with pytest.raises(RuntimeError, match="rate limit"):
            llm._extract_with_adaptive_retry(
                [f], backend="claude", api_key="k", model="m", root=tmp_path, max_depth=3
            )


# ---------------------------------------------------------------------------
# Hollow-response detection
# ---------------------------------------------------------------------------


def test_response_is_hollow_flags_empty_string():
    assert llm._response_is_hollow("", {"nodes": [], "edges": [], "hyperedges": []})


def test_response_is_hollow_flags_none_content():
    assert llm._response_is_hollow(None, {"nodes": [], "edges": [], "hyperedges": []})


def test_response_is_hollow_flags_whitespace_only():
    assert llm._response_is_hollow("   \n\t  ", {"nodes": [], "edges": [], "hyperedges": []})


def test_response_is_hollow_flags_parsed_but_no_nodes_or_edges():
    assert llm._response_is_hollow('{"sorry": "I cannot"}', {})
    assert llm._response_is_hollow("{}", {"nodes": [], "edges": [], "hyperedges": []})


def test_response_is_hollow_accepts_real_extraction():
    parsed = {"nodes": [{"id": "x"}], "edges": [], "hyperedges": []}
    assert not llm._response_is_hollow('{"nodes":[{"id":"x"}]}', parsed)
    parsed = {"nodes": [], "edges": [{"source": "a", "target": "b"}], "hyperedges": []}
    assert not llm._response_is_hollow('{"edges":[...]}', parsed)
