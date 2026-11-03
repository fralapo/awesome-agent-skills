# 13 — Color correction and grading (Lesson 13)

Summary in my own words; Lumetri params, presets and `scopes.read` verified.

## Concepts
- **Correction vs grading**: correction makes shots technically sound and consistent with each other (craft); grading gives the story a mood (art). Do them in that order.
- **Display color management**: footage without tags is read as Rec.709; HDR material (common from phones) is tone-mapped into SDR sequences. For web delivery a 2.2 viewer gamma is typical; for phone HDR to SDR web, set the sequence to Rec.709 SDR and let tone mapping work.
- **Lumetri sections**: Basic Correction (input LUT, white balance, tone: exposure, contrast, highlights, shadows, whites, blacks, saturation), Creative (look LUT, intensity, faded film, sharpen, vibrance, shadow/highlight tint), Curves (RGB and hue/saturation/luma curves), Color Wheels & Match (shadows/midtones/highlights + automatic shot match), HSL Secondary (key a color range and change only that), Vignette. Each section can be bypassed to compare. Several Lumetri instances on one clip keep correction and look separate.
- **Scopes** are objective, your eyes adapt: waveform (brightness per column), RGB parade (channel balance), histogram, vectorscope (hue/saturation; skin tones sit on a diagonal skin line).
- **Selection follows playhead** lets you grade clip after clip quickly.
- **Comparison view** shows reference vs current (UI only in FilmCraft).
- **Video Limiter** keeps levels legal for broadcast (the broadcaster states the exact limits).
- Fixes: underexposure (raise exposure/whites, lift shadows carefully, watch noise), overexposure (pull highlights/whites; clipped detail does not come back), color cast (temperature/tint, then wheels; check neutral greys in the parade).

## FilmCraft
| Task | Command |
|---|---|
| Add Lumetri | `effects.apply {clips, effect:"lumetri"}` |
| Basic | `effects.setParam {clip, effect:"lumetri", param:"exposure"|"contrast"|"temperature"|"tint"|"highlights"|"shadows"|"whites"|"blacks"|"saturation", value}` |
| Creative | `look`, `look_lut`, `look_intensity`, `faded_film`, `vibrance`, `shadow_tint`, `highlight_tint` / `lumetri.setLook {clip, lut}` |
| Curves / wheels / HSL / vignette | `curve_luma`, `hue_vs_sat`… / `wheel_shadows(_l)`, `wheel_midtones`… / `hsl_hue`, `hsl_hue_range`, `hsl_sat`… / `vignette_amount`… |
| Section on/off | `lumetri.setSection {clip, section:"basic"|"creative"|"curves"|"wheels"|"hsl"|"vignette", on}` |
| Presets | `lumetri.presets` (Cinematic, Film Emulation, Monochrome, Technical incl. "Legal Range Squeeze"), `lumetri.applyPreset {name, clips}` |
| LUTs | `lut.import`, `lut.list`, `lumetri.setInputLut`, `lut.export` |
| Shot match | `lumetri.applyMatch {clip, referenceTime, faceDetection:true}` |
| Scopes | `scopes.read {scopes:["waveform","parade","histogram","vectorscopeYuv"], seconds}` (returns min/mean/max per channel, vectorscope peaks and angle) |
| Color management | `sequence.colorSettings`, `clip.interpretFootage {colorSpace}`, `media.colorInfo` |
| Legal levels | effect `video_limiter`, or export `effects.video_limiter` |
| Other tools | `asc_cdl`, `levels`, `proc_amp`, `brightness_contrast`, `channel_mix`, `color_pass`, `black_white`, `tint` |
| Missing | Basic Correction "Auto" button; Comparison view (UI only) |

## Agent workflow with numbers
1. `scopes.read` → if `y.max` < ~85 raise whites/exposure; if `y.min` > ~10 lower blacks; if `r/g/b mean` differ a lot on a neutral scene, fix temperature/tint.
2. Re-read the scopes after each change; aim for consistent `y.mean` and channel balance between shots of the same scene.
3. Then the look on an adjustment layer; finally `render_frame` to judge it visually.

> Availability notes in this file are a snapshot as of 2026-11-03. ArtCraft apps update almost daily: re-check the live command catalogue before treating anything as missing.
