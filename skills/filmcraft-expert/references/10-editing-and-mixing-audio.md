# 10 — Editing and mixing audio (Lesson 10)

Summary in my own words; gain/normalize, ducking and auto-match verified.

## Concepts
- **Meters** read in dBFS; 0 dBFS is the ceiling (anything over clips). Watch peaks and overall loudness, not only the waveform size.
- **Channels**: stereo = two channels (L on 1, R on 2 by convention); mono = one. A single mic recorded on both channels should be mapped as mono.
- **Waveforms** in source and timeline help find words and beats; audio can be edited with sub-frame precision when displaying samples.
- **Track types and solo/mute** let you audition parts of the mix.
- **Three volume layers**: clip **gain** (before effects, good for fixing a bad recording level), clip **volume** (keyframable rubber band), track volume (mixer). They add up: −3 on the clip and −3 on the track = −6.
- **Normalize** sets gain from measured peaks (max peak per clip or all peaks together).
- **Auto-ducking**: music level is lowered automatically where dialogue is detected, with keyframes you can then refine.
- **Remix** re-edits a music track to a target duration at musical boundaries.
- **Split edits**: J-cut (audio of the next shot starts before its picture) and L-cut (audio of the previous shot continues under the next picture). They make cuts feel natural.
- **Keyframing volume**: add points on the rubber band; smooth with ease; clip keyframes travel with the clip, track keyframes stay with the timeline (mixer automation modes Read/Latch/Touch/Write).
- **Audio Clip Mixer** adjusts per-clip level/pan while playing; **Track Mixer** handles track faders, submixes, sends and inserts.

## FilmCraft
| Task | Command |
|---|---|
| Gain | `clip.audioGain {clips, mode:"set"|"adjust", db}` |
| Normalize | `clip.audioGain {clips, mode:"normalizeMax"|"normalizeAll", db:-3}` (verified, returns the applied gain) |
| Peak | `clip.audioPeak {clips}` |
| Volume keys | `clipMixer.set {clip, effect:"volume", param:"level", value, keyframe:true, time}` or `effects.setParam {effect:"volume", param:"level"}` |
| Nudge volume | `clip.nudgeVolumeUp1/Down1/Up3/Down3`, `clip.volumeUp/Down` (±1 dB), `...Many` (±6 dB) |
| Track level / pan | `timeline.setTrack {track:"A2", volumeDb, pan}`, `mixer.setStrip` |
| Automation | `mixer.setStrip {mode:"Touch"}`, `mixer.writeAutomation {strip, points:[[ticks,value]]}` |
| Submix / send / insert | `mixer.addSubmix`, `mixer.addSend`, `mixer.addInsert {strip, effect}` |
| Ducking | `essentialSound.setType {type:"music"}` + `essentialSound.generateDucking {clips}` (verified: keyframes −15 dB under dialogue, 0.8 s fades) |
| Remix | `clip.remix {clip, seconds}` |
| J/L cut | unlink or `timeline.trim {linked:false}` on the audio edge; or `timeline.roll {followLinks:false}` |
| Mixdown | `sequence.normalizeMixTrack {db}`, `sequence.renderAudio` |

## When to switch to SoundCraft
- More than a handful of dialogue tracks to balance, or a mix needing buses, sidechain, detailed automation.
- Music editing beyond a remix (bar-accurate edits, stems), sound design layering, mastering.
- Path: export WAV/OMF/AAF from FilmCraft → SoundCraft (`file.import_audio` / `file.import_video` for picture reference) → `file.bounce_mix` → re-import into FilmCraft on its own track; mute the originals, keep them for revisions.

## Practice
- Dialogue first, then music under it, then effects/ambience. Music beds typically sit 15–20 dB below dialogue during speech.
- Fades of 2–4 frames on every audio cut avoid clicks.
