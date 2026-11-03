# 09 — Putting clips in motion (Lesson 9)

Summary in my own words; keyframe commands verified (timeline time vs media time).

## Concepts
- **Motion** (fixed effect) holds position, scale (uniform or width/height), rotation, anchor point and anti-flicker. Coordinates are in sequence pixels with (0,0) top-left; the default position is the frame center.
- **Anchor point** is the pivot for rotation and scale; move it to rotate around a corner.
- **Keyframes** store a value at a time; the engine interpolates between them. Turning on animation for a parameter creates the first keyframe; any later change at another time adds another.
- **Interpolation**: temporal (linear, bezier, auto/continuous bezier, hold) controls speed; ease in/out makes starts and stops gentle. Spatial interpolation controls the path shape for position.
- **Auto Reframe** analyses motion and keeps the subject inside a new aspect ratio (16:9 → 9:16/1:1/4:5).
- **Order of effects**: Motion is processed after other effects. A drop shadow applied to a clip that rotates via Motion rotates with it unrealistically; use the **Transform** effect (or Basic 3D) above the shadow so the shadow is computed on the moved image.
- **Basic 3D** swivels and tilts a layer in perspective.
- Picture-in-picture: scale down an upper-track clip and position it; add a stroke/shadow for separation.

## FilmCraft
| Task | Command |
|---|---|
| Static value | `effects.setParam {clip, effect:"motion", param:"scale", value:80}` |
| Keyframe | `effects.setParam {..., time:<timeline ticks>, keyframe:true}` or `effects.addKeyframe` |
| Easing | `effects.setInterpolation {clip, effect, param, mediaTime, interpolation:"easeIn"|"easeOut"|"bezier"|"hold"}` |
| Edit / move keyframe | `effects.setKeyframe {mediaTime, value, inInfluence, outInfluence}`, `effects.moveKeyframe`, `effects.moveKeyframes {delta}` |
| Fit / fill | `clip.fitToFrame`, `clip.fillFrame`, `clip.scaleToFrameSize` |
| Auto reframe | `effects.apply {effect:"auto_reframe"}` (params `preset, offset, zoom, aspect`) |
| Transform / 3D / shadow | `transform`, `basic_3d`, `rotate_3d`, `drop_shadow`, `long_shadow` |
| Preset animations | `move`, `grow`, `shrink`, `spin`, `wiggle`, `camera_shake` effects |
| Reuse motion | `edit.copy` + `edit.pasteAttributes {motion:true}`; `presets.save {keyframes:"anchorIn"}` |

**Media time (verified)**: a clip placed at timeline 2 s with `sourceIn` 1 s; a keyframe written at timeline 3 s is found by `setInterpolation` at `mediaTime` 2 s (= 1 + (3−2)), not 1 s.

## Recipes
- **Ken Burns on a still**: scale 100→115 over the clip, position drift 20–40 px, ease in/out on both keyframes.
- **Slide-in lower third**: position x off-frame → final over 10–15 frames, `easeOut` on the arrival keyframe.
- **Vertical reframe with a moving subject**: `clip.fillFrame`, then position keyframes every few seconds following the subject, bezier interpolation; check with `render_frame` at each keyframe.

## Pitfalls
- Keyframes set outside the clip's range still exist (FilmCraft keeps them at the given time) but are never reached.
- Scaling video above 100% softens it; for 9:16 from 1080p the 177.8% fill is a real quality loss, prefer 4K sources.
