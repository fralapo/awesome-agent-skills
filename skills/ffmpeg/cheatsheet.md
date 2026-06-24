# FFmpeg Cheatsheet — the 90% commands

> Replace `in.mp4`/`out.mp4` as needed. `-y` overwrites without asking.

## Inspect
```bash
ffprobe -v error -show_format -show_streams in.mp4
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,codec_name -of csv=p=0 in.mp4
ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 in.mp4   # duration in seconds
```

## Remux / stream copy (no re-encode, instant)
```bash
ffmpeg -i in.mkv -c copy out.mp4              # change container only
ffmpeg -i in.mp4 -c copy -an out.mp4          # drop audio
ffmpeg -i in.mp4 -c:v copy -c:a aac out.mp4   # keep video, re-encode audio
```

## Trim / cut
```bash
ffmpeg -ss 00:01:30 -to 00:02:00 -i in.mp4 -c copy out.mp4   # fast, keyframe-snapped
ffmpeg -ss 00:01:30 -to 00:02:00 -i in.mp4 out.mp4           # re-encode, frame-accurate
ffmpeg -i in.mp4 -ss 90 -t 30 -c copy out.mp4                # start 90s, length 30s
```

## Transcode (sane defaults)
```bash
ffmpeg -i in.mov -c:v libx264 -crf 23 -preset slow -c:a aac -b:a 192k -movflags +faststart out.mp4
ffmpeg -i in.mp4 -c:v libx265 -crf 28 -c:a aac -b:a 128k -tag:v hvc1 out.mp4   # HEVC (Apple-friendly tag)
```
`-movflags +faststart` = moves moov atom to front for web/streaming playback.

## Resize / fps / pixel format
```bash
ffmpeg -i in.mp4 -vf "scale=1280:-2" out.mp4          # 720p, keep aspect, even height
ffmpeg -i in.mp4 -vf "scale=-2:1080" out.mp4
ffmpeg -i in.mp4 -r 30 out.mp4                         # set output fps (dup/drop)
ffmpeg -i in.mp4 -vf fps=30 out.mp4                    # fps via filter
ffmpeg -i in.mp4 -pix_fmt yuv420p out.mp4             # max compatibility
```

## Audio
```bash
ffmpeg -i in.mp4 -vn -c:a libmp3lame -q:a 2 out.mp3   # extract to MP3 (VBR ~190k)
ffmpeg -i in.wav -c:a aac -b:a 192k out.m4a
ffmpeg -i in.mp4 -af "volume=2.0" out.mp4             # double volume
ffmpeg -i in.mp4 -af loudnorm out.mp4                 # EBU R128 normalize
ffmpeg -i in.mp4 -ar 44100 -ac 2 out.mp4             # 44.1kHz stereo
```

## Concatenate
```bash
# Same codec/params -> demuxer, no re-encode:
printf "file '%s'\n" a.mp4 b.mp4 c.mp4 > list.txt
ffmpeg -f concat -safe 0 -i list.txt -c copy out.mp4
# Different params -> concat filter (re-encode):
ffmpeg -i a.mp4 -i b.mp4 -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" out.mp4
```

## Images / GIF / thumbnails
```bash
ffmpeg -i in.mp4 -vf fps=1 frame_%04d.png                       # 1 frame/sec
ffmpeg -ss 5 -i in.mp4 -frames:v 1 thumb.jpg                    # single thumbnail at 5s
ffmpeg -framerate 24 -i frame_%04d.png -c:v libx264 -pix_fmt yuv420p out.mp4   # images->video
ffmpeg -i in.mp4 -vf "fps=12,scale=480:-1:flags=lanczos" -loop 0 out.gif       # quick GIF
```

## Overlay / watermark / text
```bash
ffmpeg -i in.mp4 -i logo.png -filter_complex "overlay=W-w-10:H-h-10" out.mp4   # bottom-right
ffmpeg -i in.mp4 -vf "drawtext=text='Hello':x=20:y=20:fontsize=36:fontcolor=white" out.mp4
ffmpeg -i in.mp4 -vf "subtitles=subs.srt" out.mp4              # burn-in subtitles
```

## Capture (record)
```bash
# Windows screen + audio:
ffmpeg -f gdigrab -framerate 30 -i desktop -f dshow -i audio="Microphone" out.mp4
# Linux:  ffmpeg -f x11grab -framerate 30 -i :0.0 -f pulse -i default out.mp4
# macOS:  ffmpeg -f avfoundation -framerate 30 -i "1:0" out.mp4
```

## Stream out
```bash
ffmpeg -re -i in.mp4 -c:v libx264 -preset veryfast -c:a aac -f flv rtmp://host/app/key
ffmpeg -i in.mp4 -c:v libx264 -c:a aac -f hls -hls_time 6 -hls_playlist_type vod out.m3u8
```

## Decision quick-table
| Goal | Reach for |
|------|-----------|
| Fastest, lossless container/cut | `-c copy` |
| Best quality/size, 1 pass | `-crf` + `-preset` |
| Exact file size / streaming bitrate | 2-pass `-b:v` |
| Multi-input (overlay/concat/mix) | `-filter_complex` |
| Single-stream effect | `-vf` / `-af` |
| Web MP4 | `-pix_fmt yuv420p -movflags +faststart` |
