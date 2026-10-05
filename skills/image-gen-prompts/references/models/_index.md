# Model Routing Index

Map user-mentioned keywords → file. When a user names a model, read the matching file before composing the prompt.

| File | Family | Common keywords |
|---|---|---|
| `nano-banana.md` | Google Gemini 2.5 Flash Image (Nano Banana, Nano Banana Pro) | nano banana, nano-banana, gemini 2.5 flash image, gemini image gen, 纳米香蕉, banana pro |
| `gpt-image-2-5.md` | OpenAI GPT Image 2.5 — `gpt-image-2.5-flare` / `gpt-image-2.5-sunburst`, ChatGPT Images 2.5 | gpt image 2.5, gpt-image-2.5, image 2.5, chatgpt images 2.5, flare, sunburst, gpt-image-2.5-flare, gpt-image-2.5-sunburst |
| `gpt-image-2.md` | OpenAI GPT Image 2 (codename "duct-tape") | gpt image 2, gpt-image-2, duct-tape, openai image 2 |
| `gpt-image-1.md` | OpenAI GPT Image 1, DALL·E 3 | gpt image 1, gpt-image-1, dall-e, dall·e, dalle 3, dalle3 |
| `midjourney.md` | Midjourney v6 / v7, Niji v6 | midjourney, mj, niji, --ar, --stylize, --sref, --cref, --niji, --weird |
| `stable-diffusion.md` | SD 1.5, SDXL, SD3, SD3.5, ComfyUI/Auto1111 ecosystems | stable diffusion, sd 1.5, sdxl, sd3, sd3.5, comfyui, automatic1111, forge |
| `flux.md` | Black Forest Labs FLUX.1 schnell / dev / pro / Krea | flux, flux.1, flux dev, flux schnell, flux pro, flux krea, black forest labs |
| `imagen.md` | Google Imagen 3 / 4 | imagen, imagen 3, imagen 4, google imagen |
| `ideogram.md` | Ideogram 2 / 3 | ideogram, ideogram 2, ideogram 3 |
| `recraft.md` | Recraft v3 (raster + vector + brand styles) | recraft, recraft v3, recraft vector |
| `seedream.md` | ByteDance Seedream 4.x / 5.0 | seedream, seedream 5, doubao image, jimmeng, byteimage |

## Routing logic

```
If query mentions a model keyword:
  read references/models/<file>.md first
  layer model-specific syntax onto universal anatomy in SKILL.md
Else:
  use universal anatomy from SKILL.md
  ask the user which model before finalizing
```

## Cross-model capability matrix (cheat sheet)

| Capability | Nano Banana | NB Pro | GPT Image 1 | GPT Image 2 | MJ v6 | MJ v7 | SDXL | SD3.5 | FLUX dev | Imagen 3 | Ideogram 3 | Recraft v3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Photorealism | ✅ | ✅✅ | ✅ | ✅✅ | ✅✅ | ✅✅ | ✅ | ✅ | ✅✅ | ✅✅ | ✅ | ✅ |
| Cross-image consistency | ⚠️ | ✅ | ⚠️ | ✅✅ | ✅ (`--cref`) | ✅✅ | ⚠️ (IP-Adapter) | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ (brand style) |
| Long text in image | ❌ | ✅ | ⚠️ | ✅✅ | ⚠️ | ✅ | ❌ | ⚠️ | ⚠️ | ✅ | ✅✅ | ✅ |
| CJK text | ❌ | ✅ | ❌ | ✅✅ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | ⚠️ | ⚠️ |
| Native edit / inpaint | ✅ | ✅✅ | ✅ (mask) | ✅✅ | ✅ (Vary Region) | ✅ | ✅ (img2img) | ✅ | ✅ (FLUX Fill) | ⚠️ | ✅ | ✅ |
| Multi-image fusion | ✅ | ✅✅ | ⚠️ | ✅ | ⚠️ | ✅ | via IP-Adapter | via IP-Adapter | via FLUX Redux | ⚠️ | ⚠️ | ⚠️ |
| Vector output | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅✅ |
| Flag-based syntax | ❌ | ❌ | ❌ | ❌ | ✅✅ | ✅✅ | ⚠️ (weights) | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| Structured JSON prompt | ⚠️ | ✅ | ⚠️ | ✅✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ⚠️ | ⚠️ | ⚠️ |
| Negative prompt slot | inline | inline | inline | inline | `--no` | `--no` | dedicated | dedicated | minimal | inline | inline | inline |

✅✅ = best in class. ✅ = supported. ⚠️ = partial/workflow-dependent. ❌ = not supported.

**GPT Image 2.5** (not a column to keep the table readable): same as GPT Image 2 on every row, with the edge moving further on native edits (scoped edits with lock lists, multi-turn chains), multi-image fusion (role + conflict priority) and dense CJK UI text. Still no vector output and no flag syntax; size/quality/background are API parameters.

## Tier mapping

| Standard tier | Pro tier |
|---|---|
| Nano Banana | Nano Banana Pro |
| DALL·E 3 / GPT Image 1 | GPT Image 2 |
| GPT Image 2 | GPT Image 2.5 Flare (Pro) / Sunburst (Pro+, precision edits) |
| Midjourney v6 | Midjourney v7 |
| SD 1.5 | SDXL / SD3 / SD3.5 |
| FLUX.1 [schnell] | FLUX.1 [dev] / [pro] |
| Imagen 3 (basic) | Imagen 3 (long-prompt mode) / Imagen 4 |
| Ideogram 2 | Ideogram 3 |
| Seedream 4.0 / 4.5 | Seedream 5.0 |
| Nano Banana | Nano Banana 2 |
