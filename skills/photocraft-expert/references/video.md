# Video and animation (Lesson 11)

Source: synthesis of *Photoshop Classroom in a Book 2026*, Lesson 11, mapped to PhotoCraft.
⧗ = not available in PhotoCraft/LightCraft as of 2026-11-03 (snapshot — re-check with `command_list {filter}`
on the live app; ArtCraft apps update daily). The Photoshop behaviour described stays the target.

For real video work use **FilmCraft** (Premiere-class) or **EffectCraft** (After Effects-class): PhotoCraft's
timeline was minimal as of 2026-11-03 (snapshot — re-check with `command_list {filter:"timeline"}` /
`{filter:"keyframe"}` before routing elsewhere).

## Photoshop concepts (for reference)
- Timeline panel = the layer stack spread over time; video group = clips play in sequence; separate groups
  overlap in time (text over video → its own upper group).
- Dragging a clip edge changes duration, not speed; a clip cannot exceed its source.
- Keyframes: at least two; the app interpolates. Animatable property depends on layer type (Position for
  pixels/video, Transform for SO/type, Vector Mask Position for shapes).
- Strategy: the static layout is the *end* state → set end keyframes first, then the start ones.
- Transitions (Cross Fade, Fade With Black) shorten the sequence: compensate durations.
- Audio tracks with fade in/out; render to H.264 via Media Encoder. Frame Animation + tweening → GIF.

## What PhotoCraft can do (snapshot 2026-11-03 — re-check)
| Function | Call | Status |
|---|---|---|
| Create timeline | `timeline.create {duration, fps}` | ✔ |
| Settings / info / navigate | `timeline.setProps {fps, duration, workStart, workEnd}`, `timeline.info`, `timeline.setFrame`, `nextFrame`, `previousFrame` | ✔ info |
| Blank video layer, frame edits | `layer.videoLayers.newBlankVideoLayer` ✔, `insertBlankFrame`, `duplicateFrame`, `deleteFrame`, `restoreFrame` | |
| Video file import | `layer.videoLayers.newVideoLayerFromFile`, `file.import.videoFramesToLayers` | param doc `{}`: UI dialog, not usable headless |
| Render | `file.export.renderVideo {dir}` → PNG frame sequence (one file per frame) ✔ | writes under `<dir>` inside the allowed read/write root |
| Keyframes, audio, transitions, Motion presets, frame animation/tween, GIF export | — | ⧗ |

## Practical route
1. Design the static frames in PhotoCraft (end state of each element, on separate layers).
2. `doc_export_layers {dir}` ✔ to get each element as PNG with transparency.
3. Animate in EffectCraft (keyframes on position/scale/opacity, start from the end keyframe) or cut in
   FilmCraft (clips synced to music beats, cross fades, audio fades), then render there.
4. Frame sequences from `renderVideo` can be assembled with ffmpeg (skill `awesome-agent-skills:ffmpeg`).

## Checks
- Frame size from a video preset (1920×1080) from the start; safe areas for titles.
- Sync cuts to music; recheck after adding transitions.
- Delete test render folders you create.
