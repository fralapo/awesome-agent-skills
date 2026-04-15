# Category Templates

Fill-in templates for each Seedance 2.0 prompt category. Replace `{…}` placeholders.

---

## 1. Cinematic Film Style (Hollywood/Director Ref)

```
Style: {Director} Style, {genre} (e.g. Gritty Realism, Epic Scale), {film stock} (e.g. IMAX 70mm), {grading} (e.g. Desaturated).
Duration: 15s.

[00-05s] Shot 1 ({shot type, e.g. Extreme Wide Shot}): {scene establishing, scale cue}. {Hans Zimmer / Joe Hisaishi style score note}.
[05-10s] Shot 2 (Interior/Cockpit Cam): {character POV, panic/determination}. {Camera shake note}. Dialogue Cue: "{line}" (Subtitle: "{translation}").
[10-15s] Shot 3 (Climax / Slow Motion): {peak action}. {Lighting/debris detail}. Cut to {black / title card} on impact.
```

Proven refs: `Le Mans Style`, `Denis Villeneuve Style`, `Wong Kar-wai 90s Hong Kong Art Cinema`, `Christopher Nolan IMAX`.

---

## 2. Commercial / Brand Advertising

Simplest form (pure text brief):

```
Generate a promotional video for {brand}. Style: {brand aesthetic, e.g. MUJI minimal Japanese}. Duration: {N}s. Tone: {warm / aspirational / bold}.
```

Product-anchored form (image ref):

```
Based on @Image 1 script and @Image 2 product, generate advertising content for {product category}.
Voiceover: {natural female/male voice, language}. Keep {product} bottle/packaging proportional, integrated with natural lighting. Avoid heavy texture overlay and cutout effects. Pace: {brisk / contemplative}.
```

---

## 3. Social / Viral Meme Style

```
Style: {meme reference, e.g. Giant Orange Cat, absurdist scale}. Duration: 8–10s.
Scene: {ordinary setting} with {oversized/surreal element}.
Action: {subject} {unexpected action}. Camera: {static locked-off OR shaky handheld} for comedic effect.
Punchline beat at [T-1s]: {reveal / reaction}.
```

---

## 4. UGC / Surrealistic Documentary

```
Style: Handheld UGC / Phone camera aesthetic, {slight motion blur, natural lighting}. Duration: 10s.
[00-03s] Setup: {mundane shot, shaky cam}. {Subject} starts {normal activity}.
[03-07s] Break: {surreal element intrudes}. Subject reacts naturally.
[07-10s] Acceptance: {subject treats it as normal}, camera keeps rolling.
Audio: Natural room tone, no music, occasional off-camera voice.
```

---

## 5. Anime / Animation Style

```
Style: {anime tradition, e.g. 90s Shonen, Studio Ghibli, Motion Graphics, Van Gogh Post-Impressionism}. Duration: 10–15s.

[00-05s] Shot 1: {Character A} {action}. Motion lines, impact frames, speed blur. {Sound cue: "whoosh", "zing"}.
[05-10s] Shot 2: {Character B} counters. {Effect: ice/fire/lightning aura}. Camera: whip-pan to close-up.
[10-15s] Shot 3: Clash. {Character A vs B} collide mid-air. Screen splits, time freezes, then explosion.
```

Specific subtypes:
- **Mech battle**: `Otter Mecha vs Octopus. Scale contrast, parts flying, pilot close-up.`
- **Space-time folding**: `Nezha and Ao Bing ice-fire clash with Space-Time Folding effect.`
- **Comedy scene**: `Luffy coding on MacBook. Straw-hat costume + modern setting incongruity.`

---

## 6. Chinese Short-Drama (竖屏 Vertical)

```
Style: Chinese Mini-Drama Style (霸道总裁 CEO drama), Vertical Format, 9:16, high contrast colors, intense close-ups.
Duration: 15s.
画面比例：9:16

[00-05s] 特写: {female lead}, 雨夜, 眼含泪光 ({rainy night, tears}). Dialogue Cue: "{emotional line}".
[05-10s] 反打: {CEO male lead} 冷峻表情, 西装 ({stern CEO in suit}). Dialogue Cue: "{commanding line}".
[10-15s] 双人同框, 雨中对峙 ({two-shot, rainy standoff}). Slow pull back. 片尾标题: "{drama title}".

排除：画面模糊，低清，比例失调。
```

---

## 7. VFX / Experimental / Surrealism

```
Style: {Megalophobia / Surrealism / Liquid physics / Dimensional dissolve}, 8K Photorealistic, Unreal Engine 5 fluid rendering, visual illusion.
Duration: 15s.

[00-05s] Entry: Physical-seeming scene. {Subject} in {normal space}. Subtle uncanny tell.
[05-10s] Rupture: {Physical law breaks — liquid porcelain shatters into ink swallows, gravity reverses, scale inverts}.
[10-15s] Dissolve: {Scene melts into abstract vortex}. Camera plunges into {void / ink / light}.
```

---

## 8. Sound-Driven (Audio Reference)

```
{Scene description}. 背景BGM参考@视频3中的音效. 旁白参考@视频1的音色. {Action beat-synced to audio rhythm}.
```

English form:

```
{Scene description}. BGM references @audio1. Voiceover tone matches @video1. Action is beat-synced, with cuts landing on downbeats.
```

---

## 9. Character / Scene Consistency

Hard anchor pattern (most reliable):

```
使用@图片1的人物形象，生成{N}秒短片。
参考@图片1人物的: 面部特征, 发型, 服装, 身材比例 — 全程保持一致。
[00-04s] {Shot 1 with identity anchor repeated}.
[04-08s] {Shot 2 with identity anchor repeated}.
[08-12s] {Shot 3 with identity anchor repeated}.
```

English:

```
Using the character from @Image 1, generate a {N}-second clip.
Identity anchor: {facial features, hair, clothing, body proportions} — maintained across all shots.
Shot 1 ... {identity repeated}
Shot 2 ... {identity repeated}
```

---

## 10. Precise Camera Movement (Video Ref)

```
参考@图1的{主角形象}, 场景在@图2, 完全参考@视频1的所有运镜效果还有主角的面部表情.
Camera moves in order:
1. {Push-in to close-up}
2. {Hitchcock zoom on fear beat}
3. {360° orbit around subject}
4. {Exit through doorway, tracking}
5. {High-angle crane pull-back}
```

Camera-ref signature phrases:
- `完全参考@视频1的所有运镜效果` — copy all camera moves from video1
- `机械臂多角度跟随` — robotic arm multi-angle follow
- `希区柯克变焦` — Hitchcock zoom (dolly zoom)
- `鱼眼镜头` — fisheye lens

---

## 11. Video Extension / Continuity

```
Continue @视频1 seamlessly. Starting state: {exact pose, framing, lighting from last frame of @视频1}.
Next 10 seconds:
[00-04s] {logical next beat, maintain all visual continuity}.
[04-08s] {develop action}.
[08-10s] {land on new stable frame OR loop back to start frame for seamless loop}.
Maintain: {lighting direction, color grade, character identity, camera style}.
```

---

## 12. Video Edit (Character Replace / Add / Delete)

```
将@视频1中的{original subject}换成{new subject}, 场景保持不变, 参考@视频1的运镜和转场效果, 利用镜头匹配人物的动作.
```

English:

```
In @video1, replace {original subject} with {new subject}. Keep scene, camera moves, and transitions identical. Match new subject's motion to original keyframes.
```

Add/delete variants:

```
在@视频1中添加{new element} 在{specific location}. 其他保持不变.
删除@视频1中的{element}. 自然补全背景.
```

---

## 13. Music / Beat-Synced

```
Style: {dance/MV/montage}. Duration: {N}s. Beat-synced to @audio1 / {BPM note}.
Cut pattern: Every {0.5s / 1 beat / 2 beats}. 
Action lands on: downbeats.
Camera: {whip-pan on snare, push-in on drop}.
```

---

## 14. Emotion (Micro-Expression Focus)

```
Duration: 10s. Extreme close-up on {character}'s face throughout.
[00-03s] Baseline expression: {neutral / guarded}. Breathing {slow / shallow}.
[03-06s] Trigger: {subtle stimulus — a letter opens, a sound off-camera, memory flash}. Micro-expressions: {pupil dilate, jaw tense, lip quiver 0.3s}.
[06-10s] Release: {single tear / slow smile / eyes close}. Sound fades to silence.
Technical: shallow DOF, Rembrandt lighting, slow push-in 2–3mm over entire shot.
```

---

## 15. Hybrid Multi-Modal (Full Stack)

```
[Identity] @图片1 男人形象
[Scene] @图片2 电梯
[Camera] 完全参考@视频1的运镜
[Audio/BGM] @视频3的音效
[Action]
  [00-05s] 男人走进电梯, 希区柯克变焦
  [05-10s] 电梯门关闭, 360°环绕, 表情惊恐
  [10-15s] 门开, 跟随走出至@图片3场景, 环顾四周
[Tech] 16:9, 24fps, 电影级调色, 2.35:1可选
排除：模糊, 变形, 五官崩坏
```

This is the "power-user" form — combines all 4 modalities (image × 2, video × 2, text). Use sparingly; over-chaining references causes drift.
