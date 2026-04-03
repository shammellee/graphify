"""Installer-level regression tests for upgrade-in-place behavior (issue #580).

Pre-fix, the installer wrote a "## graphify" section with report-first
instructions and skipped writing if the marker was already present. So users
who installed graphify and then upgraded to the fixed package still had the
old report-first text on disk — the bug stayed live for them.

These tests seed the Claude instruction files with the old report-first
section, run the installer, and assert that the on-disk file now contains
the new query-first wording.
"""
from __future__ import annotations
import json

import graphify.__main__ as mainmod


_OLD_CLAUDE_SECTION = """\
## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- ALWAYS read graphify-out/GRAPH_REPORT.md before reading any source files, running grep/glob searches, or answering codebase questions. The graph is your primary map of the codebase.
- IF graphify-out/wiki/index.md EXISTS, navigate it instead of reading raw files
- For cross-module "how does X relate to Y" questions, prefer `graphify query "<question>"`, `graphify path "<A>" "<B>"`, or `graphify explain "<concept>"` over grep — these traverse the graph's EXTRACTED + INFERRED edges instead of scanning files
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
"""

_OLD_HOOK_PAYLOAD_SNIPPET = "Read graphify-out/GRAPH_REPORT.md for god nodes and community structure before searching raw files"


def _assert_no_report_first(text: str, ctx: str) -> None:
    assert "ALWAYS read graphify-out/GRAPH_REPORT.md" not in text, (
        f"{ctx}: old 'ALWAYS read' phrasing survived upgrade"
    )


def _assert_query_first(text: str, ctx: str) -> None:
    assert "graphify query" in text, (
        f"{ctx}: new 'graphify query' guidance missing after upgrade"
    )


def test_claude_install_upgrades_stale_section(tmp_path, monkeypatch):
    """A pre-fix CLAUDE.md gets the new section in place when the user runs
    `graphify claude install` again after upgrading to a fixed package."""
    monkeypatch.chdir(tmp_path)
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text("# My Project\n\nSome description.\n\n" + _OLD_CLAUDE_SECTION, encoding="utf-8")
    monkeypatch.setattr(mainmod, "_check_skill_version", lambda _: None)

    mainmod.claude_install(tmp_path)

    after = claude_md.read_text(encoding="utf-8")
    _assert_no_report_first(after, "CLAUDE.md")
    _assert_query_first(after, "CLAUDE.md")
    assert "# My Project" in after
    assert "Some description." in after


def test_claude_install_upgrades_stale_hook_payload(tmp_path, monkeypatch):
    """The Claude install must also rewrite a stale .claude/settings.json hook
    payload on upgrade."""
    monkeypatch.chdir(tmp_path)
    claude_md = tmp_path / "CLAUDE.md"
    claude_md.write_text(_OLD_CLAUDE_SECTION, encoding="utf-8")
    settings = tmp_path / ".claude" / "settings.json"
    settings.parent.mkdir(parents=True, exist_ok=True)
    stale_settings = {
        "hooks": {
            "PreToolUse": [
                {
                    "matcher": "Bash",
                    "hooks": [
                        {
                            "type": "command",
                            "command": (
                                "case x in *) "
                                + _OLD_HOOK_PAYLOAD_SNIPPET
                                + " esac"
                            ),
                        }
                    ],
                }
            ]
        }
    }
    settings.write_text(json.dumps(stale_settings), encoding="utf-8")
    monkeypatch.setattr(mainmod, "_check_skill_version", lambda _: None)

    mainmod.claude_install(tmp_path)

    new_settings_text = settings.read_text(encoding="utf-8")
    assert _OLD_HOOK_PAYLOAD_SNIPPET not in new_settings_text, (
        "stale hook payload survived upgrade"
    )
    assert "graphify query" in new_settings_text, (
        "new hook payload should route to `graphify query`"
    )
