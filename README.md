<a id="readme-top"></a>

<h1 align="center">awesome-agent-skills</h1>

<p align="center">
  A small, opinionated set of agent skills I actually use.
  Each one is mined from a real corpus (community awesome-lists, official docs, books, field notes), anywhere from a couple hundred examples to tens of thousands. None of it written from imagination.
  <br>
  Built on <a href="https://docs.claude.com/en/docs/claude-code/skills">Claude Code's skill format</a>, installable as a plugin and usable by any agent that reads <code>SKILL.md</code>.
</p>

<p align="center">
  <a href="https://github.com/fralapo/awesome-agent-skills/stargazers"><img src="https://img.shields.io/github/stars/fralapo/awesome-agent-skills?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/fralapo/awesome-agent-skills/commits/main"><img src="https://img.shields.io/github/last-commit/fralapo/awesome-agent-skills?style=for-the-badge" alt="Last commit"></a>
  <img src="https://img.shields.io/badge/skills-10-2ea44f?style=for-the-badge" alt="Skills count">
  <img src="https://img.shields.io/badge/agent%20skills-SKILL.md-5A67D8?style=for-the-badge" alt="Agent skills format">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/fralapo/awesome-agent-skills?style=for-the-badge" alt="License"></a>
</p>

---

## Contents

- [What's in here](#whats-in-here)
- [Install](#install)
  - [Plugin marketplace (recommended)](#plugin-marketplace-recommended)
  - [Manual (symlink or copy)](#manual-symlink-or-copy)
- [How a skill is organized](#how-a-skill-is-organized)
- [How I build them](#how-i-build-them)
- [Contributing](#contributing)
- [License](#license)

---

## What's in here

Ten skills. Each is a single folder with a `SKILL.md` (frontmatter + workflow) plus deep-dive material (a `references/` directory, or `chapters/` + cheatsheet/patterns/glossary for the book-distilled ones). The agent (Claude Code, or any tool that reads the same format) matches the `description` field against whatever you're asking and loads the skill only when it's relevant. No eager bloat.

| Skill | What it does | Corpus mined | Typical trigger |
|---|---|---|---|
| [`seedance-prompts`](./skills/seedance-prompts/) | Prompt templates for **ByteDance Seedance 2.0** video gen: storyboards, camera-move vocab, multi-modal refs. | ~195 prompts across 3 awesome-lists | `seedance`, `bytedance video`, `text-to-video prompt` |
| [`image-gen-prompts`](./skills/image-gen-prompts/) | Prompt engineering for any major image model (Midjourney, GPT Image, FLUX, SDXL, Seedream, Imagen, Ideogram...). 28+ templates, auto-routes by model named. | ~18,900 prompts across 10 sources | `image prompt`, `nano banana`, `midjourney`, `flux`, `sdxl`, `ideogram`, `dall-e`, `mockup` |
| [`awesome-readme`](./skills/awesome-readme/) | Write GitHub READMEs that land on awesome-lists and sound human, not AI-generated. 8 templates + badge/GIF recipes + anti-slop audit pass. | Best-README-Template + ~100 awesome-readme entries + Standard-Readme | `readme`, `awesome readme`, `github readme`, `humanize readme` |
| [`llm-wiki`](./skills/llm-wiki/) | Persistent LLM-maintained knowledge base in an Obsidian vault, Karpathy's "compile, don't retrieve" pattern. `ingest`/`query`/`lint` ops, hallucination spot-checks. | Karpathy's llm-wiki gist + 3 production Obsidian-wiki repos + field-tested corrections | `obsidian`, `llm wiki`, `karpathy wiki`, `second brain`, `pkm`, `wiki ingest` |
| [`creative-director`](./skills/creative-director/) | Router into 5 role toolkits (copywriter, idea generator, creative leader, visionary, evaluator), each loading only its own book digest. | 16 books + smixs evaluation engine + 23 TED talks | `creative director`, `headline`, `copywriting`, `evaluate concept`, `typography`, `visual literacy` |
| [`social-algorithm`](./skills/social-algorithm/) | Organic personal-brand growth + Instagram algorithm dynamics: indirect selling, acquisition funnels, hook patterns, delegation systems. | Practitioner field notes + tested operational frameworks | `personal brand`, `instagram algorithm`, `organic acquisition`, `hero's journey`, `manychat` |
| [`ffmpeg`](./skills/ffmpeg/) | Full FFmpeg CLI reference: codecs, formats, filtergraphs, protocols, capture devices, plus full official docs bundled for grep. | Official FFmpeg documentation, all tools & libraries | `ffmpeg`, `ffprobe`, `transcode`, `filtergraph`, `-map`, `hls`, `crf`, `nvenc` |
| [`video-editor`](./skills/video-editor/) | Software-agnostic decision system for editing viral video: hook system, pacing, motion, captions, sound design, transitions. | 25 expert YouTube video-editing breakdowns, deduped | `video editing`, `reel`, `retention`, `hook`, `pacing`, `b-roll`, `motion graphics` |
| [`public-speaking-persuasion`](./skills/public-speaking-persuasion/) | Public speaking + persuasion theory: speech structure, logical-fallacy/cognitive-bias catalogs, objection handling, pitching. | 51 theoretical transcripts on communication and persuasion | `public speaking`, `persuasion`, `pitch`, `logical fallacy`, `objection handling` |
| [`marketing-mba`](./skills/marketing-mba/) | MBA-level marketing + startup execution: segmentation, pricing, value proposition, sales pipeline, negotiation, founder frameworks. | 90 theoretical marketing/startup/business transcripts | `marketing`, `value proposition`, `pricing strategy`, `go-to-market`, `negotiation`, `porter five forces` |

More coming when I build one that earns its place. I'd rather ship seven that work than twenty that almost do.

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

Pick one. Replace `<skill>` with the skill name (`seedance-prompts`, `image-gen-prompts`, `awesome-readme`, `llm-wiki`, `social-algorithm`, `creative-director`, `ffmpeg`, `video-editor`, `public-speaking-persuasion`, or `marketing-mba`).

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

Some skills carry extra on-demand files alongside or instead of `references/`: a `glossary.md` / `patterns.md` / `cheatsheet.md` trio (`creative-director`, `ffmpeg`), a `chapters/` directory (`ffmpeg`), or `roles/` + `books/` (`creative-director`). Same idea: depth loaded only when the agent needs it.

The frontmatter `description` field is the matcher. Keep it specific and keyword-dense; the agent uses it to decide whether to load the skill at all.

The whole repo also ships as one installable plugin; see [Install](#install). The plugin manifests live in `.claude-plugin/` (`plugin.json` bundles every skill, `marketplace.json` lists it).

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

This is my personal collection. Every skill here I author and mine myself. I'm not looking to absorb new skills from outside (vendor-tool wrappers especially aren't a fit). What does help:

- **Bug fix:** the smallest diff that fixes the thing.
- **Improvement to an existing skill:** cite the specific pattern or source that motivated it.

Open an issue first. If you've built your own skill, I'd rather link to your repo than fold it into mine.

---

## License

[MIT](LICENSE).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
