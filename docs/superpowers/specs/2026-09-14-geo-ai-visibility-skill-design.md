# GEO / AI Visibility Skill — Design Spec

Date: 2026-09-14
Status: approved by user, ready for implementation plan

## Purpose

Build a Claude Code skill (`skills/geo-ai-visibility/`) that turns the
existing research notes into a reusable knowledge base + practical audit
tool for Generative Engine Optimization (GEO) / AI Visibility — how to get
content cited/mentioned by ChatGPT, Perplexity, Google AI Overviews/AI
Mode, Copilot, Gemini and similar generative answer engines.

The skill has two jobs:
1. **Knowledge base** — answer questions about GEO frameworks, mental
   models, techniques, tooling, and data, at the depth of the existing
   `skills/ux-ui-expert` skill.
2. **Practical audit** — given a piece of content (article, landing page,
   product page) or a URL/file, score it against a GEO checklist and
   return prioritized, actionable recommendations.

## Source Material

Two research batches already exist under
`skills/geo-ai-visibility/research/` (12 files, `01`–`09` web research,
`12`–`14` video-transcript digest) and must NOT be deleted — they stay as
raw reference material. The skill's chapters synthesize this material into
consultable form; they don't replace it.

## File Structure

```
skills/geo-ai-visibility/
  SKILL.md              # frontmatter + core mental models (dense, ux-ui-expert style)
  chapters/
    01-definizioni-storia.md          # cos'è GEO, paper Princeton (arXiv:2311.09735), SEO vs GEO
    02-motori-generativi-tecnico.md   # RAG pipeline: ChatGPT Search, Perplexity, Google AIO/AI Mode, Copilot, Gemini
    03-fattori-ottimizzazione.md      # tecniche concrete (quotation addition, stats, structured data...) + llms.txt
    04-tooling-misurazione.md         # Profound, Peec AI, Otterly.AI, AthenaHQ, ecc.
    05-case-study-dati.md             # numeri/statistiche, concentrazione citazioni, zero-click data
    06-checklist-best-practice.md     # checklist consolidata + anti-pattern
    07-video-insights-consenso.md     # pattern di consenso cross-video + disaccordi/segnalazioni fonte-unica
  cheatsheet.md          # checklist azionabile rapida, in formato scorribile per audit
  glossary.md            # GEO, AEO, LLMO, RAG, PAWC, Subjective Impression, llms.txt, share of voice, ecc.
  patterns.md            # modalità "audit": procedura per leggere un contenuto e scorarlo

  research/              # (esistente, invariato) — raw material di riferimento
    01-09..., 12-14...
```

This mirrors `skills/ux-ui-expert`'s structure (SKILL.md + chapters/ +
cheatsheet.md + glossary.md + patterns.md) for consistency across the repo.

## SKILL.md Contents

Frontmatter:
- `name: geo-ai-visibility`
- `description`: keyword-rich trigger description (GEO, Generative Engine
  Optimization, AI Visibility, AEO, AI Overviews, ChatGPT Search,
  Perplexity, llms.txt, AI citations, share of voice) — long-form like
  ux-ui-expert's, listing what topics/tasks route here.
- `allowed-tools: [Read, Grep, WebFetch]` (WebFetch added vs ux-ui-expert's
  Read/Grep because audit mode may need to fetch a live URL to evaluate)
- `argument-hint: [topic, technique name, or "audit <url/file>"]`

Body: "How to Use This Skill" section (no-args = core framework; topic =
route to chapter; "audit X" = route to patterns.md audit procedure), then
"Core Frameworks & Mental Models" — dense bullets covering the highest-value
findings from research, written so common questions can be answered without
opening a chapter file. Content pulled from research notes, prioritized by
cross-source consensus (per file 14/07's consensus findings) and by
measured impact (per file 01's Princeton paper numbers).

Core mental models to include (non-exhaustive, refined during writing):
- GEO vs SEO shift (citations vs ranking, no click-through)
- Princeton paper technique impact table (Quotation Addition +41% PAWC,
  Statistics +33%, keyword stuffing −8%)
- Per-platform divergence (11% citation overlap ChatGPT↔Perplexity) →
  no single strategy fits all engines
- Answer-first / BLUF content structuring (most-repeated tactical pattern)
- Branded mentions (earned media) as the strongest single factor, above
  backlinks/DR
- SEO fundamentals as prerequisite (76% AI Overview citations come from
  top-10 Google results)
- llms.txt adoption status and what it does/doesn't do
- Citation concentration (top 1% domains capture ~47% of AI citations) —
  sets realistic expectations

## Chapters

Each chapter is a synthesized, denser rewrite of the corresponding
research notes (aggregating the 12 raw files into 7 topic chapters per the
approved mapping), written in the same bullet-dense, framework-naming style
as `ux-ui-expert/chapters/*`. Each chapter cites sources (URLs / paper IDs)
inline or in a closing "Fonti" section, carried over from the research
notes' source lists.

## cheatsheet.md

A scannable checklist an agent (or the user) can run through quickly:
grouped by category (content structure, structured data, citability,
authority signals, technical/llms.txt, platform-specific notes), each item
a single actionable line. This is the primary artifact used by the audit
mode in patterns.md.

## glossary.md

Terms: GEO, AEO, LLMO, RAG, PAWC (Position-Adjusted Word Count), Subjective
Impression, llms.txt, Share of Voice, Zero-click search, Answer Engine,
Entity-based content, Chunking, E-E-A-T, BLUF, and any other jargon
surfaced across the research notes. One or two sentences per term, no
essay entries — match ux-ui-expert/glossary.md's format.

## patterns.md — Audit Mode

Defines the procedure the skill follows when asked to "audit" a piece of
content:
1. Obtain the content — Read a local file, or WebFetch a URL if given one.
2. Run it against the cheatsheet.md checklist, category by category.
3. For each category: pass/partial/fail + one-line reason.
4. Output a prioritized list of fixes, ordered by expected impact (using
   the Princeton paper's measured technique impact where applicable, e.g.
   recommend adding quotations/stats before recommending lower-impact
   tweaks).
5. Keep the audit output structured (markdown table or grouped bullets) so
   it's easy to act on — no prose report.

No new tooling/scripts — this is a reasoning procedure the agent follows
using Read/Grep/WebFetch, not a script to write or maintain.

## Testing / Verification

Manual verification after writing (no automated test suite — this is a
knowledge-base skill, not code):
1. Invoke with no args → confirm core framework loads and reads coherently.
2. Ask a topic question (e.g. "cos'è GEO", "differenza SEO e GEO") →
   confirm it either answers from SKILL.md or correctly routes to a
   chapter.
3. Run "audit questo articolo" against a sample piece of text → confirm
   the audit procedure in patterns.md produces a structured, actionable
   scorecard using cheatsheet.md categories.
4. Spot-check that every fact/statistic carried into SKILL.md/chapters
   traces back to a source cited in the research notes (no invented
   numbers).

## Out of Scope

- No automated scraping/crawling tooling built as part of this skill.
- No integration with third-party AI-visibility measurement APIs
  (Profound, Peec AI, etc.) — they're documented as reference tools only,
  not wired up.
- research/ folder content is not rewritten or deleted, only read as
  source material.
