# Painting with the Mixer Brush (Lesson 10)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 10, mapped to PhotoCraft.

## Concepts
- The Mixer Brush blends the brush colour with what is already on the canvas, like wet paint, best with
  bristle tips.
- **Wet**: how much paint it picks up from the canvas. **Load**: paint in the brush at stroke start (runs out
  along the stroke). **Mix**: canvas vs brush colour ratio. **Flow**: rate of paint.
- Presets: Dry (opaque, no blending), Dry Light Load (Wet 0, Load ≈5), Wet, Very Wet (blends strongly).
- Clean / Load the brush; options "clean after each stroke" and "load after each stroke" (both on by
  default). Turn clean-after-stroke off to carry colours between strokes and mix new hues.
- Mixes only on the active layer unless Sample All Layers.
- Brush presets can store size, tip settings, tool options and colour. Paint Symmetry repeats strokes
  around axes.

## PhotoCraft calls
| Task | Call |
|---|---|
| Paint | `paint.mixerBrush {points:[[x,y,pressure?],…], size, wet, load, mix, flow, color, sampleAllLayers, cleanAfterStroke, loadAfterStroke}` ✔ |
| Load / clean / sample | `brush.mixer.load`, `brush.mixer.clean`, `brush.mixer.sample` (or `paint.mixerLoad`) |
| Tip settings | `brush.get`, `tools.setBrush {…}` (size, shape, bristles, length, thickness, stiffness, angle, spacing) |
| Presets | `brush.presets.list`, `.save`, `.setCurrent`, `.importAbr` (path-based, may be blocked), `.rename` |
| Normal painting | `paint.stroke` (supports pressure, tilt, rotation, `mode`, `erase`, `smoothing`) |
| Symmetry | `paint.setSymmetry`, `paint.symmetryFromPath`, `paint.symmetryDisable` |
| Rotate tip | `tools.rotateBrush` |

## Procedures
**Mix colours on a palette layer**: work on a dedicated layer; `brush.mixer.clean`; red stroke with wet
settings; `cleanAfterStroke:false`; blue stroke into it → violet; clean; blue + very wet yellow → green;
yellow + red → orange.

**Photo to painting**: open the landscape, duplicate it (or work on an empty layer with
`sampleAllLayers:true`), custom preset "Sky Brush" (round fan, ~36 px, bristles 35 %, length 32 %,
thickness 2 %, stiffness 75 %, spacing 2 %, light blue #56C9FC, Dry) for the sky; wet presets diagonally for
clouds; short vertical strokes for grass highlights; wet tree/foliage presets for dark masses and highlights;
up-down strokes for dry grass; diagonal blending strokes in the foreground.

## Good practice
- Strokes depend on the colours under the brush at the start: vary the starting side.
- Short light strokes = descriptive and textured; long heavy strokes = expressive.
- In automation, stroke points with pressure values imitate a tablet; pass a `seed` for reproducible runs.
- Keep paintings on separate layers above the photo so the original survives.
- Combine with generated or photographic bases (lesson 15 suggests reworking AI output by hand).
