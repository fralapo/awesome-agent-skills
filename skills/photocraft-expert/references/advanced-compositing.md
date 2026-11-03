# Advanced compositing and mockups (Lesson 9)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 9, mapped to PhotoCraft.

## Concepts
- Regular filters change pixels permanently; on a Smart Object they become Smart Filters you can edit,
  hide, reorder or delete (`smartFilters` list in `doc_inspect` ✔).
- Liquify tools: Forward Warp pushes, Pucker pulls toward the brush centre, Bloat pushes away.
- **Color blend mode** keeps the luminance of what is below and applies hue+saturation of the paint: the way
  to colourise monochrome areas. Layer blend mode ≠ tool blend mode (`paint.stroke {mode}`).
- Adjustment Brush (Photoshop) = an adjustment layer with a painted mask, created automatically.
- History keeps the session's states (default 50); selecting an older state and acting deletes the newer
  ones. Snapshots protect a state.
- Merge Visible keeps transparency; Flatten does not.
- Upsampling adds pixels: for very small images Photoshop uses Generative Upscale (not available in PhotoCraft as of 2026-11-03 — re-check).

## PhotoCraft composite workflow
1. Load each piece as its own layer/SO: `doc_place` (files inside the allowed read/write root) or open documents and
   `layer.copyToDocument`.
2. Arrange: `layer.moveTo`; select several and `edit.transform {layers:[…], scaleX:50, scaleY:50}` (one box).
3. Fit a texture to a face: `edit.transform {quad}` or `edit.transform.warp {mesh|style}`.
4. Deform as a Smart Filter: convert to SO → `filter.liquify {strokes:[{tool:"forwardWarp", size:150,
   pressure:75, points:[…]}]}` ✔; later `layer.smartFilter.setParams` to tweak.
5. Colourise: new layer, `blend:"Color"`; load the base layer's transparency
   (`select.loadSelection {channel:"transparency", layer}`) and `paint.stroke` with a sampled colour
   (`document.sampleColor`), size 60 px, hardness 0. Skin only: `select.colorRange {select:"skinTones"}`.
6. Local adjustments ("Adjustment Brush"): make a selection or paint a mask, then
   `layer.newAdjustmentLayer.levels {gamma:1.3, blue:{gamma:…}}` – or create it and `paint.stroke
   {target:"mask"}` on its white/black mask.
7. Undo branches: `history.newSnapshot` before experiments; `history.selectState {…}` to go back;
   `paint.historyBrush {state|snapshot}` to paint back a past state.
8. Texture/grain: `filter.noise.addNoise {amount:3, distribution:"gaussian", monochromatic:true}` on the merged
   piece (or on a 50 % grey Overlay layer to stay non-destructive).
9. Paste into a feathered oval: `select.rect {ellipse:true, feather:50}` → `edit.pasteSpecial.pasteInto`
   (layer with mask) → blend Luminosity 50 %.

## Mockups (smart-object replacement)
1. Mockup base photo; `doc_place` a placeholder design (becomes an SO ✔).
2. Corner-pin it onto the surface: `edit.transform {layer, quad:[[tl],[tr],[br],[bl]]}` ✔.
3. Realism: blend Multiply (prints on paper/fabric) ✔, a slight `filter.blur.gaussianBlur {radius:0.5–1}` as
   smart filter ✔, a clipped Curves for shading, or the surface texture above it in Multiply/Overlay.
4. For each client design: `doc_replace_smart_object {layer, path}` ✔ (keeps transform and smart filters)
   → `doc_export`.
5. Many variants: define variables (`image.variables.define`, pixel replacement) + `doc_import_data_sets` +
   `image.applyDataSet`, or loop replace + export.
6. Warp for curved surfaces: `edit.transform.warp {style:"cylinder", values:[…]}` or `edit.perspectiveWarp`.

## Low-resolution images
Until a generative upscale appears (re-check `command_list {filter:"upscale"}`): `image.imageSize {percent:200, resample:"preserveDetails"}` (or bicubicSmoother), then
`filter.sharpen.smartSharpen` lightly; LightCraft `enhance.denoise` / Denoise models before enlarging noisy
raws. Never enlarge more than needed; declare the limit to the client.

## Pitfalls
- Merging is irreversible – group (`layer.new.groupFromLayers`) to stay editable.
- Pasted-into layers have an unlinked mask: moving the content reframes it inside the mask.
- PSD export drops PhotoCraft-only smart filters (Liquify ✔ warning): keep `.pcraft` as master.
- Light direction, colour temperature, black levels and grain must match across all pieces; add contact
  shadows.
