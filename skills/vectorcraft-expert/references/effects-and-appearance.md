# Appearance, live effects, 3D and graphic styles (Lesson 13)

Own-words summary of Classroom in a Book 2026, "Exploring Creative Uses of Effects and Graphic Styles".

## Appearance
- An object can carry several fills and strokes, stacked, each with its own opacity and effects. Order in the stack = drawing order.
- `appearance.addFill` (Cmd+/), `appearance.addStroke`, `appearance.setItem`, `appearance.moveItem`, `appearance.duplicateItem`, `appearance.removeItem`, `appearance.clear`, `appearance.reduceToBasic`, `appearance.copyFrom`, `appearance.targetContents`.
- Classic recipe from the book: text with a thick outer stroke under a thin inner stroke under the fill = sticker/badge lettering without outlining.
- Transparency and blend modes: `transparency.set {opacity, blendMode}`; `opacity` on draw tools is in % (doc_inspect returns `opacityPct`).

## Live effects
- `effect.apply {ids, effect, params}` or `effects:[…]` directly on `draw_shape`/`draw_path` (verified: `stylize.dropShadow` on a path). Edit with `effect.setParams`, reorder `effect.move`, remove `effect.remove`, bake `effect.expandAppearance`.
- Catalogue: `effect.list` (defaults and params per effect). Main groups:
  - **Vector effects** (stay sharp): `distort.*` (roughen, zigZag, puckerBloat, twist, tweak, transform, freeDistort), `stylize.roundCorners`, `stylize.scribble`, `path.offsetPath`, `path.outlineStroke`, `convertToShape.*`, `warp.*` (arc, arch, flag, wave, rise, fisheye, bulge, inflate, squeeze, twist…), `pathfinder.*`, `cropMarks`.
  - **Raster ("Photoshop") effects** (generate pixels): `stylize.dropShadow`, `innerGlow`, `outerGlow`, `feather`, `blur.*`, and the artistic, brushStrokes, sketch, texture, pixelate, adjust groups.
- Raster effects follow `document.rasterEffectsSettings` (book tip: set 300 ppi for print, otherwise effects look pixelated).
- Verified pitfall: in a CMYK document a drop shadow is an RGB raster; PDF/X export warns it is converted to CMYK and dark shadows may become rich black. Prefer CMYK shadow colours or keep shadows subtle.
- Warp on text (Lesson 13 "Styling text with a Warp effect"): `warp.*` keeps the text editable, unlike envelope expand.
- Disable to edit: remove/re-apply or set the effect hidden via `appearance.setItem`.

## 3D
- `threeD.extrude`, `threeD.revolve`, `threeD.inflate`, `threeD.rotate` (params: depth, rotationX/Y/Z, perspective, lighting, bevel…); lighting presets `effect.lightingPreset`.
- Revolve a half-profile path around its left edge to make bottles, cups, vases; extrude a flat logo for a 3D wordmark.
- **Not available as of 2026-11-03 (snapshot — re-check with `effect.list` and `document.formats`):** Substance materials on 3D objects and 3D export (OBJ, USDA/USDZ, GLTF via Export Selection). Target behaviour in Illustrator: apply materials from the 3D panel and export the selection for 3D apps.

## Graphic styles
- Save an appearance as a reusable style: `graphicStyle.new`, apply `graphicStyle.apply`, update `graphicStyle.redefine`, unlink `graphicStyle.breakLink`; libraries `graphicStyle.libraries` / `addFromLibrary`.
- Style on a **layer** (`layer.target` + apply): everything moved onto that layer takes the style; style on an object travels with the object.

## Scaling strokes and effects
- Scale with `object.scale {strokes:true}` (Scale Strokes & Effects) when a styled element must keep its look at another size; preference `prefs.set`.

## Common mistakes
- Expecting raster effects to stay vector in SVG: shadows/glows/blur export as SVG filters or pixels.
- Stacking many raster effects on big areas: slow and heavy PDFs.
- Expanding appearance too early and losing editability.
