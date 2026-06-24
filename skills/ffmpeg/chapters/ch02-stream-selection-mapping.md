# Chapter 2: Stream Selection & Mapping

## Core Idea
By default ffmpeg auto-picks one stream per type (best video, best audio, etc.). `-map` overrides this to choose exactly which inputs/streams flow into each output.

## Frameworks Introduced
- **Stream specifier**: `stream_type[:index]` or richer forms. Types: `v`(video), `a`(audio), `s`(subtitle), `d`(data), `t`(attachments), `V`(video w/o thumbnails). Forms: `:0`, `v:0`, `p:program_id`, `m:key[:value]` (metadata), `#id` / `i:id` (stream id), `u` (usable).
  - When to use: any per-stream option — `-c:a:0`, `-b:v:1`, `-map`, `-metadata:s:a:0`.
- **Automatic selection**: without `-map`, picks single best stream per type by channel count/resolution. Disabled the moment you use any `-map`.
- **`-map` syntax**: `-map input:stream` (e.g. `-map 0:v:0 -map 1:a`), negative `-map -0:s` to exclude, `?` suffix `-map 0:a?` to ignore-if-absent, `[label]` to map a filter_complex output pad.

## Mental Models
- Think "**once you `-map`, you map everything you want**" — autoselect is off, nothing is implicit.
- Map order = output stream order; put video first for well-behaved players.
- Use `-map 0` to take ALL streams from input 0 (then refine with negatives).

## Anti-patterns
- **Mixing autoselect with manual intent**: expecting audio to "just come along" after `-map 0:v:0` — it will not.
- **Wrong index base**: streams are 0-based; `-map 0:1` is the *second* stream of input 0.
- **Copying incompatible streams into a container** (e.g. AC3 into a strict MP4 profile) — map is fine but the muxer rejects; transcode or pick a tolerant container.

## Code Examples
```bash
# Merge external audio with a video, keep both, copy:
ffmpeg -i video.mp4 -i music.m4a -map 0:v:0 -map 1:a:0 -c copy -shortest out.mp4
# Keep all streams but drop subtitles:
ffmpeg -i in.mkv -map 0 -map -0:s -c copy out.mkv
# Pick English audio by metadata:
ffmpeg -i in.mkv -map 0:v -map 0:m:language:eng -c copy out.mkv
```

## Reference Tables
| Specifier | Selects |
|-----------|---------|
| `v:0` | first video stream |
| `a:1` | second audio stream |
| `0:a` | all audio of input 0 |
| `m:language:eng` | streams tagged English |
| `-0:s` | exclude all subtitles |
| `0:a?` | audio of input 0, ok if none |

## Key Takeaways
1. No `-map` = one best stream per type, automatically.
2. Any `-map` turns autoselect off — be explicit about every output stream.
3. `-map 0` + negative maps = "everything except X".
4. `?` makes a map optional; metadata maps select by language/title.

## Connects To
- **Ch03**: per-stream options use the same specifiers.
- **Ch06**: `-filter_complex` output pads are mapped with `[label]`.
