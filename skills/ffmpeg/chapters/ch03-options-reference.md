# Chapter 3: Options Reference (main, video, audio, subtitle, advanced)

## Core Idea
ffmpeg has a large but patterned option set: generic per-file controls, per-type knobs selected by stream specifier, and AVOptions passed straight to codecs/filters/muxers.

## Key Concepts (most-used options)
- **Timing**: `-ss` (seek), `-t` (duration), `-to` (end), `-itsoffset` (shift input ts), `-ss` placement matters (pre-`-i` fast, post-`-i` exact).
- **Codec**: `-c[:spec] name|copy` (`-c:v`, `-c:a`, `-c:s`), `-c copy` for all.
- **Video**: `-r` (fps), `-s WxH` (size, prefer `scale` filter), `-pix_fmt`, `-aspect`, `-vframes`/`-frames:v`, `-vn` (no video), `-g` (GOP).
- **Audio**: `-b:a` (bitrate), `-ar` (sample rate), `-ac` (channels), `-an` (no audio), `-q:a` (VBR quality for lame).
- **Bitrate/quality**: `-b:v`, `-crf`, `-qscale`/`-q:v`, `-maxrate`, `-bufsize`, `-minrate`, `-pass`, `-passlogfile`.
- **Metadata/disposition**: `-metadata key=val`, `-metadata:s:a:0 language=eng`, `-disposition:a:0 default`, `-map_metadata`, `-map_chapters`.
- **Misc**: `-shortest` (end at shortest input), `-stream_loop N` (loop input), `-f fmt` (force format), `-threads`, `-filter_threads`.

## Mental Models
- **Per-type via specifier**: almost any option takes `:v`/`:a`/`:s[:idx]` to target a stream — `-b:a:0 128k -b:a:1 96k`.
- **AVOptions are opaque pass-through**: encoder-specific flags (e.g. `-preset`, `-tune`, `-x264-params`) are validated by the codec, not ffmpeg core.
- `-frames:v 1` is the idiom for "grab one image".

## Anti-patterns
- **`-s WxH` instead of the `scale` filter**: deprecated-ish, no aspect/algorithm control; use `-vf scale`.
- **Setting `-b:v` and expecting constant quality**: bitrate ≠ quality; use `-crf` unless you need a size target.
- **Forgetting `-pix_fmt yuv420p`** for web/QuickTime: many encoders default to 4:4:4/10-bit that players reject.

## Reference Tables
| Need | Option |
|------|--------|
| Constant quality | `-crf N` |
| Target bitrate | `-b:v`, 2-pass |
| No re-encode | `-c copy` |
| Drop a track | `-an` / `-vn` / `-sn` |
| End at shortest | `-shortest` |
| One frame out | `-frames:v 1` |
| Loop input | `-stream_loop -1` |

## Key Takeaways
1. Append a stream specifier to target options per stream (`-c:a:1`, `-b:v:0`).
2. Prefer `scale` filter over `-s`, `-crf` over `-b:v` unless sizing.
3. `-shortest`, `-stream_loop`, `-itsoffset` solve common sync/length issues.
4. Encoder-specific tuning rides in AVOptions (`-preset`, `-tune`, `-x265-params`).

## Connects To
- **Ch04**: codec-specific AVOptions live here.
- **Ch06**: filters replace many legacy options (`-s`, `-r`, aspect).
