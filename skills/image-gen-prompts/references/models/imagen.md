# Google Imagen 3 / 4

Google's flagship image model accessed via Vertex AI, the Gemini API, ImageFX (consumer UI), and Whisk. Strong photorealism, very strong typography for short headlines, conservative safety filtering.

## Tier

- **Imagen 3** — Pro on `imagegen-3.0-generate-002` and similar
- **Imagen 4** — Pro+ tier; better text rendering, complex composition

Imagen and Nano Banana coexist in Google's stack: Imagen is for pure text-to-image at the highest quality; Nano Banana is the conversational/edit-friendly Gemini surface. Pick Imagen when you need a single very high-quality still and have no reference image to address.

## Syntax surface

- **Natural-language prose**, no flags, no weight syntax
- **Aspect ratio** via API param `aspect_ratio`: `1:1`, `9:16`, `16:9`, `3:4`, `4:3` (Imagen 4 also supports `2:3`, `3:2`)
- **Number of images** via `number_of_images` (typically 1–4)
- **Negative prompt** via `negative_prompt` API param
- **Person generation** controlled by `person_generation` policy field (`ALLOW_ADULT`, `DONT_ALLOW`, `ALLOW_ALL` per region)
- **Reference images** in `referenceImages` payload (Vertex AI customization endpoints) with `referenceType: SUBJECT` / `STYLE` / `CONTROL`

## Best-in-class for

- Photorealism with realistic skin / fabric / lighting (commercial-grade)
- Short typographic posters — Imagen 4 nails 1–2 line headlines reliably
- Editorial photography aesthetic without Midjourney's stylization bias
- Strong prompt adherence to spatial composition cues ("foreground / midground / background")

## Weak points

- Conservative safety filter — many real-person and edgy prompts get blocked
- CJK partial; not as strong as GPT Image 2 for dense Chinese
- No flag-based fine control — adjust via prose
- Reference-image fidelity below Nano Banana for face-anchored edits (use Nano Banana / Gemini for that)

## Anatomy template (prose form)

```
A <medium> of <subject> doing <action> in <environment>.
<lighting + lens>. <style cue + era>. <color palette>.
<composition: foreground/midground/background hints>.
<aspect ratio sentence, e.g. "Vertical 9:16 composition.">
```

## Reference-image workflow (Vertex AI)

```
referenceImages: [
  { referenceType: SUBJECT, image: <bytes>, subjectImageConfig: { subjectType: PERSON, ... } },
  { referenceType: STYLE,   image: <bytes>, styleImageConfig: { styleDescription: "..." } },
  { referenceType: CONTROL, image: <bytes>, controlImageConfig: { controlType: CONTROL_TYPE_CANNY } }
]
```

The text prompt then references each: `"a portrait of [1] in the style of [2], following the structure of [3]"`.

## Anti-patterns

- Long lists of stylization words — Imagen prefers a few precise cues over heaped adjectives
- Asking for sensitive content — safety filter trips and you get a blank with a refusal
- Embedding `--ar 9:16` in the prompt — parsed as text; use the API param
- Trying to do face-anchored edits via prompt prose — switch to Nano Banana or use Imagen reference customization

## Output target

Vertex AI Imagen API, Gemini API (`imagen-3.0-generate-002`, `imagen-4.0-generate-001`), Google ImageFX (consumer), Whisk (consumer mash-up tool). When integrating, prefer Vertex for reference customization features.

## See also

- `nano-banana.md` — same Google stack; pick when you need conversational / multi-image editing
- `../patterns.md`, `../templates.md`
