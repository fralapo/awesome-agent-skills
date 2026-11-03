# Layers and clipping masks (Lesson 10)

Own-words summary of Classroom in a Book 2026, "Organizing Your Project with Layers".

## Why layers
Organise content, select complex art easily, protect finished parts (lock), hide what distracts, control what prints, and apply effects or graphic styles to everything on a layer. Panel order = stacking order: the top layer is frontmost.

## Commands
| Need | VectorCraft |
|---|---|
| New layer / sublayer | `layer.new {name, top, below}` (verified with `below:true`), `layer.newSublayer {parent}` |
| Current layer (where new art goes) | `layer.setCurrent` — new art lands on the current layer, so set it before drawing |
| Rename, colour, lock, hide, print, template | `layer.setProps`, `layer.template` |
| Move objects / layers | `node.move`, `layer.move`, `object.arrange.sendToCurrentLayer` |
| Collect selection in a new layer | `layer.collectInNew` |
| Merge / flatten | `layer.merge`, `layer.flatten` |
| Release to layers (for animation/export) | `layer.releaseToLayers`, `layer.releaseToLayersBuild` |
| Isolate views | `layer.hideOthers`, `layer.lockOthers`, `layer.outlineOthers`, `layer.showAll`, `layer.unlockAll` |
| Locate an object | `layer.locate`, or `doc_inspect {ids}` (gives the ancestor path) |
| Select everything on a layer | `layer.selectAll` |
| Paste keeping layers | `layer.pasteRemembersLayers` |
| Target a layer for appearance | `layer.target` |

Read the tree with `doc_inspect {depth:0}` for the skeleton, `{kind:"Type"}` to list all text, `{ids:[…]}` for specific nodes.

## Suggested layer structure
- `Background` (locked when done) → `Artwork` (sublayers per element) → `Text` → `Logo` → `Guides/Notes` (non-printing: `layer.setProps {printable:false}`).
- Name objects at creation (`name` parameter of `draw_shape`/`draw_path`): exports, Asset Export and later edits rely on names.

## Clipping masks
- Object level: `object.clippingMask.make {ids}` — the **topmost** object becomes the mask and loses its paint (colour it later if you want a fill behind / stroke over). Edit: `object.clippingMask.editContents` / `editMask`, release `.release`.
- Layer level: `layer.clippingMask.toggle` — the top object of the layer clips the whole layer.
- Text can be a mask (photo inside letters).
- Images: crop directly with `object.cropImage`, or quick mask `object.maskImage`.

## Common mistakes
- Drawing on a locked or hidden current layer → command refused or invisible art.
- Masks that are not on top of the masked objects.
- Leaving everything on "Layer 1": impossible to hand over or edit later.
