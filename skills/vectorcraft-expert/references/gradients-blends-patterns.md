# Gradients, blends and patterns (Lesson 11)

Own-words summary of Classroom in a Book 2026, "Gradients, Blends, and Patterns". Core distinction from the book: in a **gradient** colours blend *inside* one object; in a **blend** shapes and colours step *between* objects.

## Gradients
- Fill or stroke with `fill:{gradient:{kind:"linear"|"radial"|"freeform", angle, stops:[{offset 0..1, color, opacity, midpoint}], start, end, aspect, focal, dither}}` on `draw_shape`, `draw_path`, `set_paint` or `paint.setFill` / `paint.setStroke`.
  - Verified: linear `angle:90` with two CMYK stops — **stop 0 sits at the bottom**, stop 1 at the top (y-down document; angle measured counter-clockwise from the right).
  - `span:"selection"` runs one gradient across several objects (the book's "apply to multiple objects"); default fits each object.
  - Transparent stops (`opacity`) fade art into the background; `dither:true` hides banding in large fills.
- Gradient on strokes: `paint.setStroke {gradient:{…}}`. `doc_inspect` reports the stroke mode (within / along / across) as `strokeOptions.gradientMode`; no documented parameter to change it was found in `stroke.set`, so check `paint.editGradient` params before relying on along/across.
- Edit later: `paint.editGradient`, geometry `paint.setGradientGeom`, select a stop `gradient.selectStop`.
- Save/reuse: `swatch.new {gradient}` or `gradient.presets.save` / `.apply` / `.list`.
- **Freeform** gradients (points or lines of colour): `paint.setFill {gradient:{kind:"freeform"}}` then `paint.freeform.addPoint` / `setPoint` / `addLine` / `deletePoint`. Good for soft, painterly backgrounds.
- Gradient mesh (realistic shading): `object.mesh.create`, `object.mesh.setPointColor`, `.movePoint`, `.addLine`, `.expand`.

## Blends
- `object.blend.make {ids, steps | distance | smooth:true, orientation, easingType}` (verified: 6 steps between a red and a blue circle). Options later: `object.blend.options`.
- Specified steps → repeated objects (stripes, dotted trails); smooth colour → soft shading between two shapes.
- Along a custom path: `object.blend.replaceSpine` with a drawn path; `reverseSpine`, `reverseFrontToBack`; edit the spine with `object.blend.spine.*`.
- Key objects stay editable: recolour or move an end object and the blend updates. `object.blend.expand` only when finished.

## Patterns
- Apply existing: patterns are swatches → `fill:{swatch:"Pattern name"}`; list with `pattern.list` / `swatch.list`.
- Create: select the motif, `object.pattern.make {name, tileType: grid|brickByRow|brickByColumn|hexByColumn|hexByRow, brickOffset, width, height}` → pattern editing mode; `pattern.options` for spacing/overlap; finish with `object.pattern.done` (or `cancel`, `saveCopy` for variants).
- Edit later: `object.pattern.edit`. Transform only the tile inside a shape: `pattern.transform`, or `object.transform {objects:false, patterns:true}`.
- Good seamless patterns: motifs crossing the tile edge are repeated automatically in pattern mode; check by rendering a large rectangle filled with the pattern.

## Common mistakes
- Expecting angle 90 to run top-to-bottom: it runs bottom-to-top.
- Too few blend steps (visible banding) or too many (heavy file).
- Scaling a patterned object and the tile scaling too (or not): decide with `patterns`.
