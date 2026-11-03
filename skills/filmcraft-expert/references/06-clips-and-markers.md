# 06 — Working with clips and markers (Lesson 6)

Summary in my own words; FilmCraft mapping verified.

## Concepts
- **Program Monitor** shows the sequence output; you can drop clips onto it for overwrite/insert, and drag only the picture or only the sound.
- **Playback resolution** (full, 1/2, 1/4…) separately for playback and paused frames; lower it for smooth playback.
- **Markers**: comments, chapter markers (for players that support chapters), segmentation and flash cue markers; on the sequence or inside a clip; with duration, color and notes. Useful for beats in the music, client notes, to-dos.
- **Sync lock** keeps tracks aligned during ripple/insert edits; **track lock** prevents any change to a track.
- **Gaps**: find and close them; ripple delete removes a clip and closes the gap.
- **Selecting**: single clip, linked video+audio, everything after a point on one or all tracks, gaps.
- **Moving**: drag, nudge by frames, rearrange with insert (swap order), copy/paste, paste insert.
- **Splitting**: add edit at playhead on targeted or all tracks.
- **Grouping vs linking**: linked items are one clip's video and audio; groups bind arbitrary clips together.
- **Lift/extract** with sequence In/Out; **disable** a clip to hide it without deleting.
- Premiere's VR playback modes exist for 360° media; FilmCraft carries VR effects but playback is a UI matter.

## FilmCraft
| Task | Command |
|---|---|
| Markers | `markers.add {target:"program", time|seconds, name, comment, color, durationFrames}`, `markers.addRange`, `markers.addChapter`, `markers.addFlashCue`, `markers.edit`, `markers.delete`, `markers.goNext`, `markers.exportCsv {path}` |
| Ripple sequence markers | `markers.rippleSequenceMarkers {on:true}` |
| Lock / sync lock / mute / solo | `timeline.setTrack {track, locked, syncLock, muted, solo, enabled}` |
| Gaps | `sequence.goToNextGap`, `timeline.selectGap`, `sequence.closeGap {track}` |
| Select | `timeline.select {clips, add}`, `timeline.selectClipAtPlayhead`, `edit.selectAll` |
| Move | `timeline.move {moves:[{clip,track,time}], insert, copy}`, `timeline.nudgeLeft/Right(5)` |
| Split | `timeline.razor {time, track?}` (without track it cut video and linked audio), `sequence.addEditAllTracks` |
| Link / group / enable | `clip.link`, `clip.group`, `clip.ungroup`, `clip.enable` |
| Clipboard | `edit.copy`, `edit.paste`, `edit.pasteInsert` |
| Lift / extract | `sequence.lift`, `sequence.extract` |
| Delete / ripple delete | `edit.clear`, `edit.rippleDelete {clips}`, `timeline.delete {clips, ripple:true}` |
| Linked selection toggle | `sequence.linkedSelection {on}` |

## Pitfalls
- Moving audio alone while linked selection is on drags video too; toggle linked selection or pass `linked:false`.
- Locked tracks are skipped silently by many edits; check `timeline.setTrack` state when an edit "does nothing".
- Markers do not follow ripple edits unless ripple sequence markers is on.
