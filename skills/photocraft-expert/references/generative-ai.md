# Generative AI (Lesson 15) and non-generative fallbacks

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 15, mapped to PhotoCraft.

## Photoshop concepts (reference)
- Traditional AI recognises/computes (faces, subjects, sky); generative AI creates new content.
- Firefly features: Generate Image (whole new image layer), Generative Fill (selection + prompt),
  Generative Expand (crop beyond the canvas), generative Remove, Generative Upscale, Harmonize (match a
  layer's light/colour/shadow to its background), Neural Filters (Smart Portrait, Photo Restoration,
  Colorize, Super Zoom).
- Generative layers keep variations; refine with a more descriptive prompt, style effects, style or
  composition reference images (strength slider); max ≈2000×2000 px generation, larger areas are upscaled.
- Credits, partner models with other terms, "commercially safe" training data claims, Content Credentials
  (provenance metadata).
- Ethics: ask the client whether AI is acceptable; real products/dishes deserve real photos; no invented
  content in documentary or news images.

## In PhotoCraft: not available as of 2026-11-03 (snapshot — re-check)
A `command_list` search on 2026-11-03 found no generative command (Generate Image, Generative Fill/Expand,
Upscale, Harmonize, Neural Filters, Sky Replacement, Content Credentials). ArtCraft apps update daily:
before using a fallback run `command_list {filter:"generat"}`, `{filter:"harmon"}`, `{filter:"upscale"}`,
`{filter:"neural"}`, `{filter:"sky"}` and, if a command now exists, use it with the Photoshop workflow above.

AI-*assisted* (non-generative) tools that existed on 2026-11-03:
`select.subject`, `select.object`, `select.sky`, `layer.removeBackground`, `paint.remove`,
`edit.contentAwareFill`, `image.crop {contentAware}`, `edit.contentAwareScale`, `image.detectFaces`.

## Fallbacks
| Need | Fallback |
|---|---|
| Extend a background | `image.canvasSize` or `image.crop` larger with `contentAware:true` ✔; or select the empty strip + `edit.contentAwareFill {output:"new"}` ✔ |
| Remove an object | `paint.remove` ✔ / `edit.contentAwareFill` ✔ / clone + heal |
| New image from a prompt | generate it with an external tool you are allowed to use, save the file inside the server's allowed read/write root and bring it in with `doc_place` |
| Harmonize a pasted object | clipped Curves + Color Balance to match, Color Lookup on top, contact shadow (Multiply layer, blurred), matching noise |
| Upscale | `image.imageSize {resample:"preserveDetails"}` + light sharpening; LightCraft denoise first |
| Smart Portrait | subtle `filter.liquify`; LightCraft eye/skin masks |
| Photo restoration | `filter.noise.dustAndScratches` on a masked copy, `paint.spotHealing`, `paint.cloneStamp` |
| Colorize B&W | Color-mode paint layers per area + Hue/Saturation colourize |
| Style transfer | `layer.newAdjustmentLayer.colorLookup` (.cube file) or `image.adjustments.matchColor` |

## Rules carried over
- Declare AI use to the client and respect their policy; keep originals and a non-AI version.
- Treat external design generators as inspiration/moodboards; do the production work (layers, masks, type,
  export) in PhotoCraft so the result stays editable.
- Mixing AI output with own photography and hand rework (e.g. Mixer Brush) is legitimate.
