# Pen, Curvature, Pencil and paths (Lessons 6 and 7)

Own-words summary of Classroom in a Book 2026, "Using the Basic Drawing Tools" and "Drawing with the Pen Tool". An agent does not drag a mouse: it builds paths from coordinates and handles, so Pen concepts matter even more.

## Path anatomy
- **Corner points**: no handles or split handles; the path changes direction sharply.
- **Smooth points**: both handles on one straight line; the curve flows through.
- Handle length controls how far the curve "pulls"; handle direction sets the tangent.
- Practical rules from the book, restated: few points, placed where a curve changes direction (its extremes), not mid-curve; handles roughly one third of the segment length.

## Drawing in VectorCraft
- `draw_path {d:"M…C…Z"}` with SVG path data: the most compact and precise method.
  - `M x y` move, `L` line, `C x1 y1 x2 y2 x y` cubic (previous point's out-handle, new point's in-handle, point), `Q` quadratic, `Z` close.
- Or `points:[{x, y, in:[x,y], out:[x,y], smooth:true}, …]` with `closed:true`.
- Verified: `M 40 520 C 120 440 220 600 300 520` → smooth S-wave.
- Interactive tools exposed as commands: `path.create`, `path.curvature` (Curvature: curves from points only, good for organic shapes), `path.freehand` (Pencil), `addon.pen.*` (Smart Pen: append, close, segment, togglePoint).

## Editing anchors and segments
| Action | VectorCraft |
|---|---|
| Move anchors | `path.moveAnchor`, `path.moveAnchors` |
| Handles | `path.setHandle`; rewrite all anchors `path.setAnchors` |
| Add / remove anchors | `path.insertAnchor`, `path.appendAnchor`, `path.removeAnchor(s)`, `path.deleteAnchors`, `object.path.addAnchorPoints` |
| Corner ↔ smooth | `path.convertAnchor`, `path.convertAnchors` (Anchor Point tool) |
| Reshape a segment | `path.reshapeSegment`, `path.reshape` |
| Reverse direction | `path.reverse` (matters for arrows, brushes, type on a path) |
| Close | `path.close` |
| Inspect | `addon.pathtools.inspect`; stray points `select.object.strayPoints` |

## Dashed lines and arrowheads
- `draw_path`/`draw_shape` take `dash:[d, g]`, `cap:"round"`, `join:"round"`. Round dots: `dash:[0, 8]` with `cap:"round"`.
- Advanced (align dashes to corners, arrowheads, arrow scale): `stroke.set {dash, alignDashes, startArrow, endArrow, arrowAlign}` — read allowed values with `command_list {filter:"stroke.set"}`.
- Dashes into separate objects: `addon.pathtools.divideDashes` / `expandDashes`.

## Pencil and smoothing
- The book's Pencil has a fidelity setting (accuracy vs smoothness). Agent equivalent: dense points, then `object.path.simplify` or `path.smoothRegion`.

## Picking the tool (book summary)
- Geometric forms → live shapes and Shape Builder.
- Organic curves → Curvature (or `d` with few `C` segments).
- Absolute precision, logos, lettering → Pen (`d` or points with handles).
- Sketchy expressive line → Pencil or Paintbrush, then simplify.

## Common mistakes
- Too many points: lumpy curves, heavy files. Simplify after tracing.
- Non-collinear handles on a point meant to be smooth → a kink.
- Open paths that should be closed: fills misbehave and Pathfinder fails. Check `closed` in `doc_inspect`.
