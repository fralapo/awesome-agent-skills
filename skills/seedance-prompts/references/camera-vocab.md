# Camera, Lens, Lighting Vocabulary

Terms extracted from 195+ prompts that Seedance 2.0 handles cleanly. Mixing EN/CN is acceptable — both parse.

## Shot Types

| EN | CN | Use |
|----|----|-----|
| Extreme Wide Shot (EWS) | 大远景 | Scale, landscape, scope |
| Wide Shot (WS) | 远景 | Context, establish |
| Medium Wide (MW) | 中远景 | Two-subject composition |
| Medium Shot (MS) | 中景 | Dialogue, action |
| Medium Close-Up (MCU) | 中近景 | Emotion + context |
| Close-Up (CU) | 特写 | Emotion, detail |
| Extreme Close-Up (ECU) | 极近特写 | Micro-expression, eye |
| Insert | 插入镜头 | Object detail |
| Two-Shot | 双人同框 | Relationship framing |
| Over-the-Shoulder (OTS) | 过肩镜头 | Dialogue, POV adjacency |
| POV | 主观镜头 | First-person |
| Interior/Cockpit | 内景/驾驶舱 | Confined, intimate |

## Camera Movement

| EN | CN | What |
|----|----|------|
| Push-in / Dolly-in | 推镜头 | Slow forward — emotional intensification |
| Pull-back / Dolly-out | 拉镜头 | Reveal, detachment |
| Pan | 摇镜头 | Horizontal rotate |
| Tilt | 俯仰 | Vertical rotate |
| Track / Follow | 跟拍 | Follow subject |
| Crane / Jib | 摇臂 | High sweep |
| Orbit / Arc | 环绕 | 360° around subject |
| Whip-pan | 急摇 | Fast transition |
| Handheld | 手持 | Documentary, tension |
| FPV / Drone | 无人机穿越 | Immersive flythrough |
| Bullet Time | 子弹时间 | Frozen moment, orbit |
| Hitchcock Zoom (Dolly Zoom) | 希区柯克变焦 | Vertigo effect |
| Slow Motion | 慢动作 | Dramatic emphasis |
| Frame Stepping | 抽帧效果 | Wong Kar-wai signature |
| Rack Focus | 变焦调焦 | Shift attention plane |
| Stabilized (Gimbal) | 稳定云台 | Smooth glide |
| Shaky Cam | 手持晃动 | Panic, action |
| Robotic Arm Follow | 机械臂跟随 | Complex programmed move |
| Fisheye | 鱼眼镜头 | Distortion, wide arc |
| Low Angle Up | 低角度仰拍 | Power, heroic |
| High Angle Overhead | 高角度俯拍 | Vulnerability, god-view |

## Lens / Format

- `85mm portrait` — shallow DOF, face isolation
- `24mm wide` — environmental, immersive
- `Extreme Macro` — surface detail, textures
- `Anamorphic 2.35:1` — cinematic wide
- `IMAX 70mm` — epic scale, grain
- `Sony A7S3 / Arri Alexa / RED` — camera-body references
- `8K ultra-clear`, `4K UHD`, `HD`
- `Shallow depth of field`, `Creamy blurred background`, `Bokeh`
- `24fps` (cinematic), `30fps`, `60fps`, `120fps slow-mo`

## Lighting

| Term | Effect |
|------|--------|
| Rembrandt lighting | Triangle-cheek portrait, classic drama |
| Natural transparent lighting | Soft daylight, healing mood |
| Backlighting / Side backlighting | Rim light, dust motes visible |
| Golden hour / Warm golden sunlight | Romantic, nostalgic |
| Blue hour | Moody, cold |
| Neon bokeh | Urban night, Wong Kar-wai |
| Practical lights | In-frame lamps/bulbs |
| Hard shadow | Noir, sharp |
| Soft diffused | Beauty, commercial |
| High-contrast chiaroscuro | Painterly, dramatic |
| Spotlight from above | 顶部聚光灯, performance feel |
| Flickering flame | 橘色火焰光影温暖真实 |

## Color Grading

- Desaturated, gritty
- Warm golden, creamy
- Cool cyan-teal
- Silver-blue (银蓝) — Chinese fantasy grade
- Yellow-green tint (黄绿调) — HK art cinema
- Monochrome / Black-and-white
- Dreamy pastel bokeh
- High-contrast blown-highlights

## Physical / VFX Vocabulary

- `Motion blur`, `Trailing shadows`, `Afterimage`
- `Speed lines`, `Impact frames`, `Screen shake`
- `Lens flare`, `Anamorphic streak`
- `Film grain`, `Stock footage scratches`
- `Volumetric fog`, `God rays`, `Dust motes`
- `Liquid physics`, `Fluid ink vortex`, `Shattering`
- `Ink-wash dissolve`, `Particle explosion`
- `Time-freeze`, `Space-time folding`
- `Parallax scroll`, `Depth layering`

## Dialogue / Lip-Sync Modifiers

- `mouths "line"` — silent lip movement
- `whispers`, `stutters`, `shouts`, `gasps`
- `200-400ms natural pauses`
- `beat-synced to audio`
- `subtitle appears: "..."`
- `voiceover references @audio1`

## Negative-Prompt Catalog (CN-idiomatic)

Copy whichever applies to tail of prompt (format: `排除：a, b, c`):

```
模糊, 低清, 噪点, 水印, 文字, logo, 扭曲, 变形, 五官崩坏,
动作僵硬, 画面抖动, 比例失调, 色彩溢出, 断肢, 多指, 融合, 漂移
```

English-idiomatic equivalents:

```
No blur, low resolution, noise, watermarks, text, logos, warping,
facial deformation, identity drift, stiff motion, shaky frames,
aspect-ratio distortion, extra limbs, fused anatomy, hand malformation
```
