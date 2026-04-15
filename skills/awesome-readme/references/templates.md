# Full README Templates

Eight templates, one per project shape. Pick, paste, fill placeholders, delete unused sections.

Placeholders: `OWNER`, `REPO`, `PACKAGE`, `Project Name`, `tagline`, and URLs starting with `https://example.com`.

> **Before writing**: every prose paragraph in these templates is an illustrative example, not a slogan to ship as-is. After pasting, run the audit from [voice-and-prose.md](voice-and-prose.md). Replace the sample text with specific, honest claims about your project. Templates give you structure; your words earn the trust.

---

## 1. Library / SDK

```md
<a id="readme-top"></a>

<div align="center">
  <img src="docs/logo.svg" alt="Logo" width="120" height="120">
  <h1 align="center">Project Name</h1>
  <p align="center">
    Generates TypeScript types from a JSON sample. One command, no schema file required.
    <br />
    <a href="https://example.com/docs"><strong>Explore the docs »</strong></a>
    ·
    <a href="https://github.com/OWNER/REPO/issues/new?labels=bug">Report Bug</a>
    ·
    <a href="https://github.com/OWNER/REPO/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>

<p align="center">
  <a href="https://www.npmjs.com/package/PACKAGE"><img src="https://img.shields.io/npm/v/PACKAGE?style=for-the-badge" alt="npm version"></a>
  <a href="https://github.com/OWNER/REPO/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main&style=for-the-badge" alt="CI"></a>
  <a href="https://codecov.io/gh/OWNER/REPO"><img src="https://img.shields.io/codecov/c/github/OWNER/REPO?style=for-the-badge" alt="Coverage"></a>
  <a href="https://bundlephobia.com/package/PACKAGE"><img src="https://img.shields.io/bundlephobia/minzip/PACKAGE?style=for-the-badge" alt="Size"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/OWNER/REPO?style=for-the-badge" alt="License"></a>
</p>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#install">Install</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#api">API</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About

Most JSON-to-type tools want a schema. `PACKAGE` infers the types from a sample payload, so you can point it at a response from an API you don't control and get usable interfaces back.

- Zero runtime dependencies
- Handles nested unions and discriminated types
- On a 12 MB GraphQL response it finishes in ~400 ms; quicktype takes ~3 s on the same input (your numbers may vary, replace this line with your own benchmark or remove it)

### Built With

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)

## Install

```sh
npm install PACKAGE
```

```sh
pnpm add PACKAGE
```

```sh
yarn add PACKAGE
```

## Usage

```ts
import { transform } from 'PACKAGE';

const types = transform({
  user: { id: 1, name: 'Ada', roles: ['admin'] },
});

console.log(types);
// → interface User { id: number; name: string; roles: string[]; }
```

## API

### `transform(input, options?)`

| Param | Type | Description |
|---|---|---|
| `input` | `unknown` | JSON-serializable value |
| `options.rootName` | `string` | Name of the root interface. Default: `Root` |
| `options.emitEnums` | `boolean` | Convert string unions to `enum`. Default: `false` |

Returns: `string` — generated TypeScript source.

Full API: [docs](https://example.com/docs/api).

## Contributing

PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

<a href="https://github.com/OWNER/REPO/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=OWNER/REPO" alt="contrib.rocks"/>
</a>

## License

[MIT](LICENSE) © [Your Name](https://github.com/OWNER).

<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

---

## 2. CLI Tool

```md
<a id="readme-top"></a>

<h1 align="center">mytool</h1>
<p align="center">Scaffolds, builds, and deploys projects from a single YAML config.</p>

<p align="center">
  <img src="docs/demo.gif" alt="Demo" width="720">
</p>

<p align="center">
  <a href="https://github.com/OWNER/REPO/releases"><img src="https://img.shields.io/github/v/release/OWNER/REPO?style=for-the-badge" alt="Release"></a>
  <a href="https://github.com/OWNER/REPO/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main&style=for-the-badge" alt="CI"></a>
  <a href="https://github.com/OWNER/REPO/releases"><img src="https://img.shields.io/github/downloads/OWNER/REPO/total?style=for-the-badge" alt="Downloads"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/OWNER/REPO?style=for-the-badge" alt="License"></a>
</p>

## Install

**macOS (Homebrew):**
```sh
brew install OWNER/tap/mytool
```

**Linux / WSL:**
```sh
curl -sSL https://example.com/install.sh | sh
```

**Windows (Scoop):**
```powershell
scoop install mytool
```

**From source:**
```sh
go install github.com/OWNER/REPO/cmd/mytool@latest
```

## Quick Start

```sh
mytool init my-project
cd my-project
mytool build
```

## Commands

| Command | Description |
|---|---|
| `mytool init <name>` | Scaffold a new project |
| `mytool build` | Produce the dist bundle |
| `mytool deploy --env=prod` | Push to production |
| `mytool doctor` | Verify your environment |

Full help:

```sh
mytool --help
```

## Configuration

`mytool` looks for config in these places (first match wins):

1. `--config <path>` flag
2. `./mytool.yaml`
3. `$XDG_CONFIG_HOME/mytool/config.yaml`
4. `$HOME/.mytool.yaml`

```yaml
# mytool.yaml
log_level: info
output_dir: ./dist
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[Apache 2.0](LICENSE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

---

## 3. Web App

```md
<a id="readme-top"></a>

<p align="center">
  <img src="docs/banner.png" alt="App banner" width="100%">
</p>

<h1 align="center">App Name</h1>
<p align="center">
  A collaborative whiteboard that works offline and syncs when you're back online.
  <br>
  <a href="https://app.example.com"><strong>Live Demo »</strong></a>
</p>

<p align="center">
  <a href="https://github.com/OWNER/REPO/actions"><img src="https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main&style=for-the-badge" alt="CI"></a>
  <a href="https://vercel.com/OWNER/REPO"><img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Deploy"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/OWNER/REPO?style=for-the-badge" alt="License"></a>
</p>

## Screenshots

<table>
  <tr>
    <td><img src="docs/screen-1.png" alt="Home"></td>
    <td><img src="docs/screen-2.png" alt="Dashboard"></td>
  </tr>
</table>

## Features

- Real-time collaboration over WebRTC, with automatic fall-back to a relay server
- End-to-end encryption (rooms are keyed by URL fragment, never sent to the server)
- Offline editing with CRDT-based merge on reconnect
- Installable as a PWA

### Built With

![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

## Getting Started

### Prerequisites

- Node.js ≥ 20
- PostgreSQL ≥ 15
- A free API key from [example.com](https://example.com)

### Local Setup

1. Clone
   ```sh
   git clone https://github.com/OWNER/REPO.git
   cd REPO
   ```
2. Install
   ```sh
   pnpm install
   ```
3. Configure env
   ```sh
   cp .env.example .env
   # fill in DATABASE_URL, API_KEY
   ```
4. Migrate database
   ```sh
   pnpm db:migrate
   ```
5. Run dev server
   ```sh
   pnpm dev
   ```

App runs at <http://localhost:3000>.

## Deployment

- [Vercel](https://vercel.com/new/clone?repository-url=https://github.com/OWNER/REPO) — one-click
- Docker: `docker compose up`

## Roadmap

- [x] Auth
- [x] Real-time sync
- [ ] Mobile app
- [ ] Self-hostable bundle

See [open issues](https://github.com/OWNER/REPO/issues) for the full list.

## License

[MIT](LICENSE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

---

## 4. Desktop App

```md
<a id="readme-top"></a>

<div align="center">
  <img src="docs/logo.png" alt="Logo" width="120">
  <h1>App Name</h1>
  <p>A native desktop clipboard manager with fuzzy search and per-app history.</p>
</div>

<p align="center">
  <a href="https://github.com/OWNER/REPO/releases/latest"><img src="https://img.shields.io/github/v/release/OWNER/REPO?style=for-the-badge" alt="Release"></a>
  <a href="https://github.com/OWNER/REPO/releases"><img src="https://img.shields.io/github/downloads/OWNER/REPO/total?style=for-the-badge" alt="Downloads"></a>
</p>

## Download

| Platform | Link |
|---|---|
| **macOS (Apple Silicon)** | [AppName-arm64.dmg](https://github.com/OWNER/REPO/releases/latest) |
| **macOS (Intel)** | [AppName-x64.dmg](https://github.com/OWNER/REPO/releases/latest) |
| **Windows** | [AppName-Setup.exe](https://github.com/OWNER/REPO/releases/latest) |
| **Linux (AppImage)** | [AppName.AppImage](https://github.com/OWNER/REPO/releases/latest) |
| **Linux (deb)** | [appname.deb](https://github.com/OWNER/REPO/releases/latest) |

## Screenshot

<img src="docs/screenshot.png" alt="App screenshot" width="800">

## Features

- Fuzzy search over the last 10,000 clipboard items
- Per-app history with a configurable block-list (passwords, 2FA codes)
- Global shortcut (defaults to `Cmd+Shift+V`)
- Optional iCloud / OneDrive sync

## System Requirements

- macOS 12+, Windows 10+, or Linux with glibc ≥ 2.31
- 200 MB RAM
- 150 MB disk

## Build from Source

```sh
git clone https://github.com/OWNER/REPO.git
cd REPO
pnpm install
pnpm tauri build
```

## License

[GPL-3.0](LICENSE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

---

## 5. Research / ML Project

```md
<a id="readme-top"></a>

# Paper Title: Implementation & Experiments

Official implementation of our paper, **"Paper Title"**, accepted at *Venue 2025*.

[![arXiv](https://img.shields.io/badge/arXiv-2501.00000-b31b1b?style=for-the-badge)](https://arxiv.org/abs/2501.00000)
[![License](https://img.shields.io/github/license/OWNER/REPO?style=for-the-badge)](LICENSE)

<p align="center">
  <img src="docs/figure-1.png" alt="Teaser" width="720">
</p>

## Abstract

> One-paragraph abstract of the paper, exactly as submitted.

## Requirements

- Python 3.11+
- CUDA 12.1 (for GPU training)
- 24 GB VRAM recommended

```sh
conda env create -f environment.yml
conda activate projname
```

## Data

```sh
./scripts/download_data.sh
```

This downloads [Dataset Name](https://example.com/dataset) (~40 GB) into `data/`.

## Train

```sh
python train.py --config configs/main.yaml
```

Logs go to `runs/`. Tensorboard:

```sh
tensorboard --logdir runs/
```

## Evaluate

```sh
python eval.py --checkpoint checkpoints/best.pt --split test
```

## Reproduce Paper Results

| Experiment | Config | Command | Expected metric |
|---|---|---|---|
| Main table, row 1 | `configs/main.yaml` | `python train.py -c configs/main.yaml` | 87.3 ± 0.2 |
| Ablation — no X | `configs/no_x.yaml` | `python train.py -c configs/no_x.yaml` | 82.1 ± 0.4 |

## Pretrained Weights

| Model | Params | Download |
|---|---|---|
| `projname-base` | 120 M | [weights](https://example.com/weights/base.pt) |
| `projname-large` | 340 M | [weights](https://example.com/weights/large.pt) |

## Citation

```bibtex
@inproceedings{author2025paper,
  title     = {Paper Title},
  author    = {Author, Jane and Other, John},
  booktitle = {Proceedings of Venue},
  year      = {2025},
  url       = {https://arxiv.org/abs/2501.00000}
}
```

## License

[Apache 2.0](LICENSE)

## Acknowledgments

Built on [prior-work-repo](https://github.com/OWNER/prior-work). Thanks to collaborators and funding source.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

---

## 6. Template / Boilerplate Repo

```md
<a id="readme-top"></a>

<h1 align="center">Template Name</h1>
<p align="center">
  An opinionated starter for <i>stack description</i>.
</p>

<p align="center">
  <a href="https://github.com/OWNER/REPO/generate">
    <img src="https://img.shields.io/badge/Use_this_template-2ea44f?style=for-the-badge&logo=github&logoColor=white" alt="Use template">
  </a>
</p>

## What's inside

- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript strict
- **Styling**: Tailwind v4 + shadcn/ui
- **Database**: Drizzle + Postgres
- **Auth**: Clerk
- **Tests**: Vitest + Playwright
- **CI**: GitHub Actions (lint, typecheck, test, build)
- **Deploy**: Vercel, one click

## Quick Start

```sh
# 1. Click "Use this template" above, or:
gh repo create my-app --template OWNER/REPO

# 2. Install
cd my-app && pnpm install

# 3. Env
cp .env.example .env

# 4. Dev
pnpm dev
```

## Project Structure

```
src/
├── app/              # Next.js routes
├── components/       # UI
├── lib/              # Utilities + client singletons
├── server/           # Server-side logic
└── tests/            # Unit + E2E
```

## What to change after cloning

- [ ] `package.json` → `name`, `author`, `repository`
- [ ] `README.md` (this file)
- [ ] `src/app/layout.tsx` → title + metadata
- [ ] `public/` → favicon, og-image
- [ ] `.env.example` → remove any template-specific keys

## License

[MIT](LICENSE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

---

## 7. Monorepo

```md
<a id="readme-top"></a>

# projname monorepo

Workspace for the `projname` family of packages.

<p align="center">
  <a href="https://github.com/OWNER/REPO/actions"><img src="https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main&style=for-the-badge" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/OWNER/REPO?style=for-the-badge" alt="License"></a>
</p>

## Packages

| Package | Version | Description |
|---|---|---|
| [`@projname/core`](packages/core) | [![npm](https://img.shields.io/npm/v/@projname/core)](https://www.npmjs.com/package/@projname/core) | Core runtime |
| [`@projname/cli`](packages/cli) | [![npm](https://img.shields.io/npm/v/@projname/cli)](https://www.npmjs.com/package/@projname/cli) | Command-line interface |
| [`@projname/react`](packages/react) | [![npm](https://img.shields.io/npm/v/@projname/react)](https://www.npmjs.com/package/@projname/react) | React bindings |

## Layout

```
.
├── apps/            # End-user apps (docs, playground)
├── packages/        # Published npm packages
├── internal/        # Shared configs (tsconfig, eslint)
└── .github/
```

## Dev

```sh
pnpm install
pnpm -w build           # build all
pnpm -w test            # test all
pnpm --filter core dev  # dev a single package
```

## Release

Changesets-based. Open a PR, run `pnpm changeset`, merge. CI publishes on tag.

## License

[MIT](LICENSE)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

---

## 8. Profile README

See [profile-readme.md](profile-readme.md) for the full template and patterns.

---

## Usage hint

After pasting a template:

1. Replace every `OWNER`, `REPO`, `PACKAGE`, `example.com`, `Your Name`
2. Replace every image path with a real asset, or remove the `<img>` tag
3. **Rewrite the prose.** The example paragraphs in these templates are illustrative only. Run the audit from [voice-and-prose.md](voice-and-prose.md) on your version. Cut promotional adjectives, replace vague claims with specific ones, vary sentence rhythm.
4. Trim sections you don't have content for. Empty headers hurt more than missing ones.
5. Verify every badge URL loads (open it in a browser)
6. Check all anchor links (`#section-name`) resolve
