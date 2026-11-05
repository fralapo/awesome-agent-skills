# Patterns

Concrete, repeatable techniques. Each entry: When to use / How / Trade-offs.

## Five-Setting Master Setup
**When**: opening any new PowerPoint file, even a 10-slide one.
**How**: set 1920×1080 px; in View > Slide Master place 4 margin guides on the top Master (31 / 31 / 16 / 15 cm from centre), define theme fonts and all 12 theme colour slots, set a light footer with slide number, then build layouts for recurring slide types.
**Trade-offs**: slower start; custom layouts only pay off on long decks, but the other four settings always do.

## Indent Levels as Paragraph Styles
**When**: client templates or any deck whose text must stay consistent across many slides.
**How**: on the Master body placeholder, remove bullets, drag indent markers left, format each level as a named style (title, body, caption…), rename the sample text; users switch style with Tab / Shift+Tab.
**Trade-offs**: one placeholder can hold different styles only through levels; users must be told about Tab, so add an instructions slide.

## Locked Template Delivery (.potx)
**When**: corporate delivery where many people add slides.
**How**: save as PowerPoint Template (.potx) with an instructions slide; put repeating art in the Master/layouts so it can't be selected; ship .crtx chart templates separately with install notes.
**Trade-offs**: tables or charts in the Master become uneditable background; chart templates rarely get installed by many users.

## Monochrome Theme in One Minute
**When**: a brand with one main colour, or no usable palette.
**How**: generate shades of the base hue; 90% darker for text and covers, 90% lighter for backgrounds, 0/20/40/60/80/90% steps into Accent 1–6 for charts.
**Trade-offs**: very coherent, but a single hue limits semantic contrast (e.g. best/worst values need extra colours).

## Excel-Linked Report Charts
**When**: periodic reports whose figures change.
**How**: build the chart in Excel, paste into PowerPoint keeping the link; enter percentages as decimals; organise folders before linking.
**Trade-offs**: on Mac links can't be re-pointed if files move; the file depends on the workbook.

## Autofit by Container Type
**When**: setting up every text box or placeholder.
**How**: free text → Resize shape to fit text; fixed cards, pills, tabs → Do not Autofit; never Shrink text on overflow; anchor top.
**Trade-offs**: with Do not Autofit, overflowing text must be handled by hand.

## Text Inside the Shape + Change Shape
**When**: any coloured box carrying text.
**How**: double-click the shape and type; change its silhouette with Edit Shape > Change Shape instead of rebuilding.
**Trade-offs**: none significant; internal margins must be set by hand in PowerPoint.

## Numeric Spacing Instead of Returns
**When**: any paragraph or title block.
**How**: line spacing Exactly (32 → 42 pt) or Multiple 1.1–1.15, titles 0.8–0.95; space after 8–32 pt; no empty returns.
**Trade-offs**: Exactly values must be recalculated if font size changes.

## Group, Align, Distribute
**When**: rows of logos, cards, icon + label units.
**How**: group each unit, then Align (e.g. Middle) and Distribute Horizontally/Vertically; a single selected group aligns to the slide.
**Trade-offs**: Distribute uses the first and last objects as extremes, so place those first.

## Repeat and Paint
**When**: the same formatting must reach many objects.
**How**: format one, then select others and press Ctrl/Cmd+Y; or double-click Format Painter (Esc to stop); Animation Painter for animation sets.
**Trade-offs**: Ctrl/Cmd+Y repeats only the very last action.

## Brightness Recolour for Icons
**When**: a monochrome PNG logo or icon in the wrong colour.
**How**: Brightness +100% for black → white, −100% for white → black; for other colours recolour the SVG in a free colouriser and export PNG.
**Trade-offs**: works only on monochrome PNGs.

## Merge Shapes Mask
**When**: text cut-outs, frames, windows, crescents.
**How**: stack the shape and the text (or two shapes), select both > Merge Shapes > Subtract / Combine / Union; put an image or stock footage behind.
**Trade-offs**: merged text is no longer editable text.

## Stripped-Down Table
**When**: any data table.
**How**: no fills, no borders, then horizontal mid-grey rules only; accent header with white text; merged group headers; right-aligned numbers; best green bold, worst red; highlight rectangles last.
**Trade-offs**: highlight rectangles must be moved by hand when data changes.

## Bubble Percentages
**When**: replacing a pie for one or a few percentages.
**How**: X Y (Scatter) Bubble; X=1, Y=0, sizes 100 and 33; Y min 0 cuts half-circles; labels show bubble size; dashed 100% reference.
**Trade-offs**: fiddly axis setup and a known disappearing-bubble bug (recreate the chart).

## Build-the-End-First Morph
**When**: any Morph or Magic Move sequence.
**How**: design the final composition, duplicate, derive earlier states backwards; rename objects in the Selection Pane; apply Morph to the second slide at ~1 s.
**Trade-offs**: requires storyboard planning; discovering Morph at the end costs hours.

## Park Off-Slide / 100% Transparency
**When**: objects that must enter or leave during a Morph.
**How**: entering objects sit off-slide or at 0% opacity on the earlier slide; leaving objects move off-slide or go transparent on the later slide; never delete.
**Trade-offs**: slides accumulate hidden objects; keep the Selection Pane tidy.

## Pass-Through Slide
**When**: grouping must change between two Morph states.
**How**: insert an identical slide with the group dissolved, Fade ~0.01 s, Advance After 0 s.
**Trade-offs**: extra slides; Apply To All can spread the "After" timing where unwanted.

## Cover-Rectangle Reveal
**When**: rising text, image reveals, lists fading at an edge.
**How**: place text lower under a rectangle in the background colour (keep it yellow while working); next slide moves text up; Morph or Magic Move.
**Trade-offs**: stacking order is critical and breaks easily.

## State-per-Slide Interface
**When**: converting a website interaction (tabs, sliders, galleries) into slides.
**How**: one slide per state, objects shifted by one slot each time, Morph 0.7–1 s; auto-advance closing slides so one click both closes and opens.
**Trade-offs**: many slides, but slide count doesn't lengthen the talk.

## Speaker-Controlled Choreography
**When**: every live deck.
**How**: On Click only for the item you're naming; everything else With Previous with 0.1 s (fast fill) or 0.2 s (noticed sequence) delays; entrances 0.3–0.5 s; Smooth Start/End always on.
**Trade-offs**: requires rehearsal to sync voice and clicks.

## Focus by Opacity
**When**: lists, galleries, process steps where one item is active.
**How**: active 100%, others 30% or under a background-coloured cover at ~70% opacity; side images at Brightness −60%.
**Trade-offs**: dimmed items must stay legible enough to keep context.

## Slow Premium Loop
**When**: big statement slides or waiting slides before events.
**How**: motion path, Auto-Reverse, Repeat Until End of Slide, Smooth off, 5–10 s; glows as gradient shapes or a 2000×2000 radial PNG at 50% transparency.
**Trade-offs**: on every slide it becomes noise; overlapping glows reveal the trick.

## Slide-Background Glass Card
**When**: a card must sit on a busy photo.
**How**: background picture at Sharpness −100%, sharp copy of the image on top, rounded rectangle filled with "Slide background fill", soft shadow, gradient white edge.
**Trade-offs**: use sparingly and consistently; distortion would hurt legibility.

## Fade-Only Simulation (Google Slides)
**When**: the client imposes Google Slides.
**How**: duplicate the slide per state, change colours/positions, apply a ~0.3 s Fade to all slides; cover inactive items at ~70% opacity.
**Trade-offs**: no real motion; graphic quality must carry the deck.

## Transparent Link Overlay
**When**: a grouped object must be clickable in Google Slides or an interactive PDF.
**How**: place a fully transparent shape on top and link that (Insert > Link).
**Trade-offs**: overlays must be moved if the layout changes.

## Synced Slides from a Master Deck
**When**: a large master deck feeds smaller derived decks.
**How**: in Google Slides copy a slide, paste into another deck, choose Link to original presentation; click Update after editing the original.
**Trade-offs**: updates are manual per slide.

## Canva Template Transposition
**When**: adapting a Canva template to a brand.
**How**: keep its line counts and layout; transpose its three colours to similar lightness values; change fonts consistently everywhere.
**Trade-offs**: limited freedom; if content doesn't fit, start from a blank slide.

## Design in the Destination Tool
**When**: the deck must be delivered or presented in a specific software.
**How**: build in that software from the start; deliver Canva/Google as a view-only link; always add a PDF backup.
**Trade-offs**: may mean working outside your favourite tool; converting later means rebuilding animations.

## Two-Window Online Presenting
**When**: webinars and online calls.
**How**: Keynote Play in Window, Canva Present > Presenter view, or Google/Figma two windows; share only the audience window; keep notes private; reduce builds to one-click appearances.
**Trade-offs**: weak connections still make fades stutter.

## Three-Stage Rehearsal
**When**: any important talk.
**How**: rehearse alone with the slides, then in front of people, then in the venue on the presenting machine.
**Trade-offs**: venue access isn't always possible; at minimum test the file on the presenting computer.
