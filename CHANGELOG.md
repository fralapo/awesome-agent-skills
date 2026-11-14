# Changelog

Versions follow the plugin version in `.claude-plugin/plugin.json`.

## 1.28.0 (2026-11-14)

- New skills: `exercise-science-and-programming` (evidence reasoning, hypertrophy and strength mechanisms, volume, frequency, intensity, progression, periodization, fatigue, fundamentals) and `biomechanics-and-rehab-reasoning` (clinical reasoning, pain science, load and healing, regional functional anatomy, lifting biomechanics, imaging, myths). Educational only, not medical advice.

## 1.27.0 (2026-11-14)

- New skills (7): `computer-science-fundamentals`, `ai-futures-and-intelligence`, `investing-and-financial-history`, `physics-and-math-ideas`, `institutions-and-geopolitics`, `philosophy-ideas`, `behavior-and-decision-science`.
- Extended: `software-architecture` (25 chapters), `software-engineering-practice` (14), `ai-ml-concepts` (16), `economics-finance` (13), `scientific-thinking` (17), `history-geopolitics` (14).

## 1.26.0 (2026-11-13)

- New skill `ai-ml-concepts`: 12 chapters (essential mathematics, probability and Bayes, information, learning as optimization, generalization, architectures, transformers and attention, LLM training and scaling, evaluation and benchmarks, failure modes, safety and interpretability, research principles).
- New skill `economics-finance`: 9 chapters on money creation, central banks and rates, inflation, public debt, exchange rates, financial crises, housing and rent, and how economists disagree.
- New skill `scientific-thinking`: 12 chapters on method, statistics, Bayes, cognition and belief, calibration, research failures, prediction and chaos, game theory, limits of mathematics, discovery, wellbeing and a claim-checking checklist.
- New skill `history-geopolitics`: 8 chapters on analysing collapse and resilience (environment, trade, elites, case sheets, limits of historical analogy).

## 1.25.0 (2026-11-13)

- software-architecture extended from 11 to 20 chapters and 60 patterns: operating-system cost, networking and protocols, database internals and transactions, post-mortems of real incidents, proxies and timeouts, pragmatic domain modeling, boundaries and modular monolith, event-driven and messaging patterns, workflows and sagas.

- New skill `software-engineering-practice`: 9 chapters (continuous delivery foundations, continuous integration vs feature branching, test-driven development, test design and reliable tests, coupling and complexity, design vs architecture and incremental design, engineering vs craft and quality, productivity metrics / ownership / cognitive load, quality and TDD with AI agents), plus cheatsheet, glossary and 28 patterns.

## 1.24.0 (2026-11-13)

- New skill `software-architecture`: system design reasoning with 11 chapters (senior method and estimates, consistency and consensus, availability and overload, storage engines, partitioning and geospatial indexes, caching and delivery, messaging and pipelines, studies of real systems, chat/delivery/video cases, RAG, agentic systems), plus cheatsheet, glossary and 30 patterns.

## 1.23.0 (2026-11-13)

- social-algorithm: three new chapters (predictable revenue and channel mix, paid live events as a conversion layer, starting from zero in phases); extended acquisition, algorithm, psychology and delegation chapters; patterns 46-55.
- presentation-design: new chapter on words, pictures and multimedia learning; perception and honesty in data display.
- depth-psychology: new chapter of experimental-psychology complements.
- public-speaking-persuasion, brand-strategy-storytelling, ux-ui-expert, marketing-mba, pricing-and-sales-negotiation, freelance-designer-ops: additions on clear writing, storytelling, nudges and their limits, human oversight of AI, bias and stereotype threat, trust and dignity at work, negotiation under ambiguity.

## 1.22.0 (2026-11-13)

- social-algorithm: profile-funnel components, content by awareness level and audience stage, late-era ranking priorities and long-form integration (patterns 43-45, new glossary terms).
- ux-ui-expert, public-speaking-persuasion, marketing-mba, depth-psychology: short additions on nudges and choice architecture, human-centred AI, classic style, identified-person effect, trust and dignity at work, frictionless companionship.

## 1.21.0 (2026-11-12)

Repo maintenance, no new skills.

- `geo-ai-visibility` rewritten in English. Chapters renamed to `chNN-topic.md`, the raw `research/` notes removed, the local-agency case study anonymised.
- Descriptions of `art-director`, `graphic-designer`, `ux-ui-expert` and `freelance-designer-ops` cut to the 1024-character limit (they were being truncated in the skill list). `social-algorithm` and `public-speaking-persuasion` now say when to use them.
- `art-director` and `graphic-designer` have a linked chapter index. `freelance-designer-ops`, `slide-software-techniques`, `workshop-facilitation` and `filmcraft-expert` link every supporting file.
- `social-algorithm`: person names removed from chapter 10 and chapter 12 (file renamed).
- Added `scripts/validate.py` and a GitHub Actions workflow that runs it on every push and pull request.
- README catalogue regrouped by domain with shorter rows. `marketplace.json` version brought back in line with `plugin.json`.
- Removed internal planning notes under `docs/`.

## 1.20.0 (2026-11-12)

- New skill: `coding-with-agents`.
- Extended `graphic-designer` (ch14-20), `art-director` (ch10-12), `creative-director`, `ux-ui-expert` (ch37-41), `freelance-designer-ops` (ch05-09), `pricing-and-sales-negotiation`.

## 1.19.0 (2026-11-07)

- New skills: `pricing-and-sales-negotiation`, `workshop-facilitation`, `brand-strategy-storytelling`.
- Extended the design, UX and speaking skills.

## 1.18.x (2026-11-05)

- New skills: `graphic-designer`, `art-director`, with role boundaries shared with `creative-director` and `ux-ui-expert`.
- Cross-references for visual theory between the design-role skills.

## Earlier

- `presentation-design`, `slide-software-techniques`, `freelance-designer-ops`, `depth-psychology`.
- Five ArtCraft skills: `vectorcraft-expert`, `photocraft-expert`, `effectcraft-expert`, `filmcraft-expert`, `designcraft-expert`.
- Codex CLI compatibility through `.agents/skills` symlinks.
- First skills: `seedance-prompts`, `image-gen-prompts`, `awesome-readme`, `llm-wiki`, `social-algorithm`, `creative-director`, `ffmpeg`, `video-editor`, `public-speaking-persuasion`, `marketing-mba`, `ux-ui-expert`, `geo-ai-visibility`, `jev`.
