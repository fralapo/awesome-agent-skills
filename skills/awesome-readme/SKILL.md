---
name: awesome-readme
description: Write awesome-list-worthy README.md files for GitHub repositories — project READMEs (library, CLI, app, research, template) and GitHub profile READMEs (username/username repo) — with prose that reads as human-written, not AI-generated. Covers section selection, shields.io badge stacks, banner/logo/GIF guidance, TOC patterns, expandable `<details>` blocks, back-to-top anchors, contributor widgets (contrib.rocks, star-history), typing SVGs, GitHub-readme-stats cards, Standard-Readme spec compliance, README-Driven-Development workflow, and a full anti-AI-slop audit pass on every draft (integrates the humanizer skill's Wikipedia "Signs of AI writing" patterns tuned for README prose). Triggers when user asks to generate, write, improve, refactor, humanize, or audit a README; wants badges, TOC, logo placement, demo GIF, feature list, install/usage blocks, contributing section, roadmap, "getting started", or profile README with stats/typing SVG/snake animation. Keywords - readme, README.md, github readme, profile readme, awesome readme, shields.io, badges, contrib.rocks, github-readme-stats, readme template, readme generator, best-readme-template, standard-readme, humanize readme, ai-sounding readme.
version: 1.0.0
source: local-git-analysis
analyzed_repos:
  - github.com/othneildrew/Best-README-Template
  - github.com/matiassingers/awesome-readme
  - github.com/abhisheknaiidu/awesome-github-profile-readme
  - github.com/glincker/claude-code-marketplace (skills/documentation/readme-generator)
  - github.com/RichardLitt/standard-readme
  - makeareadme.com
  - utrechtuniversity.github.io workshop-computational-reproducibility
  - tom.preston-werner.com Readme Driven Development
analyzed_examples: ~100 curated awesome-readme entries
---

# Awesome README Engineering

A GitHub README is the front door of a project. The best ones combine a clear value proposition above the fold, scannable structure, credibility signals (badges, contributors, stars), copy-pasteable install/usage, visuals (banner, demo GIF, screenshots), and — most overlooked of all — prose that sounds like a human wrote it.

That last point is non-negotiable. A visitor smells AI-generated marketing copy in seconds. Once they do, every other quality signal on the page loses its weight. See [references/voice-and-prose.md](references/voice-and-prose.md) for the full anti-AI-slop protocol; apply it to every draft before writing to disk.

This skill produces **two kinds** of READMEs:

| Kind | Lives at | Purpose |
|---|---|---|
| **Project README** | `repo-root/README.md` | Sells and explains a software project to potential users / contributors |
| **Profile README** | `username/username/README.md` (special repo) | Personal GitHub landing page — bio, skills, stats, socials |

Grammar differs per kind. See [references/profile-readme.md](references/profile-readme.md) for profile specifics.

## When to Use This Skill

Trigger on any of:

- "Write / generate / create a README for this repo"
- "Improve / refactor / audit the README"
- "Add badges / TOC / demo GIF / logo / banner"
- "Make my GitHub profile README"
- "Make my README look like an awesome-readme entry"
- "Convert this project description into a README"
- User mentions: `shields.io`, `contrib.rocks`, `github-readme-stats`, `typing SVG`, `snake animation`, `Best-README-Template`, `Standard-Readme`

## Core Workflow

```
1. DISCOVER    — read the repo (package.json, pyproject.toml, Cargo.toml,
                 go.mod, src/, LICENSE, CI workflows, existing README)
2. CLASSIFY    — library / CLI / web-app / desktop-app / research /
                 template / profile-readme
3. SELECT      — pick sections from the catalog (see references/sections.md)
                 based on project type + what the repo actually has
4. DRAFT       — write the README using templates (references/templates.md)
                 + badge stack (references/badges.md)
5. HUMANIZE    — mandatory audit pass against references/voice-and-prose.md:
                 strip promotional adjectives, significance inflation, em-dash
                 overuse, superficial -ing clauses, rule-of-three synonym
                 cycling, chatbot artifacts, generic uplift conclusions.
                 Use the two-prompt audit: "what makes this obviously AI
                 generated?" → rewrite.
6. POLISH      — banner/logo placement, TOC, back-to-top anchors,
                 `<details>` collapses, anchor links
7. VERIFY      — no broken links, all code blocks language-tagged, badges
                 resolve, placeholder tokens (owner/repo) all replaced
8. WRITE       — output README.md. If one exists, diff + confirm before
                 overwriting; offer a `README.md.bak` save
```

## Discovery Checklist

Before writing, scan:

| What | How | Signals |
|---|---|---|
| Project name | repo folder name, `name` in manifest | title |
| Description | manifest `description`, top-of-src doc | tagline |
| Language(s) | file extensions, manifest | install syntax, code-block lang |
| Package manager | `package.json`, `pyproject.toml`, etc. | install command |
| Entry point | `main`, `bin`, `src/index.*` | usage example |
| Tests | `tests/`, `__tests__/`, `*_test.*` | testing section |
| CI | `.github/workflows/*.yml` | build badge |
| License | `LICENSE*` file | license badge + section |
| Docs site | `docs/`, `mkdocs.yml`, existing URL | "Docs" link |
| Screenshots | `images/`, `assets/`, `docs/images/` | visuals section |
| Contributing | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` | contrib section |
| Releases | `CHANGELOG.md`, GitHub releases | roadmap / release history |

Ask user for anything missing: `owner/repo`, live demo URL, logo path, social handles, preferred badge style (`flat` / `flat-square` / `for-the-badge` / `plastic`).

## Section Catalog (Quick Reference)

Full definitions → [references/sections.md](references/sections.md).

**Above the fold (always)**
- Title (H1, centered optional)
- Tagline (one sentence, under 120 chars)
- Badges row (5–8 max — more = noise)
- Banner or logo (optional but high-impact)
- Elevator pitch (2–4 sentences)
- Key links bar: Docs · Demo · Report Bug · Request Feature

**Navigation**
- Table of Contents (TOC) — required for READMEs > 100 lines; collapsible via `<details>` if long

**Proof**
- Demo GIF or screenshot (above the fold for visual projects)
- "Built With" tech stack badges
- Star history chart (for popular repos)

**Onboarding**
- Prerequisites
- Installation (copy-pasteable, per-platform if relevant)
- Quick start / Usage (smallest runnable example)
- Examples (more complex recipes)
- Configuration / Environment variables
- API reference (or link to docs)

**Community**
- Roadmap (checkbox list)
- Contributing (link to CONTRIBUTING.md if long)
- Contributors (contrib.rocks widget)
- Code of Conduct link
- Security policy link
- License
- Acknowledgments
- Contact / Support

**Profile-README only** (see [references/profile-readme.md](references/profile-readme.md))
- About Me
- Current focus
- Tech stack icons
- GitHub stats card + top-languages card
- Streak stats
- Typing SVG / quote SVG
- Recent blog posts / now playing / contribution snake

## Style Rules

### 1. Above-the-fold must answer 3 questions in 5 seconds

- **What is it?** (one-line tagline)
- **Does it work?** (CI / version / downloads badges)
- **What does it look like?** (banner, logo, or demo GIF)

### 2. Code blocks are always language-tagged

````md
```bash
npm install
```

```python
from mypkg import thing
thing.run()
```
````

Never use bare ``` ```. Syntax highlighting = instant credibility.

### 3. Copy-pasteable commands

Users paste without thinking. So:
- no placeholder `<your-token>` inside the command — put it on a separate line with a comment
- no `$` prompt prefix — breaks paste
- one command per block when possible
- use `sh` / `bash` tag for shell

### 4. Badges: curate, don't dump

5–8 badges max. Order: **identity** (version) → **health** (build, coverage) → **reach** (downloads, stars) → **legal** (license) → **social** (Twitter, Discord).
See [references/badges.md](references/badges.md) for copy-paste templates.

### 5. Visuals earn their place

- **Banner** = hero image, 1280×640 or 1500×500 typical
- **Logo** = 80–120px square, centered near title
- **Demo GIF** = < 5 MB, < 15 s, shows the core loop
- **Screenshots** = explicit `width` attribute, descriptive `alt`

Tools: VHS (terminal), ScreenToGif (Windows), Gifski (macOS), Peek (Linux), terminalizer. See [references/visuals.md](references/visuals.md).

### 6. Back-to-top anchors

For READMEs > 300 lines, end each major section with:

```md
<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

Paired with `<a id="readme-top"></a>` at the top.

### 7. `<details>` collapse long blocks

TOCs over 15 items, long config lists, OS-specific install variants, FAQ — wrap in `<details>`:

```md
<details>
<summary>Advanced configuration</summary>

...long content...

</details>
```

### 8. Reference-style links for repeated URLs

Keeps prose readable. All shields.io URLs and repo anchors go at the bottom:

```md
[![Stars][stars-shield]][stars-url]

[stars-shield]: https://img.shields.io/github/stars/owner/repo.svg?style=for-the-badge
[stars-url]: https://github.com/owner/repo/stargazers
```

### 9. Emoji, selectively

- Section headings: one decorative emoji OK (✨ Features, 🚀 Quick Start, 🛠 Installation)
- Never sprinkle mid-sentence
- Skip entirely for enterprise / scientific contexts — ask user

### 10. No lies, no TODOs

Ship no section you can't back up. Empty "Acknowledgments" or "Features" = worse than no section. Replace with `<!-- hide until real -->` comment.

### 11. Write prose a human would write

The single highest-leverage polish after structure is voice. Most generated READMEs fail here.

**Strip on sight:**

- Promotional adjectives: `blazing-fast`, `seamless`, `intuitive`, `powerful`, `robust`, `cutting-edge`, `next-generation`, `best-in-class`, `vibrant`, `groundbreaking`
- Significance inflation: `pivotal`, `crucial`, `testament to`, `stands as`, `serves as`, `represents a`, `marks a`, `evolving landscape`, `ecosystem`, `journey`
- Copula avoidance: prefer `is` / `are` / `has` over `serves as`, `boasts`, `features`, `offers`, `delivers`
- Trailing `-ing` pseudo-analyses: `..., empowering developers`, `..., ensuring X`, `..., highlighting Y`
- Em dashes stacked in one paragraph — one per section, max
- Negative parallelism: `It's not just a library, it's a philosophy`
- Rule-of-three synonym cycling in flowing prose (fine in bullet lists)
- Generic uplift: `the future is bright`, `exciting times ahead`, `continues to evolve`
- Chatbot artifacts: `Of course!`, `Let me know if`, `Here's a breakdown`, `I hope this helps`

**Favor:**

- Plain copulas (`is`, `are`, `has`)
- Specific numbers, versions, dates, names
- First person (`I`, `we`) when a real person is behind the project
- Varied sentence rhythm — short, then long, then short
- Visible uncertainty (`we're still figuring out`, `probably`, `about 94% of the time`)
- Named comparisons (`faster than quicktype on 10 MB payloads` beats `blazing-fast`)

**After drafting, run the two-prompt audit:**

1. *What makes this README obviously AI generated?* (answer in bullets, be harsh)
2. *Rewrite it so it doesn't read as AI generated.* (apply fixes, prefer cutting over rewording)

Ship the second version. Full patterns and worked examples in [references/voice-and-prose.md](references/voice-and-prose.md). For deep humanization of long-form prose (about pages, philosophy sections), hand off to the `humanizer` skill for a final pass.

## Anti-Patterns (things that kill credibility)

See [references/anti-patterns.md](references/anti-patterns.md). Highlights:

- `# Project Name` and nothing else for 3 paragraphs before telling user what it is
- 20+ badge wall of noise
- Install section that doesn't actually install (missing prereq, wrong command)
- Broken image links (`images/logo.png` but `images/` not committed)
- Placeholder tokens (`github_username`, `repo_name`) left in after fork
- Sections titled "Coming soon"
- Walls of text with no headers, no code blocks, no visuals
- Lorem-ipsum-ish filler ("this is a cool project that does cool things")
- Outdated version numbers in prose (`Install v1.2` when package.json says `2.5`)

## Project-Type → Template Map

Full templates → [references/templates.md](references/templates.md).

| Project type | Use template | Key features |
|---|---|---|
| Library / SDK | `library.md` | API section, install via pkg mgr, import example |
| CLI tool | `cli.md` | `--help` output, usage GIF (VHS), subcommand table |
| Web app | `webapp.md` | Live demo link, screenshot grid, .env example |
| Desktop app | `desktop.md` | Download badges per-OS, screenshot, system requirements |
| Research / ML | `research.md` | Abstract, cite-as BibTeX, dataset, reproducibility |
| Template / Boilerplate | `template.md` | "Use this template" button, what's included, scaffolding flow |
| Monorepo | `monorepo.md` | Packages table with per-pkg badges, workspace layout |
| Profile README | `profile.md` | Intro card, stats widgets, socials — see profile-readme.md |

## Output Contract

When producing a README:

1. Draft internally (or show a first pass if user asked to see it)
2. **Run the humanize audit** from [voice-and-prose.md](references/voice-and-prose.md). List every AI tell you find. Rewrite.
3. Show the audited draft (inside a `md` code block) for user review
4. On user approval, write to `README.md`
5. If `README.md` exists: `cp README.md README.md.bak` first, then write
6. All placeholder tokens REPLACED with real values — never ship `<owner>/<repo>` or `Lorem ipsum`-like filler
7. Verify (mentally) every badge URL resolves and every anchor link exists

If the user asks you to *improve* or *humanize* an existing README (rather than generate one), skip to the audit pass: run the checklist, diff, and propose edits preserving their voice.

## Related Files in This Skill

- [references/voice-and-prose.md](references/voice-and-prose.md) — anti-AI-slop protocol tuned for README prose; run on every draft
- [references/sections.md](references/sections.md) — every section: purpose, when-to-include, snippet
- [references/badges.md](references/badges.md) — shields.io copy-paste library
- [references/templates.md](references/templates.md) — full README templates per project type
- [references/visuals.md](references/visuals.md) — banner/logo/GIF recipes + tools
- [references/profile-readme.md](references/profile-readme.md) — profile README patterns (stats, typing SVG, snake)
- [references/anti-patterns.md](references/anti-patterns.md) — structural and prose anti-patterns
- [references/examples.md](references/examples.md) — annotated excerpts from awesome-readme entries

## Related skills

- [`humanizer`](../humanizer/) — full Wikipedia "Signs of AI writing" treatment; hand off long-form README prose for a deep humanization pass.
