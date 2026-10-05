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

**GPT Image 2.5** (Flare / Sunburst) follows the GPT Image 2 column, plus: Sketch input in ChatGPT for layout/recomposition, role-assigned 2–3 reference composites, and reliable multi-turn edit chains (one change per turn). Sunburst is the pick when one element must change and everything else must stay put. Details: `models/gpt-image-2-5.md`.

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

GPT Image 2.5 is the strongest here when each reference gets **one job plus a conflict priority**: "Image 1 is the primary reference for the product; Image 2 provides only color and lighting; Image 3 provides only composition and negative space. Conflict priority: Image 1 label accuracy > Image 3 layout > Image 2 lighting. Do not replicate objects from Image 2 or 3." See `models/gpt-image-2-5.md` Pattern 3.

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

## Repair recipes (GPT Image 2.5)

Twenty focused follow-up edits for an image that is *almost* right. Each one changes a single thing and names what must stay. Written for GPT Image 2.5 (Sunburst for tight work), and they work on any natural-language editor (GPT Image 2, Nano Banana Pro). Source: `VulcanEon/awesome-gpt-image-2.5-prompts` `docs/REFINEMENTS.md` (MIT, original recipes, not independently tested).

Workflow: save the best output as the **master** → apply one recipe per turn → branch variants from the master, not from each other. Where pixels must stay identical, composite the approved region into the original instead of trusting the preservation sentence.

### Protect a face during restyling
Input: Original portrait plus latest output
```
Compare image 1, the identity reference, with image 2, the latest styled version. In image 2 correct only the face to restore image 1's eye spacing, nose shape, jaw contour and age appearance. Retain image 2's pose, clothing, framing and light. Do not beautify or change skin tone.
```

### Remove invented lettering
Input: Output with unwanted text
```
Remove the unsolicited lettering on [EXACT OBJECT OR REGION]. Rebuild that surface as plain [MATERIAL] under the existing light. Protect all approved text elsewhere, along with the person's face, object silhouettes and crop. Do not replace the removed words with symbols or different words.
```

### Replace one headline
Input: Approved poster and exact new copy
```
Replace only the headline [OLD TEXT] with [NEW TEXT]. Use the existing headline box, alignment and color. Permit a two-line break if necessary, but do not overlap the subject. Keep all secondary text, dates, product details and background objects as they are. Return one edited poster.
```

### Adapt a horizontal image to vertical
Input: Approved horizontal image
```
Adapt this composition to 4:5 portrait by extending the set above and below. Preserve the full person, shoes and product. Continue the existing wall, floor and shadow directions. Keep the headline legible with its current wording. Do not stretch the person, crop the feet or create a second subject.
```

### Create one controlled background variant
Input: One approved master image
```
From this master image, change only the backdrop color to [COLOR]. Preserve garment colors, skin, object locations, lettering, crop and light direction. Recalculate only the slight colored bounce that the new wall would physically create. Do not add set pieces. Produce one variant from this original master.
```

### Restore a product label
Input: Original packshot and edited scene
```
Use image 1 as the label reference. In image 2, correct only the front label to match its exact supplied spelling, color blocks and logo placement. Keep bottle shape, cap, hand grip and scene unchanged. Match the label to the existing perspective; do not add health, performance or certification claims.
```

### Change material while retaining geometry
Input: Approved product or room image
```
Change the [OBJECT] surface from [OLD MATERIAL] to [NEW MATERIAL]. Preserve its silhouette, thickness, dimensions, seams and position. Let the new surface respond to the current light with appropriate roughness. Keep neighboring objects and background textures untouched. No additional bevels, handles or ornament.
```

### Ground a floating subject
Input: Image with missing contact shadow
```
Repair only the contact shadow beneath [OBJECT OR FOOT]. Its darkest narrow region should meet the existing contact point and soften outward in the established light direction. Keep object position, floor texture and all other shadows unchanged. Do not move the subject to hide the error.
```

### Reduce waxy skin
Input: Over-smoothed portrait
```
Restore subtle natural skin texture on the face: fine pores, gentle tonal variation and normal under-eye detail appropriate to the same adult. Preserve identity, expression, skin tone and exposure. Avoid artificial freckles, extra wrinkles, sharpening halos or changes to makeup and hair.
```

### Keep motion blur off the subject
Input: Action image with a smeared subject
```
Retain the background train's horizontal motion blur. Restore sharp contours and natural detail only to the foreground face, hands and flowers using the attached reference. Keep the current composition and lighting. Do not sharpen the train, add speed lines or introduce a second blur direction.
```

### Repair a product grip
Input: Image with a malformed grip
```
Correct only the hand holding [PRODUCT]. Show five anatomically plausible digits, with the thumb opposing the fingers and realistic pressure at contact points. Preserve the product outline and label, wrist location, sleeve and camera angle. Do not add a second supporting hand or hide the product.
```

### Repair a sequence grid
Input: Sequence sheet and intended row/column count
```
Reformat the supplied poses into exactly [ROWS] rows and [COLUMNS] columns of equally sized cells. Preserve pose order, character identity, outfit and camera. Use uniform empty gutters. Show one complete pose per cell without cutting off extremities. Do not add numbering or invent additional poses.
```

### Stabilize character scale
Input: Pose sheet with drifting scale
```
Normalize the character's apparent scale across this pose sheet. Use the standing reference for body proportions and the same ground baseline in every cell. Keep each intended action, costume detail and face. Do not force airborne poses onto the floor; retain their deliberate vertical displacement relative to that common baseline.
```

### Restore a missing costume layer
Input: Continuity sheet with an identified error
```
In panel [NUMBER], restore the [GARMENT] already present in the previous panel. Match its color, cut and fastening. Keep the current panel's action and every other garment. Leave all other panels unchanged. The sequence must accumulate clothing; no earlier layer should disappear.
```

### Specify one next frame
Input: Accepted frame and exact next action
```
Use this image as the fixed scene reference. Create one next frame where [ONE SMALL ACTION]. Retain camera position, focal character, costume, background geometry and light. Change only the body parts needed for that action, with physically connected joints. Do not produce a collage or add scene transitions.
```

### Apply artwork to fabric
Input: Flat approved artwork and tote photograph
```
Place image 1's artwork on the front panel of the tote in image 2. Preserve the design's colors, wording and relative proportions. Let it follow the fabric's existing folds and weave, with subtle ink absorption. Keep the bag silhouette, straps, hand and background unchanged. Do not invent a second logo or print on the straps.
```

### Build a scene around a screenshot
Input: A screenshot with private information removed
```
Create a clean promotional scene around the supplied interface: a near-front-facing laptop on a pale desk with morning side light. Use the screenshot only for screen content, keeping its hierarchy and layout. Leave the right third empty for copy added later. Add no readable text elsewhere. Keep reflections weak enough to preserve screen legibility.
```

### Clean up a supplied diagram
Input: Sketch plus exact node/edge list
```
Redraw this sketch as a tidy flat diagram. The attached node and edge list is authoritative: preserve every label and connection direction. Improve spacing, alignment and contrast only. Keep crossing lines distinguishable and use one consistent arrow style. Do not add explanations, invent nodes or turn it into a decorative 3D scene.
```

### Request a clean product isolation
Input: Clear original packshot
```
Isolate the supplied product with a small margin on every side. Retain its exact outline, label, cap and material. Remove the original room, floor and cast shadow. Request a transparent export if the selected tool supports it; otherwise use a uniform neutral background for later masking. Do not paint a checkerboard into the picture.
```

### Make intentional space for copy
Input: Approved scene with a crowded copy area
```
Clear the upper-left quarter of this composition by removing only the small background decorations there. Continue the existing wall texture and light. Preserve the person, product, main set geometry and crop. Keep that area low contrast and unlettered so a designer can add copy later. Do not move the main subject or erase approved text elsewhere.
```
