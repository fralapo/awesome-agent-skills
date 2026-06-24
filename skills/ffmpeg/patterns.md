# FFmpeg Patterns — task recipes (the *why* + trade-offs)

## Stream copy vs transcode
**When**: any time you touch a file. **How**: try `-c copy` first; only re-encode if you must change codec, resolution, or apply filters. **Trade-off**: copy is instant + lossless but cuts snap to keyframes and you cannot filter; transcode is slow + lossy but frame-accurate.

## Frame-accurate trim
**When**: cut must start exactly. **How**: re-encode and put `-ss`/`-to` as needed; for copy-cuts accept keyframe snapping or force keyframes at encode time (`-force_key_frames`). **Trade-off**: accuracy costs a re-encode.

## Fast seek + accurate end
**When**: cut deep into a long file quickly but with an exact duration. **How**: `-ss` before `-i` (fast keyframe seek) + `-t DURATION` after. **Trade-off**: start snaps to a keyframe unless re-encoding.

## CRF encode (default quality target)
**When**: you want "looks good, smallest reasonable file". **How**: `-c:v libx264 -crf 23 -preset slow`. Lower CRF = bigger/better. **Trade-off**: unpredictable file size; not for fixed-bitrate delivery.

## 2-pass bitrate encode
**When**: target a specific size/bitrate (broadcast, upload caps). **How**: pass 1 `-pass 1 -an -f null NUL` (use `/dev/null` on Unix), pass 2 `-pass 2 -b:v 4M`. **Trade-off**: two encodes; deterministic size.

## Constrained quality for streaming (capped CRF)
**When**: VOD/ABR where you want CRF quality but a hard ceiling. **How**: `-crf 23 -maxrate 5M -bufsize 10M`. **Trade-off**: caps quality on busy scenes.

## Concat — pick the right method
**When**: join clips. **How**: identical codec+params then `concat` *demuxer* with `-c copy` (instant). Mixed params then `concat` *filter* (re-encode, normalizes). **Trade-off**: demuxer is fast but strict; filter is flexible but slow.

## Burn-in subtitles / text
**When**: hardcode captions or overlays. **How**: `-vf subtitles=subs.srt` (or `ass=...` for styled). drawtext for dynamic text/timecode. **Trade-off**: permanent, cannot toggle; for soft subs mux as a stream (`-c:s mov_text` / `srt`).

## Overlay / picture-in-picture / watermark
**When**: composite two videos/images. **How**: `-filter_complex "[0][1]overlay=x:y"`; position via `W,H` (main) and `w,h` (overlay) expressions. **Trade-off**: needs filter_complex; re-encode.

## Audio mix / replace
**When**: combine or swap audio. **How**: mix then `amix=inputs=2`; merge channels then `amerge`; map a separate track then `-map 0:v -map 1:a`. Normalize loudness then `loudnorm` (EBU R128). **Trade-off**: `amix` lowers volume by default (use `volume` to compensate).

## Web-ready MP4
**When**: deliver MP4 for browsers/social. **How**: `-c:v libx264 -pix_fmt yuv420p -movflags +faststart -c:a aac`. **Trade-off**: yuv420p loses chroma detail but is universally decodable; faststart enables progressive play.

## Hardware-accelerated encode
**When**: speed over max compression, or realtime. **How**: NVIDIA `-c:v h264_nvenc`; Intel `-c:v h264_qsv`; VAAPI (Linux) `-vaapi_device ... -c:v h264_vaapi`; macOS `-c:v h264_videotoolbox`. Add `-hwaccel` for decode. **Trade-off**: lower quality-per-bit than libx264; build/driver dependent.

## Images and video conversion
**When**: timelapse, frame export, slideshow. **How**: export `-vf fps=N out_%04d.png`; build `-framerate N -i in_%04d.png`; thumbnail `-ss T -frames:v 1`. **Trade-off**: PNG is lossless+large, JPG small+lossy.

## High-quality GIF (two-pass palette)
**When**: crisp GIF. **How**: `palettegen` then `paletteuse`:
`ffmpeg -i in.mp4 -vf "fps=12,scale=480:-1:flags=lanczos,palettegen" pal.png` then `-i in.mp4 -i pal.png -lavfi "fps=12,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" out.gif`. **Trade-off**: two steps; far better than single-pass.

## Live restream / ingest
**When**: push to RTMP/SRT or pull and re-mux. **How**: `-re` to read at native rate when streaming files; output `-f flv rtmp://...` or `-f mpegts srt://...`. Use `tee` muxer to send to several sinks at once. **Trade-off**: realtime; encoder preset must keep up (`veryfast`).

## HLS / DASH packaging
**When**: adaptive web delivery. **How**: HLS `-f hls -hls_time 6 -hls_playlist_type vod -hls_segment_filename`; DASH `-f dash`. Multiple renditions via multiple `-map`+`-b:v`. **Trade-off**: many files; align GOP to segment length (`-g`, `-force_key_frames`).

## Robust scaling
**When**: resize without artifacts/odd dimensions. **How**: `scale=w:-2` keeps aspect with even height (required by yuv420p); `flags=lanczos` for downscale sharpness; `pad`/`crop` to fit exact canvas. **Trade-off**: `-1` can yield odd numbers then encoder errors; prefer `-2`.
