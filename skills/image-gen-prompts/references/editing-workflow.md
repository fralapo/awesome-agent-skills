# Editing Workflow — Cross-Model

How to edit existing images: non-destructive background changes, inpainting (mask-based), multi-image fusion, before/after restoration, and cross-panel character consistency. Each model family has a different workflow surface.

## Operation × Model matrix

| Operation | Nano Banana / Pro | GPT Image 2 | GPT Image 1 / DALL·E 3 | Midjourney | SDXL / SD3 | FLUX | Imagen | Ideogram | Recraft |
|---|---|---|---|---|---|---|---|---|---|
| Background swap (preserve subject) | natural-language prompt | natural-language prompt | mask via Edit API | Vary Region | inpaint workflow | FLUX Fill | reference customization | inpainting | inpaint |
| Inpainting (masked region) | inline phrasing | OpenAI Edit API mask | OpenAI Edit API mask | Vary Region | dedicated inpaint pipeline | FLUX Fill | n/a publicly | yes | yes |
| Outfit/wardrobe swap | text edit prompt | text edit prompt | mask | Vary Region | inpaint + IP-Adapter | FLUX Fill | n/a | n/a | n/a |
| Object addition (e.g. Easter egg) | non-destructive clause | non-destructive clause | mask | Vary Region | inpaint | FLUX Fill | n/a | yes | yes |
| Object removal | inline preserve clause + remove instruction | inline | mask | Vary Region (Erase) | inpaint with empty prompt | FLUX Fill | n/a | yes | yes |
| Era / weather change | non-destructive clause | non-destructive clause | mask | new gen with `--cref` | full re-gen with ControlNet | full re-gen | re-gen | re-gen | re-gen |
| Multi-image fusion | "img1 = subject, img2 = bg, img3 = style" | "based on this character + this background" | n/a | `--cref` + `--sref` combos | IP-Adapter + ControlNet | FLUX Redux | reference customization | style ref | brand style |
| Before/after restoration | "restore + colorize the attached photo, keep identity" | strong (uses world prior) | mask + prompt | n/a | restoration LoRA | restoration model | n/a | n/a | n/a |
| Cross-panel character consistency | preserve clause + multi-panel grid prompt | strongest — single prompt for N panels | weak | `--cref --cw 100` per panel | IP-Adapter / InstantID per gen | PuLID-FLUX per gen | n/a | n/a | brand style |

## Non-Destructive Background Edit (universal pattern)

Best on Nano Banana Pro and GPT Image 2. Adapts to FLUX with FLUX Fill mask.

```
Perform non-destructive background editing on the attached photo.

Preserve entirely unchanged: foreground subject(s), posture, facial features, expression,
clothing, hairstyle, all fine details — zero alterations.

Only modify the background area: replace with [NEW_ENVIRONMENT] / add [NEW_ELEMENT]
naturally integrated into the scene.

Match the original photo's: lighting direction, color temperature, perspective, depth of field.
The result should feel like a natural part of the scene — like an unplanned Easter egg, not a composite.
```

## Inpainting (mask-based)

Used on GPT Image 1/2, FLUX Fill, SDXL/SD3 inpaint, Midjourney Vary Region, Ideogram, Recraft.

The prompt describes ONLY the change to the masked region — not the rest of the image. Common mistake: writing a full-scene prompt; the model then tries to render the whole scene inside the mask.

```
[Single sentence describing what should appear in the masked region only.]
Match the surrounding photo's lighting, perspective, and color grade exactly.
Do not introduce a hard seam at the mask edge.
```

For OpenAI Edit API: pass `image`, `mask` (transparent PNG = area to change), and the prompt above.

## Multi-Image Fusion (role-assigned)

Best on Nano Banana / Pro:

```
Combine the attached images as follows:
- Image 1 → subject identity (face, body)
- Image 2 → background / environment
- Image 3 → style reference (color grade, texture, mood)
- Image 4 → wardrobe / material reference

Blend seamlessly with consistent lighting logic from Image 2.
Preserve the face from Image 1 100%.
```

GPT Image 2 supports a similar pattern via natural-language phrasing of "the character from this image, in the environment from this other image".

Midjourney: combine via `--cref <url1> --sref <url2>` flags. Multiple `--sref` for style stacking.

SDXL/FLUX: workflow-level — IP-Adapter for style, InstantID for face, ControlNet for structure, all chained.

## Before/After Photo Restoration

Best on GPT Image 2 (strong photo-restoration prior) and Nano Banana Pro.

```
Restore and gently colorize the attached old photograph.
Preserve: composition, framing, the subject's identity (face structure, skin tone, age),
clothing silhouette, era of styling.
Repair: scratches, creases, dust, faded color, low contrast.
Do NOT modernize: clothing should remain period-accurate. Hair/makeup remain era-correct.
Output: high-resolution, natural color, restored photo print look.
```

## Cross-Panel Character Consistency (multi-shot series)

Best on GPT Image 2 (single prompt produces N consistent panels). On Nano Banana Pro use the same single-prompt approach. On Midjourney v7 use `--cref --cw 100` per panel (with drift on wardrobe). On SDXL/FLUX, use IP-Adapter + ControlNet workflow.

```
Generate a [N]-panel grid showing the same character in [N] different scenarios.
The character is the same person across all panels — identical face, hairstyle, wardrobe color
and silhouette, age, and skin tone. Only pose, expression, and camera angle change.
Same lighting style, same color grade across the series.

Panels:
1. [SCENARIO_1]
2. [SCENARIO_2]
[...]

Format: [GRID_LAYOUT, e.g. 3x3], each panel labeled with shot type in safe margin.
```

## Edit-Mode Failure Modes (universal)

| Symptom | Likely cause | Fix |
|---|---|---|
| Face changed in edit | No identity anchor in prompt | Add the strongest anchor from `identity-preservation.md` |
| Background changed beyond what was asked | Model generated a new scene | Add explicit preservation clause; for masked workflows, draw a tight mask |
| Subject pose drifted | No pose-preservation clause | Add "preserve pose, posture, body orientation" |
| Lighting feels inconsistent | No "match original lighting" clause | Add it explicitly |
| Hard seam at mask edge | Prompt described too much | Trim prompt to describe only the masked change; ensure mask has feathered edges |
| Wardrobe shifted | No wardrobe-preserve clause | Add "keep clothing design and colors unchanged" |
| Two of the subject appear | Model duplicated | Add Strict Single-Subject Rule from `patterns.md` |
| Ghostface / Easter egg too prominent | Background element too described | Reduce description; add "hidden, partially obscured by [foreground element]" |
