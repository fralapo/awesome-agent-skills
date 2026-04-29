# FLUX.1 (Black Forest Labs)

Open-weight family from the team that built the original Stable Diffusion. Strong prompt adherence, far better text rendering than SDXL, lower aesthetic bias than Midjourney.

## Variants

| Variant | Tier | Notes |
|---|---|---|
| FLUX.1 [schnell] | Standard | 4-step turbo, Apache-2.0, fast/cheap |
| FLUX.1 [dev] | Pro | 28-50 step, non-commercial weights, top open quality |
| FLUX.1 [pro] | Pro | API-only, Black Forest Labs hosted, best quality |
| FLUX.1 Krea [dev] | Pro | Photorealism-tuned variant |
| FLUX.1 Fill / Canny / Depth / Redux | Workflow | Inpainting / control / image-variation tools |

## Syntax surface

- **Natural-language prose** — FLUX rewards detail and density. Tag-soup prompts under-perform vs full-sentence descriptions.
- **No weight syntax** like SD's `(token:1.2)` — handled by the model
- **No `--flags`** — pass aspect ratio + steps + guidance as workflow/API params
- **Negative prompts**: minimal effect on `[schnell]` and `[dev]` (they were trained without classifier-free guidance the same way SDXL was). On hosted `[pro]` API there is a `negative_prompt` param but signal is weak — prefer positive prompting

### API params (typical, e.g. fal.ai / Replicate)

- `prompt` — natural-language string
- `width`, `height` — multiples of 64; common 1024×1024, 768×1344, 1344×768
- `num_inference_steps` — 4 (schnell), 28–50 (dev/pro)
- `guidance` — 3.5 default for dev; ignored for schnell
- `seed` — reproducibility

## Best-in-class for

- **Text in image** — far better than SDXL; multi-word labels and short headlines stable
- **Prompt adherence** — close to GPT Image 2 for compositional accuracy (though weaker on long CJK)
- **Photoreal portraits** with FLUX Krea variant
- **Open-weight workflows** — LoRA training, ComfyUI nodes, FLUX Fill for inpainting, FLUX Redux for variations
- **Long prose prompts** — model parses 200+ word descriptions without losing focus

## Weak points

- CJK / Cyrillic / Arabic text — partial; safer to keep Latin
- Default style is neutral / slightly cinematic — for ultra-stylized aesthetics layer a LoRA
- Negative prompts under-effective on schnell/dev — counter unwanted artifacts via positive description rephrasing

## Reference-image workflows

- **FLUX Redux** — image-to-image variation; pass an init image, model produces a related composition
- **FLUX Fill (inpaint)** — mask + prompt, edits the masked region only
- **FLUX Canny / Depth** — ControlNet-style structural conditioning
- **PuLID-FLUX / FLUX-IP-Adapter** — face/identity anchoring (community)

## Anatomy template (prose form)

```
<medium and overall framing in one sentence>. <subject described with named attributes,
wardrobe, expression, pose, age range>. <environment with named props and depth cues>.
<lighting: key/fill/rim, time-of-day, color temperature>. <camera: lens, aperture, angle>.
<style ref: film stock, era, art movement, render engine>. <atmospheric details>.
<aspect ratio note in prose, e.g. "vertical portrait orientation">.
```

## Anti-patterns

- Tag-soup prompts (`portrait, 8k, masterpiece, beautiful, highly detailed`) — under-perform vs prose
- Mixing `(token:1.3)` SD weights — parsed as literal text
- Mixing `--ar 16:9` MJ flags — parsed as literal text, pollutes output
- Long negative-prompt dumps on schnell/dev — wasted tokens
- Asking for long CJK headlines — degrades; switch to GPT Image 2 / Ideogram

## Output target

Black Forest Labs API (FLUX.1 [pro]), fal.ai, Replicate, Hugging Face Spaces, ComfyUI (FLUX nodes), self-hosted. For maximum quality use `[pro]`; for fast iteration use `[schnell]` then upscale or rerun on `[dev]`.

## See also

- `stable-diffusion.md` — sibling family, LoRA-rich
- `../patterns.md` for lighting/camera vocab (works directly in FLUX prose)
