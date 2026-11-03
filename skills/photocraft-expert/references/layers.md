# Layers (Lesson 4)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 4, mapped to PhotoCraft.

## Concepts
- A layer is a transparent sheet: edit, move or delete it without affecting others. New layers are empty.
- JPEG/GIF and Bitmap/Indexed modes cannot hold layers: keep masters in `.pcraft`, PSD or layered TIFF.
- Background is opaque, locked and at the bottom; convert with `layer.new.layerFromBackground`, reverse with
  `layer.new.backgroundFromLayer`.
- Stacking order decides what is in front. A new layer goes above the active one.
- Layer styles are non-destructive, follow the opaque pixels and update with the content.
- Blend-mode families: darken (Multiply, Darken, Color Burn), lighten (Screen, Lighten, Color Dodge),
  contrast (Overlay, Soft/Hard Light; 50 % grey is neutral), colour (Hue, Saturation, Color, Luminosity),
  inversion (Difference, Exclusion – Difference reveals misalignment).
- An adjustment layer affects everything below unless clipped or masked.
- Layer Comps store visibility/position/appearance states for variants (e.g. languages).
- Flatten is irreversible; flatten only copies.

## PhotoCraft calls
| Task | Call |
|---|---|
| Inspect tree, ids | `doc_inspect` (layers top → bottom, `id`, `kind`, `bounds`, effects, adjustments) |
| Select / multi-select | `layer.select {layer, mode:"add"|"range"}`, `select.allLayers` |
| Reorder | `layer.moveTo`, `layer.arrange.bringForward|sendBackward|bringToFront|sendToBack` |
| Visibility / solo | `layer.setProps {visible}`, `layer.showOnly` |
| Opacity, fill, blend | `layer.setProps {opacity:0.25, blend:"Multiply"}` |
| Duplicate | `layer.duplicate`, `layer.new.layerViaCopy` |
| Transform | `edit.transform {layer, scaleX:50, scaleY:50, rotate:15}` |
| Copy layers to another document | `layer.copyToDocument` |
| Render clouds | `tools.setColors` then `filter.render.clouds` on a new layer |
| Styles | `layer.layerStyle.stroke {size:5, position:"inside", color}`, `.dropShadow {angle, distance, spread, size, opacity}`, `.satin`; copy with `layer.layerStyle.copyLayerStyle`/`pasteLayerStyle` |
| Gradient | `gradient.fill.create` / `layer.newFillLayer.gradient` clipped to the layer |
| Clip an adjustment | `layer.newAdjustmentLayer.hueSaturation {…}` then `layer.createClippingMask` |
| Border from selection | `select.all` → `select.modify.border {radius:10}` → `edit.fill` white |
| Group / merge | `layer.groupLayers`, `layer.new.groupFromLayers`, `layer.mergeLayers`, `layer.stampVisible` |
| Flattened copy | `image.duplicate {mergedOnly}` or just `doc_export` (always flattens) |
| Layer Comps | `layerComp.new {name}` ✔, `layerComp.apply`, `file.export.layerCompsToFiles` |
| Align / distribute | `layer.align.*`, `layer.distribute.*` (need ≥2 selected layers; one layer moves 0 ✔) |

## Postcard procedure (condensed)
1. Bring each element in as a layer or SO (`doc_place`), name them.
2. White inside stroke on the photo layer; rotate it ~15° and scale ~50 %.
3. Stamp layer at 25 % opacity, Multiply; duplicate an element with Overlay for punch.
4. Clouds on a new layer just above Background.
5. Headline type with tracking and caps; drop shadow with global light; copy the style to other type.
6. Gradient clipped to rasterised lettering.
7. Recolour one element with a clipped Hue/Saturation layer.
8. Border via border selection + fill on a top layer.
9. Export a flattened copy; keep the layered master.

## Pitfalls
- Adjustment layer without clipping recolours everything below.
- Faux bold is worse than a real bold weight.
- In crowded files always pass explicit layer ids (Auto-Select picks the wrong layer).
- Merging is irreversible; to stay editable group instead.
- Use global light so all shadows share one angle.
