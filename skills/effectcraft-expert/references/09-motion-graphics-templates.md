# Motion graphics templates (lesson 11)

## Concepts
- A template exposes **only some** properties of a master comp, such as the title text, a colour, a position or a replaceable image. Anyone using it can then customise it without breaking the design.
- The **primary composition** is the one the template is built on.
- Controls can be grouped and commented so the end user understands them.
- **Responsive Design – Time** protects a region, such as an intro or a transition, so it does not stretch when the editor changes the template's duration.
- In AE the template is exported as a `.mogrt` for Premiere, or to a CC Library.

## EffectCraft equivalents (export verified)
| AE | EffectCraft |
|---|---|
| Primary comp, template name | `essential.setPrimary {comp}`, `essential.setName {comp, name}` |
| Solo Supported Properties | `essential.soloSupported {on:true}`, or check one property with `essential.canAdd {layer, path}` |
| Drag a property into the panel | `essential.addProperty {layer, path:"text/sourceText", name:"Title"}` (verified). Use `as:"font"` for the font family/style/size and `as:"scale"` for uniform scale. |
| Replaceable image | `essential.addMedia {layer, name}` |
| Groups and comments | `essential.addGroup`, `essential.addComment`, `essential.move`, `essential.rename`, `essential.remove` |
| Dropdown control | the `Dropdown Menu Control` effect + `effect.editDropdown`, linked with an expression |
| Protected time region | `comp.responsiveTime {op: intro|outro|workArea}`. Set the work area first with `comp.workArea`. |
| Export | `essential.exportTemplate {comp, path:"….ectemplate", name}` (verified: writes `.ectemplate`) |
| Use the template | `essential.importTemplate {path, addToComp}`, then `essential.set {layer, control, value}` on the precomp instance; `essential.instance {layer}` lists its controls |
| Push or revert overrides | `essential.pushToComp`, `essential.revert` |

**Missing:** native `.mogrt` export, Premiere Pro integration for templates, and Creative Cloud Libraries. The EffectCraft format is `.ectemplate`. `file.exportTimeline` can write a Premiere *project*, which is not a template (not tested).

## Recipe: reusable reel or story template
1. Build the master comp (for example 1080×1920, 10–15 s) with the title, subtitle, a logo slot and a brand-colour control (a `Color Control` effect on a null, linked with the pick whip).
2. Expose the title and subtitle text, their font (`as:"font"`), the brand colour, the logo (`addMedia`) and a few positions.
3. Group them into "Text", "Brand" and "Media", and add short comments.
4. Protect the intro and outro with `comp.responsiveTime`.
5. Export the `.ectemplate`. Test it by importing it into a fresh comp and changing every control, then run `render_frame` at several times.

## Good practice
- Expose few, meaningful controls and give them names an editor understands.
- Drive repeated values with expressions from a single control, so one change updates the whole template.
- Test long and short texts: text that is too long must not overflow the safe area.

> Availability notes in this file are a snapshot as of 2026-11-03. ArtCraft apps update almost daily: re-check the live command catalogue before treating anything as missing.
