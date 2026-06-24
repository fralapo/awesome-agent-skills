# Chapter 5: Formats — Muxers & Demuxers

## Core Idea
The container (format) is chosen by output extension or `-f`. Muxers accept only certain codecs and expose format-specific options (e.g. `-movflags`, `-hls_time`).

## Key Concepts
- **mp4 / mov (movenc)**: `-movflags +faststart` (web), `+frag_keyframe+empty_moov` (fragmented/streamable), `-brand`. H.264/AAC/HEVC(hvc1).
- **matroska (mkv)**: most permissive — almost any codec, subtitles, attachments, chapters.
- **hls**: `-hls_time`, `-hls_list_size`, `-hls_playlist_type vod|event`, `-hls_segment_filename`, `-hls_flags`, `-master_pl_name`.
- **dash**: `-seg_duration`, `-use_template`, `-adaptation_sets`.
- **segment**: generic chunker `-f segment -segment_time 10 -reset_timestamps 1 out_%03d.mp4`.
- **concat demuxer**: `-f concat -safe 0 -i list.txt` (lines: `file 'path'`).
- **image2**: image sequences `out_%04d.png`, `-start_number`, `-pattern_type glob`.
- **Raw/null**: `-f null -` (benchmark/pass1), `-f rawvideo`, `-f s16le` (raw PCM).

## Mental Models
- **Container is a contract**: pick one that accepts your codecs (mkv if unsure; mp4 for compatibility).
- **mp4 needs faststart** for progressive web playback (moov atom up front).
- For **cutting/segmenting without re-encode**, the segment muxer + `-c copy` snaps to keyframes.

## Anti-patterns
- **Muxing Opus/subtitles into strict MP4**: may fail; use mkv or convert.
- **Concat demuxer with mismatched params**: glitches/av-desync; use concat *filter* instead.
- **Forgetting `-reset_timestamps 1`** when segmenting → players mishandle later segments.

## Code Examples
```bash
ffmpeg -i in.mkv -c copy -movflags +faststart out.mp4
ffmpeg -i in.mp4 -c:v libx264 -c:a aac -f hls -hls_time 6 -hls_playlist_type vod -hls_segment_filename "seg_%03d.ts" out.m3u8
ffmpeg -i in.mp4 -c copy -f segment -segment_time 60 -reset_timestamps 1 part_%03d.mp4
printf "file '%s'\n" a.mp4 b.mp4 > list.txt && ffmpeg -f concat -safe 0 -i list.txt -c copy out.mp4
```

## Reference Tables
| Container | Use when | Notes |
|-----------|----------|-------|
| mp4 | max compatibility | `+faststart`; H264/HEVC/AAC |
| mkv | anything | permissive, subs/chapters |
| webm | web open codecs | VP9/AV1 + Opus |
| ts/mpegts | streaming/broadcast | concat-friendly |
| hls (.m3u8) | adaptive web | segments + playlist |

## Key Takeaways
1. Output extension or `-f` selects the muxer; muxers gate which codecs are legal.
2. `-movflags +faststart` is mandatory for web MP4.
3. concat demuxer = same params + copy; concat filter = mixed params + re-encode.
4. Use the segment muxer with `-reset_timestamps 1` for clean chunking.

## Connects To
- **Ch04**: codec/muxer compatibility (hvc1 tag, Opus-in-mp4).
- **Ch07**: HLS/DASH outputs often go over http/tee.
