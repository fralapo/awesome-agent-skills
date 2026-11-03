# Selections (Lesson 3)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 3, mapped to PhotoCraft.

## Concepts
- Editing pixels is two-step: define the area, then edit; the edit stays inside the selection.
- Selection modes on every tool: replace / add / subtract / intersect (`mode` param). Start with one tool,
  refine with another.
- Automatic tools: Select Subject (dominant subject), Object Selection (one object among many), Sky,
  Remove Background (= subject + layer mask).
- Manual tools: Quick Selection (content-based brush), Magic Wand (colour, `tolerance`), marquees
  (rect/ellipse/single row/column), lasso / polygonal / magnetic lasso.
- Other ways: Color Range (sampled colours, preset ranges such as skin tones, shadows/highlights),
  loading transparency or a channel as a selection, Quick Mask, Focus Area, Select and Mask.
- Soft edges: anti-aliasing (must be set before selecting) and feather (blurs the edge, also kills detail).
- Masks: white shows, black hides, grey is partial.
- Transform Selection moves/scales the outline only; Free Transform moves pixels.

## PhotoCraft calls
| Need | Call |
|---|---|
| Main subject | `select.subject {sampleAllLayers, mode}` ✔ |
| One object in a crowd | `select.object {rect:[x,y,w,h]}` or `{point:[x,y]}`, `mode:"add"` for its shadow |
| Sky | `select.sky {threshold, softness}` ✔ → returns coverage and bounds |
| Remove background | `layer.removeBackground {layer}` (pixel layer only ✔; rasterize or use on a copy) |
| Colour / tones | `select.colorRange {select:"sampledColors", points:[[x,y]], fuzziness}` or `select:"skinTones"|"shadows"…` |
| Wand | `select.magicWand {x,y,tolerance,contiguous}` |
| Brush-like | `select.quick {points, size, mode}` |
| Marquee / lasso | `select.rect {…, ellipse, feather}`, `select.lasso {points}`, `select.magneticLasso` |
| Refine | `select.modify.expand|contract|feather|smooth|border`, `select.grow`, `select.similar`, `select.inverse` |
| Edge refinement | `select.refineEdge {…}` (see masks-and-patterns.md) |
| Outline only | `select.transformSelection` |
| Store / recall | `select.saveSelection {name}`, `select.loadSelection {channel}`, `select.reselect` |
| Layer transparency as selection | `select.loadSelection {channel:"transparency", layer}` |
| Selection → path | `select.toWorkPath {tolerance}` |

## Procedures
**Enlarge the subject without losing the original**: `select.subject` → `layer.new.layerViaCopy` (rename) →
`edit.transform {scaleX:110, scaleY:110}` → on Background, `select.subject` again → fill the old figure with
`paint.remove` over it or `edit.contentAwareFill {output:"new"}` → show the copy. Three layers, Background
intact.

**Remove one object of many**: `select.object {point}` → add its shadow (`mode:"add"`, rect around it) →
`edit.contentAwareFill {output:"new"}` → clean leftovers with `paint.remove`.

**Cut out with a mask**: `layer.removeBackground` (or `select.subject` + `layer.layerMask.revealSelection`) →
inspect the mask (`view.layerMask`, `render_preview`) → rotate/transform the layer to sit on the new ground →
add a contact shadow.

**Sky only**: `select.sky` → `layer.new.layerViaCopy` "Sky" → `image.adjustments.shadowsHighlights` on that
copy (destructive, it is a copy) or an adjustment layer created while the selection is active.

## Pitfalls
- Moving or deleting a subject: handle its shadow and the light/colour match.
- Deselect pixels (`select.deselect`) is not deselect layers (`select.deselectLayers`).
- If Object Selection misses, enlarge the box or zoom (give a tighter `rect`).
- Feather blurs edge detail; anti-alias cannot be added afterwards.
- A live selection becomes the mask of the next adjustment layer: deselect when not wanted.
- `select.deselect` errors when nothing is selected ✔ (harmless in a batch with `stop_on_error:false`).
