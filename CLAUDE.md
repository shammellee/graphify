# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development setup

```bash
git clone <your-fork-url>
cd graphify
git checkout main

mkvirtualenv graphify
pip install -e ".[all,dev]"
```

Verify:
```bash
graphify --version
```

## Commands

```bash
# Tests
pytest tests/ -q                       # full suite
pytest tests/test_extract.py -q        # single module
pytest tests/ -q -k "python"           # filter by name

# Lint / type check
ruff check graphify tests
pyright

# Security audit
bandit -r graphify
```

> macOS note: `tests/fixtures/` includes both `sample.f90` and `sample.F90`. These collide on HFS+/APFS. Run on Linux or in Docker to test both Fortran fixtures simultaneously.

## Architecture

The pipeline is a linear chain of pure functions, each in its own module:

```
detect() → extract() → build_graph() → cluster() → analyze() → report() → export()
```

Each stage communicates through plain Python dicts and `nx.Graph` objects. There is **no shared state** and no side effects outside `graphify-out/`.

| Module | Key function | Role |
|--------|-------------|------|
| `detect.py` | `collect_files(root)` | File discovery and filtering |
| `extract.py` | `extract(path)` | AST (tree-sitter) + semantic → `{nodes, edges}` dict |
| `build.py` | `build_graph(extractions)` | Merges extraction dicts into `nx.Graph` |
| `cluster.py` | `cluster(G)` | Community detection (Leiden / fallback) |
| `analyze.py` | `analyze(G)` | God nodes, surprises, suggested questions |
| `report.py` | `render_report(G, analysis)` | Writes `GRAPH_REPORT.md` |
| `export.py` | `export(G, out_dir, ...)` | Obsidian vault, `graph.json`, `graph.html`, SVG |
| `validate.py` | `validate_extraction(data)` | Enforces extraction schema before `build_graph()` |
| `security.py` | validation helpers | All external input passes through here first |
| `cache.py` | `check_semantic_cache` | Splits files into cached vs. uncached before LLM calls |
| `serve.py` | `start_server(graph_path)` | MCP stdio server over `graph.json` |
| `ingest.py` | `ingest(url, ...)` | Fetches URLs (papers, videos) into the corpus |
| `llm.py` | LLM backend dispatch | Routes to Claude / Gemini / OpenAI / Ollama / Bedrock |
| `prs.py` | PR dashboard | GitHub PR state + graph impact |
| `watch.py` | `watch(root, flag_path)` | File watcher for `--watch` mode |

## Extraction output schema

Every extractor must return this shape (enforced by `validate.py`):

```json
{
  "nodes": [{"id": "unique_string", "label": "human name", "source_file": "path", "source_location": "L42"}],
  "edges": [{"source": "id_a", "target": "id_b", "relation": "calls|imports|uses|...", "confidence": "EXTRACTED|INFERRED|AMBIGUOUS"}]
}
```

## Adding a language extractor

1. Add `extract_<lang>(path: Path) -> dict` in `extract.py` (tree-sitter parse → walk nodes → collect nodes/edges → call-graph second pass for INFERRED `calls` edges).
2. Register the suffix in `extract()` dispatch and `collect_files()` in `detect.py`.
3. Add the suffix to `_WATCHED_EXTENSIONS` in `watch.py`.
4. Add the tree-sitter package to `pyproject.toml` dependencies.
5. Add a fixture file to `tests/fixtures/` and tests to `tests/test_languages.py`.

## Security invariants

All external input goes through `graphify/security.py`:
- URLs → `validate_url()` (http/https only) + `_NoFileRedirectHandler` (blocks `file://` redirects)
- Fetched content → `safe_fetch()` (size cap, timeout)
- Graph paths → `validate_graph_path()` (must resolve inside `graphify-out/`)
- Node labels → `sanitize_label()` (strips control chars, caps 256 chars, HTML-escapes)

Never bypass these validators for untrusted input.

## Git workflow

- Active development branch: `main`
- Commit style: `fix: …` / `feat: …` / `docs: …`
- Run `pytest tests/ -q` before opening a PR.

## Knowledge graph (AGENTS.md rules)

This repo has a graphify knowledge graph at `graphify-out/`.
- Before answering architecture questions, read `graphify-out/GRAPH_REPORT.md` for god nodes and community structure.
- If `graphify-out/wiki/index.md` exists, navigate it instead of reading raw files.
- After modifying code files, run `graphify update .` to keep the graph current (AST-only, no API cost).
