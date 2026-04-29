# GPT Image 1 / DALL·E 3 (OpenAI)

OpenAI's previous-generation image model — natural-language-first, strong photography priors, weaker at long text and CJK than its successor GPT Image 2.

## Tier

Standard. Use for single-subject generations, short prompts, simple edits. For long text in image, multi-panel consistency, or CJK, prefer GPT Image 2 (`gpt-image-2.md`).

## Syntax surface

- **Natural language only**, no flags, no weight syntax
- **Prompt rewriting on the model side** — the model reformulates short prompts into longer ones internally; this can drift from intent. Counter with explicit detail: lens, lighting, composition, framing
- **Mask-based edits** via Images Edit API — supply a transparent PNG mask + prompt describing the change to the masked region only
- **Reference images** referenced as "the provided image" in API; not addressable inline as multiple images in one prompt
- **Aspect ratios** via API `size` param: `1024x1024`, `1024x1792` (9:16-ish), `1792x1024` (16:9-ish). DALL·E 3 limited to these three sizes; GPT Image 1 adds intermediate ratios

## What works well

- Studio product photography, single hero subject
- Cartoon / illustration with strong style prior (DALL·E 3 era loves Pixar/3D-render aesthetic by default)
- Short Latin-script labels (< 10 words)
- Simple compositions with one or two subjects

## What fails

- Long text in image — letters distort past ~10 words
- CJK / Arabic / Cyrillic — breaks
- Multi-panel consistency — character drifts across generations
- Dense bento/infographic layouts — modules collapse, copy garbles

## Identity preservation

Weaker than Nano Banana / GPT Image 2. For face-preserving edits, use the Images Edit API with a mask covering only the area to change, and write the preservation clause in the prompt:

```
Preserve the subject's face, hair, and skin tone exactly. Only modify the {region} to {change}.
```

## Anti-patterns

- Overly polished default look — counter with `"natural skin texture, no airbrushing, no beauty filter"`
- Letting prompt rewriting hijack intent — be explicit about what NOT to add
- Asking for text > 10 words — splits / misspells

## Output target

OpenAI Images API (`dall-e-3`, `gpt-image-1`), ChatGPT image generation, third-party wrappers. For programmatic use specify `quality: "hd"` and `style: "natural"` (vs `"vivid"`) when the brief is photographic, not stylized.

## ChatGPT-specific conventions (DALL·E 3 / GPT Image 1 inside ChatGPT)

When prompting through ChatGPT (not the raw API), three conventions help:

### 1. Always specify deliverable format

Source: `marc-aurele-besner/prompts` (50-use-case ChatGPT image guide).

Every effective prompt names: dimensions + file format + DPI for print.

```
... in [PNG / JPEG / PDF / SVG / GIF] format at [WIDTH]x[HEIGHT] pixels [or A4 / A3 / 5x7"]
[at 300 DPI for print].
```

Examples:
- Icons: `64x64 pixels in PNG format with a transparent or white background`
- Web banners: `1500x500 pixels in JPEG format`
- Print posters: `24x36 inches at 300 DPI in PDF format`
- App icons: `512x512 pixels in PNG format`
- Album covers: `3000x3000 pixels in JPEG format`
- Logos: `SVG format for scalability`
- Animated assets: `500x500 pixels GIF`

### 2. Request a `gen_id`

ChatGPT's image renderer returns an internal `gen_id` per generation. Asking for it back in chat lets you reference the exact image later for variations or edits ("regenerate gen_id XYZ but change the background to navy"). Standard convention from the 50-prompt guide:

```
... Please include a gen_id with the delivery / Provide a gen_id along with the image.
```

Use `gen_id` only when prompting through ChatGPT — it has no meaning on the raw OpenAI Images API.

### 3. Use-case-shaped prompts beat tag-soup

The `marc-aurele-besner/prompts` 50-case set follows a consistent shape that ChatGPT/DALL·E 3 parse reliably:

```
[Action verb e.g. Design / Create / Generate / Illustrate / Craft] [object] for [audience or use case].
[Style / mood] should be [adjective list]. Use [color palette].
Provide the file in [FORMAT] at [DIMENSIONS] [DPI if print]. Please include a gen_id.
```

Use-case categories that work well in this style: flat icons, brand logos, hero website backgrounds, posters, children's book covers, infographics, social media banners, app UI elements, event invitations, product mockups, ebook covers, YouTube thumbnails, business cards, album art, newsletter headers, T-shirt graphics, desktop wallpapers, mascot characters, book illustrations, email signature banners, presentation backgrounds, webpage illustrations, stickers, character concept art, menu designs, event badges, lyric booklets, blog post images, packaging, educational diagrams, mobile app icons, recipe cards, science-fair posters, holiday greeting cards, animated GIFs, event programs, IG infographics, e-commerce product images, festival branding, bookmarks, slide templates, magazine covers, 4-panel comic strips, table tents, product labels, architectural renderings, mobile game assets, scientific illustrations, merchandise mockups, wedding seating charts.

## See also

- `gpt-image-2.md` — newer, far stronger at text + consistency
- `../patterns.md`, `../templates.md`, `../identity-preservation.md`
- `../templates.md#22a-packaging-design` and `#22b-mockup-family` for cross-model template shapes
