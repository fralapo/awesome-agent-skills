# Shape layers, keyframes, parenting and nulls (lessons 4–5)

## Shape layers
- A shape layer holds vector contents: groups, paths, fills and strokes. **Path operators** change the shape over time.
- Primitive: `layer.newShape {kind: rect|rounded|ellipse|star|polygon|none, size:[w,h], fill, stroke, strokeWidth, position}`.
- Pen path: `shape.newPath {vertices:[[x,y]…], inTangents?, outTangents?, closed, fill, stroke, space:"comp"}`.
- Add an item with `layer.addShapeItem {layer, kind}`. It returns `{uid, path}` (verified). Useful kinds:
  - `wiggle` (Wiggle Paths): a shape that animates itself. Its paths are under `contents/wiggle/...`.
  - `offset` (Offset Paths) and `pucker` (Pucker & Bloat, which pushes vertices out or in).
  - `twist`, `zigzag`, `round` and `merge`.
  - `trim` (Trim Paths): key `contents/trim/end` from 0 to 100 for a write-on (verified).
  - `repeater` for radial or row copies, `gfill` and `gstroke` for gradients.
- Duplicate a layer with `edit.duplicate`. Keys and effects come with it.
- Snapping: `view.snapping` only matters in the UI. Over MCP, use exact coordinates, `layer.align {edge, to:"composition"}` and `layer.distribute`.
- Text or vector to shapes: `layer.create {op:"shapesFromText"|"shapesFromVector"}`. Paste SVG: `edit.pasteSvg`.

## Keyframes and easing
- Several keys at once: `add_keyframe {layer, path, keys:[{time,value}…], interpolation}`. The values for `interpolation` are linear, bezier, hold, easyEase, easyEaseIn and easyEaseOut.
- Fine easing:
  - `keys.setEase {layer, path, time, side:"in"|"out", speed?, influence?}`. Influence of 60–85% gives smooth arrivals.
  - `keys.velocity` sets key speed.
- Hold key (an instant jump): `interpolation:"hold"` or `keys.toggleHold`.
- Moving, copying and reversing keys: `keys.move`, `keys.copy`/`keys.paste`, `keys.timeReverse`, `edit.pasteReversedKeyframes`.
- Random motion, three options:
  - the expression `wiggle(freq, amp)` via `set_property {expression}`;
  - `keys.wiggle`, which needs selected keys;
  - the `wiggleSoft` preset.
- Continuous spin: the expression `time*45` (degrees per second, verified).
- **Motion path:** the trajectory of the position keys.
  - Edit its curves with `keys.setSpatialTangents`.
  - Orient the layer along it with `layer.autoOrient {mode:"alongPath"}`.
  - Draw it freehand with `motion.sketch`.

## Anchor point
- Rotation and scale happen around the anchor, so put it at the pivot (for example the shoulder of an arm).
- `set_property transform/anchor` moves the anchor. `layer.centerAnchor` centres it on the content. The UI tool is Pan Behind (Y).
- Moving the anchor without compensating the position shifts the layer.

## Parenting and nulls
- `layer.setParent {layers:[children], parent:p|null}`. A child inherits position, scale and rotation, **not opacity**. Verified: a child orbits with a spinning null.
- **Null:** `layer.newNull {name}`. It is an invisible controller and does not render. Use it as a rig pivot or a group mover.
- Puppet-style chains: torso → upper arm → forearm → hand, each with its anchor on the joint.
- Linking paths and nulls:
  - `paths.nullsFollowPoints`: nulls follow a path's vertices.
  - `paths.pointsFollowNulls`: the vertices follow the nulls. Use it to connect shapes.
- Pick whip: `prop.pickWhip {layer, path, target:{layer, path}}`. It writes a reference expression.

## Multimedia presentation (lesson 5)
- Import the layered artwork as a comp. Precompose logical groups (character, background) and animate each precomp along a motion path.
- For a pan wider than the frame, nest a wide comp (for example 5000 px) inside an HD comp and key the precomp's position.
- Audio:
  - Import AAC, M4A, AIF, MP3 or WAV, then `layer.addItem`.
  - Fades are keys on the audio level properties. Check the exact path with `get_layer`.
- Sequencing: `layer.sequence {layers, overlap, duration, transition:"crossDissolve"}`, or `layer.quickOffset` to stagger entrances.

## Common mistakes
- Parenting after you animate, without `compensate`. The child jumps, so parent first.
- Too much wiggle. Five to 30 px is enough for graphics.
- Off-centre shapes. Run `layer.centerAnchor` before scaling.
