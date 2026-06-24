# Chapter 9: Utilities, Scaler (swscale) & Resampler (swresample)

## Core Idea
Shared syntax conventions (time, eval, color, size) appear across every component, and two libraries do the heavy lifting under filters: swscale (video scale + pixel-format) and swresample (audio rate/format/layout).

## Key Concepts
- **Time syntax**: `[-][HH:]MM:SS[.m...]` or seconds `S[.m]`; used by `-ss`/`-t`/`-to`, `enable=`, etc.
- **Date/size/ratio**: sizes `WxH` or named (`hd1080`, `vga`); aspect `4:3`/`1.333`.
- **Color syntax**: names (`white`, `red`) or `0xRRGGBB[AA]` / `#RRGGBB@alpha` for drawtext/pad/color source.
- **Eval / expressions**: filters accept expressions over vars like `t`, `n`, `w/h`, `iw/ih`, `PTS`; functions `between()`, `gte()`, `mod()`, `if()`, `lerp()`.
- **swscale options** (`-sws_flags` or `scale=...:flags=`): `bilinear`, `bicubic`, `lanczos`, `neighbor`, `spline`; plus `-sws_dither`.
- **swresample options**: `-ar` (sample rate), `-ac`/`-channel_layout`, `aresample`, `-resampler soxr`, dithering for bit-depth reduction.

## Mental Models
- **One syntax to learn**: time/color/size formats are uniform — learn once, reuse everywhere.
- **scale flags = quality vs speed**: `lanczos` for sharp downscale, `bilinear` for speed.
- **swresample is implicit** whenever you change `-ar`/`-ac` or pixel/sample formats mismatch.

## Anti-patterns
- **Downscaling with `neighbor`/`bilinear`**: soft/aliased; prefer `lanczos`/`spline`.
- **Reducing bit depth without dither**: banding; enable dither in swresample/swscale.
- **Ignoring channel layout**: stereo→5.1 or downmix without `pan`/layout gives wrong mapping.

## Code Examples
```bash
ffmpeg -i in.mp4 -vf "scale=1280:-2:flags=lanczos" out.mp4
ffmpeg -i in.wav -ar 48000 -ac 2 -af aresample=resampler=soxr out.flac
ffmpeg -i in.mp4 -vf "scale=640:-2,format=yuv420p" -sws_dither ed out.mp4
```

## Reference Tables
| swscale flag | Use |
|--------------|-----|
| `lanczos` | sharp downscale (default choice) |
| `bicubic` | general purpose |
| `bilinear` | fast/preview |
| `neighbor` | pixel art / no smoothing |

## Key Takeaways
1. Time, color, size, and expression syntaxes are uniform across all components.
2. `flags=lanczos` for quality downscales; bilinear only for speed.
3. Changing `-ar`/`-ac` invokes swresample; use `soxr` + dither for quality.
4. Use eval expressions (`t`, `n`, `between()`) for dynamic/timed filter behavior.

## Connects To
- **Ch06**: scale/format/aresample filters are these libraries' front-ends.
- **Ch03**: `-ar`/`-ac`/`-pix_fmt` options drive these conversions.
