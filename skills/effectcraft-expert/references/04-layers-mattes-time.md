# Layer animation, track mattes, Corner Pin, time remapping (lesson 6)

## Layered Photoshop files
Importing as a composition keeps layer order, transparency and layer styles. In EffectCraft: `file.import {paths, importAs:"composition"}` (not tested). Turn layer styles into editable ones with `layer.style.convertToEditable`. Add styles with `layer.style.add {style: dropShadow|outerGlow|stroke|…}`.

## Simulated lighting
- Duplicate the layer to get a "lit" and an "unlit" copy, then key the lit copy's opacity (hold keys for a flicker).
- Darkening sky: put a dark solid on top with an inverted mask in **Darken** mode (`layer.mask.mode`, `layer.mask.invert`) and fade its opacity.

## Linking properties (pick whip)
- `prop.pickWhip {layer, path, target:{layer, path, dimension?}}` writes an expression such as `thisComp.layer("X").transform.rotation`.
- You can also write the expression yourself: `set_property {expression:"…"}`.
- Use case from the book: a drop shadow whose direction follows the rotation of the object.

## Track matte
- One layer shows only through the shape or luminance of another layer.
- `layer.setTrackMatte {layer: fill, matte: matteLayer, kind: alpha|alphaInverted|luma|lumaInverted}` (verified). The matte layer's video is switched off automatically.
- Animate the matte to get a traveling matte, for example scrolling text revealed inside a frame shape.
- Keep the matte directly above the fill. Lottie and older players need that order.

## Corner Pin
- Fits a layer into a quadrilateral, such as a sign or a screen. Use `add_effect {layer, effect:"Corner Pin"}`, then key the four corner parameters (read their paths from the returned params).
- For moving footage, use a perspective tracker instead: `track.new {kind:"perspective"}`, then `track.apply` (see `12-stabilize-track-advanced.md`).

## Time remapping and timing
- `layer.enableTimeRemap {layers}` adds Time Remap keys at the in and out points (verified on a precomp). Key `timeRemap` (check the path with `get_layer`) to slow down, freeze or reverse.
- Simpler tools: `layer.timeStretch {percent|duration}`, `layer.timeReverse`, `layer.freezeFrame`, `layer.freezeOnLastFrame`.
- Trim and move: `layer.timing {op:"trimInToTime"…}`, `layer.moveInToStart`, `layer.slip`. In AE, Alt+[ and Alt+] trim the in and out points.
- Frame blending smooths slow motion: `layer.frameBlending {mode:"frameMix"|"pixelMotion"}`.

## Render cost
- AE shows render time per layer (the snail icon). **EffectCraft has no per-layer render-time column.**
- To find the expensive part, toggle effects (`effect.toggle`) or layers and compare `render_frame` speed.
- Lower `layer.quality` to draft or the preview resolution (`view.res.half`) while you work.
