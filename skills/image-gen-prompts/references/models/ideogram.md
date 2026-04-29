# Ideogram 2 / 3

Best-in-class typography model. Strongest open consumer choice for posters, logos, mockups, and any image where exact text rendering matters.

## Tier

- **Ideogram 2.0 / 2a** — Standard
- **Ideogram 3.0** — Pro; sharper render, better hands, longer text strings, multilingual improved

## Syntax surface

- **Natural-language prose** with **literal text in double quotes** for in-image rendering: `a movie poster reading "THE LAST EXPEDITION"`.
- **Style presets** in API/UI: `RENDER_3D`, `ANIME`, `DESIGN`, `GENERAL`, `REALISTIC`, `FICTION`. Pick `DESIGN` for typography-heavy work.
- **Aspect ratio** as API enum: `ASPECT_1_1`, `ASPECT_16_9`, `ASPECT_9_16`, `ASPECT_3_2`, etc.
- **Negative prompt** via `negative_prompt` API param.
- **Magic Prompt** auto-expands short prompts — toggle off if you want strict adherence.
- **Color palette** can be specified via `color_palette` (Ideogram 3) — list of hex codes biases output.
- **Reference image** via `style_reference_images` (Ideogram 3) — soft style transfer.

## Best-in-class for

- Posters, magazine covers, album art, book covers — any layout where the headline must read perfectly
- Logos and wordmarks (single word / short phrase)
- Mockups with branded text on packaging
- T-shirt / sticker designs
- Multi-line typography with weight variation

## Weak points

- Photoreal portraits — solid but below Imagen / FLUX Krea / GPT Image 2
- Cinematic dramatic lighting — Midjourney still stronger
- Complex narrative scenes with many subjects — drift past 3
- Long body copy (paragraph-level) — short headlines yes, paragraphs no

## Quote pattern

Always wrap exact strings in double quotes. The model treats anything in quotes as the text to render verbatim.

```
A minimalist Swiss design poster on a deep indigo background.
Large bold sans-serif headline reading "OBSIDIAN" centered upper-third.
Below: thin sans-serif subtitle reading "An exhibition of stillness, May 2026 — Milan".
Tiny credit line bottom-right: "Curated by Studio Pluma".
Generous negative space. 4:5 portrait orientation. Crisp kerning, exact spelling.
```

## Anatomy template

```
A <design medium e.g. poster / album cover / sticker> of <visual subject>.
Headline reading "<EXACT STRING>" in <font family + weight>, <size + position>.
Subtitle (if any): "<EXACT STRING>" in <font + position>.
Color palette: <named or hex>. Composition: <symmetric / off-center / asymmetric>.
<Aspect ratio>. Crisp kerning, exact spelling, no warped letters.
```

## Anti-patterns

- Paraphrasing the headline instead of quoting — model invents copy
- Vague font ("elegant", "modern") — name a family or describe weight + class
- Magic Prompt left on for typography work — it can rewrite your literal string
- Embedding very long body copy (Ideogram 2 caps quality past ~30 words; 3 stretches further but still degrades)

## Output target

Ideogram web app, mobile, public API. For the API specify `style_type` and `magic_prompt_option=OFF` for typography work.

## See also

- `gpt-image-2.md` — when you need both perfect typography AND CJK + complex multi-panel scenes
- `recraft.md` — when you need vector output of the typography
- `../text-rendering.md` for the universal text-in-image rules
