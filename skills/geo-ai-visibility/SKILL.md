---
name: geo-ai-visibility
description: "GEO (Generative Engine Optimization) / AI Visibility knowledge base: how to get content cited and mentioned by ChatGPT Search, Perplexity, Google AI Overviews/AI Mode, Copilot, and Gemini. Covers the founding GEO research (Princeton/Georgia Tech paper, technique impact data), how generative answer engines retrieve/rank/cite sources (RAG pipelines), concrete optimization techniques (quotation/statistics addition, structured data, entity-based content, llms.txt), AI-visibility measurement tooling (Profound, Peec AI, Otterly.AI, AthenaHQ), GEO vs. traditional SEO, case-study data (zero-click search, citation concentration), and cross-source consensus/best-practice checklists distilled from GEO research and practitioner videos. Use when planning content/site strategy for AI answer engines, auditing a page or article for AI citability, explaining GEO/AEO/LLMO terminology, choosing an AI-visibility tracking tool, or reasoning about why content does/doesn't get cited by an LLM-based search product."
allowed-tools:
  - Read
  - Grep
  - WebFetch
argument-hint: [topic, technique name, or "audit <url/file>"]
---

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

---

## Core Frameworks & Mental Models

**GEO vs SEO shift**: SEO optimizes a whole page to rank in a list of 10 clickable links; GEO optimizes the semantic chunk to be selected as a citation inside one synthesized answer. Click-through is often absent entirely (zero-click) — the win is being mentioned even without a click — and a single answer can cite 3-10 sources at once, so there's no exclusive "position 1." A solid technical SEO base (crawlability, speed, no robots.txt blocks on AI crawlers) remains a prerequisite: GEO builds on top of SEO, it doesn't replace it (`chapters/01-definizioni-storia.md`).

**Princeton technique-impact ranking**: the founding GEO paper (arXiv:2311.09735) tested 9 techniques on Position-Adjusted Word Count (PAWC) and Subjective Impression (SI). Quotation Addition is the top performer at +41% PAWC / +28% SI; Statistics Addition follows at +33% PAWC / +22% SI (validated on real Perplexity at +37% SI). Keyword Stuffing is the one negative result, at -8% PAWC in the paper (down to -10% on real Perplexity) — it's measurably counterproductive, contradicting classic SEO practice (`chapters/01-definizioni-storia.md`).

**Per-platform divergence**: an analysis of 680M+ citations found only 11% of domains are cited by both ChatGPT and Perplexity. Implication: no single-platform strategy is sufficient — GEO work has to be measured and optimized per engine, which is also why multi-platform AI-visibility tooling exists (`chapters/02-motori-generativi-tecnico.md`).

**Answer-first / BLUF structuring**: the most-repeated tactical pattern across the 9 practitioner videos surveyed — start every section with the direct answer before any backstory (Bottom Line Up Front), because both humans and AI models weigh the start of a passage more heavily than the middle. Explicit in Kaliber, Ahrefs, Niko, Hostinger, and Surfer Academy (`chapters/07-video-insights-consenso.md`).

**Branded mentions as top factor**: off-site brand mentions are the single strongest AI-visibility factor identified in the video material — an Ahrefs study of 75,000 brands found branded web mentions correlate more strongly with AI Overview visibility than backlinks, Domain Rating, or referring domains. Silicon Valley Girl independently reports that 82% of what AI cites is "earned media" (third-party articles, listicles, Reddit threads), not self-published content. Earned mentions outweigh backlinks (`chapters/07-video-insights-consenso.md`).

**SEO-as-prerequisite (with a caveat)**: classic Google ranking still correlates with AI Overview citation, but that correlation is weakening — only 38% of AI Overview citations now come from top-10 Google pages (2026 data), down sharply from 76% in mid-2025, as query fan-out decouples AI citation from classic ranking (`chapters/05-case-study-dati.md`). The 76% figure is also the most-repeated statistic across the 9 practitioner videos surveyed, but it traces to a single Ahrefs study rather than independent confirmation — attribute it as "Ahrefs data," not consensus (`chapters/07-video-insights-consenso.md`).

**llms.txt reality check**: llms.txt is a plain-markdown file at a site's root giving AI agents a machine-readable summary of the site — an emerging bottom-up convention, not a W3C standard. Adoption has passed 844,000 sites, including Stripe, Cloudflare, Vercel, and Anthropic. It only enables reading, not action — it's a convention, not a citation guarantee (`chapters/03-fattori-ottimizzazione.md`).

**Citation concentration**: a realistic-expectations note — an aggregated study of 680M+ citations found the top 1% of cited domains (~12 sites: Wikipedia, Reddit, Forbes, Healthline, Investopedia, NYT, and large .gov/.edu domains) capture 47% of all AI citations (`chapters/05-case-study-dati.md`).

---

## Supporting Files

- [cheatsheet.md](cheatsheet.md) — audit checklist by category
- [glossary.md](glossary.md) — terminology (GEO, AEO, LLMO, RAG, PAWC, etc.)
- [patterns.md](patterns.md) — content-audit procedure

## Scope & Limits

This skill covers GEO/AI-visibility strategy and research: how generative answer engines retrieve and cite sources, concrete content/technical optimization techniques, AI-visibility measurement tooling, and cross-source consensus on best practice. It does not cover hands-on implementation of schema markup, CMS-specific publishing workflows, or general SEO practice beyond what's needed to understand GEO as a layer on top of it — check a dedicated SEO skill or tool documentation for that.
