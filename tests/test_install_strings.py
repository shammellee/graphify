"""Regression tests for install-time instruction strings.

These strings live in graphify/__main__.py and are written into project-local
files (CLAUDE.md) or into in-process hook payloads. Earlier versions of
graphify told every assistant to "ALWAYS read graphify-out/GRAPH_REPORT.md
before answering" — which silently increased per-question token usage in
Claude Code sessions (issue #580). This file locks in the query-first policy.
"""
from __future__ import annotations
import json

from graphify.__main__ import (
    _SETTINGS_HOOK,
    _CLAUDE_MD_SECTION,
)

_INSTALL_TEXTS: dict[str, str] = {
    "_SETTINGS_HOOK": json.dumps(_SETTINGS_HOOK),
    "_CLAUDE_MD_SECTION": _CLAUDE_MD_SECTION,
}


def test_every_install_surface_recommends_graphify_query():
    """All install surfaces must point the assistant at `graphify query`
    as the first action for codebase questions (issue #580)."""
    missing: list[str] = []
    for name, text in _INSTALL_TEXTS.items():
        if "graphify query" not in text:
            missing.append(name)
    assert not missing, (
        f"these install surfaces no longer mention `graphify query`: {missing}. "
        f"If you removed it intentionally, consider whether issue #580 is back."
    )


def test_no_install_surface_demands_reading_the_full_report_first():
    """The pre-fix instructions told assistants to read GRAPH_REPORT.md as
    their first action. The new policy demotes the report to a fallback.
    """
    import re
    banned = [
        re.compile(r"read[^.\n]{0,80}GRAPH_REPORT\.md[^.\n]{0,80}before", re.IGNORECASE),
        re.compile(r"first\s+tool\s+call[^.\n]{0,80}GRAPH_REPORT", re.IGNORECASE),
        re.compile(r"always\s+read[^.\n]{0,80}GRAPH_REPORT", re.IGNORECASE),
    ]
    hits: list[tuple[str, str]] = []
    for name, text in _INSTALL_TEXTS.items():
        for pattern in banned:
            m = pattern.search(text)
            if m:
                hits.append((name, m.group(0)))
    assert not hits, (
        f"banned report-first phrasing reappeared: {hits}. "
        f"This regresses issue #580."
    )


def test_claude_md_section_references_report_as_fallback():
    """The fix demotes GRAPH_REPORT.md, it doesn't delete the reference."""
    assert "GRAPH_REPORT.md" in _CLAUDE_MD_SECTION, (
        "_CLAUDE_MD_SECTION no longer mentions GRAPH_REPORT.md. "
        "The fix should demote the report, not delete the reference."
    )


def test_how_it_works_clarifies_code_only_semantic_extraction():
    from pathlib import Path
    doc = (Path(__file__).parent.parent / "docs" / "how-it-works.md").read_text(encoding="utf-8")
    assert "Code files are not sent to the LLM semantic extractor" in doc
    assert "code files, Pass 3 is skipped entirely" in doc
    assert "docs, papers, images, and transcripts" in doc
