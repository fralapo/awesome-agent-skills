# Cheatsheet

All point sizes assume a **1920×1080 px** canvas. Italian UI names in parentheses where the chapters give them.

## File Setup Values (Ch01)
| Setting | Value |
|---|---|
| Slide size | Design > Slide Size > Custom Slide Size (Mac: File > Page Setup): **1920×1080 px** = 67.73 × 38.1 cm; never 4:3 |
| Starting theme | Plainest white theme (Office Theme); delete default placeholders and unused layouts |
| Margin guides (distance from slide centre, cm) | Vertical **31** left / **31** right; horizontal **16** top / **15** bottom |
| Acceptable guide variants | 31 / 16.5; ~32.8 for a slightly wider frame |
| Default PowerPoint size (33.87 × 19.05 cm) equivalents | ~15.5 / 8.3, or 15.3 / 8 |
| Extra guides | Centre vertical + centre horizontal on the Master; column guides for a 4-column grid |
| Guide colours in Slide Master view | Red = Master, yellow = layout, grey = slide |
| Guide handling | Right-click > Grid and Guides > Add Vertical/Horizontal Guide; Alt/Option-drag duplicates; drag off-slide deletes |
| Master view | View > Slide Master (Visualizza > Schema diapositiva); edit the top (biggest) thumbnail |
| Placeholders | Resize shape to fit text (Adatta dimensioni forma al testo), anchored top, internal margins 0 |
| Footer | No date; footer text centre or left, slide number right, inside bottom margin; margins 0; Insert > Header & Footer > Apply to All |
| Footer styling | Footer grey/dark, number in accent colour, 18–20 pt Regular (Light vanishes) |
| Logo | On the Master only if it works on light and dark; else per layout or two Masters |
| Template file | File > Save As > PowerPoint Template (**.potx**) + an instructions slide |
| Layout set to offer | Cover, section/break, text only, text + image, image only, data, quote |

### Five Master Settings (Ch01)
1. Guides 2. Theme fonts 3. Theme colours 4. Footer 5. Layouts for recurring slides (custom layouts only worth it for long decks; the other four always).

### Theme Colours (Ch01)
| Rule | Value |
|---|---|
| Real colours | At most 3–4 (white and black/near-black in addition) |
| 12 slots | Dark 1, Light 1, Dark 2, Light 2, Accent 1–6, Hyperlink, Followed Hyperlink: fill all deliberately |
| Path | Slide Master > Colors > Customize Colors |
| Monochrome theme | Base hue = accent; 90% darker = text/covers/breaks; 90% lighter = backgrounds; chart steps 0/20/40/60/80/90% into Accent 1–6 |
| Text / background | Near-black instead of #000000; off-white instead of pure white when projected |
| Picking | Always from the Theme Colors row, never Recent / More Colors |

### Theme Fonts & Type Scale (Ch01)
| Element | Size |
|---|---|
| Fonts path | Slide Master > Fonts > Customize Fonts (Heading + Body) |
| Default pairing | Aptos Semibold titles + Aptos Regular body; prefer non-default linear sans (Inter, Roboto, Epilogue, Funnel Sans, IBM Plex Sans) |
| Big titles | 80–88 pt; display words up to 200–300 pt |
| Section/slide titles | 40–48 pt; statement phrases 56–64 pt |
| List text | 32 pt, Exactly 42 pt (or 40 pt Light, Exactly 50) |
| Body | 24–32 pt; ≥32 pt for large rooms |
| Labels/eyebrows | 24 pt, 16 pt space after |
| Footer/source | 18–20 pt Regular |
| Scale | Multiples of 8 (24, 32, 40, 48, 56…), a guideline |
| Emphasis | Medium/Semibold weight, not synthetic Bold |

### Indent-Level Text Styles (Ch01)
| Level | Example style |
|---|---|
| Level 1 "title" | No bullet, Semibold, 20 pt (dense template), accent colour, Multiple 1.15, before 0, after 12 pt |
| Level 2 "body" | Smaller, Light, grey, no space before |
| Apply | New line + Tab / Shift+Tab (Increase/Decrease List Level) |
| Setup | Bullets > None on levels 1–2; drag both ruler indent markers fully left; rename sample text per level |

### Charts & Excel (Ch01)
| Item | Rule |
|---|---|
| Chart template | Right-click chart > Save as Template (**.crtx**), stored on the computer, not in the file; ship separately |
| One per type | Prefix names: "BRAND line", "BRAND column", "BRAND pie"; build with 3+ series, legend, labels, axes |
| Reuse | Insert > Chart > Templates, or Change Chart Type > Templates |
| Chart style | Axis text 18–20 pt light/mid grey; chart title 40 pt or none (never both chart title and slide title); legend bottom; monochrome palette |
| Excel link | Paste keeping the link; on Mac links can't be re-pointed after files move |
| Percent entry | Decimals (0.82), axis 0 decimals, max 1.0, major unit 0.1 (82 → 8200% otherwise) |
| Constant series | Change Series Chart Type > Line |
| Mac gaps | No saved table styles, shape styles or theme fonts (fonts only via workaround) |

## Autofit Modes (Ch02)
Path: right-click > Format Shape > Text Options > Text Box (third icon).
| Mode (Italian) | Behaviour | Use for |
|---|---|---|
| Shrink text on overflow (Adatta testo all'area di riversamento) | Text shrinks as box fills | **Never** (cause of "shrinking text") |
| Do not Autofit (Non adattare) | Box keeps its size | Fixed cards, pills, tabs, menu boxes |
| Resize shape to fit text (Adatta dimensioni forma al testo) | Box follows content + margins | Free text boxes, template placeholders |

Anchor: top for titles (first line never moves).

## Line & Paragraph Spacing (Ch02, Ch04)
| Context | Setting |
|---|---|
| Path (PowerPoint) | Home > Line Spacing > Line Spacing Options |
| Default 1.0 | Too tight for body |
| Exactly | 32 pt → 42; 40 Light → 50; Keynote 36 → 42 |
| Multiple | 1.1–1.15 for paragraphs (remove Space Before) |
| Big display titles | 0.8–0.95 |
| Space after title/label | 8 pt (dense) to 16–32 pt (airy); never empty returns |
| Google Slides | Format > Line & paragraph spacing > Custom 1.1–1.2; space before 8–24 pt; never presets 1.15/1.5/double |
| Figma Slides | Line spacing in % |
| Keynote | Exactly preferred; title-to-paragraph space > in-paragraph line spacing |

## Text & Shape Rules (Ch02)
| Item | Rule |
|---|---|
| Alignment | Left or centred; right only for small footer info; justified never; centre only short phrases |
| Internal margins | Plain text 0; cards ~0.7 cm left/bottom, 0 top; pills 0 (or ~1.2 on the text side) |
| Outline | Remove default outline (Shape Outline > No Outline) |
| Rounded corners | Yellow handle only; small radius; one master shape, duplicate |
| Card shadow | Outer, downward, 85–90% transparency, larger blur |
| Letter spacing | Increased only on 2–3 words |
| Emphasis | One device (bold OR italic OR colour) |
| Line breaks | No short words left at line end |
| Photo darkening | Brightness −40% to −65% instead of an opaque box |
| Image series | Same aspect ratio (Crop > Aspect Ratio, e.g. 2:3 / 3:2) |

## Speed Shortcuts & Tools (Ch02)
| Action | Shortcut / Path |
|---|---|
| Repeat last action | Ctrl+Y (Win) / Cmd+Y (Mac) |
| Constrained move | Shift + drag |
| Constrained duplicate | Ctrl + Shift + drag |
| Straight line / proportional resize | Shift while drawing / resizing |
| Duplicate slide | Ctrl/Cmd+D |
| Format Painter repeat | Double-click brush; Esc to stop (Animation Painter same) |
| Swap image | Right-click > Change Picture |
| Selection Pane (Riquadro di selezione) | Home > Arrange > Selection Pane: rename, lock, hide, reorder |
| Align & Distribute | Home > Arrange > Align; single object/group aligns to slide |
| Change Shape | Shape Format > Edit Shape > Change Shape |
| Merge Shapes (Unisci forme) | Shape Format > Merge Shapes > Union / Combine / Fragment / Intersect / Subtract |
| Hide slide | Right-click thumbnail > Hide Slide |
| Final check | View > Slide Sorter |
| Keynote rulers | View > Show Rulers (Cmd+R) |

## Icons, Images, Tables (Ch02)
| Item | Value |
|---|---|
| PNG black → white | Brightness **+100%** |
| PNG white → black | Brightness **−100%** (monochrome PNG only) |
| SVG recolour | Free SVG colouriser → export PNG at original size |
| Duotone | Picture Format > Color > Recolor (theme colours) |
| Photo overlay | Gradient black 0% → 100% transparency |
| Table fills/borders | No Fill; Borders none, then Bottom + Inside Horizontal in mid grey; no verticals (except 2 pt white group divider) |
| Table header | Accent fill, white text; second header lighter HSB tint; header rows lower |
| Table numbers | Right-aligned; currency label not bold; margins L/R 0, top/bottom ~1, header column 0.5, data right margin 0.3–0.5 |
| Table emphasis | Best bold green, worst red; optional rectangle at 85% transparency |
| Chart highlight | Other bars 80% transparency; Outside End label only on key value (e.g. 32 pt bold) |

### Bubble Chart for Percentages (Ch02)
| Setting | Value |
|---|---|
| Type | Insert > Chart > X Y (Scatter) > Bubble (not 3D) |
| Single % | Two rows X=1, Y=0, sizes 100 and 33; X axis 0–2, major unit 1; Y min 0, max 1 |
| Bubble scale | Up to 300 (200–250 for several side by side) |
| Several % | X = 1…5, X max 6, Y min −1 for full bubbles |
| Labels | Bubble Size only (untick Y value and leader lines) |
| Reference | 100% bubble as dashed outline, no fill |

## Morph Rules & Durations (Ch03)
| Rule | Value |
|---|---|
| Where to apply | PowerPoint Morph (Morphing): **second** slide; Keynote Magic Move (Spostamento magico): **first** slide |
| Path | Transitions > Morph > Effect Options > Objects |
| Default 2 s | Too slow |
| Most moves | ~**1 s** |
| Small moves (cards, gallery) | 0.5–0.7 s |
| Large shapes | 1–1.5 s |
| Very large travel/rotation, 3D | up to ~2 s |
| Disappearing objects | 100% transparency or off-slide, never delete |
| Groups | Morph doesn't see inside groups; group vs ungroup mismatch → fade fallback |
| Pass-through slide | Fade ~0.01 s (or none), Advance After 0 s |
| Apply To All caveat | Also applies "After" timing everywhere: remove where unwanted |
| Rotations | Slight −10°/+10° (5° for a falling card) |
| Focus | Active 100%, inactive 30% (or cover at ~70% opacity) |
| Transition shapes | Slide-size or wider, No Outline, added at the end of the job |

## Animation Timing (Ch03)
| Item | Value |
|---|---|
| Entrance | 0.3–0.5 s (Fade 0.3 s preferred); 1 s = too long |
| Transitions overall | 0.5–1 s, max 1.5 s |
| Stagger delays | 0.1 s fast fill; 0.2/0.4/0.6/0.8 s perceived sequence |
| Text by word | 1–2 lines, 0.3 s With Previous (0.7 s for slow loops) |
| Text by letter | Single word / short title only |
| Fly In | Smooth Start + Smooth End on |
| On Click | Only what you're saying now; rest With Previous |
| Corporate rule | One fade On Click, 0.3–0.5 s, few clicks per slide |

### Loops (Ch03)
| Item | Value |
|---|---|
| Recipe | Motion path + Auto-Reverse + Repeat: Until End of Slide, Smooth Start/End **off** |
| Durations | 5–10 s; circle 10 s, grow 5 s, path 8–15 s, Spin 10 s |
| Subtle drift | Spin 45° with Auto-Reverse |
| Teeter | No Auto-Reverse, ~2 s, repeat until end |
| Glow PNG | 2000×2000 radial gradient at 50% transparency |

### Effects to Use / Avoid (Ch03)
| Use | Avoid |
|---|---|
| Fade, Fly In with easing, Wipe (Cascata), Split (Morsa) on outlines/lines only, Wheel (Spirale) 1 spoke for % ring, Zoom from object centre, Grow/Shrink, motion paths | Blinds, Checkerboard, dotted dissolve, Strips, Shape, Wedge, Bounce, Boomerang, Credits, spinner stunts, 3D cube; Stretch/Expand except on lines; Pixel dissolve except on images in a digital theme |

### Glass Effect Values (Ch03)
Background picture fill Sharpness −100% (Brightness −10% for white text); card Fill = Slide background fill, No Line; shadow centred 60–74% transparency; edge gradient line white → white ~78% transparent at 45°.

## Effect Equivalents Across Tools (Ch03, Ch04)
| Function | PowerPoint | Keynote | Canva | Google Slides | Figma Slides |
|---|---|---|---|---|---|
| Object-matching transition | Morph (Morphing) | Magic Move (Spostamento magico) | Match & Move (Dinamiche combinate) | None: duplicate slide per state + ~0.3 s Fade | Smart Animate (transition only, no grouping needed) |
| Applied on | Second slide | First slide | Between two pages (~1 s, 1–2 moving objects) | All slides (fade) | Transition |
| Soft text reveal | Fade, By word | Fade and Move (Dissolvi e sposta) 0.3–0.5 s, distance ~3–10 | — | Fade only | — |
| Draw a line | Wipe (Cascata) | Line Draw (Tracciamento linea) 0.5 s | — | — | — |
| Colour filter | Recolor | None: grayscale (saturation 0) + coloured shape at reduced opacity | Duotone | Recolor | — |
| Colour change animation | Morph / emphasis | Magic Move between two slides | — | Duplicated slide + fade | Smart Animate |
| Shape booleans | Merge Shapes (Unisci forme) | Arrange > Unite / Intersect / Subtract / Exclude | — | — | — |
| Masks | Crop to Shape / Shape Fill > Picture | Double-click image; Mask with Selection | Elements > Frames | Crop > Shapes | — |
| Transparency | Fill transparency field | Opacity | — | Custom colour alpha slider | — |
| Brand colours | Theme Colors (12 slots) | Drag swatch onto theme swatch | Photo colors / picker variants | 10 Theme colors (hex, no #) | Named theme colours |
| Text styles | Indent levels in Master | — | — | — | Mandatory text styles |

## Tool-Specific Rules (Ch04)
| Tool | Rule |
|---|---|
| Keynote | Guides in pt and %; bullets 50–70% of text, offset e.g. −2 pt, indent e.g. 64; Play > Play in Window keeps presenter view; auto advance = Automatic 0 s; View > Show Object List for stacking |
| Google Slides | No eyedropper (sample from screenshot); link a group via transparent overlay shape; fades only; Link to original presentation + Update for synced slides |
| Canva | Crown = Pro; search in local language and English; one text effect on all titles or none; Hollow only on very large text; File > View settings > Show margins (aligns box, not text); labels ~20 pt, body 26 pt on default canvas |
| Canva templates | Transpose the 3 colours; don't lengthen paragraphs, shrink titles or swap the hero image at random |
| Figma Slides | Mandatory Light/Dark theme; auto layout keeps title–subtitle gap; numeric corner radius; presenter view without timer at launch; Design Mode needs a Figma Design plan |
| AI | Drafts and metaphors only; image prompts add 16:9 and "slide deck"; ignore PowerPoint Designer layouts |

### Interactive PDF Checklist (Ch04, Ch05)
- [ ] Legend slide explaining it is clickable
- [ ] Clickable index
- [ ] Home/hamburger icon on every slide
- [ ] Prev/next arrows at the bottom
- [ ] Buttons that anticipate the destination (never "click here")
- [ ] Shared-drive links public or shared with recipient
- [ ] Every link tested twice, and by someone else

## Export Compatibility Matrix (Ch05)
| Situation | Deliver | Backup |
|---|---|---|
| Corporate PC, PowerPoint | .pptx (+ .potx if template) designed in PowerPoint | PDF |
| Own Mac can be plugged in | Keynote file | PDF |
| Unknown non-Apple PC, Keynote design | PowerPoint export repaired and tested, or HTML folder | PDF |
| Canva or Google Slides | View-only link (saved offline) | PDF |
| Deck sent by email | PDF, optionally interactive | — |

### Keynote Export Formats (Ch05)
| Format | Keeps | Loses / Caveat |
|---|---|---|
| PDF | Opens everywhere; options: notes, each build stage, quality, password | Animations; notes by default; stacked builds show at once |
| HTML | Animations in any browser; uploadable as a link | Presenter notes; carry the whole folder; not from iPad / web |
| PowerPoint | Presenter notes; available on iPad | Magic Move ≠ Morph, fades converted, transparencies, fonts, arrows |
| iCloud / web | Runs without a Mac | Non-system fonts, some arrows, stuttering Magic Move, storage limits |
| Movie | Unattended playback | Live control (fixed seconds per slide) |
| Animated GIF | — | Quality (limited colours) |
| Images / Keynote '09 | Each slide or build / old versions | — |

## Presenting Checklist (Ch05)
- [ ] Asked software, version, computer, local vs online, 16:9, cables/adapters
- [ ] Fonts: embed, or system/Google fonts only
- [ ] Designed in the destination software (or time budgeted to rebuild Morph/transparencies)
- [ ] PDF safety copy checked (build stages, covered images)
- [ ] Online tools: Share > Anyone with the link > Can view; link stored offline
- [ ] Tested on the presenting machine (3D, playback, timing)
- [ ] Full-screen slideshow, presenter view, remote (from ~€10) or smartphone/iPad
- [ ] Speaker notes hold what slides don't say
- [ ] Spare slides hidden, not deleted; Slide Sorter review done
- [ ] One test click on site; backups on USB stick/cloud
- [ ] Online: share audience window only; one-click appearances
- [ ] Webinar: side LED key light, brand-colour accent light, background lights, ~€100 mic, mirrorless or good webcam, slides from iPad
- [ ] Rehearsed alone → with people → in the venue

| Pacing note | Value |
|---|---|
| Slide count vs time | ~15 slides per 10 min as a rough rule; a 20-min talk can carry 33 slides; content decides |
