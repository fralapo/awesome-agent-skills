<a id="readme-top"></a>

<h1 align="center">awesome-agent-skills</h1>

<p align="center">
  A small, opinionated set of agent skills I actually use.
  Each one is mined from a corpus of 200+ real community examples, not generated from scratch.
  <br>
  Built on <a href="https://docs.claude.com/en/docs/claude-code/skills">Claude Code's skill format</a>, works with any agent that reads <code>SKILL.md</code> + <code>references/</code>.
</p>

<p align="center">
  <a href="https://github.com/fralapo/awesome-agent-skills/stargazers"><img src="https://img.shields.io/github/stars/fralapo/awesome-agent-skills?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/fralapo/awesome-agent-skills/commits/main"><img src="https://img.shields.io/github/last-commit/fralapo/awesome-agent-skills?style=for-the-badge" alt="Last commit"></a>
  <img src="https://img.shields.io/badge/skills-6-2ea44f?style=for-the-badge" alt="Skills count">
  <img src="https://img.shields.io/badge/agent%20skills-SKILL.md-5A67D8?style=for-the-badge" alt="Agent skills format">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/fralapo/awesome-agent-skills?style=for-the-badge" alt="License"></a>
</p>

---

## What's in here

Six skills. Each is a single folder with a `SKILL.md` (frontmatter + workflow) plus a `references/` directory for deep-dive material. The agent (Claude Code, or any tool that reads the same format) matches the `description` field against whatever you're asking and loads the skill only when it's relevant. No eager bloat.

| Skill | What it does | Corpus mined | Typical trigger |
|---|---|---|---|
| [`seedance-prompts`](./skills/seedance-prompts/) | Prompt templates for **ByteDance Seedance 2.0** video generation. Timecoded 3-shot storyboards, camera-move vocab, 15 category templates, multi-modal references (`@图片`/`@视频`/`@audio`), 12 curated examples. | ~195 prompts across 3 awesome-lists | `seedance`, `bytedance video`, `text-to-video prompt` |
| [`image-gen-prompts`](./skills/image-gen-prompts/) | Generic prompt engineering for **any** major image generation/editing model — Nano Banana / Pro / 2, GPT Image 2 / 1.5 / 1 / DALL·E 3, Midjourney v6/v7 + Niji, SDXL / SD3 / SD3.5, FLUX.1, Imagen 3/4, Ideogram 2/3, Recraft v3, Seedream 4.x/5.0. Universal prompt anatomy, 28+ fill-in templates (portrait, exploded-view product diagram, bento infographic, RAW iPhone candid, character expression sheet, e-commerce hero, YouTube thumbnail, knowledge card, 3D diorama, split-view render, packaging design, mockup family — apparel/drinkware/screen/wall art/print/OOH, style-to-UI design system, livestream + gacha-game UI, character reference card, JSON-recreate-from-image…), identity-preservation per model, structured JSON/YAML/XML shapes, text-rendering tier matrix, editing-workflow matrix, 24 worked examples, plus three conversation modes (Direct Generation / Content Illustration / Remix) and pointers to public corpora (12,000+ searchable prompts) when the user wants proven templates rather than fresh composition. **Auto-routes by model** when the user names one (Midjourney, GPT Image 2, FLUX, Seedream, etc.). | ~18,900 prompts across 10 awesome-lists/skills + 3 reference sites | `image prompt`, `nano banana`, `gpt image 2`, `seedream`, `midjourney`, `flux`, `sdxl`, `imagen`, `ideogram`, `dall-e`, `packaging`, `mockup`, `chatgpt image`, `gen_id`, `content illustration` |
| [`awesome-readme`](./skills/awesome-readme/) | Write GitHub READMEs that land on awesome-lists and still sound human. 8 full templates (library/CLI/webapp/desktop/research/template-repo/monorepo/profile), shields.io badge library, banner/logo/GIF recipes, profile-README widget catalog, anti-patterns, and a dedicated anti-AI-slop audit pass integrating the `humanizer` skill's Wikipedia *Signs of AI writing* patterns. | Best-README-Template + ~100 awesome-readme entries + Standard-Readme + Make-a-README + RDD essay | `readme`, `awesome readme`, `github readme`, `humanize readme` |
| [`llm-wiki`](./skills/llm-wiki/) | Build a persistent, LLM-maintained knowledge base in an Obsidian vault following the **LLM Wiki pattern** by Andrej Karpathy ("compile, don't retrieve"). Three-layer architecture (`raw/` immutable sources → `wiki/` LLM-owned interlinked markdown → `CLAUDE.md` schema). Operations: `ingest` (one source at a time with confirmation gates — batching corrupts `raw/`), `query` (index-first routing, `[[backlinks]]` traversal, inline citations), `lint` (hallucination spot-check against `raw/`, invented-wikilink sanitisation, orphans, contradictions, stale claims via `superseded_by:`). Mandatory frontmatter with `summary:` field for cheap index scans, optional `confidence` scoring and `lifecycle` states (draft/reviewed/verified/disputed/archived). Explicit failure-mode warning (context saturation → silent summarisation → `raw/` overwrite) and security rule treating source content as untrusted input. Page templates for source/concept/entity/synthesis, `[[Wikilinks]]` discipline, append-only `log.md` parseable with `grep "^## \["`. Ships a `vault-CLAUDE.md.template` to drop into any new vault. Pairs with the optional `llm-wiki-detect.ps1` SessionStart hook that notices `.obsidian/` in cwd and suggests bootstrap. | Karpathy's [llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) + production patterns mined from [obsidian-llm-wiki-local](https://github.com/kytmanov/obsidian-llm-wiki-local) (confidence scoring, manual-edit protection, wikilink sanitisation, atomic writes) and [obsidian-wiki](https://github.com/ar9av/obsidian-wiki) (lifecycle states, tiered retrieval, untrusted-input rule) + field-tested workflow corrections from [Paolo Dalprato's ai-know.pro post-mortem](https://ai-know.pro) (200 articles + 5 manuals ingested, one-at-a-time as default) and [Urvil Joshi's walkthrough](https://medium.com/@urviljoshi) (compilation analogy, honest RAG vs Wiki tradeoffs) + ~30 community implementations (ΩmegaWiki, Eshel, Synthadoc, PulseOS, llm-wiki-manager, sigma-guard) from the comment thread | `obsidian`, `llm wiki`, `/llm-wiki`, `karpathy wiki`, `obsidian vault`, `ingest`, `ingest sources`, `inizializza wiki`, `compile knowledge base`, `second brain`, `personal wiki`, `pkm`, `note vault`, `wiki ingest`, `wiki lint` |
| [`creative-director`](./skills/creative-director/) | Multi-role creative-director knowledge base distilled from **12 books** on advertising, creative leadership, idea generation, and taste, plus an **evaluation engine** adapted from [smixs/creative-director-skill](https://github.com/smixs/creative-director-skill). Router architecture: a small always-loaded `SKILL.md` sends the agent to one of five role toolkits — **Copywriter** (Ogilvy on Advertising, Guts), **Idea Generator** (Creative Mischief, A Smile in the Mind, Predictably Irrational + Pollard/JTBD/tension insight layer), **Creative Leader** (Fired Up, The Making of a Manager, Tribal Leadership, Crucial Conversations), **Visionary** (The Creative Act, The Eye, Steve Jobs), **Evaluator** (HumanKind/Grey calibration, 6-criteria weighted scoring, recursive refine-to-9 loop) — and loads only that role plus, when needed, a single book digest. A typical task costs a few thousand tokens instead of the 1.28M-token source corpus. Ships glossary (~95 terms), patterns.md (~50 techniques), cheatsheet.md, and `references/ted-talks.md` (23 designer/creative TED talks distilled, grouped by role). *Tested Advertising Methods* was in the source folder but shipped as a scanned, text-free PDF, so it's excluded until OCR'd. | 12 books across advertising, creative leadership, idea generation, and taste + smixs evaluation engine + 23 designer TED talks | `creative director`, `headline`, `copywriting`, `brainstorm`, `creative angle`, `find the insight`, `score this idea`, `evaluate concept`, `is it good enough`, `lead creative team`, `feedback on concept`, `difficult conversation`, `team culture`, `develop taste`, `creative vision`, `judge quality`, `ogilvy`, `rick rubin`, `steve jobs` |
| [`social-algorithm`](./skills/social-algorithm/) | Knowledge base for **organic personal-brand acquisition + Instagram algorithm dynamics**. Seven chapters of field-tested practitioner material: indirect selling (4 elements — direct experience, need, hero's journey, social proof as garnish), the epochal algorithm shift (interest-based distribution, dopamine-driven users, -20/24% engagement drop), creator systems & delegation (revenue/hours formula vs content/hours, 3-stage delegation ladder, Inside Out / Reference / Pillar ideation, Reference Based / Author Mode / AI-assisted scripting, full-day blocking), end-to-end acquisition system ("I See You / I Validate You / I Associate You" triangle, 4 Circles of Hell anti-patterns, 5 awareness levels, 6 acquisition funnels including profile / follower outreach / ManyChat / Stories / lead magnet / quiz funnel, ADV integration prospecting + retargeting), dynamic video techniques (visual elements + metaphors, framing changes, custom B-roll, trailer-style scripts), 5 scaling principles, and a working algorithm knowledge base (3 pillar metrics — saves / watch time / shares — diagnostic matrix "lots of X but few Y" with a targeted fix per signal, discovery-first repost strategy, 8 non-inflated hook patterns, era-by-era evolution of platform dynamics). Plus glossary (~60 terms), patterns.md (33 operational techniques), cheatsheet.md (quick-reference tables). | Practitioner field notes + tested operational frameworks | `personal brand`, `indirect selling`, `instagram algorithm`, `organic acquisition`, `client acquisition`, `social algorithm`, `organic funnel`, `saves watch time`, `recognizability`, `hero's journey`, `personal brand positioning`, `i see you i validate you i associate you`, `circles of hell`, `manychat` |

More coming when I build one that earns its place. I'd rather ship four that work than twenty that almost do.

---

## Install

Pick one. Replace `<skill>` with the skill name (`seedance-prompts`, `image-gen-prompts`, `awesome-readme`, `llm-wiki`, `social-algorithm`, or `creative-director`).

Commands below target Claude Code's default skills dir (`~/.claude/skills/`). Other agents: swap the destination for whatever path your tool reads (commonly `~/.config/<agent>/skills/` or `.agent/skills/` in a project root).

### Symlink one skill (recommended — updates follow `git pull`)

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

### Copy (static snapshot, no auto-update)

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

### Symlink every skill at once (macOS / Linux)

```sh
git clone https://github.com/fralapo/awesome-agent-skills.git ~/src/awesome-agent-skills
for d in ~/src/awesome-agent-skills/skills/*/; do
  ln -s "$d" ~/.claude/skills/
done
```

Restart the agent after install. Most tools load skills at startup.

---

## How a skill is organized

```
skills/<skill-name>/
├── SKILL.md              # required — frontmatter (name, description) + workflow
└── references/           # optional — deep-dive files loaded only when relevant
    ├── patterns.md
    ├── templates.md
    └── examples.md
```

The frontmatter `description` field is the matcher. Keep it specific and keyword-dense; the agent uses it to decide whether to load the skill at all.

---

## How I build them

The pattern is consistent across every skill in this repo:

1. **Mine a real corpus.** Community awesome-lists, vendor docs, internal notes. Several hundred examples minimum. I don't write skills from imagination.
2. **Cluster what actually recurs.** Templates, anti-patterns, category-specific moves. Things a real prompter or writer reaches for ten times a week.
3. **Write `SKILL.md` short.** Frontmatter, when-to-use, quick rules, pointers into references. The agent reads this at load time; every extra paragraph costs context.
4. **Push depth into `references/`.** Topical files. Loaded on demand when the agent follows a link.
5. **Cite sources.** When a template or pattern came from a specific public repo, it gets named in `examples.md` or the frontmatter `analyzed_repos` list.

If you're writing your own agent skills, those five steps are the only ones that have mattered for me. Everything else is decoration.

---

## Contributing

Personal repo, but useful PRs get in. The bar:

- **New skill:** must match the structure above and cite its corpus
- **Skill improvement:** cite the specific pattern that motivated the change
- **Bug fix:** the smallest diff that fixes the thing

Open an issue before a large PR so neither of us wastes time.

---

## License

[MIT](LICENSE).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
