# GEO / AI Visibility Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `skills/geo-ai-visibility/` — a knowledge-base + audit skill for Generative Engine Optimization (GEO) / AI Visibility, matching the structure and depth of `skills/ux-ui-expert/`.

**Architecture:** SKILL.md carries a dense core-frameworks section usable without opening anything else. Seven `chapters/*.md` files synthesize the 12 existing research files (`skills/geo-ai-visibility/research/01-09,12-14`) into topic-organized reference material. `cheatsheet.md` is a flat actionable checklist. `glossary.md` defines jargon. `patterns.md` defines the audit procedure that consumes `cheatsheet.md`.

**Tech Stack:** Plain Markdown files, no code, no build step. Content-authoring task — "tests" are read-back verification steps, not automated tests.

**Spec:** `docs/superpowers/specs/2026-09-14-geo-ai-visibility-skill-design.md`

## Global Constraints

- Do not delete, rename, or edit any file under `skills/geo-ai-visibility/research/` — it is read-only source material for this plan.
- Every statistic/number/named tool/paper carried into a new file must trace back to a specific research file (cite it, e.g. "(fonte: research/01-definizioni-storia.md)" or an inline URL already present in that research file). Never invent a number.
- Match `skills/ux-ui-expert/` formatting conventions: frontmatter block (`name`, `description`, `allowed-tools`, `argument-hint`), bullet-dense prose, **bolded framework names** at the start of each bullet/paragraph.
- `SKILL.md` frontmatter `allowed-tools` must be `[Read, Grep, WebFetch]`.
- Language: Italian or English, matching whichever the source research file used (don't force-translate).
- Every new file ends with the repo's existing convention: no trailing "signature" boilerplate, just content.

---

## Task 1: Chapters 01–02 (definitions/history + technical engine mechanics)

**Files:**
- Create: `skills/geo-ai-visibility/chapters/01-definizioni-storia.md`
- Create: `skills/geo-ai-visibility/chapters/02-motori-generativi-tecnico.md`
- Read (source, do not modify): `skills/geo-ai-visibility/research/01-definizioni-storia.md`, `skills/geo-ai-visibility/research/02-seo-vs-geo.md`, `skills/geo-ai-visibility/research/03-motori-generativi-tecnico.md`

**Interfaces:**
- Produces: two chapter files other tasks link to from `SKILL.md`'s "How to Use This Skill" routing table (exact filenames above — later tasks and Task 8's SKILL.md must reference these paths verbatim).

- [ ] **Step 1: Read source research files**

Read `skills/geo-ai-visibility/research/01-definizioni-storia.md` and `skills/geo-ai-visibility/research/02-seo-vs-geo.md` in full.

- [ ] **Step 2: Write `chapters/01-definizioni-storia.md`**

Content outline (merge the two source files into one chapter):
- Section "Cos'è il GEO": definition, origin of the term, relationship to SEO/AEO/LLMO (cross-reference `glossary.md` — file created in Task 6 — for exact term boundaries, but don't wait on it; just note "(vedi glossary.md)").
- Section "Il paper fondativo": the Princeton/Georgia Tech/Allen Institute/IIT Delhi paper (arXiv:2311.09735, Nov 2023) — methodology, the two metrics (Position-Adjusted Word Count, Subjective Impression), and a table of the ~9 tested techniques with their measured % impact, pulled verbatim from `research/01-definizioni-storia.md`.
- Section "GEO vs SEO tradizionale": pull the concrete contrasts from `research/02-seo-vs-geo.md` (conversational queries vs keyword queries, citation vs ranking, no click-through, multi-source answers vs single ranked result).
- Closing "Fonti" section listing every URL/paper-ID cited, copied from the source files' own source lists.

Match `ux-ui-expert/chapters/*` style: bolded framework name leading each paragraph, dense bullets, no filler.

- [ ] **Step 3: Read source research file for chapter 02**

Read `skills/geo-ai-visibility/research/03-motori-generativi-tecnico.md` in full.

- [ ] **Step 4: Write `chapters/02-motori-generativi-tecnico.md`**

Content outline:
- One subsection per engine covered in the source file (ChatGPT Search, Perplexity, Google AI Overviews/AI Mode, Copilot, Gemini) — for each: how it retrieves (RAG pipeline steps), how it ranks/selects sources, how it decides what to cite/link.
- Section "Divergenza tra piattaforme": the cross-platform citation-overlap finding (11% ChatGPT↔Perplexity overlap, from the research notes) and what it implies for strategy (no single-platform optimization suffices).
- Closing "Fonti" section with URLs from the source file.

- [ ] **Step 5: Verify facts trace to sources**

Re-open both new chapter files and both source research files side by side. For every number/statistic/named tool in the new chapters, confirm it appears in the corresponding research file. Fix any unsourced claim by either sourcing it or removing it.

- [ ] **Step 6: Commit**

```bash
git add skills/geo-ai-visibility/chapters/01-definizioni-storia.md skills/geo-ai-visibility/chapters/02-motori-generativi-tecnico.md
git commit -m "Add GEO skill chapters 01-02 (definitions/history, engine mechanics)"
```

---

## Task 2: Chapters 03–04 (optimization factors + tooling)

**Files:**
- Create: `skills/geo-ai-visibility/chapters/03-fattori-ottimizzazione.md`
- Create: `skills/geo-ai-visibility/chapters/04-tooling-misurazione.md`
- Read (source, do not modify): `skills/geo-ai-visibility/research/04-fattori-ottimizzazione.md`, `skills/geo-ai-visibility/research/05-llms-txt-standard.md`, `skills/geo-ai-visibility/research/06-tooling-misurazione.md`

**Interfaces:**
- Produces: two chapter files (exact filenames above) referenced by `SKILL.md` in Task 8.

- [ ] **Step 1: Read source research files**

Read `skills/geo-ai-visibility/research/04-fattori-ottimizzazione.md` and `skills/geo-ai-visibility/research/05-llms-txt-standard.md` in full.

- [ ] **Step 2: Write `chapters/03-fattori-ottimizzazione.md`**

Content outline (merge the two source files):
- Section "Tecniche di contenuto citabile": quotation addition, statistics addition, structured Q&A/FAQ format, entity-based content, semantic chunking, freshness — each with its measured impact number from the research file where available.
- Section "Autorevolezza e brand mentions": E-E-A-T signals, branded mentions (even unlinked) and their measured weight in AI answers.
- Section "Structured data / schema.org": which schema types matter and why.
- Section "llms.txt e standard emergenti": what llms.txt is, adoption numbers (844k+ sites, named adopters like Stripe/Cloudflare/Anthropic), Chrome Lighthouse integration, and its actual limits (it's a convention, not a guarantee of citation).
- Closing "Fonti" section.

- [ ] **Step 3: Read source research file for chapter 04**

Read `skills/geo-ai-visibility/research/06-tooling-misurazione.md` in full.

- [ ] **Step 4: Write `chapters/04-tooling-misurazione.md`**

Content outline: one subsection per tool named in the source (Profound, Peec AI, Otterly.AI, AthenaHQ, and any others present) — what it measures (share of voice, citation tracking, prompt monitoring), how it works at a high level, pricing/positioning notes if present in the source. Close with a short "Come si sceglie" comparison paragraph (only if the source material supports one — don't invent a recommendation not grounded in the notes). Closing "Fonti" section.

- [ ] **Step 5: Verify facts trace to sources**

Cross-check every named tool, adoption number, and technique-impact percentage in both new files against the two source files. Fix unsourced claims.

- [ ] **Step 6: Commit**

```bash
git add skills/geo-ai-visibility/chapters/03-fattori-ottimizzazione.md skills/geo-ai-visibility/chapters/04-tooling-misurazione.md
git commit -m "Add GEO skill chapters 03-04 (optimization factors, tooling)"
```

---

## Task 3: Chapters 05–07 (case studies, checklist, video insights)

**Files:**
- Create: `skills/geo-ai-visibility/chapters/05-case-study-dati.md`
- Create: `skills/geo-ai-visibility/chapters/06-checklist-best-practice.md`
- Create: `skills/geo-ai-visibility/chapters/07-video-insights-consenso.md`
- Read (source, do not modify): `skills/geo-ai-visibility/research/07-case-study-dati.md`, `skills/geo-ai-visibility/research/08-checklist-best-practice.md`, `skills/geo-ai-visibility/research/12-video-transcripts-digest.md`, `skills/geo-ai-visibility/research/13-video-quotes-tecniche.md`, `skills/geo-ai-visibility/research/14-video-disaccordi-pattern-comuni.md`

**Interfaces:**
- Produces: three chapter files (exact filenames above) referenced by `SKILL.md` in Task 8.

- [ ] **Step 1: Read source research file**

Read `skills/geo-ai-visibility/research/07-case-study-dati.md` in full.

- [ ] **Step 2: Write `chapters/05-case-study-dati.md`**

Content outline:
- Section "Zero-click e volumi": traffic/query statistics from the source (zero-click search growth, AI search adoption numbers).
- Section "Concentrazione delle citazioni": the top-1%-domains-capture-~47%-of-citations finding, and any other concentration/distribution data in the source.
- Section "Casi studio nominati": any named company/site case studies present in the source, with their reported outcome and method.
- Closing "Fonti" section.

- [ ] **Step 3: Read source research file**

Read `skills/geo-ai-visibility/research/08-checklist-best-practice.md` in full.

- [ ] **Step 4: Write `chapters/06-checklist-best-practice.md`**

Content outline:
- Section "Checklist consolidata": the best-practice checklist items from the source, grouped by category (content, structure, technical, authority) — this becomes the narrative version; `cheatsheet.md` (Task 4) will be the terse scored-checklist version of the same items, so keep category names consistent between the two.
- Section "Anti-pattern": every anti-pattern/mistake named in the source, each with a one-line "why it fails" explanation pulled from the source.
- Closing "Fonti" section.

- [ ] **Step 5: Read source research files**

Read `skills/geo-ai-visibility/research/12-video-transcripts-digest.md`, `skills/geo-ai-visibility/research/13-video-quotes-tecniche.md`, and `skills/geo-ai-visibility/research/14-video-disaccordi-pattern-comuni.md` in full.

- [ ] **Step 6: Write `chapters/07-video-insights-consenso.md`**

Content outline (merge the three video-digest files into one synthesized chapter — don't just concatenate them):
- Section "Consenso cross-fonte": the patterns that recur across most/all of the 9 videos (per file 14) — e.g. SEO-as-prerequisite, branded mentions as top factor, YouTube's outsized correlation with ChatGPT visibility, answer-first/BLUF structuring as the most-repeated tactical pattern. Flag which of these numbers trace back to a single primary source (e.g. Ahrefs) reused across multiple videos, per file 14's warning — don't present those as independently-confirmed.
- Section "Divergenze": where videos disagree or use inconsistent terminology (e.g. GEO/AEO/LLMO treated as synonyms in most videos vs. distinguished in one).
- Section "Tecniche citate testualmente": 5-8 of the most concrete, actionable quotes/techniques pulled from file 13, attributed to their source video title.
- Closing "Fonti" section listing the 9 source video titles (no URLs needed if the research files didn't capture them — check file 09/`research/09-fonti.md` for any video URLs already logged, and include them if present).

- [ ] **Step 7: Verify facts trace to sources**

Cross-check every statistic and named case study in all three new chapters against their five source files. Fix unsourced claims.

- [ ] **Step 8: Commit**

```bash
git add skills/geo-ai-visibility/chapters/05-case-study-dati.md skills/geo-ai-visibility/chapters/06-checklist-best-practice.md skills/geo-ai-visibility/chapters/07-video-insights-consenso.md
git commit -m "Add GEO skill chapters 05-07 (case studies, checklist, video insights)"
```

---

## Task 4: cheatsheet.md

**Files:**
- Create: `skills/geo-ai-visibility/cheatsheet.md`
- Read: `skills/geo-ai-visibility/chapters/06-checklist-best-practice.md` (from Task 3), `skills/geo-ai-visibility/research/08-checklist-best-practice.md`

**Interfaces:**
- Consumes: category names established in `chapters/06-checklist-best-practice.md` (Task 3, Step 4) — reuse the same category names here so `patterns.md`'s audit procedure (Task 5) can map cheatsheet categories to chapter detail without a translation table.
- Produces: `cheatsheet.md` with named categories (exact names used by Task 5's audit procedure — pick them now and keep them stable): `Struttura contenuto`, `Structured data`, `Citabilità`, `Segnali di autorità`, `Tecnico / llms.txt`, `Note per piattaforma`.

- [ ] **Step 1: Read Task 3's checklist chapter and the source checklist research file**

Read `skills/geo-ai-visibility/chapters/06-checklist-best-practice.md` and `skills/geo-ai-visibility/research/08-checklist-best-practice.md`.

- [ ] **Step 2: Write `cheatsheet.md`**

Format: one `##` heading per category (the six listed in Interfaces above), each with a flat bullet list of single-line, checkable items (e.g. "- [ ] Risposta diretta nelle prime 2 frasi (answer-first/BLUF)"). Pull every item from the checklist chapter/research file — don't invent new checklist items not grounded in the research. Keep each line short enough to score in isolation (this file is read by the audit procedure in Task 5, one line at a time).

Example structure:
```markdown
# GEO Cheatsheet

## Struttura contenuto
- [ ] Risposta diretta nelle prime 1-2 frasi (answer-first / BLUF)
- [ ] Formato Q&A/FAQ dove pertinente
...

## Structured data
- [ ] Schema.org markup presente e valido per il tipo di contenuto
...
```

- [ ] **Step 3: Verify every item traces to source**

Check each cheatsheet line against `chapters/06-checklist-best-practice.md`/`research/08-checklist-best-practice.md` — no invented items.

- [ ] **Step 4: Commit**

```bash
git add skills/geo-ai-visibility/cheatsheet.md
git commit -m "Add GEO skill cheatsheet"
```

---

## Task 5: patterns.md (audit mode procedure)

**Files:**
- Create: `skills/geo-ai-visibility/patterns.md`
- Read: `skills/geo-ai-visibility/cheatsheet.md` (from Task 4), `skills/geo-ai-visibility/chapters/01-definizioni-storia.md` (for the Princeton impact-ranking table, Task 1)

**Interfaces:**
- Consumes: `cheatsheet.md`'s six category names (Task 4) and the Princeton paper's technique-impact numbers (Task 1's `chapters/01-definizioni-storia.md`) for the impact-based prioritization step.
- Produces: a documented audit procedure that `SKILL.md` (Task 8) links to when the user asks to "audit" content.

- [ ] **Step 1: Read `cheatsheet.md` and `chapters/01-definizioni-storia.md`**

- [ ] **Step 2: Write `patterns.md`**

Content — the audit procedure, written as instructions the agent follows (not a script):

```markdown
# Audit Pattern: Scoring Content Against GEO Cheatsheet

Use this procedure when asked to "audit" a piece of content for AI
visibility — a local file, pasted text, or a URL.

## Procedure

1. **Obtain the content.** If given a local file path, Read it. If given
   a URL, WebFetch it. If given pasted text, use it directly.
2. **Score category by category**, using the six categories in
   `cheatsheet.md` (Struttura contenuto, Structured data, Citabilità,
   Segnali di autorità, Tecnico / llms.txt, Note per piattaforma). For
   each category, go item by item and mark: ✅ pass / ⚠️ partial / ❌ fail,
   with a one-line reason citing what's present or missing in the content.
3. **Prioritize fixes by measured impact.** When multiple ❌/⚠️ items
   compete for attention, rank fixes using the Princeton paper's technique
   impact table from `chapters/01-definizioni-storia.md` (e.g. adding
   quotations/statistics ranks above lower-impact structural tweaks,
   keyword stuffing is never recommended — it measured negative).
4. **Output format** — a markdown table, one row per checklist item:

   | Categoria | Item | Esito | Motivo |
   |---|---|---|---|
   | Struttura contenuto | Answer-first nelle prime righe | ❌ | Il pezzo apre con storia aziendale, risposta diretta arriva al paragrafo 4 |

   Followed by a short "Prioritized fixes" numbered list (3-7 items,
   highest-impact first, each one actionable sentence — no prose report,
   no restating the whole table).
5. **Stay grounded.** Don't invent findings not visible in the content;
   don't cite statistics not already documented in this skill's chapters.
```

- [ ] **Step 3: Commit**

```bash
git add skills/geo-ai-visibility/patterns.md
git commit -m "Add GEO skill audit pattern"
```

---

## Task 6: glossary.md

**Files:**
- Create: `skills/geo-ai-visibility/glossary.md`
- Read: all of `skills/geo-ai-visibility/chapters/*.md` (Tasks 1-3) and `skills/geo-ai-visibility/research/*.md`

**Interfaces:**
- Produces: `glossary.md`, referenced from `SKILL.md` (Task 8).

- [ ] **Step 1: Scan all chapter and research files for jargon**

Read through all 7 chapter files and the 12 research files, noting every acronym/term of art used without being defined inline: GEO, AEO, LLMO, RAG, PAWC (Position-Adjusted Word Count), Subjective Impression, llms.txt, Share of Voice, Zero-click search, Answer Engine, Entity-based content, Chunking, E-E-A-T, BLUF, and any others actually present in the material (don't add terms absent from the source content).

- [ ] **Step 2: Write `glossary.md`**

Format matches `skills/ux-ui-expert/glossary.md`: one entry per term, bolded term followed by a 1-2 sentence definition, alphabetically or logically grouped, no essay-length entries.

- [ ] **Step 3: Commit**

```bash
git add skills/geo-ai-visibility/glossary.md
git commit -m "Add GEO skill glossary"
```

---

## Task 7: Verify ux-ui-expert format match

**Files:**
- Read: `skills/ux-ui-expert/SKILL.md`, `skills/ux-ui-expert/glossary.md`, `skills/ux-ui-expert/cheatsheet.md`, `skills/ux-ui-expert/patterns.md`
- Read: all `skills/geo-ai-visibility/*.md` and `skills/geo-ai-visibility/chapters/*.md` files written in Tasks 1-6

**Interfaces:**
- Consumes: every file produced in Tasks 1-6.
- Produces: no new files — this is a consistency-check task that may edit existing new files in place if it finds mismatches.

- [ ] **Step 1: Compare frontmatter and section conventions**

Open `skills/ux-ui-expert/SKILL.md` and each `skills/geo-ai-visibility/chapters/*.md`, `cheatsheet.md`, `glossary.md`, `patterns.md` written so far. Confirm: bolded-framework-name-leads-bullet convention is followed consistently, section heading levels match (`#`/`##`), and no file drifted into a different tone/format.

- [ ] **Step 2: Fix any drift found**

Edit any file that doesn't match the established convention. If everything matches, note "no changes needed" and move on — don't force edits for their own sake.

- [ ] **Step 3: Commit (only if changes were made)**

```bash
git add skills/geo-ai-visibility/
git commit -m "Align GEO skill files with ux-ui-expert formatting conventions"
```

---

## Task 8: SKILL.md (core frameworks + routing)

**Files:**
- Create: `skills/geo-ai-visibility/SKILL.md`
- Read: `skills/ux-ui-expert/SKILL.md` (frontmatter/structure reference), all `skills/geo-ai-visibility/chapters/*.md`, `cheatsheet.md`, `glossary.md`, `patterns.md` (Tasks 1-7)

**Interfaces:**
- Consumes: the 7 chapter filenames (Tasks 1-3), `cheatsheet.md` (Task 4), `patterns.md`'s audit procedure name/location (Task 5), `glossary.md` (Task 6).
- Produces: `skills/geo-ai-visibility/SKILL.md` — the skill's entry point, the only file always loaded when the skill matches.

- [ ] **Step 1: Write frontmatter**

```markdown
---
name: geo-ai-visibility
description: "GEO (Generative Engine Optimization) / AI Visibility knowledge base: how to get content cited and mentioned by ChatGPT Search, Perplexity, Google AI Overviews/AI Mode, Copilot, and Gemini. Covers the founding GEO research (Princeton/Georgia Tech paper, technique impact data), how generative answer engines retrieve/rank/cite sources (RAG pipelines), concrete optimization techniques (quotation/statistics addition, structured data, entity-based content, llms.txt), AI-visibility measurement tooling (Profound, Peec AI, Otterly.AI, AthenaHQ), GEO vs. traditional SEO, case-study data (zero-click search, citation concentration), and cross-source consensus/best-practice checklists distilled from GEO research and practitioner videos. Use when planning content/site strategy for AI answer engines, auditing a page or article for AI citability, explaining GEO/AEO/LLMO terminology, choosing an AI-visibility tracking tool, or reasoning about why content does/doesn't get cited by an LLM-based search product."
allowed-tools:
  - Read
  - Grep
  - WebFetch
argument-hint: [topic, technique name, or "audit <url/file>"]
---
```

- [ ] **Step 2: Write "How to Use This Skill" section**

```markdown
# GEO / AI Visibility Expert

## How to Use This Skill

- **Without arguments** — load Core Frameworks below for reference.
- **With a topic** — ask about `llms.txt`, `structured data`, `tooling`,
  or another indexed topic; I find and read the relevant chapter.
- **With "audit <url or file>"** — I follow the procedure in
  `patterns.md` to score the content against `cheatsheet.md` and return
  prioritized fixes.
- **Browse** — ask "what chapters do you have?" to see the full index
  below.

When you ask about a topic not covered in Core Frameworks, I read the
relevant chapter file before answering.

## Chapter Index

- `chapters/01-definizioni-storia.md` — cos'è GEO, il paper fondativo, GEO vs SEO
- `chapters/02-motori-generativi-tecnico.md` — come funzionano ChatGPT Search, Perplexity, Google AIO/AI Mode, Copilot, Gemini
- `chapters/03-fattori-ottimizzazione.md` — tecniche concrete di ottimizzazione, llms.txt
- `chapters/04-tooling-misurazione.md` — tool di misurazione AI visibility
- `chapters/05-case-study-dati.md` — dati, statistiche, casi studio
- `chapters/06-checklist-best-practice.md` — checklist e anti-pattern
- `chapters/07-video-insights-consenso.md` — consenso e divergenze cross-fonte da ricerca video

See also `cheatsheet.md` (audit checklist), `glossary.md` (terminologia), `patterns.md` (procedura di audit).
```

- [ ] **Step 3: Write "Core Frameworks & Mental Models" section**

Pull the highest-value points from every chapter written in Tasks 1-3, prioritized by cross-source consensus (per `chapters/07-video-insights-consenso.md`) and measured impact (per `chapters/01-definizioni-storia.md`'s Princeton table). Must include, each as a bolded-name-led paragraph matching `ux-ui-expert/SKILL.md`'s style:

- **GEO vs SEO shift** — citations over ranking, no click-through, multi-source answers.
- **Princeton technique-impact ranking** — name the top techniques with their measured % (Quotation Addition, Statistics Addition, and the negative result for keyword stuffing), pulled from `chapters/01-definizioni-storia.md`.
- **Per-platform divergence** — the low citation-overlap finding between engines, pulled from `chapters/02-motori-generativi-tecnico.md`; implication: no single-platform strategy.
- **Answer-first / BLUF structuring** — the most-repeated tactical pattern across video sources, pulled from `chapters/07-video-insights-consenso.md`.
- **Branded mentions as top factor** — earned media over backlinks/DR, pulled from `chapters/07-video-insights-consenso.md`.
- **SEO-as-prerequisite** — the top-10-Google-ranking correlation with AI Overview citations, pulled from `chapters/05-case-study-dati.md`/`chapters/07-video-insights-consenso.md`.
- **llms.txt reality check** — what it is, adoption data, and that it's a convention rather than a guarantee, pulled from `chapters/03-fattori-ottimizzazione.md`.
- **Citation concentration** — the top-1%-domains statistic, pulled from `chapters/05-case-study-dati.md`, framed as a realistic-expectations note.

Every number must match exactly what's written in the corresponding chapter file — this section is a compressed pointer to chapter content, not a place to introduce new figures.

- [ ] **Step 4: Verify SKILL.md against spec's "Testing / Verification" scenarios**

Manually walk through the 4 verification scenarios from the spec
(`docs/superpowers/specs/2026-09-14-geo-ai-visibility-skill-design.md`,
"Testing / Verification" section):
1. Re-read `SKILL.md` top to bottom as if loading with no args — confirm it reads coherently and every Core Frameworks bullet is traceable to a chapter.
2. Simulate the question "cos'è GEO" — confirm `SKILL.md`'s Core Frameworks already answers it, or the Chapter Index correctly routes to `chapters/01-definizioni-storia.md`.
3. Simulate "audit questo articolo" using a short 3-paragraph sample text you write inline for this check — walk through `patterns.md`'s procedure by hand and confirm it produces a structured table + prioritized fix list per `cheatsheet.md`'s categories.
4. Spot-check 5 random facts/numbers across `SKILL.md` and the chapters against their cited research files — confirm each traces correctly.

Fix anything that fails these checks before committing.

- [ ] **Step 5: Commit**

```bash
git add skills/geo-ai-visibility/SKILL.md
git commit -m "Add GEO skill SKILL.md (core frameworks, routing, audit entry point)"
```

---

## Task 9: Final spec-coverage self-review

**Files:**
- Read: `docs/superpowers/specs/2026-09-14-geo-ai-visibility-skill-design.md`, entire `skills/geo-ai-visibility/` tree (excluding `research/`)

**Interfaces:**
- Consumes: everything produced in Tasks 1-8.
- Produces: no new files unless a gap is found (in which case, fix inline in the relevant existing file and re-commit).

- [ ] **Step 1: Walk the spec section by section**

For each section of the spec (Purpose, Source Material, File Structure, SKILL.md Contents, Chapters, cheatsheet.md, glossary.md, patterns.md — Audit Mode, Testing/Verification, Out of Scope), confirm the corresponding file(s) exist and satisfy it. List any gap.

- [ ] **Step 2: Fix any gaps found**

Edit the relevant file(s) directly. If no gaps, note "spec fully covered" and stop.

- [ ] **Step 3: Confirm `research/` untouched**

```bash
git status skills/geo-ai-visibility/research/
```
Expected: no changes reported (clean — this directory must remain exactly as committed in the prior session).

- [ ] **Step 4: Final commit (only if Step 2 made changes)**

```bash
git add skills/geo-ai-visibility/
git commit -m "Close spec-coverage gaps in GEO skill"
```
