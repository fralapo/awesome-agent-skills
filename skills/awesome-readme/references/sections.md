# README Section Catalog

Every section a GitHub README can contain — purpose, when to include, and a ready-to-paste snippet.

Sections are listed in recommended rendering order. Cherry-pick by project type.

---

## 1. Above the fold

### 1.1 Anchor + top-link target

Drop in first line so every "back to top" link resolves:

```md
<a id="readme-top"></a>
```

### 1.2 Title

H1 = repo name. Use ASCII unless the project is intentionally stylized.

```md
# Project Name
```

Centered variant (stronger visual identity):

```md
<h1 align="center">Project Name</h1>
```

### 1.3 Badges row

5–8 badges max. Keep on one visual line. See [badges.md](badges.md).

```md
<p align="center">
  [![Build][build-shield]][build-url]
  [![Version][version-shield]][version-url]
  [![License][license-shield]][license-url]
  [![Stars][stars-shield]][stars-url]
</p>
```

### 1.4 Logo / Banner

Either/or — not both. Logo = small square, banner = hero strip.

```md
<div align="center">
  <a href="https://github.com/owner/repo">
    <img src="docs/logo.svg" alt="Logo" width="120" height="120">
  </a>
</div>
```

Banner:

```md
<p align="center">
  <img src="docs/banner.png" alt="Project banner" width="100%">
</p>
```

### 1.5 Tagline

One sentence. Under 120 chars. Matches package-manager description. Say what it does, not how impressive it is — see [voice-and-prose.md](voice-and-prose.md) before writing.

```md
<p align="center">
  Generate TypeScript types from a JSON sample. No schema file required.
</p>
```

### 1.6 Links bar

Standard four-link bar. Remove any link that doesn't exist.

```md
<p align="center">
  <a href="https://example.com"><strong>Docs »</strong></a>
  ·
  <a href="https://demo.example.com">Live Demo</a>
  ·
  <a href="https://github.com/owner/repo/issues/new?labels=bug">Report Bug</a>
  ·
  <a href="https://github.com/owner/repo/issues/new?labels=enhancement">Request Feature</a>
</p>
```

### 1.7 Elevator pitch

2–4 sentences. What it does, who it's for, and one concrete reason it beats the obvious alternative. Resist promotional adjectives; lean on specific capabilities and numbers.

```md
`json2ts` takes a JSON file and prints the matching TypeScript interface. Useful when you're
consuming an API whose responses you can sample but can't get a schema for. Handles nested
unions and optional fields correctly on about 94% of the payloads in our test corpus; the
rest are usually edge cases around `null` vs missing keys.
```

---

## 2. Navigation

### 2.1 Table of Contents (collapsible)

Required when README > 100 lines. Use `<details>` to keep the above-the-fold clean.

```md
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>
```

---

## 3. About / Overview

### 3.1 About the Project

Longer version of the pitch. Problem, solution, one specific differentiator. Cut every adjective that could apply to any other tool in the same space.

```md
## About The Project

[![Product Screenshot][product-screenshot]](https://example.com)

Most JSON-to-type tools want a schema. `json2ts` infers the types from a sample payload, which
is what you actually have when you're consuming a third-party API nobody bothered to document.

What it does well:
- Zero runtime dependencies
- Nested unions and discriminated types
- Streams payloads bigger than available RAM

What it doesn't do:
- Produce TypeScript from OpenAPI or JSON Schema (use quicktype for that)
- Emit runtime validators (use Zod)
```

### 3.2 Built With

Tech-stack badges. Users scan this in 1 second to decide if your project lives in their world.

```md
### Built With

* [![TypeScript][ts-shield]][ts-url]
* [![Node.js][node-shield]][node-url]
* [![Vitest][vitest-shield]][vitest-url]
```

---

## 4. Visuals / Demo

### 4.1 Screenshot

```md
<p align="center">
  <img src="docs/screenshot.png" alt="App screenshot" width="800">
</p>
```

### 4.2 Demo GIF

```md
<p align="center">
  <img src="docs/demo.gif" alt="CLI demo" width="720">
</p>
```

### 4.3 Video (YouTube thumbnail trick)

```md
[![Watch the demo](docs/video-thumb.png)](https://www.youtube.com/watch?v=VIDEO_ID)
```

### 4.4 Feature grid (image table)

```md
<table>
  <tr>
    <td><img src="docs/feat-1.png" alt="Feature 1"></td>
    <td><img src="docs/feat-2.png" alt="Feature 2"></td>
  </tr>
</table>
```

---

## 5. Getting Started

### 5.1 Prerequisites

```md
### Prerequisites

- Node.js ≥ 20
- npm ≥ 10 (or pnpm / yarn)
- A `.env` file — copy from `.env.example`
```

### 5.2 Installation

Numbered steps. Each command in its own fenced block with language tag.

```md
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/owner/repo.git
   ```
2. Install dependencies
   ```sh
   npm install
   ```
3. Copy env template
   ```sh
   cp .env.example .env
   ```
4. Start the dev server
   ```sh
   npm run dev
   ```
```

### 5.3 Quick Start (single-command variant)

For packages:

```md
### Quick Start

```sh
npm install @scope/pkg
```

```ts
import { transform } from '@scope/pkg';
const result = transform({ foo: 1 });
```
```

---

## 6. Usage

### 6.1 Basic usage

```md
## Usage

```ts
import { transform } from '@scope/pkg';

const types = transform({
  user: { id: 1, name: 'Ada', roles: ['admin'] }
});

console.log(types);
// → interface User { id: number; name: string; roles: string[]; }
```
```

### 6.2 CLI subcommand table

```md
| Command | What it does |
|---|---|
| `mytool init` | Scaffold a new project |
| `mytool build` | Produce the dist bundle |
| `mytool deploy --env=prod` | Push to production |
```

### 6.3 More examples link

```md
_For more examples, see the [docs](https://example.com/docs)._
```

---

## 7. Configuration

```md
## Configuration

| Env var | Default | Description |
|---|---|---|
| `LOG_LEVEL` | `info` | One of `debug`, `info`, `warn`, `error` |
| `CACHE_DIR` | `~/.cache/mytool` | Where compiled output lives |
| `NO_COLOR` | unset | Disable ANSI colors |
```

---

## 8. API Reference

Short inline, or link out.

```md
## API

See the full [API reference](https://example.com/api) or the inline types.

### `transform(input, options?)`

| Param | Type | Description |
|---|---|---|
| `input` | `unknown` | JSON-serializable value |
| `options.rootName` | `string` | Name of the root interface. Default: `Root` |

Returns: `string` — generated TypeScript source.
```

---

## 9. Roadmap

Checkbox list. Keep short (5–10). Link to issues for the full list.

```md
## Roadmap

- [x] JSON → TypeScript
- [x] JSON → Zod schema
- [ ] JSON → Go structs
- [ ] Watch mode
- [ ] VS Code extension

See the [open issues](https://github.com/owner/repo/issues) for the full list.
```

---

## 10. Contributing

Short in-README, full rules in `CONTRIBUTING.md`.

```md
## Contributing

Contributions are what make open source thrive. Any contribution is **greatly appreciated**.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingThing`)
3. Commit your changes (`git commit -m 'feat: add amazing thing'`)
4. Push to the branch (`git push origin feature/AmazingThing`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

### Top contributors

<a href="https://github.com/owner/repo/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=owner/repo" alt="contrib.rocks" />
</a>
```

---

## 11. License

Last section, always. Match whatever `LICENSE` file declares.

```md
## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
```

---

## 12. Contact

```md
## Contact

Jane Doe — [@janedoe](https://twitter.com/janedoe) — jane@example.com

Project link: [https://github.com/owner/repo](https://github.com/owner/repo)
```

---

## 13. Acknowledgments

Only if there's real content. Empty acknowledgments = worse than none.

```md
## Acknowledgments

- [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
```

---

## 14. Star history (for popular repos)

```md
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=owner/repo&type=Date)](https://star-history.com/#owner/repo&Date)
```

---

## 15. FAQ

Wrap long FAQs in `<details>`.

```md
## FAQ

<details>
<summary>Why another JSON-to-type tool?</summary>

The existing tools (quicktype, json-schema-to-typescript) require schemas.
This one infers everything from a sample payload.
</details>

<details>
<summary>Does it handle circular refs?</summary>

Yes — circular references are detected and replaced with a forward-declared interface.
</details>
```

---

## 16. Security

```md
## Security

Please report vulnerabilities via email to `security@example.com`.
Do not open public issues for security matters. See [`SECURITY.md`](SECURITY.md).
```

---

## 17. Code of Conduct

```md
## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md).
```

---

## Back-to-top pattern

Place at the end of each major section once README > 300 lines:

```md
<p align="right">(<a href="#readme-top">back to top</a>)</p>
```

---

## Section ordering heuristic

```
1. Anchor + Title + Badges + Logo/Banner + Tagline + Links bar
2. Elevator pitch
3. TOC (if needed)
4. About / Built With
5. Visuals / Demo
6. Getting Started (Prerequisites + Installation)
7. Usage (basic → advanced)
8. Configuration
9. API (or link)
10. Roadmap
11. Contributing + Contributors widget
12. License
13. Contact
14. Acknowledgments
15. (Optional) Star history, FAQ, Security, Code of Conduct
```

Cut sections you don't need — **do not invent content to fill them**.

Before writing any prose section, skim [voice-and-prose.md](voice-and-prose.md). Most AI tells sneak into Tagline, Elevator pitch, About, and Features.
