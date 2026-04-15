# Voice & Prose: Write README Text That Sounds Human

A README riddled with AI tells destroys trust faster than any bad badge layout. Readers spot LLM slop in seconds — promotional adjectives, synonym cycling, fake significance, tacked-on "-ing" analyses — and decide the project is vaporware or a student demo.

This reference adapts the [humanizer skill](../../humanizer/) to the specific context of README prose. Apply every pattern here during drafting, and audit every draft before writing to disk.

> **Core move:** after drafting any README section, ask yourself: *"What makes this obviously AI generated?"* Answer briefly, then rewrite.

---

## The 10 AI Tells That Kill READMEs

Ordered by how often they sink README prose specifically.

### 1. Promotional / marketing-brochure adjectives

**Tells:** `blazing-fast`, `cutting-edge`, `seamless`, `intuitive`, `powerful`, `robust`, `elegant`, `beautiful`, `stunning`, `next-generation`, `state-of-the-art`, `best-in-class`, `world-class`, `vibrant`, `rich`, `groundbreaking`, `revolutionary`.

**Why it's bad in a README:** everyone says this about their tool. It carries no signal.

**Before:**
> A blazing-fast, cutting-edge CLI that provides a seamless and intuitive experience for transforming JSON into types.

**After:**
> A CLI that converts a JSON sample into TypeScript types. One command, no schema, no config file.

**Rule:** replace every vague adjective with a specific capability or a measured number. "Fast" means nothing. "Converts 10 MB payloads in under 400 ms" means something.

---

### 2. Significance inflation

**Tells:** `pivotal`, `crucial`, `vital`, `essential`, `marks a`, `stands as`, `serves as`, `represents a`, `underscores`, `highlights the importance of`, `testament to`, `evolution of`, `landscape`, `ecosystem`, `journey`, `paradigm shift`.

**Why it's bad:** nobody's README is actually pivotal. This language reads as aspirational cope.

**Before:**
> This library represents a pivotal step in the evolution of the data-processing landscape, underscoring the crucial role of type safety.

**After:**
> This library generates TypeScript types from JSON samples.

---

### 3. Copula avoidance

**Tells:** `serves as`, `stands as`, `represents`, `functions as`, `boasts`, `features`, `offers`, `delivers`.

**Why it's bad:** "is" and "are" are fine. LLMs avoid them because plain copulas aren't "elevated" enough. Plain copulas are *exactly* what README prose needs.

**Before:**
> `json2ts` serves as a lightweight alternative that boasts zero dependencies and features a minimal API.

**After:**
> `json2ts` is a lightweight alternative. Zero dependencies. One public function.

---

### 4. Superficial "-ing" analyses

**Tells:** sentences that end with a trailing participle phrase: `..., highlighting X`, `..., underscoring Y`, `..., ensuring Z`, `..., providing A`, `..., enabling B`, `..., empowering users to C`.

**Why it's bad:** the trailing `-ing` clause pretends to add depth while restating the main clause in fancier words.

**Before:**
> The tool parses JSON and emits types, streamlining the workflow and empowering developers to move faster.

**After:**
> The tool parses JSON and emits types.

---

### 5. Rule of three (in prose, not bullet lists)

**Tells:** "X, Y, and Z" patterns repeated throughout prose, especially when the third item is a filler synonym of the first two.

**Why it's bad:** three-part lists feel natural once, padded the second time, robotic the third.

**Before:**
> Our tool delivers speed, reliability, and performance. It handles complexity, scale, and volume. Users get clarity, precision, and insight.

**After:**
> The tool handles payloads up to 50 MB without crashing. Tests cover 96% of branches.

**Note:** rule-of-three in an actual bulleted feature list is fine — the visual structure makes it a list, not prose padding. The pattern only hurts when it's three-in-a-row in flowing text.

---

### 6. Negative parallelism + tailing negations

**Tells:** `It's not just X — it's Y`, `It's more than a library, it's a philosophy`, `..., no compromises`, `..., no guessing`, `..., no bloat`.

**Why it's bad:** marketing copy. Reads as overselling.

**Before:**
> This is more than a CLI — it's a developer experience. The output is correct, no guessing.

**After:**
> A CLI that generates correct TypeScript. If the inferred type is wrong, file an issue with the input payload.

---

### 7. Em dash overuse

**Tells:** em dashes used as drumroll punctuation — like this — two or three times per paragraph — for emphasis.

**Why it's bad:** LLMs learned em-dash-heavy sales prose and cargo-cult it. Humans use em dashes sparingly; commas, periods, or parentheses work most of the time.

**Before:**
> The library — built from the ground up with type safety in mind — integrates with your existing toolchain — no extra configuration needed.

**After:**
> The library integrates with your existing toolchain. No extra configuration needed.

**Rule for READMEs:** one em dash per section maximum. If you wrote two, delete one.

---

### 8. Hedge words and filler

**Tells:** `robust`, `scalable`, `efficient`, `flexible`, `modern`, `clean`, `simple`, `powerful`, `easy-to-use`, `comprehensive`, `holistic`.

**Why it's bad:** these adjectives apply to every project claiming them. Zero signal.

**Before:**
> A modern, scalable, easy-to-use library for efficient and flexible data processing.

**After:**
> A library for converting JSON to TypeScript. Used in production at [company-list-if-real] since 2023.

---

### 9. Generic uplift conclusions

**Tells:** `The future is bright`, `exciting times ahead`, `continues to evolve`, `a journey toward excellence`, `a new era of X`.

**Why it's bad:** corporate LinkedIn-speak. No information.

**Before:**
> As we continue this journey, we look forward to an exciting future for type-safe development.

**After:**
> Roadmap below. Issues labeled `good first issue` welcome contributions.

---

### 10. Chatbot artifacts

**Tells:** `I hope this helps`, `Of course!`, `Certainly!`, `Let me know if you need clarification`, `Feel free to`, `Here's a breakdown`, `Let's dive in`.

**Why it's bad:** conversational glue that belongs in chat, not documentation. Pasted as-is from LLM responses.

**Before:**
> Of course! Here's a breakdown of the API. Let me know if you need any clarification!

**After:**
> The API has three functions: `transform`, `parse`, and `validate`. Each is documented below.

---

## README-Specific Voice Guidelines

### 1. Description paragraph: a specific statement, not a pitch

The paragraph right under the title is where most READMEs fail the AI-smell test. It wants to be a pitch. Resist.

| Bad | Better |
|---|---|
| A blazing-fast, modern CLI tool that provides a seamless and intuitive way to transform complex JSON data into type-safe TypeScript interfaces, empowering developers to build more robust applications. | A CLI that reads a JSON file and prints the equivalent TypeScript interface. No schema required. |
| Our next-generation library represents a paradigm shift in how developers approach state management. | State management for React apps. About 4 KB gzipped. |
| This project stands as a testament to the power of open source collaboration. | Started as a weekend script in 2022. Current maintainers: three people listed below. |

**Formula:** *What it does* + *one specific fact that's true* + *stop*.

### 2. Feature lists: verbs, not adjectives

Adjectives lose all meaning when stacked ("fast, scalable, reliable, robust"). Verbs carry signal because they describe what the thing actually does.

**Before:**
```md
- Fast
- Scalable
- Reliable
- Robust
- Developer-friendly
- Enterprise-ready
```

**After:**
```md
- Runs on Node, Deno, and Bun
- Streams payloads larger than RAM
- Emits valid TypeScript — not just "a string that looks like TypeScript"
- Exit code signals whether output changed (useful in CI)
```

### 3. Install sections: commands, not narration

**Before:**
```md
## Installation

To get started with installing the library, you'll want to use npm, which is the package manager that comes with Node.js. Simply run the following command to install the package globally, making it available throughout your system.
```

**After:**
```md
## Install

```sh
npm install -g PACKAGE
```
```

Same information. 90% less text. Zero AI smell.

### 4. Keep uncertainty visible

Human maintainers doubt things. They write "probably", "we're not sure if this is the right API — feedback welcome", "this is experimental". LLMs never do.

**Before:**
> The API is well-designed and intuitive.

**After:**
> The API might change in 1.0 — we're still figuring out whether `transform()` should return a string or a parsed AST. Feedback on [#42](https://github.com/OWNER/REPO/issues/42) welcome.

Signals honesty. Signals a human wrote it. Readers respond.

### 5. Short sentences mixed with long ones

The biggest AI tell at the paragraph level is rhythm. LLMs default to medium-length sentences stacked uniformly. Humans vary:

**AI-flat:**
> The library parses JSON input into an AST. It then traverses the AST to identify type patterns. After identification, it generates TypeScript interfaces. The result is a string of valid TypeScript code.

**Human-varied:**
> The library parses JSON into an AST, walks the tree to identify type patterns, and emits TypeScript interfaces as a string. That's it. There's no schema, no config file, nothing else to learn.

Short. Long. Short. That rhythm is the tell that a human wrote it.

### 6. First person is fine — when there's a person

For solo projects and opinionated tools, `I` or `we` is more credible than corporate voice.

**Before (committee-voice):**
> The project offers a comprehensive solution for JSON type generation.

**After (solo):**
> I wrote this because quicktype kept choking on the 40 MB GraphQL responses from our API. It handles them now. If you're not hitting that specific problem you probably don't need this.

### 7. No self-congratulation

**Before:**
> We're thrilled to announce the release of our groundbreaking new feature!

**After:**
> v2.1 adds a `--watch` flag. Changelog below.

---

## The Audit Pass (mandatory before writing)

After drafting the README, run this checklist against every prose section (not code blocks, not tables):

```
[ ] Replaced all promotional adjectives (blazing, seamless, powerful...)?
[ ] Replaced all significance inflations (pivotal, testament, landscape...)?
[ ] Used "is" / "are" / "has" where an LLM would have used "serves as" / "boasts"?
[ ] Cut all trailing "-ing" phrases that add nothing?
[ ] No em dash in a sentence that would work with a comma or period?
[ ] No three-in-a-row synonym cycling?
[ ] No "It's not just X, it's Y" constructions?
[ ] No chatbot artifacts (Of course!, Let me know, I hope this helps)?
[ ] No generic uplift ("the future is bright", "exciting times ahead")?
[ ] Varied sentence rhythm (short and long mixed)?
[ ] Any specific numbers, dates, names, or measurements?
[ ] Any visible uncertainty or opinion from a human maintainer?
```

### The two-prompt audit (Wikipedia method, adapted)

After drafting, do this:

1. **Prompt:** *"What makes the README prose below obviously AI generated?"*
   Answer in bullets. Be harsh. List every remaining tell.

2. **Prompt:** *"Now rewrite it so it doesn't read as AI generated."*
   Apply each fix. Prefer cutting over rewording.

Ship the second version.

---

## Worked Example — Library README intro

### Draft 1 (typical AI-generated)

```md
# json2ts

[![npm](...)] [![CI](...)]

## About

`json2ts` is a blazing-fast, modern CLI that provides a seamless and intuitive way to transform
your JSON payloads into type-safe TypeScript interfaces, empowering developers to build more robust
applications. Our tool leverages cutting-edge AST analysis techniques — ensuring that every type
is precisely inferred from your data — while also highlighting the importance of type safety in
today's rapidly evolving software development landscape.

It's not just a CLI — it's a complete workflow solution. Whether you're a solo developer or part
of an enterprise team, `json2ts` delivers speed, reliability, and a developer experience that's
truly best-in-class.
```

### Audit: what makes this obviously AI generated?

- `blazing-fast, modern` — promotional stack
- `seamless and intuitive` — brochure language, copula avoidance too (`provides` > `is`)
- `empowering developers to build more robust applications` — superficial `-ing` analysis, rule of three adjacent
- `leverages cutting-edge AST analysis techniques` — hype
- `— ensuring that every type is precisely inferred —` — em dash + `-ing` analysis
- `highlighting the importance of type safety` — vague significance
- `in today's rapidly evolving software development landscape` — classic AI phrase, twice
- `It's not just a CLI — it's a complete workflow solution` — negative parallelism + em dash
- `whether you're X or Y` — hollow audience expansion
- `delivers speed, reliability, and a developer experience` — rule of three with weak third item
- `truly best-in-class` — self-congratulation

### Draft 2 (humanized)

```md
# json2ts

[![npm](...)] [![CI](...)]

## About

`json2ts` reads a JSON file and prints the equivalent TypeScript interface. That's the whole tool.

I wrote it because `quicktype` required a schema for the payloads I was dealing with (messy, often
undocumented third-party APIs), and writing schemas by hand defeated the point. `json2ts` infers
everything from a sample — including nested unions and optional fields — and gets it right for my
test corpus about 94% of the time. The remaining 6% is usually me forgetting that a field can be `null`.

Fair warning: if your JSON is already well-typed upstream, you don't need this. Use quicktype.
```

Specific. Varied rhythm. Human uncertainty visible. Zero AI tells.

---

## When You're Handed an Existing README to Improve

If the user asks you to *improve* or *humanize* a README they already wrote:

1. Run the **audit checklist** on it section by section
2. Produce a diff showing what you'd change and why
3. Apply changes only after user confirmation
4. Preserve their voice — if the existing README uses "we" throughout, keep "we"; if it's first-person, keep first-person

The goal is their voice, cleaner. Not your voice replacing theirs.

---

## Interop with the humanizer skill

If the user wants deep humanization of long-form README prose (about-pages, philosophy sections, long-form release notes), hand the draft to the `humanizer` skill for a final pass. That skill implements the full Wikipedia "Signs of AI writing" protocol with the two-prompt audit.

This reference is the README-specific subset — optimized for short marketing prose, feature lists, install sections, and the paragraph under the title.
