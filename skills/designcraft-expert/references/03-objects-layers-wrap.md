# 03 - Objects, layers, frames, wrap, alignment, paths, flex (lesson 4)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 4. ✔ = verified 2026-11-03.

## Concepts
- **Layers** separate kinds of content (background, images, text, interactive items). Arrange commands
  (front/back) work *inside* a layer, not across layers. Use distinct layer colours to see what is where.
- **Frames**: reshape, convert shapes, rounded/fancy corners, frames with graphics cropped by the frame;
  paste-into to mask a group.
- **Captions from metadata** (file name, dimensions, alt text…) can be static or live.
- **Text wrap**: around bounding box, around the object shape/clipping path, jump object, jump to next
  column; offsets per side; wrap applies to text in *other* frames below or above.
- **Transform and align**: rotate, scale, flip, align to selection / key object / margins / page;
  distribute spacing; Alt-drag duplicates; step and repeat for grids.
- **Groups**: select inside a group without ungrouping.
- **Type on a path**, lines with arrowheads.
- **Flex containers** (2026): auto-arranging rows/columns of objects with gaps and padding, like CSS flexbox.

## DesignCraft
| Task | Command |
|---|---|
| Layers | `layer.new {name}`, `layer.set {id, color, locked, visible, printable}`, `layer.activate`, `object.setLayer {layer, ids}`, `layer.selectItems` |
| Stacking | `object.bringToFront|bringForward|sendBackward|sendToBack`, `object.reorder` |
| Lock/hide | `object.lock`, `object.hide`, `object.setFlags` |
| Frames | `frame.create {rect, shape:"rectangle"|"ellipse"|"polygon", content}`, `frame.grid {rect, cols, rows, gutter}` |
| Corners | `object.cornerOptions {shape:"rounded", size:12}` ✔ (per-corner array possible) |
| Shapes / pathfinder | `object.convertShape {to}`, `object.pathfinder {op}`, `path.*` for anchors |
| Caption | `object.caption {text:"{name} - {dimensions}", position:"below", style, live:true}` |
| Wrap | `object.textWrap {mode:"boundingBox", offset:8}` ✔, `{mode:"contour", contour:"graphicFrame", offset:6}` ✔, `jumpObject`, `jumpToNextColumn`, `side`, `invert` |
| Ignore wrap in a frame | `object.textFrameOptions {ignoreWrap:true}` |
| Transform | `transform.move|resize|rotate|scale|shear|flip`, `transform.set`, `transform.again` |
| Align / distribute | `object.align {edge, to:"margins"|"page"|"keyObject"}`, `selection.key`, `object.distribute` |
| Duplicate grid | `edit.stepAndRepeat {rows, columns, dx, dy}` |
| Groups | `object.group|ungroup`, `select.content`, `select.nextInGroup` |
| Paste into | `edit.pasteInto` (after `edit.copy`) |
| Type on path | `type.onPath {id, text, align}` |
| Lines | `line.create`, `object.stroke {weight, start, end:"triangle"}` |
| Flex | `flex.convert {ids}`, `flex.set {direction, gapH, padding, justify, align}` |

## Practical notes
- A wrap on an image sitting *inside* the body frame's area pushes the body text away ✔; the headline
  frame on top must not have the same wrap or it will push itself.
- Cut-out images: `object.clippingPath {type:"alpha"}` turns transparency into the frame outline ✔, then
  `textWrap {contour:"graphicFrame"}` follows the shape ✔.
- Keep background art on a locked bottom layer so later placements don't land inside it.
