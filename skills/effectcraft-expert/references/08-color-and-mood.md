# Color correction, grading and mood (lesson 10)

## Concepts
- **Correction** is objective: fix white balance and exposure, and match one shot to the next.
- **Grading** is creative: build a look, direct attention, set a mood.
- Correct first, then grade. Grade on an adjustment layer so you can change it globally.

## Tools in EffectCraft
| Need | Effect / command |
|---|---|
| Find cuts in an edited clip | `layer.sceneEditDetection {layer, mode: markers|split|splitPrecompose}` |
| All-in-one grade | `Lumetri Color` (`ec.color.lumetri`): `basicCorrection/whiteBalance/temperature`, `basicCorrection/tone/{exposure,contrast,highlights,shadows,whites,blacks}`, `basicCorrection/saturation`, `creative/look` (built-in looks: EC Warm Film, Cool Night, Bleach Bypass, Teal & Orange, Faded Matte, Monochrome), `creative/adjustments/{vibrance,fadedFilm,shadowTint,highlightTint}`, `curves/…`, `colorWheels/…`, `hslSecondary/…`, `vignette/vignetteAmount`. Verified paths. |
| Duotone / colorize | `Hue/Saturation` → `effects/#n/colorize:true`, `colorizeHue`, `colorizeSaturation`, `colorizeLightness` (verified paths) |
| Quick fixes | `Auto Contrast`, `Auto Levels`, `Auto Color` |
| Classic tools | `Levels`, `Curves`, `Color Balance`, `Vibrance`, `Photo Filter`, `Tritone`, `Tint`, `Selective Color`, `Shadow/Highlight`, `Exposure`, `Black & White`, `Leave Color` |
| LUT | `Apply Color LUT` |
| Scopes | `scopes.analyze` (Lumetri scopes as data) |
| Replace a sky or background | key with `Key Light` / `Color Range` / `Linear Color Key` + `Advanced Spill Suppressor`, or roto/mask; then a new layer underneath |
| Clone out an object | `paint.setCloneSource` + `paint.stroke {kind:"clone"}`, or `layer.newContentAwareFill` / `contentFill.generate` with a mask around the object |
| Track a mask (sky, a person, a wheel) | `track.mask {method:"positionScaleRotation"}`. Use it when the shape stays the same but moves, scales or rotates. |
| Darken a scene | Lumetri exposure down + a dark solid with an inverted feathered mask, or `Curves` |
| Freeze the action | `layer.freezeFrame` or time remap with a hold key |
| Transitions | `anim.applyBuiltinPreset` (fadeIn/Out, wipes, clockReveal…) or the Transition effects: `Linear Wipe`, `Radial Wipe`, `Gradient Wipe`, `Venetian Blinds`, `Block Dissolve`, `CC …` |

## Good practice
- Work in 16 or 32 bpc for strong grades: `file.cycleBitDepth`.
- Check skin tones and pure whites in `render_frame`. For broadcast-safe output use `Broadcast Colors` / `Video Limiter`.
- Use one grading adjustment layer at the top for the look, plus per-shot corrections on the footage layers.
- Keyed effects on adjustment layers let you shift the mood over time, for example day to dusk.
