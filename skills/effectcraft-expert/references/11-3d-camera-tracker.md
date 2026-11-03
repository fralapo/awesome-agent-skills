# 3D Camera Tracker (lesson 13)

## Concepts
- The 3D Camera Tracker analyses the motion in 2D footage and solves the real camera's movement and lens. It creates a matching 3D camera and leaves 3D track points on the footage, so new 3D layers (text, solids, images, models) stick to the scene.
- You choose a group of track points to define a plane (the ground, a wall). From it you create a layer, a camera or a ground plane, and new elements inherit that plane's orientation.
- **Rolling shutter** (CMOS sensors scan line by line) skews fast motion. Fix it before tracking with the `Rolling Shutter Repair` effect.

## EffectCraft commands (commands exist, not tested)
- Analyse: `track.camera {layer, shotType?: fixed|variable|specify, aov?, solveMethod?: auto|typical|flat|tripod, detailed?, lensDistortion?, wait:true}`. Check `camera.solveStatus`. Cancel with `camera.cancel`.
- Points: `camera.points`, `camera.selectPoints`, `camera.deletePoints` (remove bad ones on moving objects).
- Create:
  - `camera.createFromSolve` / `camera.create`;
  - `camera.setGroundPlane` (sets the plane and origin from the selected points).
- Export the scene to Blender: `camera.exportBlender`.
- Alternative for flat surfaces: a perspective point tracker (`track.new {kind:"perspective"}`) or `CC Power Pin` / `Corner Pin`.

## Workflow
1. If the footage has wobble or skew, apply `Rolling Shutter Repair` first.
2. Run `track.camera` and wait for the solve. Check the solve error in `camera.solveStatus`.
3. Select 3+ points on the surface where the text must sit, and create the text plus camera from them.
4. Add more elements (solids for images, 3D text). Parent them to nulls created on track points.
5. Shadows that feel real need:
   - a shadow-catcher plane that accepts shadows only (`materialOptions/acceptsShadows:"Only"`);
   - a light that casts them;
   - elements that cast them.
6. Add an Ambient light so the inserted elements match the scene exposure.
7. Grade the inserted elements to match the footage (`08-color-and-mood.md`), add `Add Grain`/`Match Grain`, and preview through the moving section.

## Tidying
Put tracker-created nulls, cameras and lights in a clear order, rename them (`layer.rename`) and mark them shy (`layer.setSwitch {switch:"shy"}`).
