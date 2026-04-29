# Universal Prompt Patterns

Extracted from ~3500 working prompts across community repos for Nano Banana, Nano Banana Pro, GPT Image 2, GPT Image 1, plus cross-checks against Midjourney / SDXL / FLUX / Imagen / Ideogram conventions. Each pattern is a building block — combine them, don't use alone.

For per-model syntax surface (flags, weights, reference-image addressing) see `models/<name>.md`. The vocabulary on this page works on any natural-language model and translates with minor adjustments to flag-based ones.

## Lighting Vocabulary

| Phrase | Effect |
|---|---|
| `three-point lighting setup` | Classic portrait studio look |
| `soft diffused studio lighting, rim light for silhouette separation` | Editorial headshot |
| `golden hour, warm rim light wrapping silhouettes` | Sunset cinematic |
| `harsh super-flash, blown-out highlights, subject still visible` | 2000s / early-digicam aesthetic |
| `narrow beam spotlight, sharp edges, high falloff shadow` | Theatrical / moody |
| `natural daylight from upper left, warm realistic shadows` | Product on surface |
| `moody atmospheric lighting, cool blues and purples contrasted by warm golden highlights` | Cinematic product poster |
| `neon-lit, electric {color} and deep {color} lighting, high-contrast, surreal sci-fi` | Cyberpunk portrait |
| `cinematic warm key + sculpting rim, film grain` | Editorial grit |
| `direct front flash, 35mm lens, nostalgic glow` | 90s film portrait |
| `harsh on-camera flash, specular highlights, strong catchlights, high-contrast film grain` | 35mm flash editorial |
| `RAW iPhone unprocessed, full camera quality, momentary blur` | RAW iPhone aesthetic (GPT Image 2 favored) |
| `2003 digital camera, slight noise, shallow flash falloff` | Early-digicam family snapshot |
| `90s point-and-shoot camera quality, slight chromatic aberration` | 90s point-and-shoot |
| `wooden lantern lighting mixed with gentle natural window light, subtle film grain` | Vintage Japanese ryokan / onsen |

## Camera / Lens Vocabulary

| Phrase | Use |
|---|---|
| `Sony A7III with 85mm f/1.4 lens, shallow depth of field` | Professional headshot compression |
| `full-frame 100mm, f/8, 1/2000, ISO100, 8K` | Product macro |
| `35mm cinematic lens, slightly wide-angle, center-weighted` | Environmental / crowd |
| `high-angle drone photograph` | Monumental / urban sculpture |
| `top-down flatlay, direct top-down view, 1:1 format` | Product flatlay |
| `orthographic-style, no forced perspective` | Isometric / architectural |
| `axonometric 3D miniature` | Diorama / model scene |
| `eye-level, full-body 3/4 studio shot, slightly elevated angle` | Fashion editorial |
| `mirror selfie, tight composition, phone in frame` | UGC selfie |
| `FPV close-up bokeh background` | Shallow-DoF portrait |

## Format-Spec Anatomy (deliverable format + dimensions + DPI)

Specify the deliverable shape, not just aspect ratio. Strongest signal on ChatGPT (DALL·E 3 / GPT Image 1) — ChatGPT respects file-format + dimension cues. Other natural-language models (GPT Image 2, Nano Banana, FLUX, Imagen) parse the cues but ignore actual file format (the API/UI controls it). Midjourney/SDXL parse via flags / output settings.

| Use case | Format spec to write into prompt |
|---|---|
| App icon / favicon | `PNG, 512x512` (or 1024x1024) `with white or transparent background` |
| Flat UI icon set | `PNG, 64x64 each, consistent palette` |
| Logo (vector-friendly) | `SVG format for scalability` (note: only ChatGPT can deliver SVG-style descriptions; raster models output raster regardless) |
| Web hero / landing | `JPEG, 1920x1080` |
| Social banner (X/Twitter header) | `JPEG, 1500x500` |
| Instagram post | `PNG, 1080x1080` |
| Instagram story / Reel | `PNG, 1080x1920` |
| YouTube thumbnail | `JPEG, 1280x720` |
| LinkedIn header | `PNG, 1584x396` |
| Print poster (small) | `PDF, 18x24 inches at 300 DPI` |
| Print poster (large) | `PDF, 24x36 inches at 300 DPI` |
| Magazine cover | `JPEG, 8.5x11 inches at 300 DPI` |
| Business card | `PDF, 3.5x2 inches at 300 DPI` |
| Wedding invite | `JPEG, 5x7 inches at 300 DPI` |
| Album art | `JPEG, 3000x3000` |
| Book / ebook cover | `JPEG, 1600x2560` (Kindle) or `JPEG, 2560x1600` |
| Mobile wallpaper | `JPEG, 1170x2532` (iPhone) |
| Desktop wallpaper | `JPEG, 2560x1440` or `3840x2160` (4K) |
| Animated GIF | `GIF, 500x500, smooth loop` |
| Sticker pack | `PNG, 512x512, transparent background` |
| Ebook page illustration | `PNG, 2480x3508 (A4)` |

For ChatGPT specifically, end the prompt with `Please include a gen_id with the delivery.` so you can reference and iterate the image later.

## Aspect Ratio Patterns

| Use case | Ratio to specify |
|---|---|
| Product marketing / Instagram square | `1:1` or `1080x1080` |
| Magazine cover / phone wallpaper | `9:16` |
| Cinematic still / landscape poster | `16:9` |
| Ultra-wide film look | `2.35:1` |
| Bento grid infographic | `16:9 landscape, asymmetric bento grid` |
| Photo book cover | `9:16 photo book style magazine cover` |

Always put the ratio as its own clause: `... 1080x1080 format.` not `... 1080x1080.`

## Style / Medium Tags (load-bearing)

These actually shift the output substantially:

- **Film stock:** `Kodak Portra 400`, `Ilford HP5`, `Polaroid SX-70`, `cross-processed slide film`
- **Era:** `1990s camera style`, `2000s digicam aesthetic`, `Tang Dynasty oil painting, Northern Song style`
- **Director/studio:** `DreamWorks Animation soft render`, `Wes Anderson symmetry`, `Studio Ghibli watercolor`
- **Art movement:** `Baroque / Rococo ornate frame`, `Swiss International typography`, `Bauhaus geometric`, `ukiyo-e woodblock`
- **Render engine:** `Octane render`, `Unreal 5 cinematic`, `Blender cycles photorealistic`
- **Material culture:** `Apple liquid glass (85-90% transparent), whisper-thin borders`, `plush PVC figure`, `origami with visible creases`, `marble bas-relief`

## Identity Anchor Phrases (ranked by strength)

These work on any natural-language model (Nano Banana, GPT Image 2, FLUX, Imagen). For Midjourney, use `--cref <url> --cw 100` instead. For SDXL/SD3, use IP-Adapter / InstantID at the workflow level.

1. `The face must be 100% identical to the uploaded image. Do not change the face.` (strongest)
2. `Keep the facial features of the person in the uploaded image exactly consistent.`
3. `Same face from the reference image. Preserve: facial features, expression, hairstyle.`
4. `The person from the attached image (uploaded image facial details).`
5. `Based on the provided image, same face.` (weakest — use only for stylistic remixes)

For multi-panel cross-image consistency on GPT Image 2 / Nano Banana Pro, layer in: `the same character from panel 1, identical wardrobe and hair`.

Repeat the anchor at the top AND near the end of long prompts.

## Preservation Clauses (for edits)

```
Preserve entirely unchanged:
- face, facial features, expression
- hairstyle and all fine details
- pose, posture, body orientation
- clothing / outfit design and colors
- background, lighting direction, color grade
- overall art style

Only modify: {explicit single region}.
Match the original: lighting logic, perspective, depth of field, grain.
```

## Single-Object Rule

When you want exactly one object, Pro still occasionally adds a second. Counter with an explicit block:

```
Strict Single-Object Rule:
Render only ONE object in the entire frame.
Do NOT show a second object — not as reflection, not as shadow, not as silhouette,
  not as a ghost image, not as a partial duplicate, not behind or beside.
No duplicate objects, no mirrored front-and-back pairings.
The object must appear alone, floating.
```

## Non-Destructive Edit Pattern

```
Perform non-destructive background editing on the attached photo:
preserve the foreground subject(s) entirely unchanged — posture, facial features,
expression, clothing, hairstyle, all fine details — with zero alterations.

Only modify the background area to naturally integrate {new element}.
Match the original photo's lighting logic, color grade, and perspective.
The result should feel like a natural, unplanned part of the scene.
```

Works for: hidden Easter eggs (Ghostface), celebrity integration, weather changes, era swap, environment replacement.

## Multi-Reference Fusion Pattern

```
Combine the attached images as follows:
- Image 1 → subject identity (face, body)
- Image 2 → background / environment
- Image 3 → style reference (color grade, texture, mood)
- Image 4 → wardrobe / material reference

Blend seamlessly with consistent lighting logic from Image 2.
```

## Text-in-Image Pattern

```
Render the text "{EXACT STRING}" in {font family, weight, size relative to frame}.
Placement: {centered / upper-third / overlaid on cube / below each base}.
Spelling must be exact. Kerning and leading consistent. No misspelling.
```

Nano Banana non-Pro: keep strings under ~15 words, Latin script only. Pro handles CJK, multi-line quotes, and longer headlines.

## Anti-AI-Glamour Clause

For candid / lifestyle / "real life" photos, all natural-language models default to glossy AI rendering unless explicitly vetoed. Append:

```
Realistic skin texture with visible pores, natural flyaway hairs, slight asymmetry,
no glamour retouching, no beauty filter, no overly polished AI aesthetic.
Faces and postures must look like real pedestrians, not styled models.
Phone-camera perspective, not studio perfection.
```

Effective on GPT Image 2 and Nano Banana Pro. Imagen needs only the first sentence; FLUX usually doesn't need it.

## Cross-Panel Consistency Pattern (Pro tier)

For multi-shot character/IP series:

```
The character is the same person across all panels — identical face, hairstyle,
wardrobe color and silhouette, age, and skin tone. Only pose, expression, and
camera angle change between panels. Same lighting style, same color grade,
same time-of-day across the series.
```

Strongest on GPT Image 2 and Nano Banana Pro. Midjourney v7 with `--cref` works for the face but wardrobe drift is common.

## Bento / Infographic Module Pattern (Pro only)

```
Create a {style} Bento grid infographic with {N} modules, {ratio} landscape.
Hero card: 28-30% | Info modules: 70-72%.

M1 — Hero: {product name}, {rendering style}, label
M2 — {section title}: {content type + count + icon rule}
M3 — {section title}: ...
...

Module cards: {card style — liquid glass, paper, matte}. 
Typography: {font family + weight pattern}.
Background: {description, blur behind cards}.
```

## Placeholder Conventions

| Style | Example | Use |
|---|---|---|
| `[BRACKET_CAPS]` | `[CHARACTER]`, `[COLOR_THEME]`, `[SUBJECT]` | Reusable templates for humans to fill |
| `{argument name="x" default="y"}` | `{argument name="quote" default="Stay hungry"}` | Raycast Snippets |
| `<tag>...</tag>` | `<role>`, `<step 1>`, `<final output format>` | Multi-step meta prompts (Pro: GPT Image 2, Nano Banana Pro) |
| `{{mustache}}` | `{{brand}}`, `{{product}}` | Programmatic templates |

Pick one convention per prompt — mixing confuses both humans and the model.

## Composition Idioms

- `symmetrical centered full-body portrait, clean editorial` — fashion
- `perfectly centered in frame, fully visible head to toe` — full-body isolation
- `subject occupies one-third, text two-thirds` — quote card
- `asymmetric bento grid` — infographic
- `axonometric miniature model in center, ink wash diffusion around` — novel/movie poster
- `isometric 3D diorama, each element on its own platform` — geographic/thematic layouts
- `4-panel grid: sketch → lineart → flat color → finished` — process reveal
- `left half realistic, right half wireframe, sharp vertical cut` — split-style render

## Negative Prompt Vocabulary

Append at the end as `NEGATIVE:` or `Do NOT:` block.

Common:
```
NEGATIVE: blur, low quality, noise, watermark, extra limbs, malformed hands,
distorted face, text errors, duplicate objects, cropped subject, flat lighting.
```

Use selectively. Over-long negatives reduce positive signal.
