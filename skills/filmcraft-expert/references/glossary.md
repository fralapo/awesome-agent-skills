# Glossary (in my own words)

Short definitions of editing terms used in the skill, with the FilmCraft id where useful.

| Term | Meaning |
|---|---|
| A/B roll | Main footage (A, usually interview) and cover footage (B) placed above it. |
| Action-safe / title-safe | Inner frame margins where action and text are guaranteed to be visible. |
| Adjustment layer | Empty clip on a top track whose effects apply to all tracks below (`file.newAdjustmentLayer`). |
| Alpha channel | Fourth image channel storing transparency. |
| Anchor point | Pivot for a layer's rotation and scaling. |
| Aspect ratio | Width-to-height proportion of the frame (16:9, 9:16, 1:1, 4:5). |
| Bin | Folder in the project panel. |
| Bitrate | Data per second of an encoded file; higher means better quality and bigger files. |
| Blend mode | Math rule for combining a layer with the ones below (screen, multiply…). |
| B-roll | Cutaway footage that illustrates or covers edits. |
| Chroma key | Making a colored background (green/blue) transparent (`ultra_key`). |
| Clip | Reference to a media file, or a piece of one on the timeline. |
| Codec | Method of compressing video/audio (H.264, HEVC, ProRes, DNxHR). |
| Color correction | Technical fixing and matching of exposure and color between shots. |
| Color grading | Creative styling of color to set a mood. |
| Container | File wrapper holding streams (MP4, MOV, MXF). |
| Crossfade | Audio transition where one sound fades out as the next fades in. |
| Cut | Instant change from one shot to the next. |
| dBFS | Decibels relative to digital full scale; 0 is the maximum before clipping. |
| Dissolve | Gradual blend between two shots. |
| Drop-frame timecode | Timecode that skips numbers to stay in step with 29.97/59.94 fps clocks. |
| Ducking | Automatically lowering music under speech (`essentialSound.generateDucking`). |
| Edit point | The boundary between two clips. |
| Effect Controls | Panel/listing of a clip's effects and their keyframes. |
| Extract | Remove a marked range and close the gap (`sequence.extract`). |
| Frame rate (fps) | Pictures per second. |
| Frame hold | A frozen frame extending or replacing motion (`clip.frameHold`). |
| Gain | Clip input level, applied before effects (`clip.audioGain`). |
| Gap | Empty space on a track; shows black or silence. |
| Handles | Unused media before In and after Out, needed by transitions and trims. |
| HDR | High dynamic range video (PQ/HLG), brighter highlights than SDR. |
| In/Out points | Start and end marks of the range you want to use. |
| Insert edit | Adding a clip that pushes later material to the right. |
| Interpret footage | Overriding how a file's fps, aspect or color is read. |
| J-cut | Next shot's audio starts before its picture. |
| Kerning | Space between two particular characters. |
| Keyframe | A value stored at a given time for animation. |
| L-cut | Previous shot's audio continues over the next picture. |
| Leading | Space between lines of text. |
| Lift | Remove a marked range leaving a gap (`sequence.lift`). |
| Linked clips | Video and audio parts of the same clip moving together. |
| Lower third | Name/title graphic in the lower part of the frame. |
| LUFS | Loudness measure relative to full scale used by loudness standards (−23 broadcast EU, about −14 streaming/social). |
| LUT | Lookup table file that maps colors to other colors (technical conversion or creative look). |
| Marker | Time-stamped note on a clip or sequence. |
| Mask | Shape limiting where an effect or opacity applies. |
| Match frame | Open the source clip at the frame under the playhead (`sequence.matchFrame`). |
| Matte | Image used to define transparency. |
| Morph Cut | Transition that hides a jump cut in an interview by interpolating faces. |
| Multicam | Editing several synchronized camera angles by switching between them. |
| Nest | A sequence used as a clip inside another sequence (`clip.nest`). |
| Normalize | Set gain so that peaks reach a chosen level. |
| Offline | A clip whose media file is missing or disconnected. |
| Optical flow | Frame interpolation that creates in-between frames for smooth slow motion. |
| Overwrite edit | Adding a clip that replaces what is underneath. |
| Pixel aspect ratio | Shape of individual pixels; square (1.0) for modern formats. |
| Playhead | Current time indicator. |
| Point text / paragraph text | Free-growing text vs text wrapped in a box. |
| Proxy | Lightweight copy of media used for editing, swapped for full-res at export. |
| Rate stretch | Change speed by dragging a clip edge to fill a duration. |
| Render | Compute effects/frames into preview or output files. |
| Ripple edit | Trim or delete that shifts all later clips to keep no gap. |
| Rolling edit | Move a cut point between two clips, total length unchanged. |
| Rubber band | Line on a clip showing volume or opacity, editable with keyframes. |
| Scopes | Objective measurements of the image: waveform, parade, histogram, vectorscope. |
| Scrub | Move the playhead by hand to find a moment. |
| Sequence | Timeline containing an edit. |
| Slip edit | Change a clip's In/Out together without moving it in the timeline. |
| Slide edit | Move a clip while neighbours adjust to keep total length. |
| Source patching | Choosing which source channels enter the timeline. |
| Spill | Colored light from a green/blue screen contaminating the subject edges. |
| Subclip | Saved portion of a master clip as its own project item. |
| Sync lock | Keeps a track aligned with others during ripple/insert edits. |
| Three-point edit | Edit defined by three of the four In/Out marks. |
| Timecode | Address of a frame as HH:MM:SS:FF. |
| Track matte | Using another track's alpha or luma as a transparency matte. |
| Track targeting | Choosing destination tracks for keyboard edits and navigation. |
| Tracking (text) | Uniform spacing across a run of characters. |
| Tracking (mask) | Making a mask follow motion automatically (`masks.track`). |
| Transition | Effect bridging two clips or fading one. |
| Trim | Adjusting where a clip starts or ends. |
| Vectorscope | Scope showing hue and saturation; reveals casts and skin tone accuracy. |
| Video limiter | Effect clamping luma/chroma to legal ranges. |
| Waveform (audio) | Visual amplitude of a sound over time. |
| Waveform (video scope) | Brightness distribution across the image width, 0–100. |
| Work area | Timeline range used for rendering/exporting a portion. |

> Availability notes in this file are a snapshot as of 2026-11-03. ArtCraft apps update almost daily: re-check the live command catalogue before treating anything as missing.
