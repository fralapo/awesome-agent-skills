# Changelog

Versions follow the plugin version in `.claude-plugin/plugin.json`.

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
