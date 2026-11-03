# Rendering and export, including social formats (lesson 15)

## Concepts
- Compression makes files small enough to store, stream and play. A **codec** compresses and decompresses the video, and no single codec suits every job: animation and live action compress differently.
- Pick the codec for the destination: web or social, an editing intermediate, or alpha overlays.
- **Render Settings** control *what* gets rendered: quality, resolution, time span, motion blur, frame blending, bit depth.
- **Output Module** settings control *how* it is written: format, codec, channels/alpha, resize, crop, audio.
- Save both as **templates** for repeated deliveries (draft for review, final for the web, alpha master).

## EffectCraft render queue (verified)
```
command_run renderQueue.add {comp, format:"h264", output:"/abs/path/name.mp4",
                             timeSpan:"comp"|"workArea"|"custom", start?, end?,
                             quality?, resolution?, bitrate?, audio?}
command_run renderQueue.render {wait:true}
command_run renderQueue.list            # status: Done, render_time, last_output
```
- The verified test was a 1080×1920, 30 fps, 1 s H.264 file: 30 frames, ffprobe OK, ~12 s on CPU in headless mode. The default output module is "H.264 – Match Render Settings – 15 Mbps".
- Formats (`renderQueue.formats`): h264, hevc, av1, prores (proxy…4444xq, with alpha), webm (vp9/av1, with alpha), gif, png/jpeg/tiff/exr/tga sequences, wav, aiff.
- Templates:
  - `renderQueue.saveTemplate {kind: renderSettings|outputModule, name, params}`;
  - `renderQueue.applyTemplate`, `renderQueue.setTemplateDefault`, `renderQueue.templates`.
- Editing a queued item: `renderQueue.setRenderSettings`, `renderQueue.setOutputModule`, `renderQueue.setOutput`, `renderQueue.duplicate`.
- Several outputs from one render: `render.addOutputModule`.
- A single still: `render_frame {time, path}` (PNG) or `comp.saveFrameAs`. For a layered PSD frame: `comp.saveFrameAsPsd`.
- Lottie for web or app animations: `file.exportLottie {comp, path:.json|.lottie, includeExpressions?, textAsShapes?}` (verified). The warnings list what is dropped: 3D, cameras, lights, most effects, Wiggle Paths, Puppet. Keep Lottie comps to 2D shapes, text, masks and transforms.
- **Missing:** Adobe Media Encoder. The render queue covers its role, and there is no separate encoder queue. Animated GIF goes through `format:"gif"`.

## Social specs (practical defaults)
| Use | Comp size | fps | Output |
|---|---|---|---|
| Reels / Stories / TikTok / Shorts (9:16) | 1080×1920 | 30 (or 25 for PAL footage) | H.264 high profile, 10–20 Mbps, AAC 48 kHz |
| Feed square (1:1) | 1080×1080 | 30 | H.264 8–15 Mbps |
| Feed portrait (4:5) | 1080×1350 | 30 | H.264 8–15 Mbps |
| YouTube / web landscape (16:9) | 1920×1080 (or 3840×2160) | 24/25/30 | H.264 or HEVC 15–40 Mbps |
| Overlay with transparency | any | match | ProRes 4444 or WebM VP9 with `channels:"rgba"` |

- Safe areas on 9:16: keep text out of roughly the top 250 px and bottom 350–400 px (platform UI), and away from the right edge where the buttons sit.
- One master, many sizes: build the master comp, then nest it in 9:16, 1:1 and 16:9 comps and reposition or scale per format, rather than re-animating. Or use `comp.scale` / `comp.cropToRegionOfInterest`.
- Short loops: make the last frame match the first. Check with `render_frame` at 0 and at duration − 1 frame.

## Pre-flight before delivery
1. `get_comp`: size, fps and duration are right. The work area covers the full piece (or use `timeSpan:"comp"`).
2. `render_frame` at 4–6 times, including the first and last frames and each key transition.
3. Motion blur is on at both the layer and comp level, if you used it.
4. No guide layers or stray solo/disabled layers are left (`layer.setSwitch`).
5. Render, then probe the file (ffprobe: codec, size, frame count, audio stream).
6. Deliver the file to the location the user asked for and report its path.

> Availability notes in this file are a snapshot as of 2026-11-03. ArtCraft apps update almost daily: re-check the live command catalogue before treating anything as missing.
