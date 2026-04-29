# Curated Working Examples

Each example is a real prompt that produced good output in the source repo. Use as reference shapes, not verbatim — swap in your own subject/constraints.

Attribution: prompts from the 7 community repos analyzed (Super-Maker-AI, YouMind-OpenLab nano-banana-pro, PicoTrex, jimmylv, ZeroLu/awesome-nanobanana-pro, ZeroLu/awesome-gpt-image, YouMind-OpenLab/awesome-gpt-image-2). Original authors noted where known.

Each example header tags its origin model (`Best on:` line) — the prompt was confirmed to work on that model in source. Most natural-language prompts also work on the other Pro-tier natural-language models with minor adjustments.

---

## 1. Identity-Preserved Professional Headshot

Source: @PavolRusnak via awesome-nanobanana-pro.

```
A professional, high-resolution profile photo, maintaining the exact facial structure,
identity, and key features of the person in the input image. The subject is framed from
the chest up, with ample headroom. The person looks directly at the camera. They are
styled for a professional photo studio shoot, wearing a premium smart casual blazer in
a subtle charcoal gray. The background is a solid '#562226' neutral studio color.
Shot from a high angle with bright and airy soft, diffused studio lighting, gently
illuminating the face and creating a subtle catchlight in the eyes. Captured on an
85mm f/1.8 lens with a shallow depth of field, exquisite focus on the eyes, and
beautiful, soft bokeh. Observe crisp detail on the fabric texture of the blazer,
individual strands of hair, and natural, realistic skin texture. The atmosphere exudes
confidence, professionalism, and approachability. Clean and bright cinematic color
grading with subtle warmth and balanced tones.
```

---

## 2. Kodak Portra Emotional Portrait

```
Keep the facial features of the person in the uploaded image exactly consistent.
Style: A cinematic, emotional portrait shot on Kodak Portra 400 film.
Setting: An urban street coffee shop window at Golden Hour (sunset).
Warm, nostalgic lighting hitting the side of the face.
Atmosphere: Apply a subtle film grain and soft focus to create a dreamy storytelling vibe.
Action: The subject is looking slightly away from the camera, holding a coffee cup,
with a relaxed, candid expression.
Details: High quality, depth of field, bokeh background of city lights.
```

---

## 3. 2000s Mirror Selfie (JSON format)

Source: @ZaraIrahh.

```json
Create a 2000s Mirror Selfie using Gemini Nano Banana.

{
  "subject": {
    "description": "A young woman taking a mirror selfie",
    "hair": { "color": "dark", "style": "very long voluminous waves with wispy bangs" },
    "clothing": {
      "top": { "type": "fitted cropped t-shirt", "color": "cream white",
               "details": "anime-style cat face graphic with big blue eyes" }
    },
    "face": { "preserve_original": true,
              "makeup": "natural glam, soft pink dewy blush, glossy red pouty lips" }
  },
  "photography": {
    "camera_style": "early-2000s digital camera aesthetic",
    "lighting": "harsh super-flash with bright blown-out highlights but subject still visible",
    "angle": "mirror selfie",
    "texture": "subtle grain, retro highlights, crisp details"
  },
  "background": {
    "setting": "nostalgic early-2000s bedroom",
    "elements": ["chunky wooden dresser", "CD player", "posters of 2000s pop icons",
                 "hanging beaded door curtain", "cluttered vanity with lip glosses"]
  }
}
```

---

## 4. Non-Destructive Ghostface Background Edit

Source: @Supermaker AI.

```
Perform non-destructive background editing on an existing personal photo: preserve the
foreground subject(s) entirely unchanged — including their original posture, facial
features, expressions, clothing, hairstyle, and all fine details — with zero alterations.

Only modify the background area to naturally integrate the iconic Ghostface character
(from the Scream franchise), creating the illusion that Ghostface was part of the
original scene (a 'hidden in the background' prank effect).

Ghostface Details: classic recognizable design — white mask with sharp black eye/mouth
details, full black hooded robe, subtle menacing yet understated posture (standing
partially obscured by background objects, leaning in from a corner, or standing a few
steps behind the foreground subject).

Match the original photo's lighting logic. Ensure Ghostface feels like a natural,
unplanned part of the scene — like a hidden Easter egg in a horror movie.
```

---

## 5. Celebrity Group Selfie

Source: @xmliisu.

```
An ultra realistic group selfie. Center: the person from the attached image (uploaded
image facial details), wearing a fitted black shirt and ripped jeans, holding an iPhone
for the selfie. Around are Chris Hemsworth as Thor, Gal Gadot as Wonder Woman, Scarlett
Johansson as Black Widow, Mark Ruffalo as Hulk, Henry Cavill as Superman, RDJ in full
armor — all hugging, smiling, posing casually like close friends.
Fun, joyful mood, bright daylight, cinematic quality, natural look, high detail.
```

---

## 6. Luxury Product Macro

Source: @AmirMushich.

```
Frosted glass bottle; label planar: "First Rain".
Shallow pool with crisp caustics.
Natural crown from a falling lychee; transparent indigo ribbons; lychees some halved +
eucalyptus sprigs ride arcs; base cluster partly submerged for refraction.
Condensation 50% 1.2 mm.
Light: sun leaf-gobo, silver rim 45°R, cool purple under-kicker, sky fill; clamp highs.
Cam: FF 100 mm, f/8, 1/2000, ISO100. 8K; no warp/banding.
```

Note: this one is deliberately dense-notational. Works because every token maps to a
real photographic concept. Don't pad with fluff.

---

## 7. Cinematic Product Poster with Aurora

Source: @rovvmut_.

```
Design a hyperrealistic cinematic poster showcasing the [PRODUCT] as the centerpiece.
The device on a sleek obsidian pedestal at the edge of a tranquil reflective lake.
Surrounding it are glowing bioluminescent plants and tall reeds swaying gently in the
breeze, giving the scene an ethereal, futuristic feel. In the background, jagged cliffs
rise dramatically, their edges kissed by a glowing aurora in the night sky.
Use moody atmospheric lighting with cool blues and purples contrasted by warm golden
highlights reflecting off the device. Capture the scene from a slightly low angle to
emphasize grandeur, with a shallow depth of field to sharpen the [PRODUCT] while
softening the surrounding mist. Add subtle lens flares, crisp polished textures, and
a cinematic vignette for a premium editorial aesthetic.
Write the brand name and a tagline as well.
```

---

## 8. 3D Isometric Diorama

Source: @DataExec.

```
Create a high-detail 3D isometric diorama of the entire United States, where each state
is represented as its own miniature platform. Inside each state, place a stylized,
small-scale 3D model of that state's most iconic landmark. Use the same visual style
as a cute, polished 3D city diorama: soft pastel colors, clean materials, smooth rounded
forms, gentle shadows, and subtle reflections. Each landmark should look like a
miniature model, charming, simplified, but clearly recognizable. Arrange the states in
accurate geographical layout, with consistent lighting and perspective. Include state
labels and landmark labels in a clean, modern font, floating above or near each model.
```

---

## 9. Bento Infographic (Pro)

Source: @MansiSanghani1.

```
Input Variable: [insert product name]
Language: [insert language]

Create an image of premium liquid glass Bento grid product infographic with 8 modules
(card 2 to 8 show text titles only).

1) Product Analysis:
  → Identify product's dominant natural color → "hero color"
  → Identify category: FOOD / MEDICINE / TECH
2) Color Palette:
  → Product + accents: full saturation hero color
  → Icons, borders: muted hero (30-40% saturation, never black)
3) Visual Style:
  → Hero product: real photography or 3D Glass version
  → Cards: Apple liquid glass (85-90% transparent), whisper-thin borders, subtle drop shadow
  → Background: blurred product essence or macro texture
  → Asymmetric Bento grid, 16:9 landscape
  → Hero card: 28-30% | Info modules: 70-72%

Module Content (8 Cards):
M1 — Hero: Product as real photo / 3D glass + product name label
M2 — Core Benefits: 4 unique benefits + hero-color icons
M3 — How to Use: 4 usage methods + icons
M4 — Key Metrics: 5 EXACT data points, format [icon] [Label] [Bold Value] [Unit]
M5 — Who It's For: 4 recommended groups (green check) | 3 caution (amber warning)
M6 — Important Notes: 4 precautions + warning icons
M7 — Quick Reference: varies by category
M8 — Did You Know: 3 facts + icons

Output: 1 image, 16:9 landscape, ultra-premium liquid glass infographic.
```

---

## 10. Quote Card with Raycast Arguments

Source: @stark_nico99 / Nicolechan.

```
A wide quote card featuring a famous person, with a brown background and a light-gold
serif font for the quote: "{argument name="famous_quote" default="Stay Hungry, Stay Foolish"}"
and smaller text: "—{argument name="author" default="Steve Jobs"}."
There is a large, subtle quotation mark before the text. The portrait of the person is
on the left, the text on the right. The text occupies two-thirds of the image and the
portrait one-third, with a slight gradient transition effect on the portrait.
```

---

## 11. Cinematic Keyframe Director (XML meta-prompt)

Source: @underwoodxie96.

```
<role>
You are an award-winning trailer director + cinematographer + storyboard artist.
Turn ONE reference image into a cohesive cinematic short sequence, then output
AI-video-ready keyframes.
</role>

<non-negotiable rules - continuity & truthfulness>
1) First, analyze the full composition: identify ALL key subjects and describe spatial
   relationships and interactions.
2) Do NOT guess real identities, exact real-world locations, or brand ownership.
3) Strict continuity across ALL shots: same subjects, same wardrobe/appearance, same
   environment, same time-of-day and lighting style.
4) Depth of field must be realistic: deeper in wides, shallower in close-ups.
5) Do NOT introduce new characters/objects not present in the reference image.
</non-negotiable rules>

<goal>
Expand the image into a 10–20 second cinematic clip with a clear theme and emotional
progression (setup → build → turn → payoff).
</goal>

<step 1 - scene breakdown>
Output: subjects list, environment + lighting, 3–6 visual anchors.
</step 1 - scene breakdown>

<step 2 - theme & story>
Propose: theme (one sentence), logline, 4-beat emotional arc.
</step 2 - theme & story>

<step 3 - cinematic approach>
Shot progression strategy, camera movement plan, lens suggestions, light & color.
</step 3 - cinematic approach>

<step 4 - keyframes>
9–12 keyframes. Each must be a plausible continuation within the SAME environment.
</step 4 - keyframes>

<step 5 - contact sheet>
Output ONE master image: a Cinematic Contact Sheet / Storyboard Grid containing ALL
keyframes in one large image. Default grid: 3x3. Labels in safe margins, never covering
the subject. Strict continuity across ALL panels.
</step 5 - contact sheet>

<final output format>
A) Scene Breakdown
B) Theme & Story
C) Cinematic Approach
D) Keyframes list
E) ONE Master Contact Sheet Image
</final output format>
```

---

## 12. Split-View Realistic/Wireframe Render

Source: @michalmalewicz.

```
Create a high-quality, realistic 3D render of exactly one instance of the object:
[Orange iPhone 17 Pro].
The object must float freely in mid-air and be gently tilted and rotated in 3D space.
Use a soft, minimalist dark background in a clean 1080×1080 composition.

Left Half — Full Realism:
accurate materials, colors, textures, reflections, and proportions. Completely opaque.

Right Half — Hard Cut Wireframe Interior:
Boundary between halves: perfectly vertical, perfectly sharp crisp cut line from top
to bottom. No diagonal edges, no curved slicing, no gradient.
Wireframe: white (≈80% of lines), accent color sampled from realistic half (<20%).
Thin, precise, engineering-style. Every wireframe component must perfectly match
the geometry.

Strict Single-Object Rule:
Render only ONE object. Do NOT show a second object — not as reflection, shadow,
silhouette, outline, ghost image, transparency, comparison, or extra device behind.
The object must appear alone, floating.

Soft neutral global illumination, no shadows under the object. No text, no labels.
```

---

## 13. Chibi Proposal Scene (mixed-style)

Source: @balconychy via awesome-nano-banana cases.

```
Transform the two people in the photo into chibi-style 3D cartoon characters.
Change the scene to a proposal setting, with a soft pastel-colored floral arch in the
background. Use romantic tones for the overall background. Rose petals are scattered
on the ground.

While the characters are rendered in cute chibi 3D style, the environment — including
the arch, lighting, and textures — should be realistic and photorealistic.
```

---

## 14. Emoji Combination (Literal / Short)

Source: Nano Banana official.

```
combine these emojis: 🍌 + 😎, on a white background as a google emoji design
```

Proof that extremely short prompts work when the model has a strong prior (emoji design language).

---

## 15. Coordinate Visualization

Source: Replicate demo.

```
35.6586° N, 139.7454° E at 19:00
```

Pure knowledge-reasoning: model resolves coords + time → Shibuya at dusk. Works because
location lookup is a strong Gemini capability.

---

## 16. RAW iPhone Subway Candid (GPT Image 2)

Best on: GPT Image 2.

Source: @WolfRiccardo via `ZeroLu/awesome-gpt-image`.

```
Create a completely RAW quality, unprocessed, unedited image with full iPhone camera quality.
A subway station in USA, a momentary blur. The subway is in motion. In front of the subway,
there is an elderly woman and man.
```

---

## 17. Convenience-Store Night Slice (GPT Image 2)

Best on: GPT Image 2 (also runs on Nano Banana Pro with anti-glamour clause).

Source: 卡尔的AI沃茨 via `ZeroLu/awesome-gpt-image`.

```
Create an ultra-realistic urban street group photo at a convenience store entrance at 10 PM
summer night. 3-4 young people briefly chatting at the entrance, someone holding drinks,
someone sitting on plastic outdoor chairs, someone standing looking at their phone.

Bright white light streaming through the glass doors and windows, warm yellow street lights
and distant car headlights outside. Characters wearing everyday clothes: T-shirts, shirts,
shorts, jeans, sneakers. No internet celebrity styling. Faces and postures must look like
real pedestrians, not overly polished.

Environment must include real convenience store elements: freezer stickers, promotional posters,
trash cans, entrance mats, glass reflections, shared bikes on roadside, water droplets from
drink bottles on ground.

The image should look like a very authentic life slice captured by a photographer in the city.
Focus on testing natural multi-person interactions, night convenience store lighting, glass
reflections, and ordinary people's vibe restoration.
```

---

## 18. Exploded-View VR Headset Poster (GPT Image 2 / JSON)

Best on: GPT Image 2.

Source: featured prompt via `YouMind-OpenLab/awesome-gpt-image-2`.

```json
{
  "type": "exploded view product diagram poster",
  "subject": "VR headset",
  "style": "clean high-tech 3D render, studio lighting, glowing accents",
  "background": "{argument name=\"background color\" default=\"soft purple and blue gradient\"}",
  "header": {
    "logo": "∞ {argument name=\"product name\" default=\"Meta Quest 3\"}",
    "subtitle": "{argument name=\"main catchphrase\" default=\"new reality, new structure\"}"
  },
  "layout": {
    "centerpiece": "vertically stacked exploded view of a VR headset showing 9 distinct layers of internal components: outer shell, camera sensors, motherboard with chip, pancake lenses, internal frame, battery packs, side straps, top strap, and facial interface cushion.",
    "callout_labels": {
      "count": 8,
      "left_side": [
        "Snapdragon® XR2 Gen 2 — overwhelming processing power for real-time experience",
        "Adjustable IPD mechanism — comfortable fit for a wide range of users",
        "Precision-engineered head strap — ergonomics tuned for long sessions"
      ],
      "right_side": [
        "Faceplate — refined design and balanced weight distribution",
        "Tracking cameras — high-precision positional tracking and environment recognition",
        "Pancake lenses — slim profile, wide field of view, sharp imagery",
        "High-performance battery — optimized power for long runtime",
        "Soft face interface — comfort that lasts during extended wear"
      ]
    },
    "footer": {
      "headline": "Experience evolves from structure",
      "body": "Every component is built to support immersion. Meta Quest 3 surfaces the future from the inside out."
    }
  }
}
```

---

## 19. 35mm Direct-Flash Editorial Portrait (GPT Image 2)

Best on: GPT Image 2 (also runs on Nano Banana Pro / FLUX Krea).

Source: @BubbleBrain via `ZeroLu/awesome-gpt-image`.

Excerpted prompt shape (full original is much longer):

```
35mm color film photography with harsh direct on-camera flash, specular highlights on skin
and clothing, strong catchlights in eyes, high contrast flash illumination, authentic film
grain and color shift, high-fashion fresh innocent [SETTING] editorial style.

Intimate first-person low-angle POV shot from below.

Subject: [DETAILED_SUBJECT_DESCRIPTION].
Wardrobe: [WARDROBE].
Pose: [POSE_DETAIL].
Expression / gaze: [EXPRESSION].

Harsh direct on-camera flash creating sharp specular highlights and strong catchlights.
Background: [BG_DESCRIPTION] with motion blur or shallow DOF.

High contrast film color grading with natural flash look. Extremely sharp yet soft skin
rendering. Authentic 35mm direct flash aesthetic. Natural hair strands. Realistic fabric texture.

NO plastic skin, NO digital over-sharpening, NO airbrushing, NO blemishes, NO moles,
NO oily skin, NO watermark, NO text.

[Aspect ratio, e.g. --ar 9:16 / "9:16 vertical"].
```

---

## 20. 360 Equirectangular Panorama (Brevity Prompt)

Best on: GPT Image 2 (model resolves the equirectangular projection prior).

Source: @LexnLin via `ZeroLu/awesome-gpt-image`.

```
360 equirectangular image of [PLACE]
```

Like the emoji-combination prompt (#14), proof that extreme brevity works when the model has a strong prior.

---

## Pattern Index (which file to read for what)

| Need | Read |
|---|---|
| General vocabulary and failure fixes | `patterns.md` |
| Ready-to-fill template for a category | `templates.md` |
| Face / identity preservation issues | `identity-preservation.md` |
| JSON / YAML / XML prompt shapes | `structured-prompts.md` |
| Text, quotes, CJK, infographic labels | `text-rendering.md` |
| Editing, inpainting, multi-image fusion | `editing-workflow.md` |
| Per-model syntax / flags / params | `models/<model>.md` |
| Copy-paste reference prompts | this file |
