# Typographic design (Lesson 7)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 7, mapped to PhotoCraft.
⧗ = not available in PhotoCraft/LightCraft as of 2026-11-03 (snapshot — re-check with `command_list {filter}`
on the live app; ArtCraft apps update daily). The Photoshop behaviour described stays the target.


## Concepts
- A type layer holds vector glyph outlines: it scales cleanly, but final sharpness is limited by the
  document's pixel size (small web files show jaggies sooner).
- Point type: anchored at a click, for short lines. Paragraph type: a box that reflows when resized.
- Clipping mask with type: put an image layer *above* the type and clip it, the image shows only inside
  the letters.
- Type on a path follows a path's direction (order of anchors); warp is a live attribute of the type layer
  (bend + horizontal/vertical distortion).
- Tracking = spacing across a range of letters; leading = line spacing; kerning = between two letters.
- OpenType features (ligatures, swash, fractions, stylistic sets), variable fonts (axes such as wght),
  colour fonts.
- JPEG/TIFF rasterise type; a PDF can keep it vector (in PhotoCraft `doc_export` to PDF is flattened ✔).

## PhotoCraft calls
| Task | Call |
|---|---|
| List fonts | `type.fonts` (verify the font exists before using it) |
| Point type | `type.create {x, y (baseline), text, font, size, color, align:"center"}` ✔ |
| Paragraph type | `type.create {box:[x,y,w,h], text, …}`; `type.convertToParagraphText` / `convertToPointText` |
| Style a range | `type.setStyle {layer, range:[start,end], font, weight, size, tracking, leading, caps:"all", color, kerning:"optical", features:{…}, variations:{wght:650}}` |
| Paragraph/character styles | `type.paragraphStyle.new|apply|redefine`, `type.characterStyle.*` |
| Image inside type | place image (`doc_place`) above the type layer → `layer.createClippingMask {layer:<image>}` |
| Inner shadow on type | `layer.layerStyle.innerShadow {blend:"multiply", opacity:48, angle:120, distance:18, size:16}` |
| Type on a path | create the path (`path.set` or a shape) → `type.attachToPath {layer, shape|work path, start|at, flip}` |
| Warp | `type.warpText {style:"wave", bend:33, horizontalDistortion:-23, verticalDistortion:5}` ✔ |
| Cylinder wrap (can label) | `edit.transform.warp {style:"cylinder", values:[7 numbers]}` (needs `values` ✔) |
| Type to shape / path | `type.convertToShape`, `type.createWorkPath` |
| Type selection | `type.createSelection` (type mask) |
| Find/replace, spelling | `edit.findAndReplaceText`, `edit.checkSpelling` |
| Missing fonts | `type.resolveMissingFonts`, `type.replaceAllMissingFonts` |
| Glyphs | `type.insertText` |

## Procedure: podcast title over a photo
1. Centre guide (`view.newGuide`); headline `type.create` serif/sans 115 pt, tracking 50.
2. Place a metal texture SO above it and clip; add an inner shadow to the type.
3. Short phrases on a path near the subject; duplicate and `path.transform`/`edit.transform` rotate ±15°.
4. Wave warp on each phrase.
5. Paragraph box from guide intersections; title 70 pt/55 leading; body 22/28; subheads bold 28; brand
   word in an accent colour.
6. Remove helper notes/guides, `doc_export` JPG.

## Pitfalls
- Point type in automation needs a baseline `y`, not the top of the text: check `bounds` in the result.
- Use a real bold instead of faux bold; check the font actually exists (`type.fonts`), else a fallback
  (e.g. Inter ✔) is used silently.
- Paste text without foreign formatting; clear style overrides when reapplying styles.
- On social carousels and slides, break lines at natural phrase or sentence boundaries, not mid-phrase.
- Keep type live until the final export; rasterise only when an effect requires pixels.
- Match Font ⧗ in PhotoCraft: identify fonts manually.
