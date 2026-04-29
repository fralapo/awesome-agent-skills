# Stable Diffusion (SD 1.5 / SDXL / SD3 / SD3.5)

Stability AI's open-source family. Self-host (ComfyUI, Automatic1111, Forge, Fooocus) or hosted APIs (StabilityAI, Replicate, fal.ai). Tag-weight grammar plus a dedicated negative-prompt slot.

## Tier

- **SD 1.5** = Standard (legacy)
- **SDXL 1.0** = Pro for photorealism era
- **SD3 / SD3.5** = current Pro for prompt adherence + text rendering (still weaker than GPT Image 2 for long copy)

## Syntax surface

Two distinct slots:

1. **Positive prompt** — comma-separated tags, weighted with parens: `(masterpiece:1.2), (8k:1.1)`
2. **Negative prompt** — separate input field (UI) or API param

```
positive: portrait photo, young woman, (sharp eyes:1.2), 85mm f/1.4, soft rim light, kodak portra 400, shallow depth of field, (natural skin texture:1.3)

negative: cartoon, lowres, jpeg artifacts, plastic skin, extra fingers, watermark, text, signature
```

### Weight syntax

| Notation | Effect |
|---|---|
| `(token:1.2)` | Boost weight (typical 1.05–1.4) |
| `(token:0.7)` | Damp |
| `[token]` | Mild damp (Auto1111 only) |
| `((token))` | Double-boost (legacy 1.5) |
| `<lora:name:0.8>` | LoRA load (workflow tools) |
| `<embedding:name>` | Textual inversion embedding |

Avoid > 1.5 weight — usually distorts.

### Sampler / scheduler / CFG (workflow params, not prompt)

- **CFG scale**: 4–7 typical for SDXL/SD3.5; lower = more creative, higher = more literal
- **Steps**: 25–40 for quality, 8–15 for SDXL Turbo / SD3.5 Turbo
- **Sampler**: `dpmpp_2m_karras`, `euler_a`, `dpmpp_3m_sde` are common defaults
- **Resolution**: SDXL trained at 1024², SD3 native ratios near 1MP

## Best-in-class for

- Open-source ecosystem — LoRAs, ControlNet, IP-Adapter, regional prompting, AnimateDiff
- Self-host privacy / on-device
- Granular composition control via ControlNet (depth, pose, canny, scribble, lineart)
- Style fine-tuning (LoRA training is community-standard)

## Weak points

- Long text in image (better on SD3.5 vs SDXL but still glitchy past short labels)
- Default aesthetic less polished than Midjourney
- Anatomy on SD 1.5 (hands, fingers) — improved on SDXL/SD3, never perfect
- CJK text — broken

## Reference-image workflows

Not in the prompt — at the workflow level:

- **IP-Adapter** — passes a reference image as a soft style/identity anchor; weight tunable
- **ControlNet** — pose / depth / canny / lineart from a reference
- **InstantID / PhotoMaker / PuLID** — stronger face-locking adapters
- **Reference-only ControlNet** — preserves composition without copying

In ComfyUI/Automatic1111 you select these as nodes/extensions; the prompt itself stays text-only.

## Anti-patterns

- Stuffing 50 boost terms with weights — model averages, signal flattens
- Putting `--ar 16:9` in the prompt (Midjourney syntax pollutes SD output as literal text)
- Negative prompt as a generic dump (`bad quality, low res, jpeg artifacts, blurry, watermark, text, signature, username, error, cropped, worst quality, low quality, normal quality, jpeg, lowres, ugly, duplicate, morbid, mutilated, out of frame, extra fingers, ...`) — over-long negatives smooth out everything including detail you wanted
- Ignoring the model's training resolution — generate at 1024² for SDXL, near-1MP for SD3

## Anatomy template

Positive:
```
<medium>, <subject>, <pose/expression>, <wardrobe>, <environment>,
(<key detail>:1.2), <lens + lighting>, <style ref>, <color grade>,
<format hints e.g. portrait orientation>
```

Negative:
```
cartoon, lowres, jpeg artifacts, plastic skin, extra fingers, watermark, text, signature, blurry, deformed
```

## Output target

ComfyUI, Automatic1111, Forge, Fooocus, ReForge, Stability API, Replicate, fal.ai. SDXL has rich LoRA + ControlNet ecosystem; SD3.5 catching up.

## See also

- `flux.md` — sibling open-weight model with stronger prompt adherence
- `../patterns.md` for lens/lighting tokens that map well to SD weights
