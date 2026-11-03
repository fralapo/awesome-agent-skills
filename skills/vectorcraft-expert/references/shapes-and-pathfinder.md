# Shapes, path editing and combining (Lessons 3 and 4)

Own-words summary of Classroom in a Book 2026, "Making Artwork with Shapes" and "Editing and Combining Shapes and Paths".

## Live shapes
- `draw_shape {shape: rectangle|ellipse|polygon|star|line, …, fill, stroke, strokeWidth, name}` → id. For a fill with no outline **always** pass `stroke:"none"` (default new art = white fill, 1 pt black stroke).
  - rectangle `x, y, width, height, radius`; ellipse `x, y, width, height`; polygon `cx, cy, radius, sides`; star `cx, cy, radius1, radius2, points`; line `x1..y2`.
- Other shapes via `command_run`: `shape.arc`, `shape.spiral`, `shape.flare`, `shape.rectangularGrid`, `shape.polarGrid`.
- Shapes stay parametric: `object.setLiveShape` changes radius, sides, corners (individual corners and corner type: round, inverted, chamfer), pie angles of an ellipse. `object.expandShape` turns them into plain paths; `object.shape.convertToShape` goes the other way.
- Stroke alignment (inside/centre/outside): `stroke.set {align}`. The book uses it so badges do not grow when the stroke gets heavier; for logos prefer **inside**.

## Drawing modes
- Draw Behind / Draw Inside: `view.drawMode` (Shift+D). Draw Inside makes a clipping mask automatically; headless it is clearer to be explicit with `object.clippingMask.make` (top object = mask).

## Cutting and joining
| Illustrator | VectorCraft | Note |
|---|---|---|
| Scissors | `path.split` (at a point) / `path.cutAtAnchors` | result is an open path |
| Knife | `path.knife` | pieces stay closed |
| Eraser | `path.eraseRegion`; Path Eraser `path.eraseSegments` | |
| Join (Cmd+J) | `path.join`; `path.average`, `path.averageJoin` | |
| Join tool | `path.joinScrub` | trims/extends ends, respects the angle |
| Compound path (Cmd+8) | `object.compoundPath.make` / `.release` | holes stay holes |
| Outline Stroke | `object.path.outlineStroke` | gives a line a fill; do it before delivering logos with strokes |
| Offset Path | `object.path.offsetPath` | outlines, sticker borders |
| Simplify / smooth / clean up | `object.path.simplify`, `object.path.smooth`, `object.path.cleanUp` | |
| Divide Objects Below / Split into Grid | `object.path.divideObjectsBelow`, `object.path.splitIntoGrid` | |

## Shape Builder
- `shapeBuilder.merge {ids, points:[[x,y]…]}` merges the regions the drag crosses; `erase:true` deletes them (Alt-drag in Illustrator). `shapeBuilder.regions` lists regions with bounds and area: query first, then pass one point inside each region to merge or delete.
- The most intuitive way to build icons from overlapping circles and rectangles.

## Pathfinder
- Destructive: tool `pathfinder {operation, ids}` — unite, minusFront, intersect, exclude, divide, trim, merge, crop, outline, minusBack. Verified: minusFront on an ellipse and a rounded rectangle → one path that keeps the back object's name and colour.
- Non-destructive (compound shape, Alt-click on shape modes in the book): `object.compoundShape.make` / `.setMode` / `.expand`, or a `pathfinder.*` effect on a group.
- Key difference: **shape modes** (unite, minus front, intersect, exclude) can stay live; **Pathfinder effects** (divide, trim, merge, crop, outline) transform immediately.

## Width tool and Intertwine
- Variable width: `stroke.widthPoint.set` / `.remove` / `.copy`, profiles `stroke.widthProfile.set`, save with `stroke.widthProfile.add`.
- Intertwine (rings, chains, crossing letters): `object.intertwine.make`, `.edit`, `.arrange`, `.release`.

## Image Trace
See images-and-image-trace.md (`imageTrace.make` / `makeAndExpand`; after expanding, the paths are grouped: clean with `object.path.simplify` and `addon.cleanup.*`).

## Common mistakes
- Forgetting `stroke:"none"` → unwanted black outline.
- Pathfinder on objects with thick strokes: outline the strokes first or they are ignored.
- Expanding too early: you lose editability.
