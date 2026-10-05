# GPT Image 2.5 (OpenAI — Flare / Sunburst, ChatGPT Images 2.5)

OpenAI's September 2026 successor to GPT Image 2. Same natural-language prompt surface as GPT Image 2 (read `gpt-image-2.md` for the shared grammar: JSON parsing, Raycast placeholders, anti-AI-glamour clause, CJK rules). What 2.5 changes is **control**: two model variants, wider request parameters, a chat surface with Sketch input, and noticeably better scoped edits, multi-reference role separation and multi-turn edit chains.

Sources: `wangrunlin/awesome-gpt-image-2-5-prompts` (73 source-checked cases incl. OpenAI's own image-prompting guide examples), `LaplaceYoung/awesome-gpt-image-2.5` (145 cases + 12 templates + model notes), `VulcanEon/awesome-gpt-image-2.5-prompts` (30 visual studies, 20 editing recipes, 24-step companion to the official guide; linked from the gptimage25ai Medium post "the missing step between inspiration and a prompt"). ~270 prompts analyzed.

> Evidence caveat carried over from all three sources: most community previews are **creator-reported** GPT Image 2.5 outputs, not independently reproduced. Treat recipes as strong starting points and always run the review check at the end of this file.

## Surfaces and variants

| Surface | ID | Use when |
|---|---|---|
| ChatGPT / Codex | **ChatGPT Images 2.5** | Conversational iteration, **Sketch** input (draw a layout), format templates, comment pins on the canvas, image gen + Python in the same chat (GIF/sprite export) |
| Image API / Responses tool | `gpt-image-2.5-flare` | Default. Fast everyday generation, volume, previews, social crops, conversational iteration |
| Image API / Responses tool | `gpt-image-2.5-sunburst` | Precision. Longer generation; campaign stills, tight edit chains, "one element must change and everything else must stay put", dense text/diagrams |
| Pinned snapshots | `gpt-image-2.5-flare-2026-09-08`, `gpt-image-2.5-sunburst-2026-09-08` | Reproducible pipelines |

Official selection advice (OpenAI guide, via VulcanEon companion): if a GPT Image 2 workflow already passes your checks, try **Flare** on the same workload first; if complex tasks fail, evaluate **Sunburst**, then test whether Flare can reach the same bar faster. Flare/Sunburst positioning is OpenAI's description, not a benchmark.

Tier mapping for this skill: **Flare = Pro**, **Sunburst = Pro+** (pick Sunburst for long exact copy, CJK UI screens, 3-reference composites, multi-round edits).

## Request parameters — keep them OUT of the prompt

| Parameter | Values |
|---|---|
| `model` | `gpt-image-2.5-flare` / `gpt-image-2.5-sunburst` |
| `quality` | `auto` (default), `low`, `medium`, `high`, `xhigh`, `max` |
| `size` | `auto` or arbitrary `WIDTHxHEIGHT` (e.g. `1536x864`) |
| `background` | `auto`, `opaque`, `transparent` |
| `output_format` | `png` / `webp` for transparency (don't set `output_compression` with PNG) |

Custom size rules: both edges multiples of 16, max 3840 per edge, long:short ratio ≤ 3:1, total 655,360–8,294,400 px (above 3,686,400 px is experimental). Asking for "16K" or "15360×8640" in the prompt text is just an instruction — it does not raise the output resolution.

Official example settings most guide prompts were shown with: `1024x1536, quality=medium` (portrait), `1536x1024` / `1536x864` `high` for slides & diagrams. Equal quality labels across Flare and Sunburst don't mean equal output or runtime.

Pricing snapshot reported by LaplaceYoung at launch (same for both variants, per 1M tokens): text in $5, cached text $1.25, image in $8, cached image $2, image out $30. Confirm live pricing before quoting.

In ChatGPT the aspect ratio and "transparent PNG" must be stated in prose; on the API they belong in parameters.

## The eight prompting habits (official guide, condensed)

1. Define the **deliverable** first: what it is, purpose, subject, framing, aspect ratio, placement.
2. Pick a format that's easy to maintain — labeled sections, short paragraphs or JSON; no special syntax required.
3. Specify visible **materials, lighting, colors, medium, scale**. Camera terms (lens, f-stop) act as appearance cues, not real optics.
4. For people: describe **framing, gaze, pose and physical interaction** (grip, contact, weight).
5. **Quote required lettering**, and say placement, type style and how many times it appears. Then inspect it.
6. Separate the **intended edit** from identity, geometry, label and scene **locks**.
7. Give **every reference image an explicit role** and say how to combine them.
8. Reuse the previous image for **one focused change per turn**; restate critical constraints when details drift.

## Prompt skeleton that wins on 2.5

The best-performing long prompts across all three corpora share the same shape — uppercase section headers, deliverable first, locks and negatives last:

```
[Deliverable sentence: one finished X, format, aspect ratio, for Y]

SUBJECT / REFERENCE LOCK:
[who/what; "Use the uploaded reference as the single source of truth for ..."]

LAYOUT:
[regions with % of canvas or rows×columns; reading order; negative space]

TEXT (EXACT, verbatim):
"..."  — placement, type style, appears once

STYLE / LIGHT / CAMERA:
[medium, palette (3–5 named colors), light direction, lens cue]

CONSTRAINTS:
- Original design only / no trademarks / no logos / no watermarks
- Do not add any other text, figures, props

OUTPUT:
[one single image, not a collage; what NOT to return (code, analysis)]
```

Short prompts also work surprisingly well on 2.5 when the reference does the work ("Make the bed.", "Move the lamp to the right", "turn it into a future building", "change the composition to this" + sketch) — but they leave everything unlocked. Use them for exploration, then lock.

## Pattern 1 — Exact text ("ONLY this text")

OpenAI's own examples use the same three-part text block:

```
Include ONLY this packaging text (verbatim):
"Christmas Memories Edition"
```
```
Billboard text (EXACT, verbatim, no extra characters):
"Fresh and clean"
Typography: bold sans-serif, high contrast, centered, clean kerning.
Ensure text appears once and is perfectly legible.
```

- Close with `All text must be clearly legible; do not add any other text, brands, logos, or watermarks.`
- For CJK, list every string in quotes and say "content should only contain the following": 2.5 renders full Simplified-Chinese web pages and UI screens when every label is supplied.
- **Known failure:** "ONLY" is respected for the main copy but small incidental writing still appears (handwriting on a box, signage). Check and fix with the *remove invented lettering* recipe below.
- For text-free scenes, veto writing on every surface: `Every illuminated panel must show only abstract gradients or geometric light, never letters or symbols resembling writing.` and `All balls, benches and nearby objects are unbranded and text-free.`

## Pattern 2 — Page-height allocation for long layouts

For long screenshots, web pages and posters, give each section a **share of the canvas** — it stops sections from collapsing:

```
A long screenshot of the desktop webpage, frontal view, no perspective, 9:16 vertical,
complete from navigation to footer.
The first screen occupies about 27% of the entire image ... The concept bar about 8% ...
The service area about 16% ... works 17% ... recruitment 18% ... news 6% ... footer 8%.
All interface copy in readable and accurate Simplified Chinese.
No garbled characters, no third-party logos, no watermarks, no browser borders, no device cases.
```

Percentages should sum to ~100%. Same idea for grids: "exactly four rows and four columns, 16 equally sized square panels".

## Pattern 3 — Reference roles + conflict priority

2.5 handles 2–3 references well **when each one has a single job**:

```
Image 1 is the primary reference for the product itself; Image 2 provides only the color,
lighting, tonal values, and overall atmosphere; Image 3 provides only the composition,
product placement, visual proportions, and negative space structure.
Conflict priority: Product authenticity and label accuracy from Image 1 > Layout structure
from Image 3 > Color and lighting from Image 2.
Do not replicate the objects, text, logos or branding from Image 2 or Image 3.
```

- Name inputs by order ("street scene first, dog source second") — order matters.
- Say what each reference must NOT contribute ("use it only for the grid layout; do not copy its character, outfit, poses").
- Product references: "Preserve the authentic aspect ratio of the product; you may scale it proportionally as a whole; do not squash, stretch or alter its structure."
- "Do not create a hybrid design combining the two products. Do not retain the old product's cap, handle, label."

## Pattern 4 — Scoped edit = change sentence + lock list

```
Change only the glossy red ceramic cup on the far right of the desktop to a matte white ceramic cup.
Keep the cup's size, shape, handle direction, position, perspective, and contact shadow unchanged.
Keep [enumerate every other visible element] unchanged. Do not change anything other than the cup.
```

- One change sentence, then an explicit **lock list** of everything visible. "Do not change anything else." alone works for simple edits (OpenAI's flower removal), but enumerated locks beat it on busy scenes.
- Allow the physically necessary side effects: "Modify only the area occupied by the new product, along with any necessary contact shadows, occlusions, and local reflections."
- Colour grading: "strictly retain the original composition ... do not add, delete or change any objects ... The end result must be like a professional color correction of the original RAW photo, not a regenerated image."
- **Preservation is visual, not pixel-identical.** Authors report small drift outside the target (a palette change desaturated the subject; small changes outside a laptop screen). Where pixels must stay identical, composite the approved region back into the original.

## Pattern 5 — Multi-turn edit chains

Keep the same conversation (or re-upload the last output) and change **one variable per round**:

```
R1  Create a 1024×1536 portrait "城市咖啡节" poster. Include only: [4 quoted strings]. Swiss grid, ivory/coffee/cobalt.
R2  Change the color scheme only to black, silver-gray, and fluorescent orange. Keep copy, hierarchy, placement, subject, composition unchanged.
R3  Enlarge "城市咖啡节" by approximately 20% and slightly increase the letter spacing. Keep everything else unchanged.
R4  Replace "2026.10.18" with "2026.10.25" only. The new date must appear only once.
R5  Remove only the steam above the dripper and naturally restore the area underneath.
```

Other proven chains: sketch → "atmospheric nighttime campsite" → "change it to daytime without changing the composition" → "change the person's clothing to overalls"; billboard → "make it look like a winter evening with snowfall". Save the best result as the **master** and branch variants from the master, not from each other.

## Pattern 6 — Sequential assets (sprite sheets, stickers, GIFs)

2.5 is widely used for sprite sheets and sticker loops, but **an image model outputs a still**. Split the job:

1. **Image step** — a grid with hard geometry: `16 frames in a 4×4 sheet on a 1024×1024 transparent canvas; each 256×256 cell; fixed baseline; at least 16 px padding; same pet, not variations; no grid lines, labels or text; true RGBA alpha, do not draw a checkerboard`.
2. **Code step** (ChatGPT/Codex with Python) — split equal cells, keep one shared canvas (never crop/recenter frame by frame → jitter), nearest-neighbour for pixel art, set GIF disposal/transparency, reopen and report frame count, durations, size. "Do not present a static image as a completed animation; if you cannot export, say so."

Tips from the corpora: describe the motion phases per frame (start → build → peak → settle → return to frame 1); for six-frame expressions use 3×2 with ~15% margin; if a grid distorts the design, generate separate single-frame variations instead; if transparency fails, repair it in a fresh chat. Never globally delete white — it erases eyes, teeth and sticker borders.

## Pattern 7 — Character / production sheets

Lock identity once, then demand continuity explicitly. Proven skeleton (meAsifAi, 1.3k likes): `REFERENCE & IDENTITY LOCK` → `Before constructing the sheet, internally analyze and lock: facial construction, head-to-body ratio, silhouette, costume construction ...` → numbered panels (hero portrait, 5-view turnaround "identical scale, aligned head/shoulder/knee lines", 6 expressions, 4–6 poses, costume callouts, material studies, palette strip, proportion guide) → `DESIGN CONTINUITY: identical facial identity, proportions, hairstyle, costume, accessory placement, consistent left/right details` → `CAMERA: orthographic-like turnaround; LIGHTING: neutral, for inspection not drama`. Character-driven variants work too: "First, visually interpret the character's personality ... invent a personalized dance vocabulary ... do not apply a generic routine."

## Pattern 8 — Compact "art-director brief"

The Sunburst comparison prompts (ImagineArt) show 2.5 executing dense one-sentence briefs with countable specifics:

```
a domestic espresso machine drawn in section, 1960s service manual style, fine black line work
with flat spot colour on cream paper. Fourteen numbered leader lines, a key down the right listing
all fourteen parts, a scale bar in centimetres, and a title block reading FIG. 3 SECTIONAL VIEW MODEL C2.
```
```
a fashion campaign for an invented label, shot from a camera on the ground with a 24mm lens tilted
fifteen degrees. Six people in electric blue, tomato red, lime green, hot pink, butter yellow and
lilac, all posed differently, against plain cobalt sky.
```

Recipe: medium + era + surface, then **numbers** (fourteen labels, six people, seven pinned items, four bus times), then one exact title string.

## Pattern 9 — Realism and anti-"slop"

- Minimal baselines work: `make me a realistic iphone photo of a woman in a cafe`.
- Two-word edit `remove slop` is a popular quick pass, but subjective — follow up with concrete fixes.
- Concrete realism kit: `real skin texture, fine pores, natural facial asymmetry`, `mildly clipped highlights, modest sensor grain`, `not over-retouched`, `Avoid: plastic skin, excessive beautification, over-sharpening, HDR, cheap influencer filters`.
- Colour casts: "The retro feeling must come from wardrobe, textures and atmosphere — not from a heavy yellow or orange filter."
- Ask for one sharp element against motion: "keep the eyes, face and bouquet sharp; let only the train stretch into horizontal motion blur."

## Pattern 10 — Transparent output

```
Fully transparent background. Deliver a single centered logo with generous padding, clean alpha
edges, and no solid backdrop, scenery, checkerboard, or watermark.
```
Pair with `background="transparent"` + PNG/WebP on the API. Always inspect decoded alpha in an editor; a preview can't prove transparency. If the tool can't do alpha, ask for a uniform neutral background and mask later.

## Templates (fill the brackets, keep the lock sentences)

Distilled from LaplaceYoung's 12-template library:

```
Editorial poster — Create one finished editorial poster about [subject]. Render the exact headline "[copy]" with clear hierarchy, generous negative space, a restrained [palette] palette, and [print texture]. Use one supporting visual metaphor. No extra text, mockups, or watermarks.

Product campaign — Create a premium product campaign image for [product]. Preserve exact proportions, materials, and label text "[copy]". Use [camera] framing, [lighting], a clean [background], and one purposeful prop. No invented logos or warped lettering.

UI screenshot — Create one high-fidelity [platform] UI screenshot for [product]. Include [layout] and render these labels exactly: [copy]. Use consistent spacing, accessible contrast, realistic controls, and no gibberish, extra windows, or gradients.

Infographic — Create a single [format] infographic about [subject] for [audience]. Use exactly [count] modules connected by [relationship]. Render supplied copy exactly, with clear reading order, restrained colors, and no invented data.

Character sheet — Create a [format] character reference sheet for [character]. Show [views] with identical face, costume, proportions, and accessories. Use a clean [background], even studio lighting, and no labels, props, or extra characters.

Cinematic keyframe — Create one cinematic [aspect ratio] keyframe of [subject] performing [action] in [location]. Specify foreground, midground, background, lens, lighting, atmosphere, and palette. Keep the silhouette readable and output one finished frame, not a storyboard.

Style transfer — Use the attached image as the identity and composition lock. Restyle it as [style]. Preserve [locks] exactly, changing only surface treatment, palette, and texture. Do not alter face, pose, camera, or background geometry.

Scoped edit — Edit only [region] of the supplied reference. Make this change: [change]. Keep [locks] untouched and blend edges, lighting, grain, focus, and perspective with the original. Output one clean image.

Packaging — Design a [product] package in [format]. Show [views] with consistent branding, exact copy "[copy]", clear hierarchy, realistic materials, and controlled studio light. No spelling errors, duplicate packages, or placeholder text.

Diagram / explainer — Create a precise visual explainer about [subject]. Arrange [count] labeled components in a clear [flow] and use arrows only where relationships exist. Keep labels short and exact; use [style] with strong contrast and clean spacing.

Social card — Create one social-media card for [message]. Use a clear hero image, readable headline "[copy]", [format] crop, and [tone] art direction. Keep the layout simple, high contrast, and free of filler text or watermarks.

Miniature diorama — Create a tactile miniature diorama of [subject] in [setting]. Use [materials], a fixed camera, shallow depth of field, believable scale cues, and soft directional light. Keep all small objects distinct and avoid duplicates or random lettering.
```

Full worked examples: `references/examples.md` §25–34. Repair recipes: `references/editing-workflow.md` → "Repair recipes (GPT Image 2.5)".

## Known failure modes (documented in sources)

| Symptom | Seen in | Fix |
|---|---|---|
| Object count off (8 pins requested → 10) | personal-enamel-pin-set | State the count twice, enumerate each item's role ("1 portrait pin, 1 name pin, 5 interest pins"), then check; repair with a scoped edit |
| Negative constraints ignored ~half the time (2 of 4 posters added decorations) | autumn-market test | Put "only" lists up front, keep the scene small, regenerate or use scoped removal |
| Extra small writing despite "ONLY this text" | OpenAI holiday card | Remove-invented-lettering recipe |
| Watermark appears despite "no watermark" | modular tower | Edit it out; don't rely on the negative |
| Two figures when one requested; headline wording changed | annotated lookbook | "One model only"; quote headline exactly; re-check |
| Drift outside the edit target | laptop screen, cup, palette change | Enumerated lock list; composite for pixel-exact work |
| Grid sheet redesigns the character | separate-frame animation | Generate frames as separate edits of the same reference |
| Transparency pass fails / checkerboard painted in | combat sprite sheet | Fresh chat for the repair; ask for true alpha; inspect decoded alpha |
| Section of a long page collapses | web mockups | Allocate % of height per section |

## Review checklist (run on every output)

The VulcanEon corpus attaches a concrete check to every prompt — adopt the habit:

- **Text**: read every string at full size and at phone size; count repetitions.
- **Counts**: people, objects, panels, wheels, fingers, legs.
- **Identity**: compare facial landmarks with the reference *before* judging the styling.
- **Geometry**: product proportions, label perspective, continuous cables/ropes/leads, wheel ellipses.
- **Edit scope**: compare everything outside the target with the original.
- **Alpha**: inspect decoded transparency, not the preview.
- **Facts**: diagrams, maps, coordinates, molecule labels, market numbers in generated slides are illustrations — verify or replace.

## Migration from GPT Image 2

Save baseline inputs/settings/outputs (hard edits, lettering, faces, product shapes, transparency). Hold prompts, references, size and format fixed for the first comparison; evaluate complete results and repeated edit sequences; then measure latency. Tune one variable at a time, count retries and cost per accepted image. Note: the runnable Python/Ruby samples in OpenAI's 2.5 guide tab were still pinned to `gpt-image-2` at launch — check the `model` field before running.

## Anti-patterns

- Putting `quality`, `size`, `background` values in the prompt on the API — set them as parameters.
- Asking for 16K/8K "resolution" in text and trusting it.
- Feeding 3 references without roles → hybrids and copied props.
- Several changes in one edit turn → the model re-renders the whole image.
- Expecting a GIF, ZIP, editable vector, HTML page or working slide from the image model alone.
- "Make it realistic" without concrete texture/lighting cues; "remove slop" as the only instruction for production work.
- Trusting "Do not change anything else" for pixel-identical output.
