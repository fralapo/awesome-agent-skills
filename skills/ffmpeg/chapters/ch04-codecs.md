# Chapter 4: Codecs — Encoders & Decoders

## Core Idea
`-c:v`/`-c:a` choose an encoder; the right rate-control + preset matter more than the codec name. x264/x265 via CRF is the workhorse; hardware encoders trade quality for speed.

## Frameworks Introduced
- **Rate control ladder**: CRF (constant quality) -> capped CRF (`-maxrate`/`-bufsize`) -> ABR 1-pass (`-b:v`) -> 2-pass (accurate size). Pick by whether you care about quality, a ceiling, or an exact size.
- **Encoder families**: software `libx264`/`libx265`/`libvpx-vp9`/`libaom-av1`/`libsvtav1`; hardware `*_nvenc` (NVIDIA), `*_qsv` (Intel), `*_vaapi` (Linux), `*_videotoolbox` (Apple).

## Key Concepts
- **libx264 options**: `-crf` (0-51, ~18-28), `-preset` (ultrafast..placebo), `-tune` (film/animation/grain/zerolatency/fastdecode), `-profile:v`, `-level`, `-x264-params`.
- **libx265**: same shape; `-crf ~28` default; `-tag:v hvc1` for Apple; `-x265-params`.
- **Audio encoders**: `aac` (`-b:a 128k-256k`), `libmp3lame` (`-q:a 0-9` VBR or `-b:a`), `libopus` (`-b:a 96k+`, best modern), `libvorbis`, `ac3`/`eac3`.
- **GOP/keyframes**: `-g` interval, `-keyint_min`, `-sc_threshold`, `-force_key_frames "expr:gte(t,n_forced*2)"` for segment alignment.

## Mental Models
- **CRF is the default brain**: set quality once, let bitrate float. Only move to 2-pass for size targets.
- **Preset = time budget**, not quality target: slower = smaller at same CRF, same visual quality.
- **Hardware encoders for speed/realtime**, software for archival/best compression.

## Anti-patterns
- **NVENC with CRF expectations**: nvenc uses `-cq`/`-rc vbr`, not `-crf`; quality-per-bit is lower than x264.
- **Tiny `-g` for VOD**: hurts compression; large GOP good for files, segment-aligned GOP for streaming.
- **AAC at 64k stereo**: audible artifacts; 128k+ for music.

## Code Examples
```bash
ffmpeg -i in.mov -c:v libx264 -crf 20 -preset slow -tune film -c:a aac -b:a 192k out.mp4
ffmpeg -i in.mp4 -c:v libx265 -crf 26 -preset medium -tag:v hvc1 -c:a libopus -b:a 128k out.mp4
ffmpeg -hwaccel cuda -i in.mp4 -c:v h264_nvenc -rc vbr -cq 23 -b:v 0 -c:a copy out.mp4   # NVENC
ffmpeg -i in.mp4 -c:v libx264 -b:v 4M -pass 1 -an -f null NUL && \
ffmpeg -i in.mp4 -c:v libx264 -b:v 4M -pass 2 -c:a aac out.mp4                          # 2-pass
```

## Reference Tables
| Goal | Encoder + control |
|------|-------------------|
| Best size/quality H.264 | `libx264 -crf 18-23 -preset slow` |
| Smaller, modern | `libx265 -crf 24-28` |
| Realtime / GPU | `h264_nvenc`/`h264_qsv` |
| Exact bitrate | `libx264 -b:v ... ` 2-pass |
| Transparent audio | `libopus -b:a 128k` or `aac 192k` |

## Key Takeaways
1. Default to `libx264 -crf -preset`; reach for 2-pass only for size targets.
2. Preset trades CPU for compression at constant quality.
3. Hardware encoders win on speed, lose on quality-per-bit.
4. Align GOP (`-g`/`-force_key_frames`) with segment duration for HLS/DASH.

## Connects To
- **Ch05**: muxer must accept the codec (e.g. hvc1 tag for MP4/HEVC).
- **Ch06**: hardware encode often pairs with hw scale/format filters.
