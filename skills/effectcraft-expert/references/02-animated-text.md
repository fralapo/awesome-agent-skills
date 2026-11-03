# Animated text (lesson 3)

## Concepts
- A text layer is vector, so it stays crisp at any scale. It animates like any other layer.
- It also has **text animators**, which act per character, word or line.
  - An **animator** holds one or more properties: position, scale, opacity, tracking, blur, fill colour…
  - It also holds one or more **selectors**. A selector works like a mask over the characters and decides which ones the animator affects.
- The **range selector** has Start, End and Offset in percent. The usual move is to animate Offset from −100 to 100, or animate Start/End.
- Text imported from a PSD must first become editable: `layer.create {op:"editableText"}`.

## EffectCraft commands (verified)
- Create: `command_run layer.newText {text, size, fill:"#fff", position:[x,y], font?, tracking?, justify?}`. It returns `{layer:id}`. For paragraph text, pass `box:[x,y,w,h]`.
- Edit content or formatting: `layer.setText {layer, text?, font?, size?, tracking?, leading?, range?:[a,b]}`. Use `range` to format only some characters.
- Fonts: `text.fonts` or `list_fonts`. **No Adobe Fonts**, so use the installed fonts.
- Ready-made preset: `layer.applyTextPreset {layer, preset:"fadeUpCharacters"}`. It creates an animator (opacity plus Y position) with Offset already keyed.
- Custom animator:
  1. Create it with `layer.addTextAnimator {layer, properties:["tracking"], name}` (verified).
  2. Add more with `layer.addTextAnimatorProperty` and `layer.addTextSelector {kind: range|wiggly|expression}`.
  3. Key the selector at `text/animators/<name>/selectors/rangeSelector/offset` (or `.../start`, `.../end`).
  4. Set the animated values at `text/animators/<name>/properties/<prop>`.
- Other paths:
  - Source text: `text/sourceText`.
  - Selector options: `.../rangeSelector/advanced/{basedOn, shape, easeHigh, easeLow, randomize}`.
  - Text on a path: `text/pathOptions/path`, which points to a mask on the same layer.
- Per-character 3D: `layer.enablePerChar3D`. Remove every animator: `text.removeAllAnimators`.

## Recipes
- **Title that pops in:** key `transform/scale` from [0,0] to [110,110] to [100,100] with `interpolation:"easyEase"` (verified).
- **Tracking that opens up:** a `tracking` animator, property −20, selector Offset from −100 to 100. Or use the `trackingIn` preset.
- **Character reveal:** `fadeUpCharacters` or `typewriter`. Or build an animator with opacity 0 and key its Offset.
- **Word replaced by an image:** key the image layer's opacity up while the text fades out.
- **Movement:** key `transform/position`. Use `easyEaseOut` on the start key and `easyEaseIn` on the end key.
- **Motion blur:** run `layer.setSwitch {layers, switch:"motionBlur", value:true}` **and** `comp.setSwitch {switch:"motionBlur", value:true}`. You need both.

## Good practice
- Use few, large fonts. For social video, keep headlines around 120–200 px on a 1080-wide frame.
- Set the work area to the animation with `comp.workArea`.
- Always ease. Linear motion looks mechanical.
- A new text layer's anchor can sit on the baseline. Run `layer.centerAnchor` before you scale or rotate it.
- Check legibility with `render_frame` at the start, middle and end of the animation.
