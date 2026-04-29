---
name: image-gen-prompts
description: Write production-grade prompts for any major image generation/editing model — Google Nano Banana / Nano Banana Pro (Gemini 2.5 Flash Image), OpenAI GPT Image 2 ("duct-tape") and GPT Image 1 / DALL·E 3, Midjourney v6/v7 + Niji, Stable Diffusion (SDXL / SD3 / SD3.5), FLUX.1, Google Imagen 3/4, Ideogram 2/3, Recraft v3, and others. Use when the user wants to generate or edit images, needs prompt templates for portraits, product shots, 3D dioramas, infographics, anime/illustration, cinematic scenes, posters, comic panels, storyboards, e-commerce visuals, or asks about face/identity preservation, multi-image fusion, non-destructive editing, isometric/bento layouts, text rendering in images, JSON/YAML/XML structured prompts, or Raycast-style argument placeholders. If the user names a specific model, route through `references/models/_index.md` and read the matching per-model file. Triggers on keywords: image prompt, image generation, image editing, prompt engineering, nano banana, nano-banana, nano banana pro, gemini 2.5 flash image, gemini image gen, gpt image, gpt-image-2, duct-tape, dall-e, dall·e, dalle 3, midjourney, mj, niji, stable diffusion, sdxl, sd3, flux, flux.1, imagen, ideogram, recraft, 纳米香蕉.
version: 2.0.0
source: local-git-analysis
analyzed_repos:
  - github.com/Super-Maker-AI/awesome-nano-banana
  - github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts
  - github.com/PicoTrex/Awesome-Nano-Banana-images
  - github.com/jimmylv/awesome-nano-banana
  - github.com/ZeroLu/awesome-nanobanana-pro
  - github.com/ZeroLu/awesome-gpt-image
  - github.com/YouMind-OpenLab/awesome-gpt-image-2
  - github.com/EvoLinkAI/awesome-gpt-image-2-prompts
  - github.com/marc-aurele-besner/prompts
  - openart.ai/blog/post/midjourney-prompts-for-packaging-design
  - openart.ai/blog/post/midjourney-prompts-for-mockup
  - godofprompt.ai
analyzed_prompts: ~6100
---

# Image Generation Prompt Engineering — Universal

Generic prompt-engineering skill for **any** modern image generation / editing model. Works model-agnostic by default; switches to model-specific guidance when the user names a model.

Strong prompts share the same anatomy across models — subject, environment, lighting, camera/lens, style, format, and (for edits) what to preserve. What differs is **syntax surface**: Midjourney uses `--flags`, GPT Image 2 likes structured JSON, Nano Banana parses natural-language addressing of reference images, SDXL leans on weighted token blocks plus negative prompts, FLUX rewards prose density, Ideogram is the strongest at typography.

## When to Use This Skill

- User asks to write or improve an image prompt for any model
- User wants to edit an uploaded image (outfit swap, background change, face-preserving restyle, object addition/removal, inpainting)
- User requests identity-preserved portraits, celebrity integration, aging sequences, multi-character group shots
- User wants a bento/infographic layout, isometric diorama, exploded-view product poster, magazine cover, comic panel, storyboard grid, e-commerce main image, YouTube thumbnail
- User needs style-specific prompts: cinematic, Kodak Portra, anime, 3D chibi, pixel art, Baroque frame, ukiyo-e, Swiss design, cyberpunk, RAW iPhone, 90s point-and-shoot, 35mm direct flash
- User mentions "preserve face", "same face 100%", "change only the background", "keep pose", "multi-view", "action figure box", "exploded view"
- User wants Raycast-friendly prompts with `{argument name="..." default="..."}` placeholders
- User explicitly names a model (Midjourney, MJ, SDXL, FLUX, GPT Image 2, Nano Banana, etc.)

## Model Routing

Whenever the user names a model in their query, **read the matching file** under `references/models/` for syntax surface and quirks, then layer it on top of the universal anatomy below.

| Trigger keywords (any) | Read |
|---|---|
| `nano banana`, `nano-banana`, `gemini 2.5 flash image`, `gemini image`, `nano banana pro`, `纳米香蕉` | `references/models/nano-banana.md` |
| `gpt image 2`, `gpt-image-2`, `duct-tape`, `gpt image 2 prompts` | `references/models/gpt-image-2.md` |
| `gpt image 1`, `gpt-image-1`, `dall-e 3`, `dall·e 3`, `dalle 3` | `references/models/gpt-image-1.md` |
| `midjourney`, `mj`, `--ar`, `--stylize`, `--sref`, `--cref`, `niji`, `--niji` | `references/models/midjourney.md` |
| `stable diffusion`, `sd 1.5`, `sdxl`, `sd 3`, `sd3`, `sd3.5`, `comfyui`, `automatic1111`, `forge` | `references/models/stable-diffusion.md` |
| `flux`, `flux.1`, `flux dev`, `flux schnell`, `flux pro`, `black forest labs` | `references/models/flux.md` |
| `imagen`, `imagen 3`, `imagen 4` | `references/models/imagen.md` |
| `ideogram`, `ideogram 2`, `ideogram 3` | `references/models/ideogram.md` |
| `recraft`, `recraft v3` | `references/models/recraft.md` |
| no model named | default to model-agnostic universal pattern; ask user which model |

Always start with `references/models/_index.md` if you need to scan all routes at once.

## Two Capability Tiers (general)

| Capability | "Standard" tier | "Pro" tier |
|---|---|---|
| Photorealistic portraits | ✅ | ✅ (sharper skin/pores) |
| Multi-image fusion | ⚠️ 2–3 refs | ✅ 5+ refs |
| Text rendering in image | Short labels only | Long quotes, multi-line, CJK |
| Bento/infographic layouts | Simple grids | 8+ modules with data fields |
| Dense crowd scenes | Drifts past 4–5 faces | Holds identity across many |
| Structured JSON/YAML prompts | Partial parsing | Reliable parsing |
| Complex conditional rules | Weak | Strong |

Per-model mapping of "Standard" vs "Pro" is documented in each `references/models/<name>.md`. Examples:
- Nano Banana = Standard; Nano Banana Pro = Pro
- GPT Image 1 / DALL·E 3 = Standard; GPT Image 2 = Pro
- Midjourney v6 = Standard; v7 = Pro
- SD 1.5 = Standard; SDXL / SD3 / SD3.5 = Pro
- FLUX.1 [schnell] = Standard; FLUX.1 [dev] / [pro] = Pro

**Rule of thumb:** default to Pro tier for infographics, posters with headlines, multi-character scenes, structured JSON/YAML prompts, and CJK text. Standard tier suffices for single-subject edits and short prompts.

## Universal Prompt Anatomy

Every strong prompt stacks these blocks. Order is flexible; labels are optional when context is clear.

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

### Minimum viable template — generation

```
A {style/medium} of {subject} {action} in {environment}.
{Wardrobe + props}.
Lighting: {key + rim + mood}. Camera: {lens, angle}.
{Aspect ratio}, {resolution}. {Style ref}.
```

### Minimum viable template — image edit

```
{Edit verb} the {target region} of the attached image:
{specific change}.
Preserve: face/identity, pose, outfit, background lighting — zero alteration.
Only modify: {explicit region}.
Match the original {lighting logic / color grade / perspective}.
```

## Reference Inputs (per model)

How to address an uploaded reference image varies. Universal pattern works across most natural-language models; flag-based models need explicit syntax.

| Model family | Phrasing |
|---|---|
| Nano Banana / Gemini | "the person in the uploaded image", "same face 100% from reference" — natural language |
| GPT Image 2 | "Based on this character", "Using this portrait", "Upload a source image" — natural language |
| Midjourney | `--cref <url>` for character ref, `--sref <url>` for style ref, `--cw 100` weight |
| Stable Diffusion / FLUX | IP-Adapter / ControlNet at the workflow level, not in the prompt text |
| Imagen / Ideogram / Recraft | API-level `referenceImages` payload; prompt text references via "the provided reference" |

For exact syntax see the matching file under `references/models/`.

## Category Catalog

Detailed templates and examples live in `references/`.

- `references/patterns.md` — universal vocabulary: lighting, camera, ratios, style tags, composition idioms, single-object rules, multi-reference fusion, negative-prompt vocabulary
- `references/templates.md` — fill-in templates for 18+ common categories (portrait, product, poster, diorama, infographic, comic grid, exploded-view, e-commerce hero, YouTube thumbnail, character sheet, storyboard, etc.)
- `references/identity-preservation.md` — face-lock phrases, failure modes, fixes, multi-person handling, mixed-style face preservation, aging sequences
- `references/structured-prompts.md` — JSON / YAML / XML formats and which models parse them reliably
- `references/text-rendering.md` — putting readable headlines, quotes, CJK in the image, per-model tier limits
- `references/editing-workflow.md` — non-destructive editing, inpainting, multi-image fusion, before/after, character consistency across panels
- `references/examples.md` — curated working prompts per category, attributed, with the model that produced each
- `references/models/` — per-model quirks, syntax surface, parameters, anti-patterns

## Quick Rules (model-agnostic)

1. **Paragraph + constraint lines beats tag soup** for natural-language models (Nano Banana, GPT Image 2, FLUX, Imagen). For Midjourney and SDXL, dense comma-separated tag blocks plus flags still work.
2. **Specify aspect ratio explicitly** — `1080x1080`, `16:9`, `9:16`, or `--ar 9:16` for Midjourney. Don't rely on defaults.
3. **Identity anchor every edit.** "Same face 100% from reference", "keep facial features exactly consistent", "do not change the face".
4. **Non-destructive edits need an allow-list.** Name what changes AND what is preserved — most models otherwise drift on wardrobe/pose.
5. **Lens + lighting = photorealism.** `85mm f/1.4`, `Kodak Portra 400`, `three-point lighting`, `golden hour rim light`, `harsh on-camera flash` all carry real weight on every model.
6. **Single-object constraints must be repeated.** If you want exactly one object, write an explicit strict-single-object block (see `references/patterns.md#single-object-rule`).
7. **Text in image = quote it exactly.** Wrap exact strings in double quotes: `serif font reading "Stay Hungry, Stay Foolish"`. For CJK, prefer Pro-tier models.
8. **Use `[PLACEHOLDERS]`** (square brackets, uppercase) for reusable templates. Use `{argument name="x" default="y"}` for Raycast snippets — supported as a literal placeholder by Nano Banana, GPT Image 2, and any natural-language model.
9. **For bento/infographic layouts**, enumerate modules (M1…M8) with content type per cell — strongly favors Pro-tier models.
10. **Negatives go at the end** as a `NEGATIVE:` list or `Do NOT:` bullet — except SDXL/Midjourney where negatives have dedicated syntax (`--no` for MJ, dedicated negative prompt input for SD).
11. **For natural / un-AI looks**: explicitly request "natural skin texture, flyaway hairs, slight asymmetry, no glamour retouching, no beauty filter, no overly polished AI aesthetic". GPT Image 2 and Nano Banana Pro both respect these.
12. **For cross-image consistency** (same character across N panels): describe the character once in detail, then reference back as "the same character from panel 1" — works on GPT Image 2 and Nano Banana Pro; weaker on others.

## Anti-Patterns

- Tag-salad prompts on natural-language models (`portrait, 8k, masterpiece, beautiful, highly detailed`) — under-perform vs structured paragraph
- Asking for "photorealistic" without lens/lighting — produces generic render
- Editing without a preservation clause — model mutates face/pose
- Multiple conflicting aspect ratios in one prompt — one wins, unpredictably
- Face-swap with only facial description (no ref image) — low fidelity
- Packing > 10 named subjects in one prompt — identity drift past ~5 on Standard tier, past ~8 on Pro
- Embedding exact text > 15 words on Standard-tier models — spelling breaks
- Mixing Midjourney `--flags` into a Nano Banana / GPT Image / FLUX prompt — flags get parsed as literal text and pollute output
- "Polished AI" defaults when shooting for candid lifestyle — explicitly veto glamour retouching
- Forcing JSON on a tiny prompt — `{"subject":"red apple"}` is worse than `A red apple on a white table, studio lighting, 1:1.`

## Workflow

1. Ask user — generate from scratch or edit an existing image? Which model? Which tier? Aspect ratio?
2. If a model is named, read `references/models/<name>.md` first.
3. Identify category → pick from `references/templates.md`.
4. If editing with a reference image: lock identity + add preservation clause first (see `references/identity-preservation.md`).
5. Fill subject → environment → lighting → camera → format → style.
6. Add negatives only for known failure modes (not prophylactically). Use the model's native negative-prompt mechanism if it has one.
7. For text in image, follow `references/text-rendering.md` and downgrade to a Pro-tier model if the string is long or non-Latin.
8. Output the prompt in a single fenced block; user pastes into the target model UI/API. For Midjourney, end with the flag block; for SD/FLUX, output positive + negative prompt separately.
