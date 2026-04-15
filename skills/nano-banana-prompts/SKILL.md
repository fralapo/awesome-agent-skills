---
name: nano-banana-prompts
description: Write production-grade prompts for Google Nano Banana (Gemini 2.5 Flash Image) and Nano Banana Pro image generation/editing. Use when the user wants to generate or edit images with Nano Banana / Gemini image model, needs prompt templates for portraits, product shots, 3D dioramas, infographics, anime/illustration, cinematic scenes, or asks about face/identity preservation, multi-image fusion, non-destructive editing, isometric/bento layouts, text rendering in images, or Raycast-style argument placeholders. Triggers on keywords: nano banana, nano-banana, nano banana pro, gemini 2.5 flash image, gemini image gen, 纳米香蕉.
version: 1.0.0
source: local-git-analysis
analyzed_repos:
  - github.com/Super-Maker-AI/awesome-nano-banana
  - github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts
  - github.com/PicoTrex/Awesome-Nano-Banana-images
  - github.com/jimmylv/awesome-nano-banana
  - github.com/ZeroLu/awesome-nanobanana-pro
analyzed_prompts: ~600
---

# Nano Banana Prompt Engineering

**Nano Banana** = Google Gemini 2.5 Flash Image. **Nano Banana Pro** = the higher-quality successor. Both share the same prompt grammar but Pro handles denser composition, longer text strings, and more reference images in parallel.

Prompts are **paragraph + explicit constraint blocks**, not one-line tags. Strong prompts specify subject, environment, lighting, camera/lens, style reference, output format, and — when editing — what to preserve.

## When to Use This Skill

- User asks to write / improve a Nano Banana or Gemini image prompt
- User wants to edit an uploaded image (outfit swap, background change, face-preserving restyle, object addition/removal)
- User requests identity-preserved portraits, celebrity integration, aging sequences, multi-character group photos
- User wants a bento/infographic layout, isometric diorama, product poster, magazine cover, comic panel, storyboard grid
- User needs style-specific prompts: cinematic, Kodak Portra, anime, 3D chibi, pixel art, Baroque frame, ukiyo-e, Swiss design, cyberpunk
- User mentions "preserve face", "same face 100%", "change only the background", "keep pose", "multi-view", "action figure box"
- User wants Raycast-friendly prompts with `{argument name="..." default="..."}` placeholders

## Two Model Tiers

| Capability | Nano Banana | Nano Banana Pro |
|---|---|---|
| Photorealistic portraits | ✅ | ✅ (sharper skin/pores) |
| Multi-image fusion | ✅ 2–3 refs | ✅ 5+ refs |
| Text rendering in image | Short labels only | Long quotes, multi-line, CJK |
| Bento/infographic layouts | Simple | 8+ modules, data fields |
| Dense crowd scenes | Drifts past 4–5 faces | Holds identity across many |
| Structured JSON/YAML prompts | Partial parsing | Reliable parsing |
| Complex conditional rules | Weak | Strong (see `references/structured-prompts.md`) |

**Rule of thumb:** default to Nano Banana Pro for infographics, posters with headlines, multi-character scenes, and structured JSON/YAML prompts. Nano Banana suffices for single-subject edits and short prompts.

## Core Prompt Anatomy

Every strong prompt stacks these blocks. Order flexible; labels optional when clear from context.

```
[Subject]        who/what — reference handling ("keep face 100%")
[Action/Pose]    what they're doing, body orientation
[Wardrobe]       clothes, accessories, materials, color
[Environment]    location, props, ground, background wall
[Lighting]       key/fill/rim, time-of-day, quality (hard/soft), color temp
[Camera/Lens]    85mm f/1.4, drone top-down, orthographic, eye-level
[Style ref]      film stock (Kodak Portra 400), director, era (2000s), render engine
[Format]         aspect ratio (1:1, 16:9, 9:16), resolution (1080x1080, 8K)
[Preserve]       (edit mode) what must NOT change
[Negative]       anti-artifacts: "no text", "no second object", "no warping"
```

### Minimum viable template (generation)

```
A {style/medium} of {subject} {action} in {environment}.
{Wardrobe + props}.
Lighting: {key + rim + mood}. Camera: {lens, angle}.
{Aspect ratio}, {resolution}. {Style ref}.
```

### Minimum viable template (image edit)

```
{Edit verb} the {target region} of the attached image:
{specific change}.
Preserve: face/identity, pose, outfit, background lighting — zero alteration.
Only modify: {explicit region}.
Match the original {lighting logic / color grade / perspective}.
```

## Reference Inputs

Nano Banana accepts 1–5+ images uploaded alongside the prompt. Address them inline:

| Phrasing | Use |
|---|---|
| "the person in the uploaded image" | Single-ref identity anchor |
| "same face 100% from reference" | Strongest identity lock |
| "from the attached image (uploaded image facial details)" | Pro tier multi-attribute |
| "combine the two uploaded images" | Multi-image fusion |
| "use image 1 as subject, image 2 as background, image 3 as style" | Role-assigned refs |

No `@image1` syntax — unlike Seedance, Nano Banana uses natural-language addressing.

## Category Catalog

Detailed templates and examples live in `references/`.

- `references/patterns.md` — structural patterns, lighting/camera vocab, ratios, style tags
- `references/templates.md` — fill-in templates for 12 common categories
- `references/identity-preservation.md` — face-lock phrases, failure modes, fixes
- `references/structured-prompts.md` — JSON / YAML / role-tag formats that Pro parses reliably
- `references/text-rendering.md` — putting readable headlines, quotes, CJK in the image
- `references/examples.md` — curated working prompts per category with attribution

## Quick Rules

1. **Paragraph + constraint lines beats tag soup.** Nano Banana parses natural language better than comma-separated tag lists.
2. **Specify aspect ratio explicitly** (`1080x1080`, `16:9`, `9:16`). Don't rely on defaults.
3. **Identity anchor every edit.** "Same face 100% from reference", "keep facial features exactly consistent", "do not change the face".
4. **Non-destructive edits need an allow-list.** Name what changes AND what is preserved — model otherwise drifts on wardrobe/pose.
5. **Lens + lighting = photorealism.** `85mm f/1.4`, `Kodak Portra 400`, `three-point lighting`, `golden hour rim light` all carry real weight.
6. **Single-object constraints must be repeated.** If you want exactly one object, write an explicit strict-single-object rule (see `references/patterns.md#single-object-rule`).
7. **Text in image = quote in prompt.** Wrap exact strings in double quotes: `serif font reading "Stay Hungry, Stay Foolish"`.
8. **Use `[PLACEHOLDERS]`** (square brackets, uppercase) for reusable templates. Use `{argument name="x" default="y"}` for Raycast snippets.
9. **For bento/infographic layouts**, enumerate modules (M1…M8) with content type per cell — Pro-only feature.
10. **Negatives go at the end** as `NEGATIVE:` list or `Do NOT:` bullet — don't scatter them inline.

## Anti-Patterns

- Tag-salad prompts (`portrait, 8k, masterpiece, beautiful, highly detailed`) — under-perform vs structured paragraph
- Asking for "photorealistic" without lens/lighting — produces generic render
- Editing without a preservation clause — model mutates face/pose
- Multiple conflicting aspect ratios in one prompt — one wins, unpredictably
- Face-swap with only facial description (no ref image) — low fidelity
- Packing > 10 named subjects in one prompt — identity drift past 5 on Nano Banana, past ~8 on Pro
- Embedding exact text > 15 words on Nano Banana (non-Pro) — spelling breaks

## Workflow

1. Ask user: generate from scratch or edit an existing image? Which tier (Banana vs Pro)? Aspect ratio?
2. Identify category → pick from `references/templates.md`
3. If editing with a reference image: lock identity + preservation clause first (see `references/identity-preservation.md`)
4. Fill subject → environment → lighting → camera → format → style
5. Add negatives only for known failure modes (not prophylactically)
6. Output the prompt in a single fenced block; user pastes into Gemini / Nano Banana UI
