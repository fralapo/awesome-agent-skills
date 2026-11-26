---
name: vintage-electronics-repair
description: "Evergreen method for restoring and repairing vintage consumer electronics: triage and diagnosis order (mechanical and contact faults before electronic), service manuals, isolating variables, evaluating and shipping used units; safety reasoning and when to stop (mains, stored charge, valves, CRT and high voltage, fumes, batteries, lasers); tape transports (cassette, reel, DAT, ADAT, DCC, cartridges, VCRs: belts, rollers, gears, heads, alignment); power supplies, electrolytic capacitors and failing parts; turntables, amplifiers, mixers, valve gear, speakers; analog video, capture and CRT sets; retrocomputers, backup batteries, storage, old servers; instruments, 3D printing and laser for parts. Use when the user wants to diagnose, restore, buy, ship or reason about old audio, video or computer hardware. Gives method and caveats, not a safety guarantee; high voltage and CRT work go to a qualified technician."
allowed-tools:
  - Read
  - Grep
argument-hint: [device type, symptom, repair step, safety question, or chapter number]
---

# Vintage Electronics Repair
**Chapters**: 8 | **Corpus**: ~60 practitioner restoration and repair walkthroughs on audio, video and computer hardware | **Generated**: 2026-11-26

## Role and Boundaries

This skill **explains how to approach the restoration of vintage consumer electronics**: where faults usually are, in what order to look, how to power a unit up cautiously, how to measure instead of guess, which parts age and why, and when to stop. It gives sequences, reasoning and evidence status; the user owns the device and the risk.

| This skill decides | This skill hands off |
|---|---|
| Diagnosis order, what to check first, how to isolate a fault, how to read a symptom, what a part failure usually means, how to evaluate a used unit | Electrical theory, circuit analysis, signal and information theory -> `computer-science-fundamentals`, `physics-and-math-ideas` |
| Cleaning, lubrication, belts, rollers, heads, capacitors, batteries and alignment at the level of method | Current PC hardware (power supplies, GPUs, benchmarks) -> `pc-hardware-fundamentals` |
| When a job is beyond a hobbyist and needs a qualified person | Work on mains installations, medical or safety-certified equipment -> qualified professionals |
| Fabricating small parts and reusing cases as a method | Software-specific operation of design apps -> the matching `*-expert` skill |

**Stay in lane.** This skill **does not guarantee safety**. It gives reasoning, not step-by-step instructions for live work; mains-connected circuits, stored charge, valve (tube) supplies and cathode-ray tubes can kill, and the skill refers high-voltage and CRT work to a qualified technician. Figures are rules of thumb from worked examples, often read aloud and garbled; "approximate" marks values that were unclear, and every adjustment value belongs to the unit's own service manual. Products, prices and sources of supply are deliberately left out because they change.

## Facts vs Positions: how evidence is labelled

Each concept in the chapters has fields such as **Principle**, **How it works / sequence**, **Moves**, **Evidence**, **Trade-off** and **Does not hold when**. The **Evidence** line uses these labels:

- **Practitioner**: a method that several independent restorers use the same way, without a controlled test (nearly all of this field).
- **Observational**: a pattern seen across many repairs (which parts fail most often).
- **Position**: one practitioner's judgement or taste, written as such (a sound comparison, a preferred approach).
- **Contested**: methods that give different answers (cleaning rubber with alcohol, wholesale capacitor replacement, thermal treatment of sticky tapes, undecoded noise reduction); the chapter lists the variants and when each wins.

Read **Does not hold when** before applying a rule. Where the sources were uncertain or contradictory, the chapters say so or omit the claim.

## How to Use This Skill

Diagnose before prescribing: what device, what symptom, what condition, whether it has been opened or modified, what instruments the user has, and the user's experience with mains and high voltage. Then decide whether the next step is measurement, cleaning, replacement or stopping.

| Task | Start with | Then |
|---|---|---|
| "It does not work" on any unit; what to check first; buying or shipping a used unit | [ch01](chapters/ch01-triage-diagnosis-and-used-equipment.md) | ch02, ch04 |
| Anything involving mains, stored charge, valves, CRT, solvents, batteries, lasers, data privacy | [ch02](chapters/ch02-safety-and-when-to-stop.md) | the relevant device chapter |
| Cassette, reel, DAT, ADAT, DCC, cartridge: belts, rollers, heads, alignment | [ch03](chapters/ch03-tape-mechanics-and-transports.md) | ch04 |
| Power-up method, hum, electrolytic capacitors, regulators, fuses, batteries, contacts | [ch04](chapters/ch04-power-supplies-capacitors-and-failing-parts.md) | ch01, ch02 |
| Turntable, cartridge, amplifier, mixer, valve gear, CD player, speakers, microphones | [ch05](chapters/ch05-hifi-audio-turntables-amplifiers-and-speakers.md) | ch04, ch08 |
| VCR, camcorder, capture and transfer, CRT sets, projection and displays | [ch06](chapters/ch06-analog-video-vcrs-and-crt-displays.md) | ch03, ch02 |
| Old PCs, backup battery, drives, SCSI, RAID, servers, salvaged machines | [ch07](chapters/ch07-retrocomputers-storage-and-decommissioned-servers.md) | ch04, ch02 |
| Instruments, test gear, printed parts, laser, reuse projects | [ch08](chapters/ch08-instruments-measurement-and-fabricated-parts.md) | ch04, ch05 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Mechanical and contact faults come first.** Belts, rubber, gears, lubricant, connectors and sockets before components.
2. **Know what was done before.** Previous repairs, moved jumpers and reversed connectors are common causes; photograph before disassembly.
3. **Limit the damage of the first power-up.** Current limiting, gradual voltage and measurement of rails before connecting signals; this limits equipment damage and does not make a unit safe to touch.
4. **Measure, do not assume.** A reading beats a hunch; replacing parts is not diagnosis.
5. **Change one variable at a time,** and log it.
6. **Capacitors age, but they are not always the fault.** Test them, replace known-bad series, and still look for the real cause.
7. **A part that fails again has an upstream cause.** Find why before the second replacement.
8. **Clean before adjusting; adjust only against a reference.** Alignment is measurement with test signals, not listening.
9. **High voltage, stored charge and CRTs are for qualified people.** Being able to stop is a skill.
10. **Protect data and other people's property.** Copy before repair; treat salvaged drives as private.
11. **Not everything is recoverable.** Decide in advance what makes you stop.
12. **Fabricated parts are drafts.** Measure, print, test, repeat.

## Chapter Index

| # | Chapter | Covers |
|---|---|---|
| 01 | [Triage, Diagnosis and Evaluating Used Equipment](chapters/ch01-triage-diagnosis-and-used-equipment.md) | Mechanical-first logic, manuals, previous repairs, isolating variables, measuring, cold joints, knowing when to stop, buying and shipping |
| 02 | [Safety and When to Stop](chapters/ch02-safety-and-when-to-stop.md) | Mains, stored charge, valves, CRT, chemicals, static, lasers, data privacy, stop-and-hand-off list |
| 03 | [Tape Mechanics and Transports](chapters/ch03-tape-mechanics-and-transports.md) | Belts, pinch rollers, gears, lubrication, heads and demagnetising, speed and azimuth, digital tape, handling old tapes |
| 04 | [Power Supplies, Electrolytic Capacitors and Parts That Fail](chapters/ch04-power-supplies-capacitors-and-failing-parts.md) | First power-up, capacitor ageing and ESR, filter capacitors, rectifiers and regulators, batteries, contacts, wiring, counterfeit parts |
| 05 | [Hi-Fi Audio](chapters/ch05-hifi-audio-turntables-amplifiers-and-speakers.md) | Turntable speed, tonearm and stylus, record cleaning, hum, amplifier and mixer bench method, valve gear, CD players, speakers, microphones |
| 06 | [Analog Video, VCRs and CRT Displays](chapters/ch06-analog-video-vcrs-and-crt-displays.md) | Protection sensors, drum and heads, capture and time-base correction, period cards, cameras, CRT sets, modified inputs, other displays |
| 07 | [Retrocomputers, Storage and Decommissioned Servers](chapters/ch07-retrocomputers-storage-and-decommissioned-servers.md) | Data protection, no-boot checklist, backup battery, SCSI and RAID, drivers, micro-repair, servers, salvaged data |
| 08 | [Instruments, Measurement and Fabricated Parts](chapters/ch08-instruments-measurement-and-fabricated-parts.md) | Core instruments, test gear, reading measurements, 3D printing, laser, reuse projects, mains DIY warning |

## Topic Index

- **Alignment, azimuth, speed**: ch03 (3.6), ch05 (5.1). **Backup battery**: ch04 (4.5), ch07 (7.3). **Belts**: ch03 (3.1), ch05 (5.1), ch06 (6.2).
- **Buying, shipping, used lots**: ch01 (1.8). **Capacitors, ESR**: ch04 (4.2-4.3), ch08 (8.1-8.2). **Capture and TBC**: ch06 (6.4).
- **CRT and high voltage**: ch02 (2.4), ch06 (6.7). **Data privacy**: ch02 (2.8), ch07 (7.8). **Diagnosis order**: ch01 (1.1-1.5).
- **First power-up, lamp and variac**: ch02 (2.1), ch04 (4.1). **Hum and grounding**: ch05 (5.4). **Lubrication**: ch03 (3.4).
- **Laser (engraving, optical pickup)**: ch02 (2.7), ch05 (5.7), ch08 (8.5). **Noise reduction**: ch03 (3.7), ch05 (5.3).
- **Pinch rollers and capstans**: ch03 (3.2). **Regulators and fuses**: ch04 (4.4). **SCSI and RAID**: ch07 (7.4).
- **Servers**: ch07 (7.7). **Speakers**: ch05 (5.8). **3D printing**: ch03 (3.3), ch08 (8.4). **Valves**: ch02 (2.3), ch05 (5.6).

## Related Skills

- `pc-hardware-fundamentals`: current PC components, power supplies and diagnosing faults in modern machines.
- `computer-science-fundamentals`: the theory under memory, storage, networks and signals.
- `physics-and-math-ideas`: background on electricity, waves and measurement.
- `coding-with-agents`: backups and safety when automation touches storage.
- `scientific-thinking`: evidence, causes and avoiding false explanations.

## Scope & Limits

Built from practitioner walkthroughs of restorations and repairs, with automatic captions as the main text source. Captions garble model names, component values and units, so figures here are confirmed by several sources or marked approximate, and model-specific values are left to the service manual. Many repairs in the material ended partially or with the cause still open; this skill reports such cases as open rather than invented. Covered: audio, video and computer hardware of the analog and early digital eras. Not covered: telephone-network equipment, medical or safety-certified equipment, power electronics beyond hobbyist scale, and any procedure that requires live work on high-voltage circuits. This skill is a method for thinking, not a substitute for training, the unit's documentation, or a qualified technician.
