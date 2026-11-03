# Masks and patterns (Lesson 6)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 6, mapped to PhotoCraft.
⧗ = not available in PhotoCraft/LightCraft as of 2026-11-03 (snapshot — re-check with `command_list {filter}`
on the live app; ArtCraft apps update daily). The Photoshop behaviour described stays the target.


## Concepts
- A mask hides reversibly; erasing is permanent. Selection = temporary, mask = stored with the layer.
- Black hides, white shows, grey is semi-transparent. Painting on a masked layer shows only where white.
- Mask/channel types: colour channels; alpha channels (stored selections, also PNG transparency); layer mask
  (pixel); vector mask (path, resolution-independent); clipping mask (lower layer's pixels mask the upper
  layer); channel mask (from a channel's tones); quick mask (temporary, painted).
- Select and Mask: a dedicated space to build and refine edges; view modes Overlay / Black & White /
  On Layers; global refinements Smooth, Feather, Contrast, Shift Edge; output with colour decontamination.
- Puppet Warp rotates parts of a layer around pins (something Liquify/Transform cannot do).
- Vector shapes (polygon/star with star ratio, rounded corners) make crisp, editable pattern tiles.

## PhotoCraft: hair-quality cut-out
```
select.subject {sampleAllLayers:false}
select.refineEdge {
  smartRadius:true, radius:10, smooth:1, contrast:20, shiftEdge:-15,
  decontaminate:true, amount:25, output:"newLayerWithMask",
  refineStrokes:[{points:[[x,y],…], size:20, mode:"add"}],     # along hair gaps
  edits:[{tool:"quick", points:[…], size:15, mode:"add"}]        # fill holes inside the figure
}
```
- Check the mask: in a good mask grey only appears along transition edges (black outside, white inside).
- Touch up: `paint.stroke {target:"mask", color:"#ffffff"|"#000000", size, hardness}` ✔;
  `layer.layerMask.edit {feather, density}` for global softening.
- Output `newLayerWithMask` creates a copy because decontamination writes new pixels; without it, output
  `layerMask` on the original.
- Too much Smooth rounds corners, too much Feather makes halos; reduce decontamination amount if artefacts.

## Puppet Warp
`edit.puppetWarp {pins:[{src:[x,y], dst:[x,y], rotate:deg}…], mode:"normal", density:"normal", expansion:2}`:
place 10–12 pins around the body and neck as anchors (src = dst), rotate the head pin. On an SO it becomes a
smart filter.

## Pattern from vector shapes
1. New document for the tile; `shape.create {kind:"star", rect, sides:8, starRatio:0.7, fill:null,
   stroke:{width:20, color:"#173199"}}` (`cornerRadius` rounds points).
2. Duplicate, `edit.transform {rotate:24, scaleX, scaleY}` (or `path.transform`), change sides/stroke.
3. Hide Background for a transparent tile, `edit.definePattern {name:"Podcast Pattern"}`.
4. In the target document: `layer.newFillLayer.pattern {pattern:"Podcast Pattern", angle:45, scale:35}`.
5. Pattern Preview mode ⧗ in PhotoCraft: check seamlessness with `filter.other.offset {horizontal:w/2,
   vertical:h/2, undefinedAreas:"wrap"}` on a flattened copy.

## Other mask tools
`layer.layerMask.revealAll|hideAll|revealSelection|hideSelection|fromTransparency|apply|delete`,
`layer.layerMask.enabled`, `layer.layerMask.linked`, `layer.vectorMask.add|fromPath`,
`channel.target.layerMask`, `select.editInQuickMaskMode`, `layer.maskAllObjects`.

## Pitfalls
- Dragging Quick Selection beyond the subject teaches it the background: keep strokes inside.
- Use the refine brush only on transitions (hair, fur), plain brush for hard edges.
- Compare Device/Cloud or Color-/Object-aware modes in Photoshop; in PhotoCraft compare `select.subject`
  vs `select.object` + `select.refineEdge` parameters.
