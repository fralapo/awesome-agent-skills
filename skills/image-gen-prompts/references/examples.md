# Curated Working Examples

Each example is a real prompt that produced good output in the source repo. Use as reference shapes, not verbatim — swap in your own subject/constraints.

Attribution: prompts from the 12 community repos and 3 reference sites analyzed (Super-Maker-AI, YouMind-OpenLab nano-banana-pro, PicoTrex, jimmylv, ZeroLu/awesome-nanobanana-pro, ZeroLu/awesome-gpt-image, YouMind-OpenLab/awesome-gpt-image-2, EvoLinkAI/awesome-gpt-image-2-prompts, wangrunlin/awesome-gpt-image-2-5-prompts, LaplaceYoung/awesome-gpt-image-2.5, VulcanEon/awesome-gpt-image-2.5-prompts, marc-aurele-besner/prompts, openart.ai packaging-design + mockup posts, godofprompt.ai prompt marketplace). Original authors noted where known.

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

## 21. Luxury Perfume on Marble Vanity (E-commerce Main Image)

Best on: GPT Image 2 (high-fidelity reflective product surfaces). Also runs on Imagen 4 / FLUX Krea.

Source: `EvoLinkAI/awesome-gpt-image-2-prompts` Case 118 (@MiguelMaestroIA).

Prompt shape:

```
Ultra-realistic e-commerce main image. A frosted-amber [PERFUME_BOTTLE] of "[BRAND_NAME]"
displayed on a polished marble vanity. Surrounding props: [PETAL_OR_BOTANICAL_DETAILS,
EAU-DE-PARFUM_BOX, ATOMIZER_PUFF].
Lighting: warm directional key from upper-right, soft fill from front, gentle rim along
the bottle's left edge, specular highlight on the cap. Subtle reflection on the marble surface.
Camera: 100mm f/8 macro, 3/4 frontal, slight elevation, sharp focus on the front label.
Label reads "[BRAND_NAME]" in [FONT]. Crisp letterpress feel, no warping.
Color palette: warm ambers, ivory, polished gold accents.
1:1 square e-commerce hero, ample padding, premium editorial mood.
```

---

## 22. 9-Panel Product TVC Storyboard

Best on: GPT Image 2 (single-prompt cross-panel consistency).

Source: `EvoLinkAI/awesome-gpt-image-2-prompts` Case 160 (@Magncsans).

```
Generate a 9-panel TVC storyboard for [PRODUCT_NAME], 3x3 grid, 16:9 frame.
Same product across all panels — identical packaging design, color, and proportions.
Same overall lighting style and color grade.

Panels:
1. Wide establishing shot — [LOCATION + TIME_OF_DAY]
2. Push-in to product on [SURFACE]
3. Hero close-up of front label
4. Macro detail of [SPECIFIC_FEATURE — texture, ingredient, finish]
5. Hand interaction — opening / pouring / pressing
6. Lifestyle context — [USER_PERSONA] using the product
7. Result / payoff — [BEFORE/AFTER or REACTION]
8. Brand logo card with tagline "[TAGLINE]"
9. Call-to-action card — "[CTA_TEXT]"

Each panel labeled with shot number in safe margin. Continuity across all 9. Cinematic color grading.
```

---

## 23. Vintage Photo Restoration

Best on: GPT Image 2 (strong restoration prior).

Source: `EvoLinkAI/awesome-gpt-image-2-prompts` Case 82 (@gdb).

```
Restore the attached vintage photograph. Preserve composition, framing, the subjects' identity
(face structure, age, period-accurate hairstyles), wardrobe, and overall era of styling.
Repair: scratches, creases, dust, faded color, chemical staining, low contrast.
Do NOT modernize: clothing remains period-accurate, hair/makeup remain era-correct,
print grain remains visible.
Output: high-resolution, gently colorized, restored photo print look.
```

---

## 24. Style-to-UI Landing Page (Reference-driven)

Best on: GPT Image 2.

Source: `EvoLinkAI/awesome-gpt-image-2-prompts` Case 42 (@D_studioproject).

```
Create a landing page mockup using the attached image as a reference for style and color grading.
Match the reference's saturation, contrast, typography mood, and density without copying any
literal element.

Page content:
- Hero: large headline reading "[HERO_HEADLINE]", subhead "[SUBHEAD]", primary CTA button "[CTA_TEXT]"
- Below hero: [N]-card feature grid with [TOPIC_LIST]
- Footer: [FOOTER_BRIEF]

Render as a hyper-realistic UI mockup displayed on a [DEVICE — slim modern laptop / 4K monitor]
on a [SURFACE]. Soft natural daylight, gentle screen glow, subtle device reflections.
Crisp typography. 16:9 landscape. No moiré, no text artifacts.
```

---

## 25. Full Web-Page Mockup with Height Allocation (GPT Image 2.5)

Best on: GPT Image 2.5 Sunburst (dense CJK UI copy).

Source: `wangrunlin/awesome-gpt-image-2-5-prompts` — chinese-agency-page-layout (@listudio). Condensed; original lists every Chinese UI string.

```
Generate a complete visual design of the official website of [COMPANY / SECTOR], a long screenshot
of the desktop webpage, frontal view, no perspective, 9:16 vertical, complete from navigation to footer.
[BACKGROUND] with [4 NAMED COLORS], neat grid, right-angled cards, [STYLE MOTIF].

Slim navigation bar at the top: wordmark "[BRAND]" and slogan "[SLOGAN]" on the left; navigation
"[ITEM 1, ITEM 2, ITEM 3, ITEM 4]" on the right; a "[CTA →]" button at the far right.
The hero occupies about 27% of the image: two-line headline "[LINE 1]" / "[LINE 2]" in bold [COLOR]
sans-serif on the left; [HERO SUBJECT, wardrobe, light] on the right.
Concept bar about 8% · services about 16% (three equal cards: "[A]", "[B]", "[C]") · works about 17%
(four thumbnails titled "[W1]", "[W2]", "[W3]", "[W4]") · recruitment band about 18% · news about 6%
(three dated lines) · footer about 8% with "© [YEAR] [BRAND]".

All interface copy is readable and accurate [LANGUAGE], with clear title/body levels.
No garbled characters, no third-party logos, no watermarks, no browser borders, no device cases.
Output a complete web design drawing.
```

Check: section shares sum to 100%; proofread small text at full size. It's an image, not HTML.

---

## 26. Three-Reference Product Ad with Conflict Priority (GPT Image 2.5)

Best on: GPT Image 2.5.

Source: `wangrunlin/awesome-gpt-image-2-5-prompts` — three-reference-product-ad (@jackzhang123vip).

```
Image 1 is the primary reference for the product itself; Image 2 provides only the color, lighting,
tonal values, and overall atmosphere; Image 3 provides only the composition, product placement,
visual proportions, and negative space structure.
Conflict priority: Product authenticity and label accuracy from Image 1 > Layout structure from
Image 3 > Color and lighting from Image 2.
Create a 1024×1536 vertical commercial product advertisement. Use the exact [PRODUCT] from Image 1,
placing it fully on the left side of the frame, while reserving a large, clean, uniform area of
negative space for copy on the right, as shown in Image 3. Apply the atmosphere from Image 2 —
[LIGHT DIRECTION, TONES] — but do not replicate the objects found in Image 2.
Fully preserve the product's shape, proportions, materials, label size and placement, and the
label text ("[LINE 1]" and "[LINE 2]"). The text must be clear, in the correct order, and appear
only on the product label. Do not redesign, recolor, distort, crop, duplicate, or alter the product.
Only physically accurate reflections and natural contact shadows may be added.
No text on the right side. Do not replicate props, text, logos or branding from Image 2 or Image 3.
Do not add copy, placeholder text, garbled characters, QR codes, watermarks, props, people, or a second product.
```

---

## 27. Replace the Product in a Fixed Poster (GPT Image 2.5)

Best on: GPT Image 2.5.

Source: `wangrunlin/awesome-gpt-image-2-5-prompts` — fixed-template-product-swap (@AdrianPunk115).

```
Please edit Image 1 by replacing the main product with the product shown in Image 2.
Strictly separate the functions of the two reference images:
Image 1 dictates the advertising composition, background, lighting direction, decorative elements,
and text layout (excluding the product itself).
Image 2 dictates the new product's authentic shape, structure, material, color, logo, and packaging details.
Remove the old product from Image 1 and naturally place the product from Image 2 into the area
previously occupied by the original product.
Preserve the authentic aspect ratio of the product from Image 2; do not squash, stretch, or alter its
structure to fit the original outline. You may scale the product proportionally as a whole.
Modify only the area occupied by the new product, along with any necessary contact shadows,
occlusions, and local reflections. Do not recreate the entire poster.
Keep the headline, text content, font, font size, positioning, background texture, decorative
elements, and canvas dimensions unchanged.
Do not create a hybrid design combining the two products. Do not retain the old product's cap,
handle, label, or other components. Do not add accessories not present in Image 2, do not guess
at illegible packaging text, and do not alter the product's color to match the background.
Output only the single, completed poster with the product replaced.
```

---

## 28. Person Holding a Reference Product (GPT Image 2.5)

Best on: GPT Image 2.5.

Source: `wangrunlin/awesome-gpt-image-2-5-prompts` — person-holding-reference-product (@AdrianPunk115). Condensed.

```
Generate a natural, realistic product display photo based on the two uploaded images.
Image 1 = the person: identity, facial features, hairstyle, skin tone, clothing.
Image 2 = the product: shape, structure, color, material, logo, packaging details.
The person holds the product as if showing it to the camera, in front of the chest or side-front,
main display face toward the camera, never covering the face.
Choose a logical grip for the product's shape: fingers wrap, cradle or pinch it with correct
foreground/background layering and contact shadows. The hand must not clip into the product,
and the product must not float above the palm.
Preserve the person's face, apparent age and body shape; only arm and hand positions may change.
Do not redesign the product, mirror the logo or add accessories.
Same lighting environment for person and product; keep the person's original background, simplified.
3:4 vertical. No titles, slogans or customer reviews.
```

---

## 29. Japanese-Film Colour Grade Without Redrawing (GPT Image 2.5)

Best on: GPT Image 2.5.

Source: `wangrunlin/awesome-gpt-image-2-5-prompts` — garden-photo-color-grading (@HoodyLiu). Condensed.

```
Only perform professional color grading and light-and-shadow optimization on the original photo.
Strictly retain the original composition, scenery positions, [KEY OBJECTS] and proportions; do not
add, delete or change any objects.
Style: high-end, restrained, quiet Japanese film look.
Brighten dark details moderately but keep deep shadows (no gray blacks). Reduce sky highlights and
blue saturation to a calm gray-blue, no HDR. [HERO ELEMENT] in natural [COLOR], not pure white or
fluorescent. Greens to low-saturated moss / forest / slight olive; reduce yellow-green digital feel.
Soft highlights, deep shadows, medium-strong contrast, warm sun vs cool shadow.
Slight film fog, natural halation, fine 35mm grain, soft sharpening; color reference Kodak Portra 400.
Prohibited: changing composition, adding objects/clouds/people/lights, new branches, season change,
overexposure, crushed blacks, HDR, over-sharpening, fluorescent green, heavy filters, painterly or
illustration feel, AI-redrawing feel.
The result must look like a professional color correction of the original RAW photo, not a regenerated image.
```

Check: inspect branches, reflections and small objects for redraws.

---

## 30. Character Production Reference Sheet (GPT Image 2.5)

Best on: GPT Image 2.5 Sunburst.

Source: `wangrunlin/awesome-gpt-image-2-5-prompts` — character-design-reference-sheet (@meAsifAi, 1.3k likes). Condensed from 9 numbered sections.

```
Create a premium professional character design reference sheet based strictly on the provided reference image.

REFERENCE & IDENTITY LOCK: the uploaded reference is the single source of truth. Preserve exact facial
identity, hairline, eye shape/color, skin tone, body proportions, costume, accessories, colors, patterns.
Do not redesign, beautify, simplify, age or de-age. Before constructing the sheet, internally analyze
and lock: facial construction, head-to-body ratio, silhouette, costume construction, accessory placement,
color relationships, materials, identity anchors.

PAGE: one studio-grade board, landscape 16:9, off-white background, subtle guide lines, restrained labels.
01 HERO PORTRAIT · 02 FULL-BODY TURNAROUND (front, 3/4 front, side, 3/4 back, back — identical scale,
aligned head/shoulder/waist/knee lines) · 03 EXPRESSIONS (neutral, smile, serious, determined, surprised,
sad) · 04 SIGNATURE POSES (4–6) · 05 COSTUME & DETAIL CALLOUTS · 06 MATERIAL STUDIES · 07 COLOR PALETTE
(skin, hair, primary, secondary, accent) · 08 PROPORTION & SILHOUETTE GUIDE · 09 DESIGN CONTINUITY
(identical identity, costume, accessory placement, consistent left/right details).

CAMERA: orthographic-like turnaround; consistent head framing for expressions.
LIGHTING: neutral studio light for design inspection, not cinematic drama.
NEGATIVE: no identity drift, costume variations, missing or duplicated accessories, extra limbs,
malformed hands, random props, dramatic scenery, clutter, watermark, logo, cropped views.
```

---

## 31. Pixel-Art Pet Sprite Sheet → GIF (GPT Image 2.5 + Python)

Best on: ChatGPT Images 2.5 (needs a chat that can also run Python).

Source: `wangrunlin/awesome-gpt-image-2-5-prompts` — pixel-pet-loop (@Mayz1169). Condensed.

```
Turn the pet in my uploaded reference into an adorable pixel-art sprite with a subtle, seamless
looping idle animation. Preserve species, colors, markings, eye color, accessories; chibi proportions
but recognizable anatomy. Do not add limbs or features the animal does not have.
STYLE: crisp square pixels, clean outlines, limited palette; no anti-aliased or vector edges.
ANIMATION: 16 consecutive frames of one gentle idle — breathing + one secondary motion (ear twitch,
tail sway) + one blink only if the species has eyelids. Same position, anchored contact points,
no walking/turning/camera movement. Last frame flows back into the first.
SPRITE SHEET: exactly 4 columns × 4 rows, left→right, top→bottom; canvas 1024×1024, cells 256×256;
fixed body anchor and baseline; ≥16 px transparent padding in every cell; same pet, not variations;
no grid lines, labels, text or watermarks.
TRANSPARENCY: genuine RGBA, alpha zero outside the pet; no checkerboard, floor or shadow.
DELIVERABLES: 1) the PNG sheet; 2) a transparent looping GIF, 150 ms per frame; 3) a ZIP of
frame_01.png…frame_16.png. Split into equal cells on one shared canvas (no per-frame crop/scale),
nearest-neighbor resizing, correct GIF disposal. Inspect all frames before exporting.
If you cannot create the GIF or ZIP, say which deliverables are missing.
```

---

## 32. Exact Copy on Products and Billboards (OpenAI guide, GPT Image 2.5)

Best on: GPT Image 2.5 Flare / Sunburst. Settings: `1024x1536`, `quality=medium`.

Source: OpenAI image-prompting guide examples, via `wangrunlin/awesome-gpt-image-2-5-prompts` and `VulcanEon/awesome-gpt-image-2.5-prompts`.

```
Create a collectible action figure of a vintage-style toy propeller airplane with rounded wings,
a front-mounted spinning propeller, slightly worn paint edges, classic childhood proportions,
designed as a nostalgic holiday collectible, in blister packaging.

Style:
Premium toy photography, realistic plastic and painted metal textures, studio lighting,
shallow depth of field, sharp label printing, high-end retail presentation.

Constraints:
- Original design only
- No trademarks
- No watermarks
- No logos

Include ONLY this packaging text (verbatim):
"Christmas Memories Edition"
```

Two-turn variant (turn 2 edits turn 1's output in the same conversation):

```
T1  Create a realistic billboard mockup of the shampoo on a highway scene during sunset.
    Billboard text (EXACT, verbatim, no extra characters):
    "Fresh and clean"
    Typography: bold sans-serif, high contrast, centered, clean kerning.
    Ensure text appears once and is perfectly legible. No watermarks, no logos.
T2  Make it look like a winter evening with snowfall.
```

---

## 33. Text-Free Scene That Resists Invented Lettering (GPT Image 2.5)

Best on: GPT Image 2.5.

Source: `VulcanEon/awesome-gpt-image-2.5-prompts` — cyberpunk-without-copy (written as a fix for a documented failure where the model invented signage).

```
Restyle my adult portrait as a rainy near-future street photograph. Keep my face, age and expression.
Use violet rim light, cyan window reflections and a dark technical jacket. Every illuminated panel
must show only abstract gradients or geometric light, never letters or symbols resembling writing.
Include no slogans, subtitles, labels, logos or watermark. Keep visible skin naturally textured.
Return one portrait image rather than a poster or magazine cover.
```

Check: zoom into every luminous panel and smooth surface; if pseudo-lettering remains, use the *Remove invented lettering* repair recipe.

---

## 34. Selective Sharpness Against Motion (GPT Image 2.5)

Best on: GPT Image 2.5.

Source: `VulcanEon/awesome-gpt-image-2.5-prompts` — subway-stillness (visual reconstruction, not a verified reproduction).

```
Photograph an adult standing safely behind the platform warning line while a train passes behind
them. Keep the eyes, face and orange flower bouquet sharp; let only the train stretch into
horizontal motion blur. Use a cream knit sweater against cool gray station materials. A breeze
lifts a few hair strands without blurring the face. Blend soft overhead light with warmer skin
highlights. Portrait framing, natural pores and wool fibers. No platform-edge pose, extra hands,
text overlays or smeared flowers.
```

Check: blur follows one direction and spares the person, hands and bouquet.

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
