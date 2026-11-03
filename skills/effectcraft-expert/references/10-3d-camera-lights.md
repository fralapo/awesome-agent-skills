# 3D features, cameras and lights (lesson 12)

## Concepts
- Turning on a layer's 3D switch adds a Z axis. The layer gains `orientation`, `rotationX` and `rotationY` and **Material Options** (casts/accepts shadows, accepts lights, ambient, diffuse, specular…).
- A 3D scene can fool you in the active camera view. Check it from other views (Front, Top, Left, custom) to see where each layer really sits.
- A **camera** layer looks at the 3D layers. You can animate its position, its point of interest, its zoom and its depth of field.
- A **light** layer can be Parallel, Spot, Point, Ambient or Environment (image-based, from an equirectangular layer).
- Renderers:
  - **Classic 3D:** flat layers in 3D space.
  - **Advanced 3D:** real meshes, extruded text and shapes, 3D models, environment lighting.

## EffectCraft commands (verified unless marked)
- Make a layer 3D: `layer.setSwitch {layers, switch:"threeD", value:true}` (verified on text).
- Camera: `layer.newCamera {name, type: oneNode|twoNode, preset:"35mm"…, dof?, focusDistance?, aperture?, position?, poi?}`.
  - Paths: `transform/position`, `transform/poi`, `cameraOptions/zoom`, `cameraOptions/dof`, `cameraOptions/focusDistance`.
  - The default position is [w/2, h/2, −1500]. A dolly from z −2500 to −1200 with easyEase was verified.
- Camera helpers:
  - `camera.orbitNull` (an orbit rig), `camera.linkFocusToLayer` / `camera.setFocusToLayer` (focus);
  - `camera.orbit`, `camera.pan`, `camera.dolly`;
  - `camera.fromView`.
- Light: `layer.newLight {kind: Parallel|Spot|Point|Ambient|Environment, intensity, color, coneAngle, coneFeather, castsShadows, shadowDarkness, shadowDiffusion, position, poi}` (verified Spot).
  - Shadows need the light to cast them, a layer that casts (`layer.castsShadows` or `materialOptions/castsShadows`) and a layer that accepts (`materialOptions/acceptsShadows`).
- Meshes:
  - Primitives: `layer.new3dPrimitive {kind: cube|sphere|plane|torus|cone|cylinder, radius, baseColor, metallic, roughness, position:[x,y,z]}` (verified sphere). This switches the comp to **Advanced 3D**.
  - Models: `layer.newModel {path: .glb|.gltf|.obj|.fbx|.stl}` (not tested). Materials: `material.set` / `material.reset`.
- Extruded 3D text: `geometryOptions/extrusionDepth`, `bevelStyle`, `bevelDepth` on the text layer (Advanced 3D). Per-character 3D: `layer.enablePerChar3D`.
- Ground plane, views and environment:
  - Views: `view.3d.front/top/left/custom1`, `view.set3DView` (UI-only value in headless mode; renders use the active camera).
  - Environment: `layer.environment`, `light.environmentBackground`.
- Renderer: `comp.renderer`, or `comp.new {renderer:"advanced3D"}`.

## Recipe: 3D logo or title reveal
1. Create the comp. Add a background solid, set 3D on, and push it back in Z.
2. Add the logo or text as a 3D layer (extrude in Advanced 3D for depth), centred at z=0.
3. Add a two-node camera (35–50 mm). Key position from far and offset to near and centred over 2–3 s with easyEase. Optionally use an orbit null for a slow turn.
4. Add a Spot light with casts shadows plus a low Ambient (around 20–30%) so the shadows aren't black.
5. Turn on DOF with focus on the logo for a premium look, and keep blur subtle.
6. Check with `render_frame` at the start, middle and end. 3D layers react to lights: check they don't go too dark.

## Gotchas
- 3D and lights are not exported to Lottie (they become hidden nulls).
- Moving a camera with its point of interest on (two-node) re-aims it. Use a one-node camera for free flying.
- Scale versus Z: to make an element look further away while keeping perspective consistent, move it in Z (or scale it, as the book suggests for tracked scenes).
