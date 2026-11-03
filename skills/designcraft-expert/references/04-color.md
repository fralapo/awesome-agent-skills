# 04 - Colour: management, swatches, spot vs process, tints, gradients, groups (lesson 5)

Snapshot of DesignCraft on 2026-11-03: the apps update daily, so re-check absent features with `list_commands {filter}` before using a workaround; the Adobe behaviour described here is the target.

Source: synthesis of *InDesign Classroom in a Book 2026*, lesson 5 (plus colour parts of lesson 13).
✔ = verified 2026-11-03.

## Concepts
- **Colour management**: devices see colour differently; working spaces and the proof profile (US default
  SWOP; in Europe usually Coated FOGRA39 / PSO) simulate the press. Only change colour settings if you
  know the workflow; calibrate the monitor.
- **Printing requirements first**: ask the printer for specs or a preflight profile; check brand guidelines
  (approved colours, fonts, logo rules).
- **Named swatches** are the point: change the definition and every use updates. Unnamed colours from the
  Color panel cannot be updated globally.
- **Process (CMYK)** builds colours from four inks: right for photos and many colours. **Spot** inks
  (e.g. PANTONE) give exact brand colour but each one is an extra plate = cost. Pick spot colours from a
  printed guide, not from the screen.
- **Tints** keep a link to their parent swatch: change the parent, tints follow.
- **Gradients**: linear/radial, stops from swatches; direction set by dragging the Gradient tool; test on
  the real output device. Gradient of a tint: make the tint swatch first.
- **Colour groups** organise palettes; colour themes can be extracted from an image.
- Reverse type = light text on a dark frame or paragraph shading.
- Delete unused swatches at the end so nobody applies them by mistake; deleting a used swatch asks for a
  replacement (fastest global colour swap).

## DesignCraft
| Task | Command |
|---|---|
| Working spaces / intent | `color.settings {rgb, cmyk, intent, bpc}`, `color.loadProfile` |
| Process swatch | `swatch.create {name:"Brand Blue", color:{c:100,m:70,y:0,k:10}}` ✔ |
| Spot swatch | `swatch.create {name:"PANTONE 185 C", color:{c:0,m:100,y:85,k:0}, spot:true}` ✔ |
| RGB (screen) | `swatch.create {color:"#1d3557"}` or `[r,g,b]` |
| Tint swatch | `swatch.options {name, tint, base}`; quick tint on an object: `object.fill {swatch, tint:0.3}` ✔ |
| Gradient | `swatch.create {gradient:{kind, stops:[{location, swatch|color}]}}`, on an object `object.gradient {kind, angle, stops}` ✔ (angle 90 ran from stop 0 at the bottom to stop 100 at the top) |
| Apply | `object.fill`, `object.stroke {swatch, weight}`, text: `type.char {attrs:{fill}}` or `object.color {text:true}` |
| Rename / redefine | `swatch.options {name, to, color, spot}` - every use follows ✔ (by design) |
| Delete / replace | `swatch.delete` (see params for replacement), `swatch.addUnnamed` collects unnamed colours |
| Groups / themes | `swatch.newColorGroup`, `swatch.moveToGroup`, `color.extractTheme {id}`, `swatch.addColorTheme {colors}` |
| Exchange | `swatch.save`, `swatch.load` |
| Convert values | `color.convert {color, to:"cmyk"}` |
| Inks | `ink.list` ✔ (spot inks, process or not, alias), `ink.options` (alias / all to process) |
| Check separations | `ink.separations {page, inkLimit:300}` ✔ → per-ink coverage, `maxTotal`, `overLimit` |

## Rules of thumb for the agent
- Print job: CMYK process swatches; spot only if the client prints with that ink; otherwise convert the
  spot to process (`swatch.options {spot:false}` or `ink.options` all-to-process) before export.
- Total ink limit typically 300% (coated) / 260-280% (uncoated): check `ink.separations.maxTotal`.
- Body text in 100% K, not rich black or four-colour (registration risk on small type).
- Screen/social: RGB hex swatches, document intent `web`.
- Not available as of 2026-11-03 (re-check `list_commands`): mixed-ink swatches, Pantone Connect libraries (enter the CMYK/Lab equivalent manually).
