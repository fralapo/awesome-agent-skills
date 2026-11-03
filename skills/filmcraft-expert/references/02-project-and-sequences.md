# 02 — Setting up a project and sequences (Lesson 2)

Summary in my own words; FilmCraft mapping verified 2026-11-03.

## Concepts
- A **project file** stores organization, edit decisions and settings, never the media itself.
- A **sequence preset** bundles frame size, frame rate, pixel aspect, field order, audio sample rate and track layout. Best playback comes from matching the dominant camera format; when sources are mixed or the delivery is fixed (e.g. 1080×1920 for social), pick the delivery format.
- The fastest safe route: create the sequence *from a clip*, so its settings copy the footage.
- **Timecode** = HH:MM:SS:FF; the frame count per second depends on the format (23.976, 25, 29.97, 50…). Drop-frame only matters for 29.97/59.94.
- **Audio track types**: standard (mono or stereo clips), mono, adaptive (flexible channel routing), 5.1. Master mix: stereo for almost all web/social work.
- **Preview/render settings**: preview codec and max render quality / max bit depth trade speed for quality.
- **Display formats**: video as timecode/frames/feet, audio as samples or milliseconds (for sub-frame audio edits).
- **Safe areas**: action-safe and title-safe margins; still useful as framing guides even if modern screens do not overscan.
- **Color settings**: working space (Rec.709 SDR is the usual web/TV target; Rec.2100 PQ/HLG for HDR), auto tone mapping for HDR sources.
- **Scratch disks**: where previews, captures and auto-saves go; keep them on fast storage next to the project.
- **Ingest settings**: copy, transcode or create proxies automatically on import.

## FilmCraft
| Task | Command |
|---|---|
| New project / from template | `file.newProject {name}`, `file.templates`, `file.newProjectFromTemplate` |
| New sequence | `file.newSequence {name,width,height,fps,sampleRate,video,audio,mix}` |
| Sequence from clip(s) | `file.newSequence {fromItem}` / `file.newSequenceFromClip {items}` or `timeline.place {matchSequence:true}` |
| Change settings later | `sequence.settings {width,height,fps,maxRenderQuality,scaleMotion}` |
| Color management | `sequence.colorSettings {workingSpace, wideGamut, autoToneMap}` |
| Project settings | `file.projectSettings.general {renderer, videoDisplay, audioDisplay, titleSafe…}` |
| Scratch disks | `file.projectSettings.scratchDisks` |
| Ingest | `project.ingestSettings {enabled, action, destination, preset}` |
| Add/remove tracks | `sequence.addTracks`, `sequence.deleteTracks {video:"empty"}` |

Common presets (width×height @ fps): 1920×1080 @ 25 (PAL regions, e.g. Europe; use 29.97/30 in NTSC regions), 3840×2160 @ 25, 1080×1920 @ 25/30 (reels, TikTok, stories), 1080×1080 (square feed), 1080×1350 (4:5 feed).

## Mistakes to avoid
- Building a sequence at the wrong fps and discovering it at export: every clip gets frame-rate converted.
- Changing the frame size of a finished sequence without `scaleMotion`: framing shifts.
- Putting cache/previews on a slow or synced cloud folder.
