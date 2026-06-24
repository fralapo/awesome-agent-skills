---
name: ffmpeg
description: "Complete FFmpeg reference and toolkit, distilled from the official FFmpeg documentation (ffmpeg/ffplay/ffprobe + codecs, formats, filters, protocols, devices, libraries). Use when building or debugging FFmpeg command lines: transcoding, remuxing, stream copy, cutting/trimming, concatenation, scaling/cropping/padding, frame-rate and pixel-format conversion, audio resampling/mixing, filtergraphs (-vf/-af/-filter_complex), overlays, drawtext/subtitles burn-in, HLS/DASH segmenting, screen/webcam capture, piping, hardware accel (NVENC/QSV/VAAPI/VideoToolbox), and choosing encoder options (libx264/libx265/aac/libmp3lame/etc.). Keywords - ffmpeg, ffplay, ffprobe, transcode, remux, filtergraph, vf, af, filter_complex, map, stream specifier, codec, muxer, demuxer, hls, scale, overlay, concat, crf, bitrate, gop, pix_fmt."
version: 1.0.0
source: "FFmpeg official documentation — https://ffmpeg.org/documentation.html (nightly, fetched 2026-06-24)"
---

# FFmpeg — Reference & Command Toolkit

FFmpeg is a universal media converter: it reads any number of inputs (files, pipes, network streams, capture devices), filters and transcodes them, and writes any number of outputs. This skill is a practitioner's toolkit for **constructing correct command lines fast** and knowing which option, codec, or filter to reach for.

> The full official source text ships with this skill at [reference/FFmpeg-Complete-Documentation.md](reference/FFmpeg-Complete-Documentation.md) (~1.9 MB). This skill extracts the structure; grep that file or the chapter files for exhaustive option lists.

## How to Use This Skill

- **No arguments** — load the core mental model + the cheatsheet of common commands.
- **A task** — "trim without re-encoding", "burn subtitles", "capture screen" → I map it to a pattern in [patterns.md](patterns.md) / [cheatsheet.md](cheatsheet.md).
- **A topic** — "filters", "codecs", "hls", "protocols" → I read the matching `chapters/` file before answering.
- **A name** — a specific filter/encoder (e.g. `scale`, `libx264`) → grep the chapter for exact options.

---

## Core Mental Model (read this first)

**1. Command anatomy — order matters.**
```
ffmpeg [global_opts] {[input_opts] -i INPUT}... {[output_opts] OUTPUT}...
```
Options apply to the **next** file specified. Put input options (e.g. `-ss`, `-f`, `-r`, `-framerate`) **before** the `-i` they modify; output options before the output URL. Global options (e.g. `-y`, `-loglevel`) go first. Anything not parsed as an option is treated as an output URL.

**2. Indices & stream specifiers.** Inputs/streams are 0-based. `-map 0:v:0` = first video stream of input 0. Stream specifier forms: `:v` `:a` `:s` (type), `:0` (index), `:v:0`, `:m:language:eng` (metadata), `:p:1` (program). Used by `-map`, `-c:`, `-b:`, `-metadata:`, etc.

**3. The fundamental choice: stream copy vs transcode.**
- `-c copy` → remux/cut with **no re-encode** (instant, lossless, but cuts land on keyframes only).
- omit / `-c:v libx264 -c:a aac` → **re-encode** (slow, lossy, frame-accurate, enables filters).
- You **cannot** apply filters to a copied stream.

**4. Quality knobs (re-encoding).**
- **CRF** (constant quality, 1-pass): `-crf 23` for x264/x265 (lower = better, ~18–28 sane). Preferred default.
- **Bitrate** (target size): `-b:v 4M`; add `-maxrate`/`-bufsize` for caps; 2-pass for streaming targets.
- **Preset**: `-preset slow` trades CPU for compression (x264/x265: ultrafast…placebo).

**5. Filtering.**
- `-vf` / `-af` = simple linear filtergraph (one input→one output, single stream).
- `-filter_complex` = multi-input/multi-output graphs; reference pads with `[label]`. Required for overlay, concat of differing streams, mixing, split.
- Graph syntax: `filter=arg=val:arg2=val2, next`. Chains separated by `,`; parallel chains by `;`.

**6. `-ss` placement.** Before `-i` = fast input seek (keyframe-snapped, very fast). After `-i` (output opt) = slow decode-then-discard but exact. With `-c copy`, cuts snap to keyframes regardless.

**7. Diagnose with ffprobe.** `ffprobe -v error -show_streams -show_format in.mp4`. Add `-of json`/`-of csv` for machine output. ffplay for quick visual check (`ffplay -vf ... in`).

---

## Chapter Index

| # | File | Covers |
|---|------|--------|
| 01 | [ch01-cli-tools](chapters/ch01-cli-tools.md) | ffmpeg/ffplay/ffprobe invocation, option ordering, loglevel |
| 02 | [ch02-stream-selection-mapping](chapters/ch02-stream-selection-mapping.md) | stream specifiers, automatic selection, `-map` |
| 03 | [ch03-options-reference](chapters/ch03-options-reference.md) | main/video/audio/subtitle/advanced options |
| 04 | [ch04-codecs](chapters/ch04-codecs.md) | encoders/decoders, libx264/265, NVENC, aac, mp3 options |
| 05 | [ch05-formats](chapters/ch05-formats.md) | muxers/demuxers: mp4, matroska, hls, dash, segment, concat, image2 |
| 06 | [ch06-filters](chapters/ch06-filters.md) | filtergraph syntax, key video/audio filters, hw filters |
| 07 | [ch07-protocols](chapters/ch07-protocols.md) | file, pipe, http(s), tcp/udp, rtmp, rtp, srt, tee |
| 08 | [ch08-devices](chapters/ch08-devices.md) | capture/output: gdigrab, dshow, x11grab, v4l2, avfoundation |
| 09 | [ch09-utils-scaler-resampler](chapters/ch09-utils-scaler-resampler.md) | syntax (time/eval/color), swscale, swresample options |
| 10 | [ch10-libraries-general](chapters/ch10-libraries-general.md) | libav* overview, supported formats, platform notes, FAQ |

## Topic Index

- **trim / cut / seek** → ch01, ch03, [patterns](patterns.md)
- **stream copy / remux** → ch02, ch04, [cheatsheet](cheatsheet.md)
- **map / stream selection** → ch02
- **CRF / bitrate / 2-pass / preset** → ch04
- **x264 / x265 / hevc / NVENC / QSV / VAAPI** → ch04, ch06
- **aac / mp3 / opus / audio bitrate** → ch04
- **scale / crop / pad / fps / pix_fmt / format** → ch06
- **overlay / concat / split / xfade / hstack** → ch06, patterns
- **drawtext / subtitles / burn-in** → ch06, patterns
- **amix / amerge / pan / volume / loudnorm** → ch06
- **HLS / DASH / segment / live streaming** → ch05, ch07, patterns
- **rtmp / srt / udp / tee / piping** → ch07, patterns
- **screen capture / webcam / record** → ch08, patterns
- **images ↔ video / thumbnails / gif** → ch05, ch06, patterns
- **ffprobe / inspect / metadata** → ch01, ch03

## Supporting Files

- [cheatsheet.md](cheatsheet.md) — copy-paste commands for the 90% cases
- [patterns.md](patterns.md) — task recipes with the *why* and trade-offs
- [glossary.md](glossary.md) — terms, options, and acronyms

---

## Scope & Limits

Distilled from the official docs; for the exhaustive per-filter / per-encoder option list, grep the chapter files or the bundled [reference/FFmpeg-Complete-Documentation.md](reference/FFmpeg-Complete-Documentation.md). Option availability depends on how the local FFmpeg build was compiled (`ffmpeg -encoders`, `-filters`, `-protocols`, `-buildconf` to verify). Hardware-accel paths depend on drivers/OS.
