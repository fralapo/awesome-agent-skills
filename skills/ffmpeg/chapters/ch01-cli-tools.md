# Chapter 1: Command-Line Tools (ffmpeg, ffplay, ffprobe)

## Core Idea
Three tools share one option grammar: `ffmpeg` converts, `ffplay` previews, `ffprobe` inspects. Mastering option *placement* and stream specifiers is 80% of using them.

## Key Concepts
- **ffmpeg**: `ffmpeg [global] {[in_opts] -i IN}... {[out_opts] OUT}...` — options bind to the *next* file.
- **ffplay**: minimal SDL player; `ffplay -vf eq=brightness=0.1 in.mp4`, `-loop`, `-autoexit`, `-fs`.
- **ffprobe**: structured inspection; `-show_streams`, `-show_format`, `-show_packets`, `-show_frames`, `-of json|csv|flat|xml`.
- **Global options**: `-y` (overwrite), `-n` (never overwrite), `-loglevel`/`-v` (quiet|error|warning|info|verbose|debug), `-hide_banner`, `-stats`, `-nostdin`.

## Mental Models
- Think of the command as a **pipeline of files**, not flags: each `-i` opens an input context, each output URL closes one. Options are sticky to the next context.
- Use **ffprobe before ffmpeg**: confirm codec/resolution/fps/duration so you pick the right `-c`, `-vf scale`, `-r`.
- `ffplay` is your **fast feedback loop** for filter tuning before committing to a slow encode.

## Anti-patterns
- **Putting input options after `-i`**: `-r 30 -i in` (input rate) vs `-i in -r 30` (output rate) behave differently. Know which you want.
- **Forgetting `-hide_banner`/`-loglevel error`** in scripts: noisy logs hide real errors.
- **Parsing human log output**: use `ffprobe -of json` for automation, never scrape stderr.

## Commands & APIs
```bash
ffmpeg -hide_banner -loglevel error -stats -i in.mov out.mp4
ffprobe -v error -show_streams -show_format -of json in.mp4
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height,r_frame_rate -of csv=p=0 in.mp4
ffplay -autoexit -vf "scale=1280:-2" in.mp4
ffmpeg -encoders | grep 264   # what your build supports
ffmpeg -buildconf            # compile-time options
```

## Key Takeaways
1. Option order encodes meaning — input opts before `-i`, output opts before the output URL.
2. `ffprobe -of json` is the contract for scripts; never parse pretty logs.
3. `-loglevel error -stats` is the right verbosity for batch jobs.
4. Verify your build (`-encoders`, `-filters`, `-protocols`) before assuming a feature exists.

## Connects To
- **Ch02**: stream specifiers used across all three tools.
- **Ch03**: the full option catalog.
