# Puppet tools (lesson 8)

## Concepts
- The puppet tools build a triangle mesh over the layer's opaque area and deform it with pins.
- Pin types:
  - **Position:** moves a point.
  - **Advanced:** position plus scale and rotation of that region.
  - **Bend:** rotation and scale only, around a fixed point.
  - **Starch:** stiffens an area so it does not distort.
  - **Overlap:** decides which part passes in front when parts cross.
- Mesh options: **density** (more triangles gives a smoother bend but is slower) and **expansion** (the mesh reaches past the edge).

## EffectCraft commands (pins verified)
- Add pins with `puppet.addPin {layer, kind: position|advanced|bend|starch|overlap, position:[x,y], time?}`.
  - The first pin creates the Puppet effect and mesh. It returns `{effect, mesh, pin, rest}`.
  - Coordinates are in effect (layer) space.
- Animate pins:
  - `puppet.movePin {layer, pin, position, time}` keys a pin.
  - `puppet.setPin {pin, scale?, rotation?, amount?, extent?, inFront?}` sets the other pin values.
- Record motion (the AE Ctrl/Cmd-drag sketch): `puppet.recordPin {layer, pin, samples:[[t,x,y]…], speed?, smoothing?}`. Set its options with `puppet.recordOptions`.
- Secondary motion: `puppet.follow {leader, pins, delay, amount, cascade}`.
- Mesh: `puppet.mesh {density, expansion, triangles, showMesh}`. **Avoid `puppet.info` inside batches**: it returns every deformed vertex, which can be tens of KB.

## Workflow
1. Put each moving part on its own layer, or cut it out with a mask first.
2. Place Position or Advanced pins at the extremities and joints: head, hands, feet, tail tip.
3. Add Starch pins where the shape must stay rigid, such as the torso or a face.
4. Key a few poses, or record a gesture, then ease the keys.
5. Check frames where the deformation is strongest. Watch for tearing or folding.
6. Puppet works on footage too: pin a still region and bend the rest (the book's flag example).

## Note
Character Animator is an Adobe app and has **no EffectCraft equivalent**. For lip sync or face-driven rigs, use face tracking (`track.mask {method:"faceDetailed"}` + `track.extractFaceMeasurements`, not tested) and expressions.
