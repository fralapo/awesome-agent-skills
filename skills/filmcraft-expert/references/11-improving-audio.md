# 11 — Improving audio (Lesson 11)

Summary in my own words; Essential Sound commands verified.

## Concepts
- **Essential Sound** works by **audio type**: Dialogue, Music, SFX, Ambience. Each type exposes the relevant tools; settings are stored as ordinary effects on the clip (visible in effect controls).
- **Loudness auto-match** measures each clip and sets gain to a target (broadcast dialogue standard is −23 LUFS; LUFS = loudness units relative to full scale).
- **Repair**: noise reduction, rumble, hum removal (50 Hz in Europe, 60 Hz in the Americas), de-essing, reverb reduction. Push only as far as needed: too much makes voices watery.
- **Clarity**: dynamics (compression), EQ presets, speech enhancement.
- **Creative**: reverb, stereo width.
- **Parametric EQ**: bands with frequency, gain and Q (width); raise the range to allow bigger boosts/cuts. Low-cut around 80–100 Hz cleans voice rumble; small cuts in 200–400 Hz reduce muddiness; 3–5 kHz adds presence.
- **Notch filter**: very narrow cuts to remove a constant tone and its harmonics.
- Other tools: DeNoise, DeReverb, Click remover, Hard Limiter, Multiband compressor, Pitch shifter.

## FilmCraft
| Task | Command / effect id |
|---|---|
| Set type | `essentialSound.setType {clips, type:"dialogue"|"music"|"sfx"|"ambience"}` |
| Settings | `essentialSound.set {clips, key, value}` or `{values:{...}}`; keys seen: `repair.noise.on`, `repair.noise.amount`, `repair.humHz`, `clarity.eqPreset`, `creative.reverbPreset`, `ducking.reduceDb`, `volume.levelDb`, `mute` (`ducking.on` is **not** a key) |
| Inspect | `essentialSound.inspect {clips}` (lists presets, EQ/reverb presets, targets per type) |
| Presets | `essentialSound.applyPreset {preset:"Clean Up Noisy Dialogue"|"Podcast Voice"|"Duck Under Dialogue"…}` |
| Auto-match | `essentialSound.autoMatch {clips, target}`: defaults Dialogue −23, Music −25, SFX −21, Ambience −30 LUFS |
| Effects | `parametric_eq`, `notch`, `simple_notch`, `highpass`, `denoise`, `dehummer`, `dereverb`, `declicker`, `deesser`, `speech_enhance`, `vocal_enhancer`, `dynamics_rack`, `single_band_compressor`, `multiband_compressor`, `hard_limiter`, `loudness_radar`, `mastering`, `studio_reverb`, `convolution_reverb`, `pitch_shifter` |

## Recipe: talking head clean-up
1. `setType dialogue` → `autoMatch` → `set repair.noise.on true` (amount small) → if hum, `repair.humHz` 50.
2. If still boomy: `parametric_eq` low-cut ~90 Hz; if sibilant: `deesser`.
3. `hard_limiter` on the mix (max −1 dBTP) or rely on export `loudnessLufs`.
4. Listen-equivalent check for an agent: `clip.audioPeak`, `essentialSound.inspect` measured LUFS.

## SoundCraft threshold
Noise that changes over time, overlapping voices, spectral repairs (a phone ring, a cough), room matching between mics: export the dialogue and do it in SoundCraft, then bring back a bounced stem.
