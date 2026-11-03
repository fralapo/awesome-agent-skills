# Stabilizing, point tracking, cleanup, particles, Timewarp (lesson 14)

## Stabilizing
- Handheld shake can be removed by analysing the motion and counter-moving the layer.
- `track.warpStabilizer {layer, wait:true}` applies and analyses Warp Stabilizer (check `warp.status`). Settings (smoothness, method, framing/crop) are on the `Warp Stabilizer` effect (paths via `get_layer`).
- Classic tracker stabilisation: `track.stabilize {layer}` → set the points → `track.analyze` → `track.apply`.
- Too much smoothing crops or warps the image, so use the lowest smoothness that works.

## Single-point motion tracking (verified)
The book's "glue an element to a moving object" workflow:
1. `track.motion {layer}`. It creates "Tracker 1" with a single point.
2. `track.setPoint {layer, point:1, center:[x,y], featureSize:[w,h], searchSize:[w,h], time:0}`. Pick a high-contrast feature. Make the search box larger than the motion per frame.
3. `track.analyze {layer, direction:"forward", start:0, wait:true}`.
4. `track.setTarget {layer, target:"NullName"}` → `track.apply {layer}`. The null gets one position key per frame. Parent the overlay to the null.
   - Verified: the expected x at 1.5 s was 310, the tracked value 309.
- Track types: `track.new {kind: transform|stabilize|affine|perspective|raw, position, rotation, scale}`. Use two points for rotation/scale and four for perspective (a screen).
- **Drift** happens when the feature changes (lighting, angle, occlusion).
  - Reposition the point on the bad frame and re-analyse from there.
  - Enlarge the feature or search areas.
  - Change `track.options` (channel: luminance/rgb/saturation, `adaptEveryFrame`, `threshold`, `action: adapt|extrapolate|stop`).
- Read the result with `get_layer {layer:null, flat:true, time}`, **not** `prop.get`, which dumps every key.
- Face tracking: `track.mask {method:"faceOutline"|"faceDetailed"}`, then the `Face Track Points` effect.

## Removing unwanted objects
- **Content-Aware Fill:** draw a mask around the object (Subtract or None mode, tracked with `track.mask`), then run `layer.newContentAwareFill {layer, method: object|surface|edgeBlend, range, lightingCorrection, wait:true}` or `contentFill.generate`.
  - `object` is for moving objects.
  - `surface` is for flat textures.
  - `edgeBlend` is for simple backgrounds.
  - A clean **reference frame** (painted in an image editor and imported) improves the result: `referenceLayer`, `referenceTime`.
- Small items: clone with `paint.stroke {kind:"clone"}` after `paint.setCloneSource`.

## Particle simulation
- Effects:
  - `CC Particle World` and `CC Particle Systems II` for general particles;
  - `Particle Playground`;
  - `CC Rainfall`, `CC Snowfall`, `CC Bubbles` and `CC Star Burst` for specific looks.
- **Birth rate** sets how many new particles appear per second. Other controls are longevity, producer position and radius, physics (velocity, gravity), and particle type, size and colour over life.
- Put particles on their own black solid in `Screen`/`Add` mode, add `Glow` and motion blur, and precompose for reuse.

## Timewarp
- `Timewarp` changes speed with frame interpolation (Pixel Motion / Frame Mix / Whole Frames), plus motion blur and source cropping to hide edge artifacts. Key its `speed` for speed ramps.
- Lighter alternatives: time remapping (`04-layers-mattes-time.md`) with `layer.frameBlending {mode:"pixelMotion"}`. For a stepped look: `Posterize Time`.
