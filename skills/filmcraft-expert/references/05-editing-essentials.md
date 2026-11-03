# 05 — Editing essentials (Lesson 5)

Summary in my own words; FilmCraft commands verified on a scratch project.

## Concepts
- **Source Monitor**: view a raw clip, mark In/Out, choose whether video, audio or both go into the edit. Subclips save a marked range as a reusable project item (handy for long interviews).
- **Sequence**: ordered clips on tracks, with its own In/Out, playhead and settings.
- **Tracks**: upper video covers lower video; audio tracks mix together. Track headers carry targeting, source patching, lock, sync lock, mute/solo, visibility.
- **Targeting** chooses the destination track for keyboard edits; **source patching** chooses which source channels enter.
- **Overwrite** replaces what sits under the playhead range; **insert** splits at the playhead and pushes the rest later.
- **Three-point editing**: any three of source In/Out and sequence In/Out define the edit; with no marks the whole clip is used from the playhead.
- **Storyboard editing**: order clips (e.g. in freeform/icon view), then send them to the sequence in that order, optionally with default transitions.
- Sequence In/Out mark ranges to remove, render or export.

## FilmCraft
| Task | Command |
|---|---|
| Open clip in source | `source.open {item}` |
| Mark source range | `markers.markIn/markOut {target:"source", seconds}` or `project.setMarks {item,in,out}` |
| Subclip | `clip.makeSubclip {item, start, end, name}` |
| Overwrite / insert from source | `source.overwrite`, `source.insert` (use targeting + playhead) |
| Direct placement (agent-friendly) | `timeline.place {item|items, track, seconds, insert, sourceIn, duration, video, audio}` |
| Targeting / patching | `timeline.setTargeting {track, targeted, sourcePatch}` |
| Sequence In/Out | `markers.markIn/markOut {target:"program"}` |
| Storyboard to sequence | `clip.automateToSequence {items, ordering:"selection", method:"insert", videoTransition}` |
| Playhead | `playhead.set {seconds}`, `playhead.nextEdit/prevEdit` |

Verified: `timeline.place {items:[1,2,3], track:"V1", seconds:0}` lays clips back to back and returns `[video,audio]` pairs; `track:"A2", video:false` places only the sound.

## Good practice
- Prefer `timeline.place` with explicit `sourceIn`/`duration` for scripted edits; use source In/Out only when mirroring a human workflow.
- Build the story with insert edits (order matters), then switch to overwrite for B-roll on V2 above the A-roll.
- Keep A-roll on V1/A1, B-roll on V2, music on A2–A3, graphics on the top tracks.
