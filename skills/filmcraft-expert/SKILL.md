---
name: filmcraft-expert
description: "Premiere Pro-grade video editing in FilmCraft, the ArtCraft editor driven over MCP (mcp__filmcraft__* tools: command_list, command_run, command_batch, doc_inspect, sequence_inspect, render_frame, media_import). Use whenever working with FilmCraft or editing any video: rough and fine cuts, ripple/roll/slip/slide trims, 9:16 reels/TikTok/Shorts from 16:9, captions and titles, transitions, keyframes, speed and time remapping, Lumetri color, LUTs and scopes, chroma key, audio mixing, LUFS loudness and ducking, multicam, proxies, export for social, web or a ProRes/DNxHR master, and project archiving. Includes a verified Premiere-to-FilmCraft command map, QC checklists, and hand-offs to SoundCraft and EffectCraft."
version: 1.0.0
source: "Workflow informed by Adobe Premiere Classroom in a Book 2026 Release (Adobe Press); mappings verified against FilmCraft's live command catalogue on 2026-11-03. Written independently; no text from the book is reproduced."
---

# FilmCraft expert

Operational knowledge for editing video in **FilmCraft** (the ArtCraft Premiere Pro-class editor) from Claude Code or any SKILL.md-compatible agent with the FilmCraft MCP server connected (SoundCraft and EffectCraft are optional hand-off targets). Per-lesson summaries live in `references/`. Every mapping below was checked against `command_list` (716 commands) and `effects.list` (304 effects) on 2026-11-03.

> **Sources.** The workflow is informed by Adobe's *Premiere Classroom in a Book 2026 Release* (Adobe Press) and verified against FilmCraft's live command catalogue on 2026-11-03. This skill is written independently and reproduces no text from the book.

For *what* to cut and *why* (hooks, pacing, retention, structure), pair this with the [`video-editor`](../video-editor/SKILL.md) skill; for command-line transcoding, probing or batch conversion outside FilmCraft, see [`ffmpeg`](../ffmpeg/SKILL.md).

**Verification legend.** "(verified)" / "Verified:" = the command was actually executed on a live FilmCraft session and the behaviour described was observed. Unmarked mappings = the command/effect id exists in the live catalogue on 2026-11-03 with matching parameters, but was not exercised end to end. "Not available" = searched in the catalogue on that date with no match (a snapshot, see §0).

## 0. The app changes every day — re-check before saying "missing"

ArtCraft apps get updates almost daily. Every "absent" or "missing" item in this skill and in `references/` is a **snapshot as of 2026-11-03**, not a permanent limit.
- Before you tell the user that a feature is missing, or fall back to a workaround, search the live catalogue with a filter (`command_list` / `list_effects` / `effects.list`). If the command exists now, use it.
- The Adobe method described here is the **target**. Apply it in full as soon as the app supports it.
- If you find a command that this skill lists as absent, or a mapping that has changed, update this skill (or open an issue on the repository) so the snapshot stays accurate.

## Ground rules for the agent

- **Time**: 254016000000 ticks = 1 s. Most commands also accept `seconds`, `frame` or `timecode`; transition durations are in `frames`.
- **Keyframe time**: `effects.setParam {time, keyframe:true}` takes **timeline** time. `effects.setInterpolation`, `setKeyframe`, `moveKeyframe` and `deleteKeyframe` take `mediaTime` = **source** time = `sourceIn + (t_timeline − start)` (verified).
- **Ids**: timeline clips and project items have different ids. `timeline.place` returns linked `[video, audio]` pairs. `sequence_inspect` is very verbose (~15k tokens with 3 clips); for targeted questions use `state.inspect`, `graphics.list`, `essentialSound.inspect`, `mixer.inspect`, `captions.list`.
- **Batches**: `command_batch {stop_on_error:false}` runs everything and reports `ok`/error per step; each step is its own undo (`edit.undo`).
- **Export**: **always** pass an explicit `path` (without one the file lands in the user's home folder as `<sequence name>.mp4`), `wait:true` to get the result; check first with `export.resolve`.
- **User files**: never open or save user projects unless asked. For experiments use `file.newProject` + `file.importDemoFootage` (OceanSunset, Aurora, CityNight, Dunes, Plasma, Forest).
- **Visual check**: `render_frame {seconds, max_side:480}` at several points; for color, `scopes.read` (numbers, not pictures).

## Key concepts (short)

- **Project**: holds bins, clips, sequences and settings, but only *references* to media files. Deleting/renaming a clip never touches the original.
- **Bins**: project folders (`file.newBin`, `project.moveToBin`); search bins (`file.newSearchBin`) are dynamic metadata collections.
- **Sequence**: the timeline. Its settings (frame size, fps, audio) set the working format; match the main footage, or the delivery when sources are mixed.
- **Tracks**: higher V tracks cover lower ones; A tracks add up. *Targeting* (`timeline.setTargeting`) decides where insert/overwrite land; *source patching* decides which source channels come in. *Sync lock* and *lock*: `timeline.setTrack`.
- **In/Out**: on the source they choose what to use; on the timeline they mark a range to remove, render or export.
- **Insert vs overwrite**: insert pushes everything later (sequence gets longer); overwrite replaces what is underneath.
- **3/4-point edits**: give three points and the fourth is computed; four points that disagree force a choice between trimming and changing speed.
- **Lift vs extract**: lift leaves a gap, extract closes it. Same for delete vs ripple delete.
- **Trims**: *regular* moves one edge and leaves a gap; *ripple* moves an edge and drags the rest along; *roll* moves the cut between two clips without changing total length; *slip* changes which part of the source is shown at a fixed position; *slide* moves the clip and shortens/lengthens its neighbours.
- **Handles**: extra media beyond In/Out; without them transitions repeat frames.
- **Markers**: sequence or clip markers with name, comment, color and duration; chapter and flash-cue markers too.
- **Nesting**: `clip.nest` turns several clips into a sub-sequence that behaves as one clip (group effects, reframing, partial exports).
- **Fixed effects**: Motion, Opacity, Time Remapping, Volume, Channel Volume and Panner are on every clip already.

## Recommended workflow

1. Project + bins (Footage, Audio, Graphics, Sequences) → import → check formats (`file.mediaProperties`, `media.colorInfo`).
2. Sequence with correct settings (or `matchSequence:true` on the first `timeline.place`).
3. Selects with In/Out or subclips → rough cut.
4. Fine cut: trims, pacing, J/L-cuts, transitions only where they earn their place.
5. Audio: types, loudness, cleanup, music, ducking, mix.
6. Effects, motion, stabilization, compositing.
7. Color: correction first (balance, shot matching), then grading (the look).
8. Titles, graphics, captions.
9. QC → export → archive (Project Manager).

## Premiere → FilmCraft mapping

| Premiere feature | FilmCraft |
|---|---|
| New project / sequence / bin | `file.newProject`, `file.newSequence {width,height,fps}`, `file.newBin` |
| Sequence settings | `sequence.settings`, `sequence.colorSettings` |
| Import / Media Browser | `media_import` (tool), `file.import`, `mediaBrowser.list/import` |
| Layered PSD/AI | no layer dialog: export layers from PhotoCraft/VectorCraft as PNG |
| Voice-over recording | `audio.voiceover.start/stop` (needs the app with an audio input) |
| Synthetic narration | `tts.create` (not in Premiere) |
| Metadata and columns | `metadata.set`, `project.columns.set`, `edit.find` |
| Subclips | `clip.makeSubclip` |
| Audio channels / interpret footage | `clip.audioChannels`, `clip.interpretFootage` |
| Merge clips (dual-system audio) / synchronize | `clip.mergeClips`, `clip.synchronize {method:"audio"}` |
| Source Monitor, In/Out | `source.open`, `markers.markIn/markOut {target:"source"}`, `project.setMarks` |
| Insert / overwrite | `source.insert`, `source.overwrite`, `timeline.place {insert}` |
| Storyboard → sequence | `clip.automateToSequence` |
| Razor / Add Edit | `timeline.razor`, `sequence.addEdit(AllTracks)` |
| Lift / extract / ripple delete | `sequence.lift`, `sequence.extract`, `edit.rippleDelete`, `timeline.delete {ripple}` |
| Close gaps | `sequence.closeGap`, `timeline.selectGap` |
| Trim, ripple, roll, slip, slide | `timeline.trim {mode}`, `timeline.roll`, `timeline.slip`, `timeline.slide` |
| Keyboard trims Q/W, E | `trim.ripplePrevious/rippleNext`, `trim.extendToPlayhead` |
| Dynamic trimming | `trim.shuttle`, `trim.playAround` |
| Rate stretch / speed / reverse | `timeline.rateStretch`, `clip.speedDuration {speed,reverse,ripple}` |
| Frame hold / optical flow | `clip.frameHold`, `clip.setTimeInterpolation` |
| Replace clip / footage | `clip.replaceFromBin`, `media.replaceFootage` |
| Markers | `markers.add/addRange/addChapter/edit/exportCsv` |
| Link, group, enable | `clip.link`, `clip.group`, `clip.enable` |
| Nest | `clip.nest`, `sequence.makeSubsequence` |
| Video/audio transitions | `sequence.applyVideoTransition`, `sequence.applyAudioTransition`, `trim.applyDefaultTransition` |
| Morph Cut | transition effect `morph_cut` |
| Text-Based Editing | `transcript.generate` → `transcript.extract/lift`, `removePauses`, `removeFillers` |
| Effects / params / keyframes | `effects.apply`, `effects.setParam`, `effects.addKeyframe`, `effects.setInterpolation` |
| Effect presets / adjustment layer | `presets.save/apply`, `file.newAdjustmentLayer` |
| Paste/remove attributes | `edit.pasteAttributes`, `edit.removeAttributes` |
| Masks and tracking | `masks.add`, `masks.set`, `masks.track` |
| Warp Stabilizer / Auto Reframe | effects `warp_stabilizer`, `auto_reframe`; `clip.fillFrame/fitToFrame` |
| Scene Edit Detection | `clip.sceneEditDetection` |
| Lumetri (panel, presets, LUTs, match) | effect `lumetri` + `effects.setParam`, `lumetri.applyPreset`, `lumetri.setInputLut/setLook`, `lumetri.applyMatch`, `lut.import` |
| Lumetri Scopes | `scopes.read` (waveform, parade, histogram, vectorscope as numbers) |
| Video Limiter | effect `video_limiter` or the limiter in export settings |
| Opacity, blend modes | `effects.setParam {effect:"opacity", param:"blend", value:"Screen"}` |
| Ultra Key / Track Matte / Luma Key | effects `ultra_key`, `track_matte`, `luma_key`, `color_key` |
| Essential Graphics text/shapes | `graphics.newText`, `graphics.newShape/newRectangle`, `graphics.set`, `graphics.setCharStyle`, `graphics.align` |
| Title roll/crawl | `graphics.setRoll` |
| Motion Graphics templates | `graphics.template.list/apply/export` (`.fcgt`; `.mogrt` is refused) |
| Captions | `captions.newTrack/add/setStyle/import/export`, `transcript.createCaptions`, `graphics.upgradeCaption` |
| Audio gain / normalize | `clip.audioGain {mode:"set|adjust|normalizeMax|normalizeAll", db}` |
| Clip volume and keyframes | `clipMixer.set`, `effects.setParam {effect:"volume", param:"level"}` |
| Track mixer, submix, sends, automation | `mixer.setStrip/addSubmix/addSend/addInsert/writeAutomation` |
| Essential Sound (types, repair, clarity, ducking, auto-match) | `essentialSound.setType/set/applyPreset/autoMatch/generateDucking` |
| Remix (refit music length) | `clip.remix {seconds}` |
| Audio effects (EQ, notch, DeNoise, DeHum, Enhance Speech…) | `effects.apply` (see `references/11-improving-audio.md`) |
| Multicam | `clip.createMulticam`, `multicam.cut`, `clip.multicamFlatten` |
| Proxies / ingest | `media.createProxies`, `media.toggleProxies`, `project.ingestSettings` |
| Quick Export / export media / Media Encoder | `export.quick`, `file.exportMedia`, `export.queue.add/start` |
| Export a frame | `file.exportFrame` |
| EDL/XML/AAF/OMF/OTIO | `file.exportInterchange`, `file.exportAaf`, `file.exportOmf` |
| Project Manager / Remove Unused / Link Media | `file.projectManager {mode, handles, dryRun}`, `edit.removeUnused`, `media.findMissing/relink/autoRelink` |
| Cache cleanup | `mediaCache.clean`, `sequence.deleteRenderFiles` |

**Not available as of 2026-11-03 — snapshot, re-check (§0)** (searched in `command_list`/`effects.list`, no match): Generative Extend (AI), Object Mask tool (AI), Media Intelligence search / "search similar frames", Adobe Stock (video and audio), the Lumetri Basic Correction Auto button (only `applyMatch` exists), Render and Replace, Dynamic Link to After Effects/Audition, Team Projects/Productions/Frame.io, direct upload to social platforms, layered PSD/AI import. Workspaces and Comparison view are UI-only (use the `ui_*` tools in bridge mode). Workarounds: extend by hand with frame hold/slip, manual masks + `masks.track`, EffectCraft for motion, SoundCraft for audio.

## Recipes

**Rough → fine cut**
1. Import, organize in bins, name clips; with lots of footage use subclips.
2. Create the sequence, then `timeline.place {items:[...]}` in order (or `clip.automateToSequence`); use `sourceIn`/`duration` to pick ranges.
3. Remove the fat: `timeline.razor` + `edit.rippleDelete`, or In/Out + `sequence.extract`.
4. Pacing: `timeline.roll` on cuts, `timeline.slip` to pick the right moment.
5. Long talking-head: `transcript.generate` (needs the Whisper model, not installed: `transcript.downloadModel`, ~290 MB, ask first) → `removeFillers`, `removePauses`.

**9:16 reel from 16:9 footage**
1. `file.newSequence {width:1080, height:1920, fps:<footage fps>}`.
2. `timeline.place` the clips → `clip.fillFrame` (fills the frame; 177.8% from 1080p) and, if needed, the `auto_reframe` effect or manual `motion.position` keyframes. Alternative: nest the 16:9 sequence and reframe the nest.
3. Keep text inside the safe zone: leave roughly the top 15% and bottom 25% free for platform UI.
4. Big captions and bold graphics are the norm; keep the hook short (first 1–2 s).
5. Export with preset "Social Vertical 1080×1920" + `loudnessLufs:-14`.

**Transitions**: a straight cut is the default; dissolves (`cross_dissolve`, `dip_to_black`) signal a change of time or place. `effects.setDefaultTransition` → `trim.applyDefaultTransition` on selected clips. Audio: `constant_power` of 6–12 frames on cuts that pop. Check handles first.

**Motion and keyframes**: `effects.setParam {effect:"motion", param:"scale|position|rotation", value, time, keyframe:true}` at two times → `effects.setInterpolation {mediaTime, interpolation:"easeIn|easeOut|bezier"}`. For a shadow that rotates with the object use `transform` or `basic_3d` with `drop_shadow` below it, not Motion (Motion is applied last).

**Audio**: `essentialSound.setType` (dialogue/music/sfx/ambience) → `autoMatch` (defaults: dialogue −23, music −25, sfx −21, ambience −30 LUFS) → voice `set {key:"repair.noise.on"}` etc. → music `type:"music"` + `generateDucking` → master via export `loudnessLufs` (social −14, broadcast −23). Peaks around −6/−3 dBFS. **Hand off to SoundCraft** for waveform/spectral editing, serious restoration, many dialogue tracks, multitrack mixing with buses and complex automation, or music mastering: FilmCraft `file.exportMedia {format:"wav"}` (or `file.exportOmf`/`exportAaf` for separate tracks) → SoundCraft `file.import_audio`/`import_video` → `file.bounce_mix {format:"wav", bit_depth:24}` → back to FilmCraft with `media_import` onto a dedicated A track, originals muted.

**Effects**: apply to many clips via an adjustment layer or `presets.save/apply`. Masks: `masks.add` on the effect → `masks.set {feather, inverted}` → `masks.track`. Stabilize (`warp_stabilizer`) before scaling.

**Color**: 1) for HDR/phone footage check color management (`sequence.colorSettings`, `media.colorInfo`). 2) Basic correction with `lumetri` (temperature, tint, exposure, contrast, highlights, shadows, whites, blacks, saturation), checked with `scopes.read` (luma within ~0–100%, skin on the vectorscope skin line). 3) Match shots with `lumetri.applyMatch`. 4) Look with `lumetri.applyPreset` or `setLook` (LUT) on an adjustment layer. 5) Secondaries (`hsl_*` params, curves), vignette. 6) Broadcast: `video_limiter`.

**Compositing / chroma key**: green screen on V2, background on V1 → `ultra_key {key_color}`, tune choke/soften/spill, cut dirty areas with a garbage mask. Shape-based transparency: `track_matte` (matte on the track above). Blend modes via `opacity.blend`.

**Titles and graphics**: `graphics.newText {text, position, size}`. `position` is the baseline point of **left-aligned** text; to center use `graphics.set {props:{align:"center"}}` + `graphics.alignFrame.hcenter`. Styling: fill, stroke, shadow, background. Credit rolls: `graphics.setRoll`. Recurring graphics: templates + `graphics.template.apply {values}`.

**Captions**: `captions.newTrack {format:"Subtitle", language:"en"}` → `captions.add` or `transcript.createCaptions {maxChars:32, lines:2}` → `captions.setStyle` → deliver as `captions.export` (srt/vtt) or burn in with `exportMedia {burnCaptions:true}` for social.

**Export**: social/web "Match Source – Adaptive High Bitrate", "YouTube 1080p", "Social Vertical 1080×1920"; master ProRes 422 HQ or DNxHR HQ (`.mov`); with transparency ProRes 4444 with Alpha; separate audio WAV 24-bit. Partial test render: `range:"custom", startSeconds, endSeconds`. Several deliverables: `export.queue.add` ×N + `export.queue.start {wait:true}`.

**Project management / archive**: `file.projectManager {mode:"collect"}` gathers everything; `mode:"consolidate"` + `handles:30` + `preset:"prores_lt"` keeps only the used parts with margin. Run with `dryRun:true` first. Then `edit.removeUnused`, `media.findMissing`, `mediaCache.clean`.

## Common mistakes

- Wrong sequence fps/size: everything gets resampled. Check `sequence.settings` right away.
- Wrong targeting/source patching: clip lands on the wrong track or audio is missing.
- Delete instead of ripple delete: black gaps remain (find them with `sequence.goToNextGap`).
- Sync lock off during inserts: music or graphics drift out of sync.
- Transitions without handles: repeated frames.
- Treating point text as centered when it is left-aligned: it sits off-center (verified).
- Title overlapping the captions at the bottom: move one of them.
- Volume pushed past 0 dBFS: clipping. Use gain/normalization, not just the fader.
- Look applied before correction, or on every clip instead of an adjustment layer.
- Export without `path`: the file ends up in the home folder.

## Pre-delivery checks

1. `render_frame` at the start, at every scene change, on titles and captions, and 1 s before the end (`max_side:480` to save tokens).
2. `sequence.goToNextGap` (no gaps), `sequence.duplicateFrames` if relevant, offline clips (`media.findMissing`).
3. Color: `scopes.read` at 2–3 points (luma 0–100, no casts).
4. Audio: `essentialSound.autoMatch`, `clip.audioPeak`, export loudness matching the platform.
5. `export.resolve` with the chosen preset: frame size, fps, bitrate, `warnings`, `path`.
6. After export: check `result.bytes` and `frames`; if possible re-import with `media_import` in a scratch project.

## References

- Lessons: `references/01-touring-and-workflow.md` … `references/17-managing-projects.md`; glossary in `references/glossary.md`.
- Related skills: [`video-editor`](../video-editor/SKILL.md) (editing decisions), [`ffmpeg`](../ffmpeg/SKILL.md) (command-line media work).
- Keep deliverables in a predictable place: export to an explicit, agreed folder and name files with project, version and target (e.g. `promo_v3_9x16_-14LUFS.mp4`).
