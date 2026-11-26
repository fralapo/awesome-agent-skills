# Vintage Electronics Repair: Cheatsheet

Rules of thumb from worked examples; confirm every value in the unit's own service manual. This cheatsheet is not a safety guide: high voltage, CRT and mains work belong to a qualified technician (ch02). "Position" = judgement, not fact. Chapter references in brackets.

## Where to Start
| Situation | First move |
|---|---|
| Unit dead or erratic | Mechanical and contact faults first: belts, rubber, gears, connectors, sockets [ch01.1] |
| Unknown history | Look for earlier repairs, moved jumpers, reversed connectors; photograph before disassembly [ch01.3] |
| First power-up | Disconnect signals, limit current, raise voltage gradually, measure rails; this protects the unit, not you [ch04.1] |
| Machine stops itself | Sensors and protection logic before electronics [ch06.1] |
| Hum | Test with input shorted: inside the amplifier, or cables and grounding [ch05.4] |
| Tape speed or tone wrong | Belts, pinch roller, heads, then reference-tone and azimuth checks [ch03.6] |
| Intermittent fault | Cold joints and cracked traces: flex, reflow, magnify [ch01.6] |
| Computer behaves oddly | Backup battery, contacts, then memory [ch07.3] |
| Fuse blows | Find the short first; never fit a larger fuse [ch04.4] |
| Sparks, burning smell, CRT, valve supply | Stop; qualified technician [ch02.9] |
| Offer for a used unit | Ask what was tested, see the internals, plan for shipping damage [ch01.8] |

## Diagnosis order
| Step | Rule |
|---|---|
| 1 | Identify model, manual, previous work |
| 2 | Inspect mechanics and contacts |
| 3 | Current-limited power-up, measure rails |
| 4 | Isolate subsystems one at a time; swap with a known-good unit if possible |
| 5 | Measure the suspect part; replace only with reason |
| 6 | Clean, then adjust against a reference signal |
| 7 | Log what changed |

## Tape and mechanics (ch03)
| Item | Rule |
|---|---|
| Belts | Try nearby sizes; too long slips, too short loads the motor; clean pulleys |
| Pinch roller | Hard, glazed or cracked: replace; test cleaning on a spare (Contested) |
| Gears and cams | Check even in machines that run; reproduce by printing only with measured geometry |
| Lubricant | A drop where it moves under load; keep off rubber and tape path |
| Demagnetising | Approach slowly, move across heads, withdraw slowly |
| Speed | Reference tone (for example 1 kHz) against the nominal reading |
| Azimuth | High-frequency tone (about 10 kHz); XY scope shows phase |
| Sticky or mouldy tape | Dry soft cleaning; avoid improvised heating |

## Parts that fail (ch04)
| Item | Rule |
|---|---|
| Electrolytic capacitors | ESR meter; replace bulged or high-ESR; polarity; voltage rating at or above the original |
| Wholesale replacement | Rarely harmful, often not the cause (Contested) |
| Regulators | Check pin-out of positive and negative series; beware fakes |
| Backup cells | Remove leaking cells early; clean corrosion; check the charging path |
| Potentiometers, relays | Clean contacts; replace worn tracks |
| Old wiring | Perished insulation is a hazard; replace |

## Audio (ch05)
| Item | Rule |
|---|---|
| Turntable speed | Strobe pattern stationary at each speed |
| Tracking | Use the cartridge maker's force as the start; check alignment with a template |
| Record cleaning | Purified water with a little alcohol, limit cycle time, air dry |
| Amplifier test | Dummy load or cheap speakers; check DC at output; compare channels |
| Valve gear | Lethal supplies; competent person only |
| Speakers | Seal sealed boxes; replace voice coils in pairs |

## Video and computers (ch06-ch07)
| Item | Rule |
|---|---|
| Capture | Best available output, time-base corrector if the capture drops, connect ground |
| CRT set | Qualified technician; chassis may be live |
| No boot | Mains, rails, backup battery, memory and cards, board |
| SCSI | Unique IDs, termination, one controller |
| RAID | Image first; do not delete the array without a clone |
| Servers | ECC memory, check power draw, test memory for hours |
| Salvaged data | Private; do not publish; return or wipe |

## Fabrication (ch08)
| Item | Rule |
|---|---|
| 3D printing | Expect reprints; fine nozzle for gears; temporary materials for belts |
| Laser | Test on scrap, ventilate, eye protection, never leave unattended |
| Reuse projects | Protect against reversed polarity; start at low volume; avoid permanent glue |
| Mains DIY | Use certified adapters |
