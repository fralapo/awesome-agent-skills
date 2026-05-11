---
name: llm-wiki
description: Use when user wants to build/maintain a personal knowledge base in Obsidian using the LLM Wiki pattern (Karpathy). Triggers on "llm wiki", "/llm-wiki", "init wiki", "ingest sources", "inizializza wiki", or when working in a directory containing an Obsidian vault (.obsidian/ folder) and user references knowledge-base work.
---

# LLM Wiki Skill

Pattern by Andrej Karpathy. Build personal knowledge base where LLM maintains an interlinked markdown wiki sitting between user and raw sources. Knowledge compiled once, kept current, not re-derived per query.

## Core idea

Unlike RAG (rediscovers per query, no accumulation), LLM Wiki:
- Reads new source → integrates into existing wiki
- Updates entity pages, revises summaries, flags contradictions
- Cross-references already there. Synthesis reflects everything read
- User curates sources + asks questions. LLM does bookkeeping

Obsidian = IDE. LLM = programmer. Wiki = codebase.

## Three layers

1. **`raw/`** — immutable source documents (PDF, MD, articles, images, data). Read-only for LLM
2. **`wiki/`** — LLM-owned markdown. Entity pages, concept pages, summaries, syntheses. LLM creates/updates
3. **`CLAUDE.md`** (or `AGENTS.md`) — schema. Conventions, workflows, ingest/query/lint rules. Co-evolves with user

## Operations

### Ingest
User drops source in `raw/`. LLM:
1. Reads source
2. Discusses key takeaways with user
3. Writes summary page in `wiki/sources/`
4. Updates `index.md`
5. Updates relevant entity/concept pages (touches 10-15 pages typical)
6. Appends entry to `log.md`

Default: one-at-a-time, supervised. Batch mode optional.

### Query
1. Read `index.md` first to find candidate pages
2. Drill into relevant wiki pages, follow `[[backlinks]]`
3. Synthesize answer with citations to source pages
4. Offer to save substantive answers as `wiki/synthesis/` page (compounds knowledge)

Output formats: markdown page, comparison table, Marp slide deck, matplotlib chart, canvas.

### Lint (health check)
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages (no inbound links)
- Concepts mentioned but lacking dedicated page
- Missing cross-references
- Data gaps fillable via web search

## Directory convention

```
vault/
├── CLAUDE.md              # schema (this skill seeds it)
├── raw/                   # immutable sources
│   ├── assets/            # downloaded images
│   └── *.md, *.pdf, ...
├── wiki/
│   ├── index.md           # content catalog
│   ├── log.md             # chronological append-only
│   ├── concepts/
│   ├── entities/
│   ├── sources/           # one summary per ingested source
│   └── synthesis/         # saved query answers
└── presentations/         # Marp slide decks
```

## Special files

### `index.md`
Content catalog. Each page = link + 1-line summary + optional frontmatter (date, source count). Organized by category. Updated every ingest. Read FIRST on every query.

### `log.md`
Append-only chronological. Consistent prefix for grep:
```
## [2026-05-11] ingest | Article Title
## [2026-05-11] query | "best diet for brain"
## [2026-05-11] lint | found 3 orphans, 1 contradiction
```

## Wikilinks
Use `[[Page Name]]` syntax. Obsidian renders graph from these. Always link entity/concept mentions to dedicated pages — orphans get caught by lint.

## Initialization workflow (user says "init wiki" or `/llm-wiki`)

1. Ask domain/purpose (research, personal, team, hobby, etc.)
2. Confirm vault path. If no `.obsidian/` present, instruct user to create Obsidian vault first
3. Create `CLAUDE.md` in vault root with:
   - Domain purpose statement
   - Folder conventions (this skill's structure, customizable)
   - Ingest/query/lint workflow rules
   - Citation format
   - Page templates (entity, concept, source, synthesis)
4. Create `raw/`, `wiki/{concepts,entities,sources,synthesis}/`, `presentations/`
5. Create empty `wiki/index.md` and `wiki/log.md` with header
6. Log init in `log.md`
7. Tell user: drop sources in `raw/`, then say "ingest"

## Tips

- **Obsidian Web Clipper** extension → web→MD into `raw/`
- Image download hotkey in Obsidian: Settings→Hotkeys→"Download attachments for current file" → Ctrl+Shift+D. Set attachment folder to `raw/assets/`
- Wiki is just git repo of MD → version it
- Marp plugin in Obsidian for slide output
- Dataview plugin for dynamic tables from frontmatter

## Anti-patterns

- Don't bypass `raw/` immutability. Never edit source files
- Don't write wiki pages without backlinks — every page must connect
- Don't batch-ingest 50 sources blind. Stay in the loop
- Don't ignore `log.md` — it's how next session knows what happened
- Don't re-derive on each query — read existing wiki first

## When to suggest using this skill

- User mentions Obsidian + knowledge base / wiki / notes accumulation
- User has `.obsidian/` folder in cwd
- User asks about RAG alternatives for personal knowledge
- User wants to track research/reading over time

## When NOT to use

- One-shot summarization (no accumulation value)
- Pure code work in repo (use AGENTS.md/CLAUDE.md normally)
- User explicitly wants RAG with embeddings (different tool)
