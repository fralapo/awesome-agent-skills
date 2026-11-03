# 12 — Adding video effects (Lesson 12)

Summary in my own words; effects, masks and presets verified.

## Concepts
- **Fixed effects** (Motion, Opacity, Time Remapping) are always on a clip; **standard effects** are added from the effects library, stack top-to-bottom, can be toggled, reset, reordered, copied and pasted.
- Effects can be applied to the **source clip** (every use of it inherits them) or to the timeline instance.
- **Adjustment layers** sit on a track above and apply their effects to everything below; ideal for a look over a whole scene.
- **Masks** limit an effect to a shape (ellipse, rectangle, polygon, bezier) with feather, expansion, opacity, invert; masks can be **tracked** to follow movement (blurring a face or a logo).
- **Keyframing effects** works like Motion: stopwatch on, values at different times, interpolation/velocity for smoothness.
- **Effect presets** save one or more effects (with keyframes) to reuse.
- Useful classics: Warp Stabilizer (also reduces rolling shutter), Lens Distortion, Transform, Timecode/clip-name burn-ins on an adjustment layer for review copies, Gaussian Blur, Sharpen, Noise for film grain.
- Premiere's Object Mask (AI) and Render and Replace are not in FilmCraft.

## FilmCraft
| Task | Command |
|---|---|
| List effects | `effects.list {kind:"Video", folder:"Video Effects/Blur & Sharpen"}` |
| Apply / remove | `effects.apply {clips, effect}`, `effects.remove {clip, index}` |
| Params | `effects.setParam {clip, effect:<index|id>, param, value}` (id works, e.g. `"lumetri"`) |
| Toggle / reset | `effects.toggleEnabled`, `effects.reset`, `effects.resetParam` |
| Adjustment layer | `file.newAdjustmentLayer {seconds}` then `timeline.place` on a top track |
| Masks | `masks.add {clip, effect, shape:"ellipse", center, size}` → `masks.set {mask, feather, inverted, expansion, mode}` → `masks.track {direction:"forward", method:"position"}` |
| Presets | `presets.save {clip, effects:[idx], name, keyframes}`, `presets.apply`, `presets.export/import` |
| Copy effects | `edit.pasteAttributes {clips, effects:true}` |
| Stabilize | `warp_stabilizer` (`smoothness`, `method`, `framing`, `crop_less`) |
| Burn-in for review | `metadata_burnin`, `timecode`, `clip_name`, or export `timecode_overlay` |
| Render | `sequence.renderEffectsInToOut {wait}`, `sequence.renderInToOut` |

## Recipes
- **Blur a face/plate**: `effects.apply gaussian_blur` → `masks.add` ellipse on that effect → `masks.set feather 20–40` → `masks.track`; spot-check with `render_frame` every second.
- **Film look**: adjustment layer with `lumetri` look + `noise` (small amount) + `vignette`.
- **Shaky phone clip**: `warp_stabilizer` first, then reframe/scale; if it warps, lower smoothness or switch method to position only.
