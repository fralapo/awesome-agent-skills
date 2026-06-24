# Chapter 6: Filters & Filtergraphs

## Core Idea
Filters transform frames. `-vf`/`-af` build a single linear chain on one stream; `-filter_complex` builds arbitrary multi-input/multi-output graphs. Syntax precision matters: commas chain, semicolons branch, `[labels]` wire pads.

## Frameworks Introduced
- **Filtergraph grammar**: `[in] filter=k=v:k2=v2, filter2 [out]`. `,` = chain within one path; `;` = separate parallel chains; `[name]` = named pad to connect chains.
- **Simple vs complex**: `-vf`/`-af` = 1 in, 1 out, implicit stream. `-filter_complex` = name inputs (`[0:v]`), produce labels (`[v]`), then `-map "[v]"`.
- **framesync options** (multi-input filters like overlay): `eof_action`, `shortest`, `repeatlast`.
- **Timeline editing**: gate a filter by time with `enable=between(t,5,10)`.

## Key Concepts — high-value filters
- **Geometry**: `scale=w:h[:flags=lanczos]`, `crop=w:h:x:y`, `pad`, `transpose`, `hflip`/`vflip`, `rotate`, `setsar`/`setdar`.
- **Rate/format**: `fps=30`, `format=yuv420p`, `setpts`/`atempo` (speed), `framerate` (interp).
- **Compositing**: `overlay=x:y`, `hstack`/`vstack`/`xstack`, `split`, `blend`, `chromakey`, `colorkey`.
- **Text/marks**: `drawtext=text=...:x:y:fontsize:fontcolor`, `drawbox`, `subtitles=f.srt`, `ass=f.ass`.
- **Color**: `eq`, `curves`, `colorbalance`, `hue`, `lut3d`, `colorspace`, `tonemap`.
- **Transitions**: `xfade=transition=fade:duration=1:offset=4` (video), `acrossfade` (audio).
- **Audio**: `volume`, `loudnorm`, `aresample`, `aformat`, `amix`, `amerge`, `pan`, `atempo`, `highpass`/`lowpass`, `silenceremove`.
- **Hardware**: `scale_cuda`/`scale_npp`, `scale_qsv`, `scale_vaapi`, `hwupload`/`hwdownload`, `*_opencl`, `*_vulkan`.

## Mental Models
- **overlay/concat/mix REQUIRE `-filter_complex`** (multiple inputs) — `-vf` cannot.
- **`-2` over `-1`** in scale to keep even dimensions for yuv420p.
- **split then process then recombine** for picture-in-picture or A/B effects.

## Anti-patterns
- **`-vf` with two inputs**: silently wrong/erroring; use `-filter_complex`.
- **Filtering a `-c copy` stream**: impossible — filtering forces a re-encode.
- **Odd dimensions from `scale=-1`**: encoder fails; use `-2`.
- **`amix` then surprised by quiet output**: it averages; boost with `volume`.

## Code Examples
```bash
# Picture-in-picture (scale overlay to 1/4, top-right):
ffmpeg -i main.mp4 -i pip.mp4 -filter_complex "[1:v]scale=iw/4:-2[s];[0:v][s]overlay=W-w-10:10" out.mp4
# Crossfade two clips:
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "[0][1]xfade=transition=fade:duration=1:offset=4,format=yuv420p" out.mp4
# Timecode/text with timeline gate:
ffmpeg -i in.mp4 -vf "drawtext=text='LIVE':x=20:y=20:fontsize=48:fontcolor=red:enable='gt(mod(t,2),1)'" out.mp4
```

## Reference Tables
| Task | Filter |
|------|--------|
| Resize keep aspect | `scale=1280:-2` |
| Crop region | `crop=w:h:x:y` |
| Watermark | `overlay=x:y` |
| Burn subs | `subtitles=f.srt` |
| Side-by-side | `hstack` |
| Normalize loudness | `loudnorm` |
| Speed up 2x video | `setpts=0.5*PTS` |
| Speed up 2x audio | `atempo=2.0` |

## Key Takeaways
1. `,` chains, `;` branches, `[label]` wires — get the punctuation right.
2. Multi-input work (overlay/concat/mix/stack) needs `-filter_complex` + `-map "[out]"`.
3. Filtering implies re-encoding; you cannot filter a copied stream.
4. Use `scale=...:-2` and `format=yuv420p` for compatible output.

## Connects To
- **Ch04**: filtered frames feed the encoder; hw filters pair with hw encoders.
- **Ch09**: scale/format internals live in swscale; resample in swresample.
