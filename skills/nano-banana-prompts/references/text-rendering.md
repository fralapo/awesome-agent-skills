# Rendering Text in Images

Nano Banana Pro is one of the strongest open image models at rendering readable text — including CJK, long quotes, and multi-module layouts. Non-Pro handles short Latin labels only. This file covers how to get the text you want.

## Tier Cheatsheet

| Capability | Nano Banana | Nano Banana Pro |
|---|---|---|
| Single label (< 5 words, Latin) | ✅ | ✅ |
| Short tagline (5–15 words, Latin) | ⚠️ spelling often drifts | ✅ |
| Full quote (15–40 words) | ❌ | ✅ |
| Multi-line typography (headline + subtitle) | ⚠️ one line usually OK | ✅ |
| CJK / Arabic / Cyrillic | ❌ breaks | ✅ |
| Mixed-script (CJK + Latin in one layout) | ❌ | ✅ |
| Small text (fine print) | ❌ mush | ⚠️ still risky, test |
| Data tables / infographic labels | ❌ | ✅ |

Default to **Pro** for anything past a one-word label.

## Prompt Pattern for Text

Always:

1. **Quote the exact string.** `"Stay Hungry, Stay Foolish"` — double-quote it.
2. **Specify font family and weight.** `serif`, `sans-serif`, `bold sans-serif`, `light serif`, `condensed`, `monospace`.
3. **Specify size relative to frame.** `large centered headline`, `small caption below`, `medium subtitle`.
4. **Specify color + contrast.** `light-gold on brown background`, `white on black`, `#562226 on cream`.
5. **Specify placement.** `upper-third`, `lower-left corner`, `below each base`, `centered above the buildings`.
6. **Add spelling guardrail.** `Spelling must be exact. No misspelling. No warped letters.`

### Minimal text-in-image template

```
Render the text "EXACT STRING" in {font family, weight}, {color}, {size}.
Placement: {position}. Spelling must be exact. Kerning consistent.
```

### Multi-line / multi-block pattern

```
Text block 1 (headline): "STRING ONE"
  Font: bold serif, large, centered, color #1a1a1a.
Text block 2 (subtitle): "STRING TWO"
  Font: light serif italic, medium, directly below headline, color #6a6a6a.
Text block 3 (byline): "—Author Name"
  Font: small sans-serif caps, lower-right corner.

All text: exact spelling, consistent kerning and leading, no warping.
```

## Raycast Argument Snippets

For parameterized prompts reused via Raycast Snippets:

```
A wide quote card with "{argument name="quote" default="Stay Hungry, Stay Foolish"}"
by {argument name="author" default="Steve Jobs"}.
```

- `{argument name="..." default="..."}` is Raycast syntax — the model treats the whole token as the literal string if Raycast doesn't pre-process it.
- Pair with Raycast Snippets feature so users fill the slot before send.
- Also usable as a human-readable placeholder when not using Raycast.

## Common Failure Modes

| Symptom | Cause | Fix |
|---|---|---|
| Misspelled word | String too long for tier | Shorten; upgrade to Pro |
| Warped / melted letters | Font left unspecified, generic rendering fails | Specify font family + weight |
| Wrong font style | "Elegant" / "modern" too vague | Use concrete: `serif`, `sans-serif`, `monospace` |
| Text cropped at edge | No placement or size guidance | Add `with ample padding from frame edge` |
| Right-to-left broken | Arabic / Hebrew on Nano non-Pro | Upgrade to Pro |
| Decorative but unreadable | Model prioritized aesthetic over legibility | Add `crisp, highly legible, no stylization of letterforms` |
| Text overlaps subject | No z-order rule | Add `text in safe margins, never covering the subject` |

## Negative Prompt for Text Issues

Append only when you've seen the failure:

```
NEGATIVE: misspelled text, warped letters, inconsistent kerning,
duplicate text, text cut off at frame edge, jumbled characters.
```

## CJK / Multi-Script Pattern (Pro only)

```
Render Chinese text: "你好世界" in a traditional serif (楷体 / Kai style),
centered, medium weight, color black on cream background.
Below it, render English translation: "Hello World" in a light sans-serif,
smaller size, same color.

Spelling and character strokes must be exact. No distortion. No missing strokes.
```

- Name the target script style (Kai, Song, Hei for Chinese; Mincho, Gothic for Japanese)
- Pair CJK with a Latin transliteration block when targeting bilingual output
- Test once — if strokes mangle, simplify the string

## Bento / Infographic Text (Pro only)

Module labels carry most of the text in bento layouts. Structure the content:

```
M1 — Hero:
  Title: "PRODUCT NAME" — bold sans-serif, 42pt equivalent, white on hero-color.
M2 — Core Benefits (4 items):
  Each row: [icon] "benefit title" (semibold) / "one-line description" (light).
M4 — Key Metrics (5 data points):
  Format: [icon] [label in small caps] [BOLD VALUE] [unit]
  Example: [⚡] BATTERY 18 hrs
```

Enumerate text per module. The model treats vague module briefs as "put some words here" and invents plausible-looking but wrong copy.

## Long-Form Quote Card

```
A {bg_color} quote card, 9:16 vertical.
Large centered quote in {font}: "{EXACT MULTI-LINE QUOTE}"
The quote is {N} lines, each line breaks at the words shown.
Below the quote, author byline: "—{AUTHOR}" in smaller italic.
Margins: generous. Kerning: consistent. Spelling: exact.
No decorative flourishes that obscure letters.
```

Show line breaks explicitly if specific layout matters — paste the quote with manual `\n` equivalents or use "line one / line two / line three" phrasing.

## When Text Still Fails on Pro

1. Shorten the string — each word past ~40 increases risk
2. Split into two generations and composite externally
3. Pre-render the text as an image in another tool, then use multi-reference fusion: `place the text layout from image 2 onto the scene from image 1`
4. Switch to vector tools for precise typography — image models are never pixel-accurate for typesetting
