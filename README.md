<a id="readme-top"></a>

<h1 align="center">awesome-agent-skills</h1>

<p align="center">
  A small, opinionated set of agent skills I actually use.
  Each one is mined from a real corpus (community awesome-lists, official docs, books, field notes), anywhere from a couple hundred examples to tens of thousands. None of it written from imagination.
  <br>
  Built on <a href="https://docs.claude.com/en/docs/claude-code/skills">Claude Code's skill format</a>, installable as a plugin, and usable by any agent that reads <code>SKILL.md</code> — including <a href="https://developers.openai.com/codex/skills">OpenAI Codex CLI</a>, which this repo also ships ready-to-discover folders for.
</p>

<p align="center">
  <a href="https://github.com/fralapo/awesome-agent-skills/stargazers"><img src="https://img.shields.io/github/stars/fralapo/awesome-agent-skills?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/fralapo/awesome-agent-skills/commits/main"><img src="https://img.shields.io/github/last-commit/fralapo/awesome-agent-skills?style=for-the-badge" alt="Last commit"></a>
  <img src="https://img.shields.io/badge/skills-29-2ea44f?style=for-the-badge" alt="Skills count">
  <img src="https://img.shields.io/badge/agent%20skills-SKILL.md-5A67D8?style=for-the-badge" alt="Agent skills format">
  <a href="https://github.com/fralapo/awesome-agent-skills/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/fralapo/awesome-agent-skills/validate.yml?style=for-the-badge&label=checks" alt="Checks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/fralapo/awesome-agent-skills?style=for-the-badge" alt="License"></a>
</p>

---

## Contents

- [What's in here](#whats-in-here)
  - [Design roles](#design-roles)
  - [Presentations, speaking and workshops](#presentations-speaking-and-workshops)
  - [Marketing, brand and business](#marketing-brand-and-business)
  - [Image, video and motion](#image-video-and-motion)
  - [ArtCraft apps over MCP](#artcraft-apps-over-mcp)
  - [Code, docs and knowledge](#code-docs-and-knowledge)
  - [People](#people)
- [Install](#install)
  - [Plugin marketplace (recommended)](#plugin-marketplace-recommended)
  - [Manual (symlink or copy)](#manual-symlink-or-copy)
  - [Codex CLI (OpenAI)](#codex-cli-openai)
- [How a skill is organized](#how-a-skill-is-organized)
- [How I build them](#how-i-build-them)
- [Checks](#checks)
- [Contributing](#contributing)
- [License](#license)

---

## What's in here

29 skills. Each is one folder with a `SKILL.md` (frontmatter plus workflow) and deeper material next to it (`references/`, or `chapters/` with a cheatsheet, patterns and glossary). The agent matches the `description` field against what you ask and loads a skill only when it is relevant, then opens only the chapters the task needs.

### Design roles

Four roles that hand work to each other instead of overlapping: idea, direction, craft, screens.

| Skill | What it covers | Typical triggers |
|---|---|---|
| [`creative-director`](./skills/creative-director/) | Router into five toolkits (copywriter, idea generator, creative leader, visionary, evaluator). Concepts, insights, headlines, feedback to creative teams, scoring an idea against a quality bar. | `headline`, `campaign idea`, `evaluate concept`, `creative feedback` |
| [`art-director`](./skills/art-director/) | From concept to visual direction: one-emotion method, moodboards, three routes, identity-system rules, stylescapes, rebrand analysis, quality levels and perception tests, getting a direction approved. | `moodboard`, `look and feel`, `visual identity`, `rebrand` |
| [`graphic-designer`](./skills/graphic-designer/) | Hands-on craft: grids, typography, posters, logo construction and tests, spacing systems, hierarchy and contrast, colour craft, print and packaging, the amateur-to-pro fix list, file handover. | `poster`, `layout`, `grid`, `typography`, `logo` |
| [`ux-ui-expert`](./skills/ux-ui-expert/) | UX research (study plans, sample sizes, ethics, ROI) and UI design (flows, hierarchy, design systems, typography laws, microcopy, colour systems, UX psychology), plus product flows such as onboarding, paywalls and retention. | `usability test`, `ui review`, `user flow`, `microcopy`, `design system` |

### Presentations, speaking and workshops

| Skill | What it covers | Typical triggers |
|---|---|---|
| [`presentation-design`](./skills/presentation-design/) | Slide decks from message to delivery: slide-type system, layout, a type scale for 1920×1080, colour roles, charts, animation timings, redesign method, and a workflow for generating .pptx with code. | `slides`, `pitch deck`, `redesign this deck` |
| [`slide-software-techniques`](./skills/slide-software-techniques/) | Click-level how-to in PowerPoint, Keynote, Google Slides, Canva and Figma Slides: Slide Master, theme fonts and colours, templates, Morph and Magic Move recipes, export and presenting. | `slide master`, `morph`, `magic move`, `potx` |
| [`public-speaking-persuasion`](./skills/public-speaking-persuasion/) | Speech structure, storytelling, fallacy and bias catalogues, delivery, stage anxiety, objection handling, pitching and client conversations. | `speech`, `pitch`, `persuasion`, `objection handling` |
| [`workshop-facilitation`](./skills/workshop-facilitation/) | Workshops that end in decisions: agendas, timeboxing, silent-first techniques and voting, difficult participants, the design sprint day by day, remote facilitation. | `workshop`, `design sprint`, `agenda`, `dot voting` |

### Marketing, brand and business

| Skill | What it covers | Typical triggers |
|---|---|---|
| [`marketing-mba`](./skills/marketing-mba/) | MBA-level marketing and startup execution: segmentation, value proposition, pricing strategy, sales pipeline, negotiation, founder frameworks. | `go-to-market`, `value proposition`, `segmentation` |
| [`brand-strategy-storytelling`](./skills/brand-strategy-storytelling/) | Brand ladder, client discovery, positioning and niche, voice and messaging, story arcs, personal brand, case-study narrative. | `positioning`, `brand voice`, `brand story`, `niche` |
| [`social-algorithm`](./skills/social-algorithm/) | Organic personal-brand growth and Instagram dynamics: indirect selling, the interaction loop, diagnostic metrics, hooks, acquisition funnels without ads, content systems, YouTube positioning. | `instagram`, `reel underperformed`, `hook`, `personal brand` |
| [`geo-ai-visibility`](./skills/geo-ai-visibility/) | Getting cited by ChatGPT Search, Perplexity, Google AI Overviews, Copilot and Gemini: the founding GEO research, how generative engines retrieve and rank, optimisation techniques, measurement tools, an audit checklist, entity GEO for local service businesses. | `geo`, `ai visibility`, `llms.txt`, `audit <url>` |
| [`pricing-and-sales-negotiation`](./skills/pricing-and-sales-negotiation/) | Pricing and selling for freelancers and small studios: value-based pricing, cost bids, option ladders, discovery calls, objections and discounts, retainers, raising rates, when to walk away. | `quote`, `proposal`, `too expensive`, `raise rates` |
| [`freelance-designer-ops`](./skills/freelance-designer-ops/) | Running a freelance design practice: scoping and timing, a buildable Notion workspace with hour-tracker formulas, time blocking, winning and onboarding clients, presenting work, portfolio and content. | `freelance`, `notion workspace`, `hour tracker`, `find clients` |

### Image, video and motion

| Skill | What it covers | Typical triggers |
|---|---|---|
| [`image-gen-prompts`](./skills/image-gen-prompts/) | Prompt engineering for the major image models (Midjourney, GPT Image, FLUX, SDXL, Seedream, Imagen, Ideogram). 40+ templates, 20 edit-repair recipes, routing by the model named. Mined from about 19,000 public prompts. | `image prompt`, `midjourney`, `flux`, `mockup` |
| [`seedance-prompts`](./skills/seedance-prompts/) | Prompt templates for ByteDance Seedance video generation: storyboards, camera-move vocabulary, multi-modal references, identity locks, POV and found-footage styles. | `seedance`, `text-to-video prompt` |
| [`video-editor`](./skills/video-editor/) | Software-agnostic decisions for short-form video: hook system, pacing, motion, captions, sound design, transitions. | `reel`, `retention`, `pacing`, `b-roll` |
| [`ffmpeg`](./skills/ffmpeg/) | FFmpeg CLI reference: codecs, formats, filtergraphs, protocols, capture devices, with the official documentation bundled for grep. | `ffmpeg`, `transcode`, `filtergraph`, `hls`, `nvenc` |

### ArtCraft apps over MCP

Each skill maps the equivalent Adobe workflow to real commands of an [ArtCraft](https://getartcraft.com) app and was checked against the live command catalogue.

| Skill | What it covers | Typical triggers |
|---|---|---|
| [`vectorcraft-expert`](./skills/vectorcraft-expert/) | Illustrator-grade vector work in VectorCraft: logos, icons, illustrations, patterns, print files (CMYK, bleed, outlined type), SVG/PDF/PNG export. | `logo`, `icon`, `pathfinder`, `svg`, `pdf/x` |
| [`photocraft-expert`](./skills/photocraft-expert/) | Photoshop-grade retouching and compositing in PhotoCraft, raw development in LightCraft: layers and masks, cut-outs, smart-object mockups, export for web, social and print. | `retouch`, `cut-out`, `mask`, `mockup` |
| [`effectcraft-expert`](./skills/effectcraft-expert/) | After Effects-grade motion graphics in EffectCraft: animated text and logos, easing, masks, tracking, 3D camera, templates, Lottie and social renders. | `motion graphics`, `keyframes`, `animated logo`, `lottie` |
| [`filmcraft-expert`](./skills/filmcraft-expert/) | Premiere-grade editing in FilmCraft: rough to fine cut, 9:16 reels from 16:9, audio ducking and loudness, colour, chroma key, captions, export presets. | `video edit`, `subtitles`, `color grading`, `export` |
| [`designcraft-expert`](./skills/designcraft-expert/) | InDesign-grade layout in DesignCraft: parent pages, threaded text, paragraph and table styles, preflight, PDF/X and EPUB export, interactive PDF through PdfCraft. | `brochure`, `catalog`, `paragraph styles`, `preflight` |

### Code, docs and knowledge

| Skill | What it covers | Typical triggers |
|---|---|---|
| [`coding-with-agents`](./skills/coding-with-agents/) | Building software with AI coding agents: when AI helps or hurts, the working loop (context, specs, task shaping), reviewing and testing AI output, complexity, and how LLMs work for practitioners. | `coding agent`, `ai code review`, `token cost` |
| [`software-architecture`](./skills/software-architecture/) | System design and architecture reasoning: requirements and estimates, consistency and consensus, high availability and cascading failures, storage engines, sharding and geohash, caching, messaging, studies of real large-scale systems, chat/delivery/video case studies, RAG and agentic systems. | `system design`, `consistency`, `sharding`, `rag architecture` |
| [`awesome-readme`](./skills/awesome-readme/) | GitHub READMEs that read as written by a person: 8 templates, badge and GIF recipes, and an anti-slop audit pass on every draft. | `readme`, `github profile readme`, `humanize readme` |
| [`llm-wiki`](./skills/llm-wiki/) | An LLM-maintained knowledge base in an Obsidian vault (compile, don't retrieve): ingest, query and lint operations with hallucination spot-checks. | `obsidian`, `llm wiki`, `second brain` |
| [`jev`](./skills/jev/) | Sends typed yes/no, choice and score questions to TypeSafe's Jev model through OpenRouter, so the agent doesn't spend a full LLM turn on each: triage, routing, reranking, diff review. Needs `OPENROUTER_API_KEY`. | `classify`, `triage`, `rerank`, `yes/no gate` |

### People

| Skill | What it covers | Typical triggers |
|---|---|---|
| [`depth-psychology`](./skills/depth-psychology/) | A psychoanalytic lens on motives and relationships: ego and false ego, repression and projection, fears and addictions as symptoms, family dynamics, manipulation red flags, dreams. Separates the model's claims from mainstream psychology; not clinical advice. | `projection`, `inner child`, `manipulation`, `dream meaning` |

The ArtCraft apps ship updates almost daily, so every "not available" list in those five skills is a dated snapshot and the agent re-checks the live command catalogue before calling something missing. They are independent write-ups: no text from the Adobe Press books is reproduced. Adobe, Illustrator, Photoshop, After Effects, Premiere and InDesign are trademarks of Adobe; this repo isn't affiliated with Adobe or ArtCraft.

More coming when I build one that earns its place.

---

## Install

### Plugin marketplace (recommended)

One command set, every skill, native on Windows (no symlink permissions needed), updates via `/plugin`. Run inside Claude Code:

```text
/plugin marketplace add fralapo/awesome-agent-skills
/plugin install awesome-agent-skills@awesome-agent-skills
```

That installs the whole collection as a single plugin, so all skills become available at once. Update later with:

```text
/plugin marketplace update awesome-agent-skills
/plugin update awesome-agent-skills@awesome-agent-skills
```

Prefer just one skill? Use the manual method below and symlink/copy only that folder.

### Manual (symlink or copy)

Pick one. Replace `<skill>` with a folder name from [`skills/`](./skills/).

Commands below target Claude Code's default skills dir (`~/.claude/skills/`). Other agents: swap the destination for whatever path your tool reads (commonly `~/.config/<agent>/skills/` or `.agent/skills/` in a project root).

#### Symlink one skill (updates follow `git pull`)

**macOS / Linux:**
```sh
git clone https://github.com/fralapo/awesome-agent-skills.git ~/src/awesome-agent-skills
ln -s ~/src/awesome-agent-skills/skills/<skill> ~/.claude/skills/<skill>
```

**Windows (PowerShell, admin or developer mode):**
```powershell
git clone https://github.com/fralapo/awesome-agent-skills.git $env:USERPROFILE\src\awesome-agent-skills
New-Item -ItemType SymbolicLink `
  -Path "$env:USERPROFILE\.claude\skills\<skill>" `
  -Target "$env:USERPROFILE\src\awesome-agent-skills\skills\<skill>"
```

#### Copy (static snapshot, no auto-update)

**macOS / Linux:**
```sh
git clone https://github.com/fralapo/awesome-agent-skills.git
cp -r awesome-agent-skills/skills/<skill> ~/.claude/skills/
```

**Windows:**
```powershell
git clone https://github.com/fralapo/awesome-agent-skills.git
xcopy /E /I awesome-agent-skills\skills\<skill> $env:USERPROFILE\.claude\skills\<skill>
```

#### Symlink every skill at once (macOS / Linux)

```sh
git clone https://github.com/fralapo/awesome-agent-skills.git ~/src/awesome-agent-skills
for d in ~/src/awesome-agent-skills/skills/*/; do
  ln -s "$d" ~/.claude/skills/
done
```

Restart the agent after install. Most tools load skills at startup.

### Codex CLI (OpenAI)

Every `SKILL.md` here already uses the two fields [Codex's skill format](https://developers.openai.com/codex/skills) requires — `name` and `description` — so no content changes were needed. Codex just needs the folders somewhere it scans. This repo ships the symlinks already: `.agents/skills/<skill>` at repo root, one per skill, pointing at `skills/<skill>`.

**Project-scoped (works as soon as you clone):**

```sh
git clone https://github.com/fralapo/awesome-agent-skills.git
cd awesome-agent-skills
codex   # Codex scans ./.agents/skills automatically
```

**Global, for use from any directory:**

```sh
git clone https://github.com/fralapo/awesome-agent-skills.git ~/src/awesome-agent-skills
mkdir -p ~/.agents/skills
for d in ~/src/awesome-agent-skills/.agents/skills/*/; do
  ln -s "$(readlink -f "$d")" ~/.agents/skills/"$(basename "$d")"
done
```

Run `/skills` (or type `$`) inside Codex to confirm they loaded; restart Codex if a skill you just added doesn't show up. See Codex's docs for the full list of scan paths (repo, user, admin, system) and how to disable a skill via `~/.codex/config.toml`.

---

## How a skill is organized

```
skills/<skill-name>/
├── SKILL.md              # required: frontmatter (name, description) + workflow
└── references/           # optional: deep-dive files loaded only when relevant
    ├── patterns.md
    ├── templates.md
    └── examples.md
```

The book- and theory-based skills use `chapters/` plus a `cheatsheet.md` / `patterns.md` / `glossary.md` trio instead of `references/`; `creative-director` uses `roles/` and `books/`. Same idea: depth loaded only when the agent needs it. Every file is linked from `SKILL.md`, so nothing sits in the folder unreachable.

The frontmatter `description` field is the matcher: it says what the skill covers and when to use it, in at most 1024 characters. The agent reads only that to decide whether to load the skill.

The whole repo also ships as one installable plugin; see [Install](#install). The plugin manifests live in `.claude-plugin/` (`plugin.json` bundles every skill, `marketplace.json` lists it). For Codex CLI, `.agents/skills/<skill>` at the repo root is a symlink to the matching `skills/<skill>` folder — same content, no duplication, just a second, Codex-scanned path to the same files.

---

## How I build them

The pattern is consistent across every skill in this repo:

1. **Mine a real corpus.** Community awesome-lists, vendor docs, books, study notes. I don't write skills from imagination.
2. **Cluster what actually recurs.** Templates, anti-patterns, category-specific moves. Things a real prompter or writer reaches for ten times a week.
3. **Write `SKILL.md` short.** Frontmatter, when-to-use, quick rules, pointers into references. The agent reads this at load time; every extra paragraph costs context.
4. **Push depth into `references/`.** Topical files. Loaded on demand when the agent follows a link.
5. **Credit public sources, keep the rest as theory.** Open repos, papers, books and official docs are named. Material from private study notes is distilled into plain theory, in English, with no names attached.

If you're writing your own agent skills, those five steps are the only ones that have mattered for me. Everything else is decoration.

---

## Checks

`scripts/validate.py` runs on every push and pull request. It fails the build when a `SKILL.md` has broken frontmatter, a name that doesn't match its folder, a description over 1024 characters, a relative link that points nowhere, a missing Codex symlink, manifest versions that disagree, or a skill missing from this README. It also warns about files no other file in the skill links to.

```sh
python3 scripts/validate.py
```

Release notes are in [CHANGELOG.md](CHANGELOG.md).

---

## Contributing

This is my personal collection. Every skill here I author and mine myself. I'm not looking to absorb new skills from outside (vendor-tool wrappers especially aren't a fit). What does help:

- **Bug fix:** the smallest diff that fixes the thing.
- **Improvement to an existing skill:** cite the specific pattern or source that motivated it.

Open an issue first. If you've built your own skill, I'd rather link to your repo than fold it into mine.

---

## License

[MIT](LICENSE).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
