# Chapter 8: Devices (capture & playback)

## Core Idea
Devices are special inputs/outputs accessed via `-f <device>`: screen, webcam, microphone capture differ per OS. List capabilities first, then construct the input.

## Key Concepts
- **Windows**: `gdigrab` (screen: `-i desktop` or `-i title=Window`), `dshow` (cameras/mics: `-i video=...:audio=...`). List: `ffmpeg -list_devices true -f dshow -i dummy`.
- **Linux**: `x11grab` (screen `-i :0.0+x,y`), `v4l2` (webcam `-i /dev/video0`), `pulse`/`alsa` (audio). List v4l2: `v4l2-ctl --list-devices`.
- **macOS**: `avfoundation` (`-i "video:audio"`, e.g. `"1:0"`). List: `ffmpeg -f avfoundation -list_devices true -i ""`.
- **Common opts**: `-framerate`, `-video_size WxH`, `-pixel_format`, `-draw_mouse`, `-offset_x/-offset_y` (region).
- **Output devices**: `sdl` window output `-f sdl "title"`; mostly for preview.

## Mental Models
- **Enumerate before capturing**: device names/indices are host-specific and must match exactly.
- **Set capture `-framerate`/`-video_size` BEFORE `-i`** (they are input options).
- For realtime capture, **use a fast preset** (`-preset ultrafast`/`veryfast`) so encoding keeps up.

## Anti-patterns
- **Guessing the device name**: dshow/avfoundation names must be copied verbatim from the list command.
- **High CRF + slow preset on live capture**: drops frames; favor speed and bitrate caps.
- **Missing audio sync**: capture A/V together where possible, or use `-itsoffset` to align.

## Code Examples
```bash
# Windows: full screen + mic, 30 fps:
ffmpeg -f gdigrab -framerate 30 -i desktop -f dshow -i audio="Microphone (Realtek)" -c:v libx264 -preset veryfast -pix_fmt yuv420p out.mp4
# Windows: webcam via dshow:
ffmpeg -f dshow -i video="Integrated Camera" out.mp4
# Linux: screen region + audio:
ffmpeg -f x11grab -framerate 30 -video_size 1280x720 -i :0.0+100,100 -f pulse -i default out.mp4
# macOS: screen+mic:
ffmpeg -f avfoundation -framerate 30 -i "1:0" out.mp4
```

## Reference Tables
| OS | Screen | Camera | Audio |
|----|--------|--------|-------|
| Windows | gdigrab | dshow | dshow |
| Linux | x11grab | v4l2 | pulse/alsa |
| macOS | avfoundation | avfoundation | avfoundation |

## Key Takeaways
1. `-f <device>` + an OS-specific source string; list devices first.
2. Capture params (`-framerate`, `-video_size`) are input options — before `-i`.
3. Favor fast presets and bitrate caps for realtime capture.
4. Capture A/V together or align with `-itsoffset` to avoid drift.

## Connects To
- **Ch04**: realtime encoder preset choices.
- **Ch07**: pipe captured streams to rtmp/srt for live.
