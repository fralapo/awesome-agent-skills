# Generative AI features and VectorCraft substitutes (Lessons 3, 8, 14)

Own-words summary of the generative sections of Classroom in a Book 2026. The book itself warns these features change often.

## What Illustrator offers
| Feature | What it does (target behaviour) | VectorCraft |
|---|---|---|
| Text to Vector Graphic | prompt → editable vector art; content types Scene / Subject / Icon; detail slider; style reference, effects, colour and tone; works inside a placeholder shape to control size; several variations | not available as of 2026-11-03 — re-check |
| Generative Shape Fill | fills a simple outline with detailed art matching the document's style (prompt optional); the original outline stays underneath | not available as of 2026-11-03 — re-check |
| Generative Expand | extends artwork beyond its bounds (wider layout, print bleed), then "Combine" turns it into normal art | not available as of 2026-11-03 — re-check |
| Generative Recolor | colour variations of art from a text prompt or sample prompts | not available as of 2026-11-03 — re-check (non-AI `recolor.*` exists) |
| Retype | recognises fonts in outlined text/images | not available as of 2026-11-03 — re-check |
| Mockup | applies art to product photos | not available as of 2026-11-03 — re-check |

Snapshot of 2026-11-03: searching all 906 command ids (`command_list`) and the 140 effect ids (`effect.list`) found no generate/prompt/mockup/retype command. ArtCraft apps update daily: **before using the substitutes below, re-check** with `command_list {filter:"generat"}`, `{filter:"mockup"}`, `{filter:"retype"}`, `{filter:"recolor"}`. If a command appears, use it following the target behaviour in the table (placeholder shape for size, Icon/Subject/Scene choice, detail level, style reference, several variations, then pick and keep it editable).

## Substitutes while the features are absent
- **Text to Vector**: the agent *is* the generator. Plan the shapes, write SVG path data (`draw_path {d}`) or build from live shapes + Shape Builder, keep the detail level of an "Icon" (few shapes, flat colours) unless a scene is requested. External generators can serve as a moodboard, but build the production art yourself in VectorCraft so it stays clean, editable vector.
- **Shape Fill**: draw the detail inside the outline and clip it with `object.clippingMask.make` (outline on top), or use Draw Inside semantics.
- **Generative Expand / bleed**: extend backgrounds geometrically (enlarge the background rectangle to the bleed box, mirror or repeat pattern art with `object.repeat.mirror`), or for photos extend the image in a raster editor (e.g. ArtCraft PhotoCraft, if available) before placing.
- **Generative Recolor**: produce palettes with `color.harmony` or from brand swatches, then apply with `recolor.apply {map}`; export one PNG per variant for comparison.
- **Prompt habits from the book that still apply**: be specific about subject, style and colour count; generate several variants and pick; always check the result is editable vector, simple enough, and on brand.

## Caution
- Never present generated or AI-helped art as licensed material without checking rights; do not reuse third-party template or stock catalogue assets in production unless their licence allows it.
