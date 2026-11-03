# 07 — Adding transitions (Lesson 7)

Summary in my own words; FilmCraft transitions verified (`cross_dissolve`, `dip_to_black`, `constant_power`).

## Concepts
- A transition is a timed blend between two shots (or a fade on one side). It should have a narrative reason: passage of time, change of location, softening a jump. Overuse looks amateurish; a straight cut is the default.
- **Handles**: transitions consume media beyond the edit point. Without enough head/tail media the editor repeats frames or forces an off-center alignment.
- **Alignment**: centered on the cut, starting at the cut, or ending at the cut.
- **Single-sided** transitions fade from/to black or transparency at the start or end of a clip.
- **Default transition**: one video and one audio default applied with a shortcut to every selected edit.
- Replacing a transition keeps its timing.
- **Morph Cut** smooths jump cuts in talking-head interviews by interpolating faces; works only on a static framing with small differences.
- **Generative Extend** (AI frame extension) does not exist in FilmCraft: extend with a frame hold, slow-motion or a slip.
- **Audio transitions**: constant power (natural crossfade, default), constant gain (can dip), exponential fade. Short audio fades (a few frames) remove clicks at cuts.

## FilmCraft
| Task | Command |
|---|---|
| Video transition | `sequence.applyVideoTransition {clip, effect, frames, edge:"in"|"out", align:"center"|"start"|"end", params}` |
| Audio transition | `sequence.applyAudioTransition {clip, effect:"constant_power", frames, edge}` |
| Default transitions | `effects.setDefaultTransition {effect}`, `trim.applyDefaultTransition {clips}` |
| Edit settings / duration | `sequence.setTransition {transition, frames, align, params, reverse}` |
| Remove | `sequence.removeTransition {transitions}` |
| List available | `effects.list {kind:"VideoTransition"}` (~110, incl. Legacy and Obsolete folders) |
| Extend without media | `clip.insertFrameHoldSegment`, `clip.frameHold`, `timeline.slip` |

Useful ids: `cross_dissolve`, `dip_to_black`, `dip_to_white`, `dip_to_color`, `film_dissolve`, `morph_cut`, `push`, `slide`, `whip`, `zoom_blur`, `cross_zoom`, `light_leak`, `glitch`, `linear_wipe`, `clock_wipe`.

## Practice
- Typical durations at 25 fps: dissolve 12–25 frames, dip to black 15–30, whip/push 8–12, audio crossfade 6–12.
- Put a short dip to black at the very start and end of a piece only if the platform/brief wants it; social reels usually start on content immediately.
- For a sequence of photos use `clip.automateToSequence` with `overlapFrames` to get uniform dissolves.
