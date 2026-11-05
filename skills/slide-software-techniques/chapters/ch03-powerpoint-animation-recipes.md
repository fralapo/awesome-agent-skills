# Chapter 03: PowerPoint Morph & Animation Recipes

## Core Idea
Good motion in slides does not come from complex effects but from a few soft animations (Fade, Morph, Fly In with easing, Wipe for lines) choreographed with timing, order and delays, designed together with the layout rather than added at the end. Morph (Morphing; Keynote's Magic Move, Canva's Match & Move, Figma Slides' Smart Animate) is "a transition that lets you build hundreds of others": build the start state, duplicate the slide, change position/size/rotation/color/opacity, apply Morph to the second slide. Objects must exist on both slides, so things "disappear" by going to 0% opacity or off-slide, never by deletion. Keep durations short (0.3–0.5 s for animations, about 1 s for Morph), use On Click only for what you are saying at that moment, and populate the rest automatically with With Previous + small delays. Most recipes — zoom, slider, gallery, cards, reveal, keyword scroll, tabbed menu — are the same trick: parked objects off-slide, cover rectangles in the background color, and state-per-slide sequences inspired by website interactions.

## Frameworks Introduced
**Animation vs transition**: an animation acts on one object (Entrance, Emphasis, Exit, Motion Path); a transition acts on the whole slide change. Morph is a transition that animates every object common to both slides.
When to use: choose transitions for state changes between layouts, animations for revealing items within one layout.

**Three functions of motion**: functional (focus: one point at a time, enlarge, recolor, move), staging (compose/decompose the scene: a cover that assembles while you introduce the topic), expressive (express brand/topic: a checkered-flag wipe for a racing deck; the hardest, born from research on websites).
When to use: justify every animation with one of the three; if none applies, remove it.

**Style, timing, sequence**: style = which effect (keep a minimal set); timing = duration depending on object size, path length and function; sequence = On Click / With Previous / After Previous plus delays.
When to use: as the review grid for any animated slide.

**State-per-slide**: each state of an interface (active tab, selected color, focused image) becomes one slide; Morph interpolates. "The number of slides is insignificant": five slides can look like three, and more slides do not lengthen the talk.
When to use: converting a website interaction into slides; when one slide's animation pane becomes unmanageable ("make more slides instead of animating everything in one").

**Park off-slide**: objects that will enter are already placed outside the slide (or at 0% opacity) on the earlier slide; objects that leave are moved outside on the later slide.
When to use: every Morph recipe.

**Cover-rectangle mask**: a rectangle filled with the background color, stacked above text/images, hides them; Morph moves the text from under it so it seems to rise from a cut line.
When to use: text reveals, image reveals, word lists that fade out at an edge.

**Speaker control**: content animations On Click, synced with the voice ("I say lemon, lemon appears"); service animations (built transitions, populating a slide, loops) automatic.
When to use: every live deck; avoid making the speaker click 10 times to fill one slide.

## Rules & Numbers
- In PowerPoint Morph is applied to the SECOND slide (the destination); in Keynote Magic Move is applied to the FIRST slide (the origin).
- Morph default 2 s is too slow: use about 1 s for most moves; 0.5–0.7 s for small moves (stacked cards, gallery shifts); 1–1.5 s for large shapes; up to about 2 s only for very large travel/rotation (an oval rotating to cover the slide, a 3D model moving across), where faster looks frantic.
- Entrance animations: 0.3–0.5 s (Fade 0.3 s preferred over the 0.5 s default; 0.5 s acceptable). 1 s for a fade is "an eternity" and creates dead pauses. An element you mention must appear immediately (~0.3 s), not after a second. Long durations only to create suspense.
- Transitions overall: 0.5–1 s, max 1.5 s.
- Delays between staggered items: 0.1 s for fast population of many items (the slide fills in under a second); 0.2 s steps (0.2/0.4/0.6/0.8) when the sequence must be perceived — 0.1 s between text blocks may not register. In PowerPoint delays of With Previous items are counted from the first item of the group.
- Text animation: by word for 1–2 lines (0.3 s, With Previous; 0.7 s for slower loops); by letter only for a single word or short title; never letter-by-letter on paragraphs.
- Fly In: always with Smooth Start + Smooth End on; objects on the left enter from the left, on the right from the right (symmetry allowed); never let entering objects cross.
- Effects worth using: Fade (versatile, "minimum effort, maximum result"), Fly In with easing, Wipe (it. Cascata) left-to-right or bottom-up to "draw" lines, Split (it. Morsa) only on outline-only shapes and lines, Wheel (it. Spirale) with 1 spoke on an outline-only circle to draw a percentage ring, Zoom from object centre (from slide centre only for radial layouts), Grow/Shrink and motion paths for loops.
- Effects to avoid: Blinds, Checkerboard, dotted dissolve, Strips, Shape, Wedge, Bounce and fade-with-bounce, all "exciting" ones (Boomerang, Credits, Spinner-type stunts) unless the context is literal (a basketball, a quiz, a newspaper page). Stretch/Expand only on lines, never on text, images or filled shapes. Pixel dissolve only on images in a "digital" theme. No 3D cube transitions.
- Soft "pro" motion = Fade + a motion/emphasis animation whose easing you can set. Fast animations without easing look like a slam.
- Use the same small animation set from the first to the last slide; one character per slide (no bounce among soft moves).
- Order communicates hierarchy: the biggest/most important element leaves or enters first, then smaller ones.
- Motion feels alive when several attributes change together (position + rotation + size + color + opacity) and objects take different paths/speeds; everything on one axis feels static. Slight rotations (−10°/+10°, 5° for a falling card) make Morph more natural; avoid "twister" rotations.
- Slight offset (one element starts or ends after the other) makes two objects read as distinct and smoother.
- Focus by opacity: active item 100%, inactive 30% (or covered by a background-colored rectangle at ~70% opacity).
- Transition shapes as big as the slide or wider (no white corners); always No Outline; add many-shape transitions at the end of the job, otherwise the slides underneath become unmanageable.
- Morph does not see inside groups: objects that must transform individually must be ungrouped; conversely group items that must move together, otherwise Morph moves them independently or just fades them.
- Group on one slide vs ungrouped on the next = Morph/Magic Move falls back to a fade: insert an identical "pass-through" slide with the group dissolved and automatic advance.
- Pass-through slide timing: transition Fade ~0.01 s (or none), Advance After 0 s. Changing Morph timing with Apply To All also applies "After" everywhere; remove it where not wanted.
- With Morph, remove leftover entrance animations from objects that should stay still, or they vanish and re-enter. Conversely Morph alone makes texts pop out abruptly: complete it with fades on text.
- Loops: motion path + Auto-Reverse + Repeat: Until End of Slide, Smooth Start/End OFF (constant speed), long durations 5–10 s (circular path 10 s, grow 5 s, path 8–15 s, Spin 10 s). Spin 45° instead of 90° with Auto-Reverse for an almost imperceptible drift. Teeter: no Auto-Reverse (it already oscillates), ~2 s, Repeat until end of slide.
- Loops only where they add premium feel (big statement slides in a tech pitch, waiting/intro slides before events/webinars), never everywhere; glows must not overlap or the trick shows.
- 3D models are heavy: insert texts first and the model last; test on the presenting PC (lag).
- Online presenting: animations may lag or stutter; prefer Appear-type reveals one item per click.
- Emphasis animations highlight an object already on the slide (color, glow, grow, spin); motion paths are invisible lines the object follows (preset or custom); combining entrance + emphasis + path, with intent, is what makes advanced slides.
- Morph on a 3D or rotating object: keep rotations moderate (no "twister" effect) and slow the Morph rather than speeding up large travel.
- Corporate rule instead of a ban: allow one fade On Click for focus, 0.3–0.5 s, few clicks per slide.

## Procedures
**A. Morph step by step**
1. Set 1920×1080, Master guides; build slide 1 completely (final positions are easier to design first: build the final composition, then derive earlier slides backwards).
2. Rename key objects in the Selection Pane.
3. Duplicate the slide (Ctrl/Cmd+D); change position, size, rotation, color, opacity. Objects to remove: set fill/text transparency to 100% or move off-slide. Objects to add: paste them into the previous slide off-slide or at 0% opacity in the same position.
4. Select slide 2 > Transitions > Morph; Effect Options > Objects; Duration ~1 s. Preview; if Morph "invents" paths, fix stacking order in the Selection Pane or add a pass-through slide.
5. Add text fades (By word, With Previous, 0.3 s) where Morph alone pops text.

**B. Animation Pane and timing**: Animations > Animation Pane. For each item: Effect Options (direction, Smooth Start/End, Auto-Reverse, Animate text: By word/By letter, Group text: All paragraphs at once so a box and its text appear together); Timing (Start: On Click / With Previous / After Previous, Duration, Delay, Repeat, Rewind when done, Triggers). Animation Painter copies a whole animation set to another object. Drag rows to reorder; move service animations to the top.

**C. Zoom into an image through a frame**: full-slide white rectangle; smaller rectangle centred; select both > Merge Shapes > Subtract → frame with a hole; insert the image and Send to Back; duplicate the slide and scale the frame up until only the image is visible; Morph.

**D. Image slider (product gallery window)**: full-slide white rectangle, No Outline; second rectangle sized to the photo ratio; Merge Shapes > Combine → window; send all photos behind (photo 1 in the window, 2 and 3 off-slide to the right); progress bar = 4 pt grey line + black segment about 1/3 long (shorter with more photos); logo top-left on margins, product name very large (e.g. 200 pt bold), description 24 pt grey bottom-aligned, Multiple 1.1, text box margins 0; duplicate, shift photos one position left and move the segment; repeat; Morph 1 s.

**E. Horizontal scroll**: select all slides > Transitions > Push > Effect Options: From Right. For a continuous timeline, Push left-to-right with the last line segment leaving the slide and continuing on the next.

**F. Gallery with central focus**: three equidistant images, centre larger, sides at Brightness −60% (Picture Format > Corrections); each slide shifts all images by one slot; Morph 0.7–1 s. Thumbnail variant: big rounded image centred with white or black title, next images small top-right / below / one fully off-slide, thumbnails darker; on each slide 1 shrinks left, 2 takes 1's place, etc.; entrance animation on slide 1, fades on texts. If Morph "gets stuck", reorder images in the Selection Pane.

**G. Stacked cards (one point at a time)**: rounded rectangle with all content inside; copy next card into the earlier slide lower and transparent; on the next slide shrink the previous card behind and make it semi-transparent (two visible levels; back copies ~50% transparency and more); Morph. Tilted-cards list: 3–4 cards placed off-slide with different tilts and uneven spacing; next slide brings them in straight, title transparent; Morph.

**H. Tabbed menu navigation**: top bar (footer moved to top) with brand and copyright in white solid rectangles; tabs below (active in accent, e.g. #E9592D, others grey with light grey text), extra tabs off-slide, tabs sent backward; Do not Autofit, margins 0 except ~1.2 on the text side; uppercase bold, slightly tight spacing; next slide: active tab grows to full slide (white with accent text) to host content, others leave; closing slide set to advance automatically so one click closes and opens the next tab; lock the tab in the Selection Pane while adding content; Morph 0.7–1 s.

**I. Chapter boxes instead of static break slides**: footer at top; three equal-height boxes filling the area (first colored, others grey) with text inside, top-left anchored; next slide: grey boxes drop off-slide, colored box fills the space (can turn white for content); return to slide-1 copy; then shift boxes up so the second chapter is colored; Morph.

**J. Glass effect (glassmorphism)**: Design > Format Background > Picture fill; Picture Corrections > Sharpness −100% (Brightness −10% if white text must read); insert the same image as a normal sharp picture exactly matching the background edges, sent to back; rounded rectangle with Fill: Slide background fill (it always shows the right blurred portion even when moved/resized), No Line; for text legibility a black→transparent gradient rectangle at 0° placed via the Selection Pane; shadow: centred, transparency 60–74%, more blur (much lighter on light backgrounds); "glass" edge: gradient line white → white ~78% transparent at 45°. Use sparingly and consistently. A Liquid-Glass look without distortion is fine — distortion would hurt legibility.

**K. Loop animation**: select object > Animations > Motion Paths > Custom Path/Freeform (or Arc, Circle fitted around the target; green = start, red = end); drag the path start onto the object to avoid a jump; Effect Options: Smooth off, Auto-Reverse on (off for a continuous clockwise circle; Reverse Path Direction for anticlockwise); Timing: With Previous, 5–10 s, Repeat: Until End of Slide. Background glows: irregular shapes with gradient from color to the same color at 0% opacity (or soft edges), or a radial PNG gradient (2000×2000, e.g. from Angry Tools' gradient generator) at 50% transparency; red + blue overlap reads purple. Put entrance fades before the loops in the pane.

**L. 3D models**: Insert > 3D Models > Stock 3D Models (search works in local language); rotate with the central handle; entrance with 3D-specific effects (Turntable/Swing, with direction, intensity, axis), With Previous with computed delay; duplicate slide, move/scale/rotate the model and advance a progress bar; Morph ~2 s. Starry background: picture fill, Brightness −65%. Text leaving with Morph: copy it to the next slide, remove its animation, send behind, set text fill 100% transparent and move it with the model.

**M. Text mask reveal (rising words)**: text boxes placed lower and covered by rectangles in the background color (stacking order critical; keep cover shapes yellow while working, then recolor); next slide moves text up into view; Morph or Magic Move. Small extra: Fade-and-move down 0.5 s, distance 3, right after the transition; second line placed lower so it arrives later.

**N. Animated timeline**: one module (date + description grouped) duplicated; dates large (e.g. 200 pt serif) with small era label; step line 1.5–2 pt in accent; 3 dates per slide alternating above/below the line; Fade 0.3 s on date groups, lines with Wipe in the stroke direction, vertical segment With Previous delay 0.2 s, next date After Previous; Push transition for continuity. Minimal variant: one date per slide, thin line at the bottom with outline circles (active filled accent, past filled dark), plain Fade between slides.

**O. Animated keywords**: centre title and list, remove bullets (a centred bullet is never acceptable), enlarge strongly; first word black, others grey; white gradient overlay 100% at top and bottom, transparent in the middle; Morph scrolls the words up, changing which one is black.

**P. Custom transitions with Morph**: growing card (small rounded card becomes full slide, slide-1 content behind on both slides); color bands (three slide-sized rectangles off-slide → overlapping centre, a final white one to land on white; group slide-2 content with the entering band); bars revealing an image (~7 white bars over a big image, scattered off irregularly as the image shrinks); color panel entering from the right sampled from images in 3:2; rotating oval growing to cover the slide with the text as a separate scaling object; image shrinking into a row of white rectangles; grid of B&W images where the chosen one regains color while a rectangle of its dominant color grows (Morph 0.5 s).

**Q. Highlight a product detail**: slide 1 product as is; slide 2 enlarged; a circle frames one detail; text box in free space joined by a connector; Morph.

**R. Tilted text emphasis**: phrase large in grey, emphasized part duplicated in an overlaid white box; By-word Fade 0.3 s With Previous, then emphasis On Click with by-letter Fade 0.3 s. Moving pill indicator: pills of identical width, a separate white rounded rectangle sent backward that moves under the active pill (Cut/Paste it into later slides at the right spot), Morph 1 s.

## Common Mistakes
- Morph left at 2 s → ~1 s (0.5–0.7 s small moves).
- Deleting an object on the next slide → set it transparent or move it off-slide.
- Effects chosen because they are "cute" → each motion must be functional, staging or expressive.
- Ten clicks to build one slide → only cited items On Click, the rest With Previous + 0.1–0.2 s.
- Ungrouped/grouped mismatch between slides → pass-through slide.
- Fly In without Smooth Start/End → enable easing or use Fade.
- Animating a weak layout to save it → fix the graphic first; a trashy animation destroys even good design, a delicate one only improves good design.
- Loops on every slide → only on statement or waiting slides, slow and barely perceptible.
- Copying a website animation literally → adapt: bigger text, thicker strokes, mask moved right instead of centre so text stays large.

## Mental Models
- Animation is choreography: every movement is designed in relation to the others.
- To work, animations must be invisible: the audience notices the message, not the effect.
- "Sometimes a fade is the most beautiful thing you can do."
- Morph is the main "wow" tool in a client PowerPoint, and it must be planned at storyboard stage, not discovered at the end.
- Sketch slides and animations (enter, exit, action) on paper first; otherwise you lose hours in the software.

## Examples
- A smartphone colors page: phone on a black half, color circles on the right; each click slides and recolors the phone while the highlighted circle's outline opacity changes.
- A console launch mock deck: three features on stacked rounded cards, product PNG breaking out of the card, glows below, a progress pill at ~80% transparency with an opaque marker; fades at 0.5 s with 0.2 s staggered delays, product rising at 1 s delay/0.65 s, a card falling off rotated 5°.
- A product page in a furniture-retailer style: window slider with three photos and a progress segment.
- A space-themed trio: stock 3D moon moving and rotating across three slides with a 01/03 progress line.
- A pitch deck for a tech startup: slow glow loops only behind big statement slides; a teetering graphic on the problem slide.
- A list of four services as four vertical photo strips covered by white panels: each reveals in turn, then one expands to full slide (Morph 1 s).
