# Masks (lesson 7)

## Concepts
- A mask is a path made of vertices and segments that belongs to a layer. A **closed** mask changes the layer's alpha. An **open** mask defines no transparency, but effects (Stroke, Write-on) and text on a path can use it.
- Bezier direction handles control the angle and length of each curve.
- **Mask modes** combine masks on the same layer: Add (the default), Subtract, Intersect, Lighten, Darken, Difference and None.
  - The first mask works against the layer's alpha. Each later mask works against the masks above it.
  - The mode cannot be animated.
- **Feather** softens the edge. **Variable feather** (feather points) changes the softness along the path. **Expansion** grows or shrinks the mask.

## EffectCraft commands
| Task | Command |
|---|---|
| Geometric mask | `layer.addMask {layer, shape: rect|ellipse|rounded|polygon|star, rect:[x,y,w,h] (layer space), mode?}` (verified) |
| Pen mask | `mask.new {layer, vertices:[[x,y]…], inTangents?, outTangents?, closed:true, mode?}` |
| Edit vertices | `mask.addVertex`, `mask.insertVertex`, `mask.setVertex`, `mask.moveVertices`, `mask.deleteVertices`, `mask.convertVertex` (corner or smooth) |
| Open or close a path | `mask.setClosed` |
| Feather, opacity, expansion | `layer.mask.set {layer, field:"feather", value}` (verified). Animated path: `masks/<name>/feather` (a vec2). |
| Variable feather | `mask.featherPoint.add/set/remove/list` |
| Mode, invert, lock | `layer.mask.mode`, `layer.mask.invert`, `layer.mask.lock` |
| Animate the shape | keys on `masks/<name>/path`. Morph options: `mask.interpolate`. Smoother paths: `path.rotoBezier`. |
| Track a mask | `track.mask {layer, mask, method:"positionScaleRotation"…, wait:true}` |
| Masks from text or alpha | `layer.create {op:"masksFromText"}`, `layer.autoTrace` |

## Recipes
- **Content inside a shape** (the book's "replace the screen content"): put the new footage under the masked layer. Or put the mask on the new footage itself, or use a track matte with the shape layer.
- **Vignette:** solid or adjustment layer → large ellipse mask, inverted → feather 200–400 px → opacity 30–60%. Verified: an ellipse mask with feather 200 on a full-frame solid. Alternative: Lumetri `vignette/vignetteAmount`.
- **Mask shadow:** duplicate the masked layer, fill it black (`Fill` effect), offset it, blur it, and lower its opacity. Or apply `Drop Shadow` to the masked layer.

## Tips
- Use as few vertices as you can.
- Animating a mask path with many vertices gives jitter. Prefer RotoBezier or the Roto Brush (see `07-roto-brush.md`).
- Coordinates for `layer.addMask`/`mask.new` are in **layer space**. On a full-frame solid that equals comp space.
- Check the edge with `render_frame {transparent:true}`.
