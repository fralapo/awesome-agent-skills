# Nano Banana / Nano Banana Pro (Gemini 2.5 Flash Image)

Google Gemini's image model. **Nano Banana** = standard tier, **Nano Banana Pro** = higher-quality successor. Both share the same prompt grammar; Pro handles denser composition, longer text strings, and more reference images in parallel.

Source repos: `Super-Maker-AI/awesome-nano-banana`, `YouMind-OpenLab/awesome-nano-banana-pro-prompts`, `PicoTrex/Awesome-Nano-Banana-images`, `jimmylv/awesome-nano-banana`, `ZeroLu/awesome-nanobanana-pro`. ~600 prompts analyzed.

## Tier comparison

| Capability | Nano Banana | Nano Banana Pro |
|---|---|---|
| Photorealistic portraits | ✅ | ✅ (sharper skin/pores) |
| Multi-image fusion | ✅ 2–3 refs | ✅ 5+ refs |
| Text rendering in image | Short labels only (Latin, < 15 words) | Long quotes, multi-line, CJK |
| Bento/infographic layouts | Simple | 8+ modules with data fields |
| Dense crowd scenes | Drifts past 4–5 faces | Holds identity across many |
| Structured JSON/YAML prompts | Partial parsing | Reliable parsing |
| Complex conditional rules / `<tag>` blocks | Weak | Strong |

## Syntax surface

- **Natural language only.** No `--flags`, no `(weight:1.2)` syntax.
- **Reference images addressed by phrase**, not index syntax: "the person in the uploaded image", "image 1", "the attached photo". No `@image1` / no `--cref`.
- **Aspect ratio in prose**: `1080x1080`, `16:9`, `9:16`, `2.35:1`. Always explicit, never default.
- **JSON / YAML / `<tag>` blocks** parsed reliably on Pro, partially on standard.
- **Raycast `{argument name="x" default="y"}` placeholders** treated as literal text — pair with Raycast Snippets to substitute before send.

## Identity anchor (ranked)

| Rank | Phrase |
|---|---|
| 🥇 | `The face must be 100% identical to the uploaded image. Do not change the face.` |
| 🥈 | `Keep the facial features of the person in the uploaded image exactly consistent.` |
| 🥉 | `Same face 100% from the reference image. Preserve facial features, expression, hairstyle.` |
| 4 | `The person from the attached image (uploaded image facial details).` |
| 5 | `Using the attached reference, same face.` |

Repeat the anchor at top AND near the end of long prompts (>200 words) — attention decays in the middle.

## Reference-input phrasings

| Phrasing | Use |
|---|---|
| "the person in the uploaded image" | Single-ref identity anchor |
| "same face 100% from reference" | Strongest identity lock |
| "from the attached image (uploaded image facial details)" | Pro tier multi-attribute |
| "combine the two uploaded images" | Multi-image fusion |
| "use image 1 as subject, image 2 as background, image 3 as style" | Role-assigned refs |

## Strengths (where Nano Banana wins)

- Non-destructive editing with explicit preservation clause (Ghostface-in-background, weather change, era swap)
- Mixed-style face-island patterns (chibi body + photoreal face)
- Celebrity priors — name-based recognition for public figures
- Multi-reference role assignment ("img1 subject, img2 bg, img3 style")
- Natural-language addressing avoids syntax-error pollution

## Anti-patterns

- Tag-salad prompts (`portrait, 8k, masterpiece, beautiful, highly detailed`) — under-perform
- Editing without a preservation clause — model mutates face/pose
- Embedding text > 15 words on non-Pro — spelling breaks
- > 10 named subjects in one prompt — drifts past 5 on standard, past ~8 on Pro
- Mixing Midjourney `--flags` — parsed as literal text, pollutes output
- Combining multiple face references without explicit roles — model averages them

## Quirks worth knowing

- Coordinates + time → real location resolution (e.g. `35.6586° N, 139.7454° E at 19:00` → Shibuya at dusk). Strong Gemini world-knowledge prior.
- Emoji combination prompts work with extreme brevity (`combine these emojis: 🍌 + 😎, on a white background as a google emoji design`).
- "Strict Single-Object Rule" block needed when you want exactly one object — Pro still occasionally adds a second, third, or shadow-twin.

## Output target

Paste into Gemini app, AI Studio, or via Gemini API. No flag syntax to append.

## See also

- `../patterns.md` for universal lighting/camera vocab
- `../templates.md` for fillable Nano-Banana-tested category templates
- `../identity-preservation.md` for failure modes + fixes
- `../structured-prompts.md` for JSON/YAML/XML shapes
- `../text-rendering.md` for tier-aware text-in-image rules
- `../examples.md` for curated working prompts
