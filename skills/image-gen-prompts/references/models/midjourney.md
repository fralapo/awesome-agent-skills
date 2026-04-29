# Midjourney v6 / v7 + Niji v6

Discord-first (also web/app). Flag-based syntax surface. Strongest aesthetic-default prior of any major model — biased toward beautiful by default, sometimes at the cost of literal prompt adherence.

## Tier

- **v6** = Standard
- **v7** = Pro (better adherence, longer prompts, improved hands/text)
- **Niji v6** = anime/illustration specialist; layered onto v6/v7 with `--niji 6`

## Syntax surface

Prompt is **comma-separated tag block + positional flags** at the end. Flags are model-aware — passing wrong flags throws errors.

```
<subject>, <medium>, <style>, <lens>, <lighting>, <mood>, <details>, <colors> --ar 16:9 --stylize 250 --v 7
```

### Common flags

| Flag | Purpose | Notes |
|---|---|---|
| `--ar W:H` | Aspect ratio | e.g. `--ar 16:9`, `--ar 9:16`, `--ar 2:3` |
| `--v 6` / `--v 7` | Model version | Default = newest at job time |
| `--niji 6` | Niji anime model | Replaces `--v` |
| `--stylize 0..1000` | Aesthetic pressure | Default 100. Lower = literal, higher = stylized |
| `--weird 0..3000` | Off-beat aesthetics | Use sparingly |
| `--chaos 0..100` | Initial-grid variance | High = wider exploration |
| `--seed N` | Deterministic seed | Reproduce a roll |
| `--no <terms>` | Negative prompt | Comma-separated, no quotes |
| `--cref <url>` | Character reference | Identity anchor |
| `--cw 0..100` | Character weight | 100 = full face+hair+outfit; 0 = face only |
| `--sref <url>` | Style reference | Aesthetic transfer |
| `--sw 0..1000` | Style weight | Default 100 |
| `--sref random` | Random style ID | Use `--sref <numericID>` to repeat it |
| `--p` (v7) | Personalize | Apply your `/imagine` style profile |
| `--draft` (v7) | Fast/cheap mode | Lower quality |
| `--tile` | Tileable texture | For seamless patterns |
| `--q .25 / .5 / 1` | Quality/time | Higher = slower, more detail |
| `--repeat N` | Repeat prompt | N variants |

### v7 additions

- Improved prompt comprehension; long natural-language prose now parses
- `--exp` for exposure-style biases
- Personalize via `--p` based on user-trained `/preferences`

## Best-in-class for

- Editorial photography, fashion, fantasy art, sci-fi, dramatic lighting
- Style references (`--sref`) — you can lock a visual look across many gens
- High aesthetic floor — even short prompts produce striking output
- Vary Region (in-painting via web UI)

## Weak points

- Literal text rendering (better in v7 but still inconsistent past short labels)
- CJK text — broken
- Dense infographics / charts — not the right tool
- Strict adherence — model "improves" prompts, sometimes ignoring constraints

## Reference-image syntax

```
<prompt> --cref https://example.com/face.png --cw 100 --sref https://example.com/style.png --sw 250 --ar 9:16 --v 7
```

- Multiple `--sref` URLs allowed (style mixing)
- Multiple `--cref` URLs allowed (composite identity, but drift increases)
- Image URLs must be public; Discord upload returns a URL you can paste back

## Negative prompts

```
--no plastic skin, low quality, watermark, text artifacts, distorted hands
```

Negatives are subtractive only — they don't add positive signal. Don't dump 30 terms.

## Anti-patterns

- `8k masterpiece beautiful highly detailed trending on artstation` — vestigial SDXL hype tags; drown out specific signal
- `--stylize 1000` on a literal photo brief — fights the realism cue
- Mixing v6 flags with v7 (some flags model-specific)
- Putting `--ar` without space before colon — silently ignored
- Using `--no text` while requesting "tagline reading XYZ" — contradicts itself

## Anatomy template

```
<subject - 1 sentence>, <medium e.g. editorial photograph / oil painting>,
<style refs / era>, <lens + lighting>, <color palette>, <mood>,
<details>
--ar <ratio> --stylize <0-1000> --v 7
```

## Output target

Discord (`/imagine`), Midjourney web app, Midjourney REST API (where licensed). Outputs delivered as 4-grid; click U1..U4 to upscale, V1..V4 to vary.

## See also

- `../patterns.md` for lens/lighting vocab (works on MJ)
- `../examples.md` for cross-model prompt comparisons
