# 16 — Exporting frames, clips and sequences (Lesson 16)

Summary in my own words; presets listed and a real 2 s H.264 export verified.

## Concepts
- **Quick export**: one click with a preset; "Match Source – Adaptive High Bitrate" is a good general-purpose master for upload.
- **Full export settings**: format/container vs codec; match sequence settings or change frame size, fps, bitrate (CBR/VBR 1 or 2 pass), audio codec; source range (whole sequence, In/Out, work area, custom); scaling when aspect ratios differ (fit with bars, fill with crop, stretch); export-time effects (LUT, overlay image/name/timecode, loudness normalization, video limiter); captions burn-in or sidecar; metadata.
- **Single frames** as PNG/JPEG/TIFF for thumbnails and review.
- **High-quality masters / intermediates**: ProRes (422 HQ, 4444 with alpha) or DNxHR in MOV/MXF; check the recipient's delivery specs.
- **Background queue** (Media Encoder in Premiere): several outputs and presets processed while you keep working.
- **Social**: platforms re-compress; upload a high-bitrate file at native size and fps rather than a small one.
- **Interchange**: EDL, XML, AAF, OMF, OTIO for handing the edit to other NLEs, colorists or audio mixers.

## FilmCraft
| Task | Command |
|---|---|
| Presets | `export.presets.list {query, category}`, `export.presets.get`, `export.presets.save` |
| Dry run | `export.resolve {preset, …}` (shows output size, bitrate, range, warnings, **default path in ~**) |
| Export | `file.exportMedia {path, preset|format, width, height, fps, bitrateKbps, bitrateMode, crf, range:"entire"|"inOut"|"workArea"|"custom", startSeconds, endSeconds, loudnessLufs, burnCaptions, captionSidecar, alpha, wait:true}` |
| Quick | `export.quick {preset, path, wait}` |
| Queue | `export.queue.add {…, path, sequences}`, `export.queue.start {wait:true}`, `export.queue.list/cancel/retry` |
| Frame | `file.exportFrame {path, format:"png", time}` |
| Captions only | `captions.export {path, format}` |
| Audio only | presets "Waveform Audio 48 kHz 24-bit", "AAC Audio 48 kHz 320 kbps"; `format:"wav"` |
| Interchange | `file.exportInterchange {format:"xml"|"edl"|"fcpxml"|"otio"|"aaf"|"omf", path}`, `file.exportAaf`, `file.exportOmf` |
| Missing | direct upload to YouTube/Vimeo/social |

Built-in presets: Match Source High/Medium/Low; High Quality 1080p/2160p; YouTube 1080p/2160p; Vimeo 1080p/2160p; Social Vertical 1080×1920 (12 Mbps, scale to fill); ProRes 422 HQ/422/LT/Proxy/4444/4444 with Alpha/4444 XQ; DNxHR HQ/SQ/LB; APV; MXF OP1a/OP-Atom; PNG/TIFF/DPX/EXR sequences; Animated GIF; WAV/AIFF/AAC/FLAC.

## Delivery cheat-sheet
| Target | Settings |
|---|---|
| Instagram Reels / TikTok / Stories | 1080×1920, 25/30 fps, "Social Vertical 1080×1920", `loudnessLufs:-14`, burned captions |
| YouTube | "YouTube 1080p Full HD" or 2160p, loudness −14 |
| Web player / client preview | Match Source Medium, optional `timecode_overlay` |
| Broadcast | ProRes 422 HQ / MXF OP1a per spec, −23 LUFS, video limiter |
| Archive master | ProRes 422 HQ (or 4444 if alpha) + WAV 24-bit stems + XML |

Verified run: `exportMedia {preset:"Social Vertical 1080×1920", range:"custom", startSeconds:0, endSeconds:2, loudnessLufs:-14, wait:true}` → 50 frames, ~0.6 MB; the result reports `bytes`, `frames`, `render_fps`.

> Availability notes in this file are a snapshot as of 2026-11-03. ArtCraft apps update almost daily: re-check the live command catalogue before treating anything as missing.
