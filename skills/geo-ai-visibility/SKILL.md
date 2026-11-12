---
name: geo-ai-visibility
description: "GEO (Generative Engine Optimization) / AI-visibility knowledge base: how to get content cited by ChatGPT Search, Perplexity, Google AI Overviews/AI Mode, Copilot and Gemini. Covers the founding GEO research and technique impact data, how answer engines retrieve, rank and cite (RAG), optimization techniques (quotations, statistics, structured data, entity content, llms.txt), AI-visibility tools (Profound, Peec AI, Otterly, AthenaHQ), GEO vs. SEO, and audit checklists. Use when planning content for AI answer engines, auditing a page for AI citability, explaining GEO/AEO/LLMO, choosing a tracking tool, or diagnosing why an AI recommends a competitor over a local business or agency (entity disambiguation, 'service + city' coverage, LocalBusiness schema with sameAs, NAP consistency, third-party corroboration)."
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
  [patterns.md](patterns.md) to score the content against
  [cheatsheet.md](cheatsheet.md) and return prioritized fixes.
- **Browse** — ask "what chapters do you have?" to see the full index
  below.

When you ask about a topic not covered in Core Frameworks, I read the
relevant chapter file before answering.

## Chapter Index

| # | Chapter | Covers |
|---|---|---|
| 1 | [Definitions and history](chapters/ch01-definitions-and-history.md) | What GEO is, the founding paper, GEO vs SEO |
| 2 | [How generative engines work](chapters/ch02-how-generative-engines-work.md) | How ChatGPT Search, Perplexity, Google AIO/AI Mode, Copilot and Gemini retrieve and cite |
| 3 | [Optimization factors](chapters/ch03-optimization-factors.md) | Concrete optimization techniques, llms.txt |
| 4 | [Tooling and measurement](chapters/ch04-tooling-and-measurement.md) | AI-visibility measurement tools |
| 5 | [Case studies and data](chapters/ch05-case-studies-and-data.md) | Data, statistics, market signals |
| 6 | [Checklist and best practices](chapters/ch06-checklist-and-best-practices.md) | Consolidated checklist and anti-patterns |
| 7 | [Cross-source consensus](chapters/ch07-cross-source-consensus.md) | Where practitioners agree and disagree, and which repeated figures share one origin |
| 8 | [Entity GEO for local service businesses](chapters/ch08-entity-geo-for-local-service-businesses.md) | Anonymised Agency A vs Agency B case: why an LLM recommends one agency and not another, gap analysis against the competitor |

See also [cheatsheet.md](cheatsheet.md) (audit checklist), [glossary.md](glossary.md) (terminology), [patterns.md](patterns.md) (audit procedure).

---

## Core Frameworks & Mental Models

**GEO vs SEO shift**: SEO optimizes a whole page to rank in a list of 10 clickable links; GEO optimizes the semantic chunk to be selected as a citation inside one synthesized answer. Click-through is often absent entirely (zero-click) — the win is being mentioned even without a click — and a single answer can cite 3-10 sources at once, so there's no exclusive "position 1." A solid technical SEO base (crawlability, speed, no robots.txt blocks on AI crawlers) remains a prerequisite: GEO builds on top of SEO, it doesn't replace it ([chapter 1](chapters/ch01-definitions-and-history.md)).

**Princeton technique-impact ranking**: the founding GEO paper (arXiv:2311.09735) tested 9 techniques on Position-Adjusted Word Count (PAWC) and Subjective Impression (SI). Quotation Addition is the top performer at +41% PAWC / +28% SI; Statistics Addition follows at +33% PAWC / +22% SI (validated on real Perplexity at +37% SI). Keyword Stuffing is the one negative result, at -8% PAWC in the paper (down to -10% on real Perplexity) — it's measurably counterproductive, contradicting classic SEO practice ([chapter 1](chapters/ch01-definitions-and-history.md)).

**Per-platform divergence**: an analysis of 680M+ citations found only 11% of domains are cited by both ChatGPT and Perplexity. Implication: no single-platform strategy is sufficient — GEO work has to be measured and optimized per engine, which is also why multi-platform AI-visibility tooling exists ([chapter 2](chapters/ch02-how-generative-engines-work.md)).

**Answer-first / BLUF structuring**: the most-repeated tactical pattern among practitioners — start every section with the direct answer before any backstory (Bottom Line Up Front), because both humans and AI models weigh the start of a passage more heavily than the middle. Explicit in five of the nine practitioner sources surveyed ([chapter 7](chapters/ch07-cross-source-consensus.md)).

**Branded mentions as top factor**: off-site brand mentions are the single strongest AI-visibility factor in practitioner material — an Ahrefs study of 75,000 brands found branded web mentions correlate more strongly with AI Overview visibility than backlinks, Domain Rating, or referring domains. An independent practitioner-reported figure says 82% of what AI cites is "earned media" (third-party articles, listicles, Reddit threads), not self-published content. Earned mentions outweigh backlinks ([chapter 7](chapters/ch07-cross-source-consensus.md)).

**SEO-as-prerequisite (with a caveat)**: classic Google ranking still correlates with AI Overview citation, but that correlation is weakening — only 38% of AI Overview citations now come from top-10 Google pages (2026 data), down sharply from 76% in mid-2025, as query fan-out decouples AI citation from classic ranking ([chapter 5](chapters/ch05-case-studies-and-data.md)). The 76% figure is also the statistic practitioners repeat most, but it traces to a single Ahrefs study rather than independent confirmation — attribute it as "Ahrefs data," not consensus ([chapter 7](chapters/ch07-cross-source-consensus.md)).

**llms.txt reality check**: llms.txt is a plain-markdown file at a site's root giving AI agents a machine-readable summary of the site — an emerging bottom-up convention, not a W3C standard. Adoption has passed 844,000 sites, including Stripe, Cloudflare, Vercel, and Anthropic. It only enables reading, not action — it's a convention, not a citation guarantee ([chapter 3](chapters/ch03-optimization-factors.md)).

**Citation concentration**: a realistic-expectations note — an aggregated study of 680M+ citations found the top 1% of cited domains (~12 sites: Wikipedia, Reddit, Forbes, Healthline, Investopedia, NYT, and large .gov/.edu domains) capture 47% of all AI citations ([chapter 5](chapters/ch05-case-studies-and-data.md)).

**Retrieval before persuasion (local services)**: an LLM recommends the business its retrieval returns with enough corroboration, not the "best" one. In an anonymised case of two communication agencies, Agency A, with the stronger portfolio, never appeared in "agency + service + city" answers, while Agency B appeared even when the city changed, because Agency B had a literal page or section for every "service + city" phrasing, the same entity definition in every footer, textual case studies, author pages, and fresh informational content. Agency A had an ambiguous name, a brand-first hero with no who/where/what sentence, a gallery-style portfolio, and almost no third-party sources. Fix order: disambiguate the entity and align NAP and description everywhere, add third-party corroboration, add schema with a shared `@id`, then rework the service pages, and lead with a vertical niche where you have real credentials. Avoid doorway pages and self-ranking listicles ([chapter 8](chapters/ch08-entity-geo-for-local-service-businesses.md)).

---

## Supporting Files

- [cheatsheet.md](cheatsheet.md) — audit checklist by category
- [glossary.md](glossary.md) — terminology (GEO, AEO, LLMO, RAG, PAWC, etc.)
- [patterns.md](patterns.md) — content-audit procedure

## Scope & Limits

This skill covers GEO/AI-visibility strategy and research: how generative answer engines retrieve and cite sources, concrete content/technical optimization techniques, AI-visibility measurement tooling, and cross-source consensus on best practice. It does not cover hands-on implementation of schema markup, CMS-specific publishing workflows, or general SEO practice beyond what's needed to understand GEO as a layer on top of it — check a dedicated SEO skill or tool documentation for that. Chapter 8 does list the schema properties and NAP fields that matter for local entity disambiguation, as a checklist rather than an implementation guide.
