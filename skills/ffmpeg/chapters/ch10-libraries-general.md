# Chapter 10: Libraries & General Documentation

## Core Idea
The CLI tools are thin wrappers over the libav* libraries. The general docs (supported formats, platform notes, FAQ) tell you what your build can do and how to operate it correctly.

## Key Concepts
- **Library stack**: `libavutil` (helpers/math/pixfmt), `libavcodec` (encode/decode), `libavformat` (mux/demux + protocols), `libavfilter` (filtergraphs), `libavdevice` (capture/playback), `libswscale` (scale/pixfmt), `libswresample` (audio convert).
- **Capability discovery**: `ffmpeg -version`, `-buildconf`, `-formats`, `-codecs`, `-encoders`, `-decoders`, `-filters`, `-protocols`, `-pix_fmts`, `-hwaccels`.
- **External libraries**: features depend on compile-time `--enable-*` (libx264, libx265, libvpx, libaom, libfdk_aac, libopus, libass, fontconfig, etc.). `general` doc lists supported formats/codecs.
- **Platform notes**: Windows/macOS/Linux build + runtime specifics (paths, device backends, threading).
- **FAQ themes**: why a codec is missing (build flags), licensing (GPL vs LGPL, nonfree fdk-aac), seeking accuracy, concat, A/V sync.

## Mental Models
- **"It depends on the build"**: a missing encoder/filter usually means it was not compiled in — check `-buildconf`.
- **CLI options map to AVOptions** on the underlying libav* objects; the same names appear in the C API.
- **Licensing gates features**: `--enable-gpl`/`--enable-nonfree` change what binaries you can redistribute.

## Anti-patterns
- **Assuming a feature exists**: always verify with `-encoders`/`-filters` on the actual binary.
- **Mixing GPL/nonfree builds in distribution**: legal issue (e.g. libfdk_aac is nonfree).
- **Reporting "ffmpeg can't X" without checking build**: most "missing" features are just disabled flags.

## Code Examples
```bash
ffmpeg -version            # version + config summary
ffmpeg -buildconf          # exact compile flags
ffmpeg -hwaccels           # available hardware accel methods
ffmpeg -codecs | grep -i hevc
ffmpeg -filters | grep -i scale
```

## Reference Tables
| Library | Responsibility |
|---------|----------------|
| libavcodec | encoders/decoders |
| libavformat | muxers/demuxers/protocols |
| libavfilter | filters/filtergraphs |
| libavdevice | capture/playback devices |
| libswscale | video scale + pixel format |
| libswresample | audio resample/format/layout |
| libavutil | shared utilities |

## Key Takeaways
1. CLI behavior is defined by the libav* libraries and the build's enabled features.
2. Discover capabilities with `-buildconf`, `-encoders`, `-filters`, `-protocols`, `-hwaccels`.
3. Many "missing" features are just compile flags (libx264, libfdk_aac, libass).
4. Licensing (GPL/nonfree) constrains redistributable builds.

## Connects To
- **Ch04/Ch05/Ch06/Ch07/Ch08**: each maps to one libav* library.
- **Ch01**: discovery commands run through the same tools.
