# Chapter 05: Color

## Core Idea
Picking "pretty" colours does not work; a slide palette is built consciously and then applied by role. Start from one main colour chosen for the topic and the feelings it must convey, define it precisely (hue, saturation, lightness — "green" is not a choice, there are hundreds of thousands of greens), then add very few colours with a standard harmony or, most reliably, derive light and dark tints of that same hue. Every colour gets a job: a near-black for text and dark slides, a near-white for most backgrounds, the base hue as the accent for small elements, extra tints only for charts and illustrations. Colour is always relative (Josef Albers, *Interaction of Color*): it changes with its neighbours, with what sits on top or underneath, and with the percentage used — so palettes are judged on real slides, with a contrast check, and across the whole deck, where background colour also creates rhythm and signals structure. Never keep software default colours, never pure black on pure white, and never a rainbow.

## Frameworks Introduced
- **Three properties of colour**: hue (red, green…), lightness (closeness to white or black), saturation (how pure vs. how much grey it contains).
  When to use: whenever you define or adjust a colour; describe colours this way instead of by name.
- **Monochrome palette from one hue (Shadowlord-style tints/shades)**: enter the main HEX into a tint/shade generator; keep the base (0%) as accent, ~90% darker for text, ~90% lighter for backgrounds; keep 0/20/40/60/80/90% steps for charts and illustrations. Inverting light and dark gives a dark version with the same palette.
  When to use: the fastest coherent palette for any deck, especially from a brand's single main colour.
- **Colour roles map**: background (near-white) · text and partial backgrounds/cover/break slides/back cover (near-black or deep tint) · accent (base hue, small elements, 2–3 key words, icons, page number) · data tints (lighter/darker steps for charts, diagrams, icons, illustrations). Variant: 3 main colours + 6 tints of different lightness based on the darkest one.
  When to use: before designing the first slide; saves time and guarantees consistency.
- **Standard harmonies (12-colour wheel)**: monochrome (one hue, light and dark tones — calm, not aggressive); complementary (opposites — daring: add white, never overlap them or set them small side by side, or they vibrate); analogous (three neighbours — one main, the other two only as accents); neutral triad (white + black, or white + grey, plus one colour — the easiest).
  When to use: when you need more than one hue; the neutral triad is the safe default.
- **Background rhythm by slide type**: cover in the main colour, content slides white/light, section dividers in the secondary colour, closing slide identical to the cover.
  When to use: every deck; strictly in long trainings (2–3 hours), with more freedom in 5–10-minute talks.
- **Colour psychology, read with context**: universal associations exist but are also subjective (personal experience) and shift with hue, pairings and quantity.
  When to use: choosing the first colour; always check how a reference used it on a similar topic.

## Rules & Numbers
**Palette size**
- 2–3 colours are usually enough; white and black (or their substitutes) are counted on top.
- Max 4 colours defined in the theme (PowerPoint's scheme has 12 slots, including two hyperlink colours). Too many colours become a "harlequin".
- One accent colour across the deck, to avoid the rainbow effect.
- When the client has a corporate template/palette, use it; otherwise build a custom one. Never the default palettes of PowerPoint, Keynote or Google Slides ("seen a thousand times").

**Choosing the main colour**
- Topic + psychological effect. Look at how designers used colour on similar topics on Dribbble, Behance, Pinterest (less obvious than a web search) and on award-winning websites (e.g. Awwwards) — websites are a more evolved, similar medium.
- Sample from the brand's materials (site, social, letterhead, brochure) or from the main images (eyedropper/picker). If photos are the focus of the deck, take text and shape colours from the photos.
- A colour sampled for a dark background usually needs more saturation and lightness (flag colours look dull on black).
- Context: serious presentations avoid very strong colours; school/young audiences can take more saturation (e.g. a boosted blue plus a fluo yellow accent).
- Photo portfolios: white or black backgrounds only — a coloured background alters the photos.

**Near-white and near-black instead of pure**
- Text never pure black: very dark grey or a deep colour (night blue, dark green, bordeaux), ideally a dark taken from the images with the eyedropper.
- Backgrounds never pure white: very light grey or off-white with a cool or warm undertone; projected pure white tires the eyes. Cream instead of white gives an innovative but non-technological feel.
- Pure black on white is too much contrast; dark grey is the default (black is an exception when it pairs better with the content).
- Blue text: use a blue tending to black/grey.

**Red as accent**
- Red works almost only with neutrals (white, cream, grey, black); as an accent on black or white it is elegant and energetic. Generally not the right colour for a whole series of slides — use it at precise moments.
- Never black text on red (unreadable or gloomy): white text on red.
- Highly saturated red as a background is excessive; coral (lighter, less saturated) holds as background and on titles.
- Red on saturated pink hurts small text: desaturate and lighten the pink.
- Purple-red (dark, low saturation): fine as accent on white, gloomy on black.
- Hue sets the tone: purple-red = elegant, coral = innovative. Keep red palettes as conservative as possible: red + grey or white.
- In charts/interfaces red signals alert: errors, irreversible actions, negative trends — reserve red in charts for negative data.

**Contrast and legibility**
- Always verify text/background contrast with a contrast checker, on the real slide, not as swatches side by side.
- Known bad pairs: yellow on yellow; grey on blue (use white); black on blue; black on green (gloomy); light pink on white (raise contrast); light green highlight text (use an underline in that colour instead).
- Red is hard for titles.
- Complementary pairs never small and adjacent (vibration).

**Gradients**
- Difficult; risk of looking "90s/trash". Light, few colours (2, not PowerPoint's default 4 theme colours), used as background only or limited to titles in a precise style (e.g. Apple-like).
- With strong colours pick neighbours (green → teal, yellow → orange), never high-contrast pairs like green/red; add white to soften; try a radial gradient as a glow; on black, a moving glow guides focus between slides.
- Tech/AI covers: mesh gradients (made with a free generator and imported as an image) instead of linear ones.

**Shadows and icons in colour**
- Coloured shadows (main colour instead of black) tie into titles, icons and highlighted words.
- Icons and illustrations always in the palette colours.
- Partner logos: all monochrome (black-and-white, all white or all black depending on background), with each brand's approval.

**Formats**
- HEX for screen, CMYK for print. Copy HEX codes into the software rather than exporting palette images.

## Procedures
**Build a palette in Coolors**
1. Palette generator: space bar for random palettes; lock the colour you already have; view shades, remove/move, copy HEX.
2. Three-dot menu > Generate method: monochromatic, analogous, complementary, etc.
3. Explore palettes: search by theme (e.g. "nature" — spring greens vs autumn earth tones), colour, style, number of colours.
4. Image picker: sample colours from a photo (slider and +/- colours), open in the generator.
5. Other tools: contrast checker, image colorizer for SVG, gradient palette (in-between steps of two colours), colour picker (names, HEX/RGB/CMYK conversion, lightness variants, temperature, harmonies including split-complementary and triad).

**Find colours from a word (Picular)**: type a keyword (e.g. "sustainability"), press Enter, click a colour to copy its code, paste in the slides. Useful when the client has no palette.

**Monochrome palette (Shadowlord)**
1. Enter the HEX.
2. Copy one much lighter and one much darker tint (strong contrast between them).
3. Light = background, dark = text, base = accent on a few pieces of information.
4. Keep 0/20/40/60/80/90% steps for charts; invert light/dark for dark slides.

**Make the palette the theme (PowerPoint)**
1. Sample colours from an image: draw squares, Fill > More colours > eyedropper.
2. View > Slide Master > Colours > Customise colours; assign them and name the palette.
3. Always pick from "Theme colours" (above "Recent colours"), never via More colours/recent: theme colours propagate to charts, image recolouring and shapes, and a colour used on hundreds of objects changes at once.
- Google Slides has no eyedropper: screenshot, sample with an online colour picker, add as custom colours. Canva: text colour picker > "Photo colours" uses colours of images in the project.

**Transpose a template's colours**: map its three roles — white background → very light beige, black text → dark brown or very dark green, accent → a green of similar lightness; optionally invert light/dark.

## Common Mistakes
- Default theme colours → custom or brand palette.
- Choosing a colour by name only ("green") → define hue, saturation, lightness.
- Rainbow deck / many unrelated colours → 1 main + neutrals + at most one accent.
- Pure black text on pure white → near-black on off-white.
- Black text on red or on dark images → white.
- Saturated red full-bleed backgrounds → coral, or red as accent only.
- Colours picked from "recent colours" → theme colours.
- Background colours alternating with no rule → colour assigned per slide type.
- Four-colour default gradients → two neighbouring hues, light.
- Evaluating swatches in isolation → test on the slides and in the projection setting.

## Mental Models
- Colour is relative: the same red reads differently next to cream, grey or black and at 5% vs 60% of the surface.
- Every colour added changes the psychological meaning, by quantity and position too.
- Roles beat beauty: a dull hue used consistently in fixed roles looks more professional than five beautiful colours used at random.
- Background colour is structural information: the audience learns cover/divider/content colours and knows where it is.
- Psychology of red as a worked example: love (Valentine's), power and boldness (the red car), energy and appetite (restaurants), danger and maximum visibility (stop signs) — the meaning that wins depends on hue, pairing and amount.

## Examples
- A brand purple derived by mixing two earlier identity colours (a blue and a red), read as ambition and wisdom.
- Five red websites: a city site with flag red as accent on white and black; a tech site with coral, very dark grey and off-white; an infrared/innovation site with red-orange, pink and cream; a literature site with purple-red on black and white; a historical memorial with dull blood red, grey and white.
- A design-project index: black on green replaced by green/beige/white; covers and dividers green, index and contents beige.
- A school slide: blue saturation increased, fluo yellow introduced only to highlight "10 rules".
- An AI-startup slide: pure black text replaced with a deep blue sampled from the image; gradient text reduced from 4 colours to 2.
- A list redesign: white background with blue and grey as the only accents, blue icons on grey squares.
