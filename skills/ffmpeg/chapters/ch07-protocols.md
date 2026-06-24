# Chapter 7: Protocols (I/O transports)

## Core Idea
The URL scheme picks a protocol for reading inputs and writing outputs: local files, pipes, and network transports (http, tcp, udp, rtmp, rtp, srt) plus the multi-output `tee`.

## Key Concepts
- **file / pipe**: `file:in.mp4`, `-` or `pipe:1` for stdout, `pipe:0` for stdin. Pair with `-f` to declare format on a pipe.
- **http(s)**: read remote inputs; options `-headers`, `-user_agent`, `-reconnect 1 -reconnect_streamed 1`.
- **tcp / udp**: low-level; `udp://host:port?pkt_size=1316&buffer_size=...`, `tcp://...?listen=1`.
- **rtmp / rtmps**: classic live ingest `rtmp://host/app/streamkey` (use `-f flv`).
- **rtp / rtsp**: real-time transport; `-f rtp`, SDP handling.
- **srt**: modern reliable UDP `srt://host:port?mode=caller|listener&latency=...` (use `-f mpegts`).
- **tee**: fan-out one encode to many sinks `-f tee "[f=flv]rtmp://...|[f=hls]out.m3u8"`.

## Mental Models
- **Scheme = transport, `-f` = container**: streaming nearly always needs both (e.g. `-f flv rtmp://`, `-f mpegts srt://`).
- **`-re` belongs with streaming a file**: paces reading to realtime so the server is not flooded.
- **tee avoids double-encoding**: encode once, mux to several outputs.

## Anti-patterns
- **rtmp without `-f flv`** / **srt without `-f mpegts`**: muxer mismatch → failure.
- **Streaming a file without `-re`**: blasts the whole file instantly, breaking live timing.
- **No `-reconnect` on flaky http**: long pulls die on transient errors.

## Code Examples
```bash
# Pipe ffmpeg into ffmpeg:
ffmpeg -i in.mp4 -f matroska - | ffmpeg -i - -c copy out.mkv
# Stream a file to RTMP in realtime:
ffmpeg -re -i in.mp4 -c:v libx264 -preset veryfast -c:a aac -f flv rtmp://host/app/key
# Reliable SRT push:
ffmpeg -re -i in.mp4 -c:v libx264 -c:a aac -f mpegts "srt://host:9000?mode=caller&latency=200000"
# One encode, two destinations:
ffmpeg -i in.mp4 -c:v libx264 -c:a aac -f tee "[f=flv]rtmp://a/live/k|[f=hls:hls_time=6]out.m3u8"
```

## Reference Tables
| Scheme | Pair with `-f` | Use |
|--------|----------------|-----|
| `rtmp://` | flv | classic live ingest |
| `srt://` | mpegts | reliable internet contribution |
| `udp://` | mpegts | LAN low-latency |
| `http(s)://` | (input) | remote pull |
| `pipe:`/`-` | explicit | chaining processes |

## Key Takeaways
1. URL scheme selects the protocol; streaming needs a matching `-f` container.
2. Use `-re` when streaming files so output is paced to realtime.
3. `tee` sends a single encode to multiple sinks — no re-encode tax.
4. Add `-reconnect` for resilient HTTP input.

## Connects To
- **Ch05**: containers carried over these transports (flv, mpegts, hls).
- **Ch08**: capture devices are inputs; protocols are the outputs.
