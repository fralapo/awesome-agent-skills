# 03 — Importing media (Lesson 3)

Summary in my own words; FilmCraft mapping verified.

## Concepts
- **Import command** for ordinary files (video, audio, stills, graphics). **Media Browser / import mode** for camera cards: it understands camera folder structures and joins spanned files into one clip.
- Supported formats are wide (MP4/MOV/MXF, camera RAW in Premiere). Check codecs: long-GOP H.264/HEVC is heavy to edit; proxies help.
- **Stills**: single-layer images import as clips of the default still duration. Layered Photoshop/Illustrator files can come in merged, as separate layers or as a sequence (Premiere). Large stills should be prepared near the sequence frame size.
- **Image sequences**: numbered stills imported as one clip.
- **Voice-over**: record straight into an audio track with pre-roll and countdown.
- **Stock**: Premiere links Adobe Stock; FilmCraft has no stock browser.
- **Media cache**: conformed audio and index files; keep it on fast storage and clean it periodically.

## FilmCraft
| Task | Command |
|---|---|
| Import files | `media_import {paths, bin}` or `file.import {paths, bin}` |
| Image sequence | `media_import {image_sequence:true}` / `file.importImageSequence` |
| Browse folders / probe files | `mediaBrowser.list {path}`, `mediaBrowser.probe`, `file.mediaPropertiesFile` |
| Import from browser | `mediaBrowser.import`, `file.importFromMediaBrowser` |
| Graphic file as a layer on top | `graphics.newFromFile {path}` |
| Voice-over | `audio.voiceover.settings`, `audio.voiceover.start {track}`, `audio.voiceover.stop` (needs the desktop app with an input) |
| Text-to-speech scratch narration | `tts.voices`, `tts.create {text, voice, track}` |
| Import another project / AAF | `file.import` (a project file), `file.importAaf` |
| Cache | `mediaCache.info`, `mediaCache.clean {all}` |
| Missing | layered PSD/AI options, Adobe Stock |

## Workflow tips
- Layered PSD/AI: export the needed layers from PhotoCraft/VectorCraft as transparent PNGs, then import (stack them on separate V tracks).
- Prepare a folder per project with `footage/ audio/ graphics/ exports/` before importing; it makes Project Manager and relinking painless.
- After import run `file.mediaProperties {items}` and `media.colorInfo {item}` to see fps, size and color space (HDR phone clips!).

> Availability notes in this file are a snapshot as of 2026-11-03. ArtCraft apps update almost daily: re-check the live command catalogue before treating anything as missing.
