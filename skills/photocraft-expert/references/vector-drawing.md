# Vector drawing techniques (Lesson 8)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 8, mapped to PhotoCraft.
⧗ = not available in PhotoCraft/LightCraft as of 2026-11-03 (snapshot — re-check with `command_list {filter}`
on the live app; ArtCraft apps update daily). The Photoshop behaviour described stays the target.


## Concepts
- Raster = fixed pixel grid (photos); vector = mathematical curves, crisp at any scale (logos, type).
- A path is an open or closed outline; it does not print by itself. Anchor points end segments; direction
  handles shape curves. Smooth points have linked handles; corner points break the curve.
- The Work Path is temporary: save it (rename) or it is replaced by the next drawing.
- Tool modes: **Shape** (vector layer with fill/stroke, prints), **Path** (only in Paths, for selections,
  type on path, clipping paths), **Pixels** (paints on the active layer).
- Shapes and type never exceed the document's pixel resolution when exported; for true vector print use
  VectorCraft/DesignCraft (Illustrator/InDesign equivalents).
- Fewer anchor points = smoother, easier curves.

## PhotoCraft calls
Pen-tool gestures (click-drag) are not needed: give the knots directly.
| Task | Call |
|---|---|
| Draw / replace a path | `path.set {name:"work", path:{subpaths:[{closed:true, knots:[[x,y] | {anchor,in,out,smooth}]}]}}` |
| Save/rename path | `path.rename`; list with `path.list`, inspect `path.info` |
| Edit points | `path.moveAnchors`, `path.moveHandle`, `path.bendSegment`, `path.addAnchor`, `path.deleteAnchor`, `path.convertPoint` |
| Path → selection | `path.toSelection` (`addToSelection`, `subtractFromSelection`) |
| Selection → path | `select.toWorkPath {tolerance:2}` |
| Path → vector mask | `layer.vectorMask.fromPath`; or `"path"` param of `layer.newAdjustmentLayer.*` |
| Shape layer | `shape.create {kind:"rect|roundedRect|ellipse|polygon|star|line|path", rect, fill, stroke}` ✔ |
| Edit shape | `shape.edit`, `shape.info`; booleans `layer.combineShapes.unite|subtractFrontShape|intersectShapeAreas|excludeOverlappingShapes` |
| Custom shapes | `shape.presets.list`, `shape.presets.place`, `edit.defineCustomShape` |
| Fill / stroke a path on pixels | `path.fill`, `path.stroke` |
| Clipping path for print | `path.clippingPath.set` |
| Export paths | `file.export.pathsToIllustrator` (path-based; may be blocked in automation) |

## Procedure: recolour a traced object + logo
1. Trace the fruit with `path.set` (closed, smooth knots on curves, corners where needed); or faster:
   `select.object` / `select.subject` → `select.toWorkPath`.
2. `path.rename` → "Lemon"; `path.toSelection`.
3. With the selection active, `layer.newAdjustmentLayer.hueSaturation {hue:17}` – the selection becomes its
   mask ✔ (orange → lemon yellow).
4. Logo: paragraph type bold 55 pt, right aligned, white, tracking −25, all caps.
5. `shape.presets.place` a flower shape, scale to ~1.5 in height, fill yellow, no stroke.
6. Optional: duplicate the shape at 50 % opacity for a pattern; use `layer.distribute.*` for even spacing.

## Pitfalls
- Choose Shape vs Path before drawing (`shape.create` vs `path.set`).
- Preset shapes inherit the current fill/stroke: recolour after placing.
- For a mask that stays editable as geometry, use a vector mask; pixel masks are edited by painting.
- If a style seems to have no effect, clear old effects and reset Opacity/Fill to 100 %.
- Curvature Pen / Freeform Pen interaction ⧗ in automation; use knots or selection → path.
