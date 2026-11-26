# Chapter 8: Instruments, Measurement, 3D Printing, Lasers and DIY Conversions

## Core Idea
A small set of instruments covers most vintage repair, and a printer or laser cutter can supply the parts that no longer exist. In this model the order of investment is: a good multimeter, a way to limit current, an ESR meter, an oscilloscope, a signal generator, magnification, then specialised gear. Fabrication tools solve a real problem (a missing gear, a bracket, a faceplate), but the results are first drafts that need measuring and re-printing. The same skills support reusing old cases for new projects, which carries its own risks.

## 8.1 The core instrument set
- **Principle**: Match the instrument to the question: voltage, resistance and continuity (meter), waveform and timing (oscilloscope), temperature (thermal camera or probe), speed (strobe), signal source (generator).
- **How it works / sequence**: Start with a meter and current limiter; add an ESR meter for capacitors; add an oscilloscope and a function generator for audio and servo work; add a magnifier or stereo microscope for fine work.
- **Moves**:
  - An oscilloscope in XY mode shows phase between two audio channels and focus patterns; a camera sensitive to infrared shows an optical pickup's laser.
  - A thermal camera quickly identifies a part running hot; compare with a healthy unit.
  - A cheap USB microscope is enough to see socket pins and hairline cracks.
  - A valve tester has a place when valves are common.
  - A test tape, a test disc and a reference tone are instruments too.
  - Analog instruments from the vintage era are still useful, and calibration matters more than age. **Position** (some practitioners prefer vintage instruments for vintage work, new ones for simple jobs).
- **Evidence**: Practitioner
- **Trade-off**: More instruments mean more to learn and maintain; a few well-understood ones beat many.
- **Does not hold when**: The task is purely mechanical.

## 8.2 Building simple test gear
- **Principle**: Kits and small projects teach as they tool you up, if you understand the limits.
- **How it works / sequence**: Choose a documented kit; calibrate against known references; record the limits.
- **Moves**:
  - A kit ESR meter can be calibrated with known new capacitors and resistors; a first version is for quick pass-fail, not precision.
  - A simple A/V signal generator, a microcontroller pattern source or a function generator gives a stable test signal.
  - Check polarity and supply voltage twice; a 12 V supply on a 5 V board can destroy it.
  - Compare readings with a trusted instrument.
- **Evidence**: Practitioner
- **Trade-off**: Self-built gear is cheap and less accurate.
- **Does not hold when**: You need a certified measurement.

## 8.3 Reading a measurement
- **Principle**: A value without its conditions is not a measurement.
- **How it works / sequence**: Record load, range, probe, ground point and time; compare with the manual's tolerance; repeat.
- **Moves**:
  - Values read aloud or in transcripts are easily garbled; verify from the manual before acting on a number.
  - A rail with the signal unplugged is not the same as under load.
  - A capacitor out of circuit may read differently than in circuit.
  - Do not trust a spec sheet's top figures without a measurement.
- **Evidence**: Practitioner
- **Trade-off**: Recording takes time and avoids repeat work.
- **Does not hold when**: The reading is trivial.

## 8.4 3D printing parts
- **Principle**: A printed part is a fast prototype of a missing part, and it should be treated as an iteration.
- **How it works / sequence**: Measure the original; model it; print; test fit; adjust the model; print again; choose a material for the load and temperature.
- **Moves**:
  - Expect to reprint: a few millimetres of error is common and a part can be 1 mm too tight.
  - Scanning a part can help, with a matte, light-coloured surface scanning better than a reflective one; the scan then needs modelling.
  - Use a fine nozzle for small gears; flexible material for belts and washers only as a temporary solution; stronger materials for load-bearing parts.
  - Spacers and washers (for example to replace motor isolation rubbers) are good candidates.
  - Cases, brackets and adapters for reusing old equipment are the easiest wins.
  - Prototype printers and early firmware can have bugs; check the start code before printing.
- **Evidence**: Practitioner
- **Trade-off**: Printing is fast and imperfect; casting or machining is stronger.
- **Does not hold when**: The part is safety-critical (mains insulation, high temperature).

## 8.5 Laser engraving and cutting
- **Principle**: Lasers engrave faceplates and cut panels; they also burn, blind and start fires.
- **How it works / sequence**: Choose material and settings from a test; secure the work; use air assist and ventilation; stay present; wear the correct eye protection.
- **Moves**:
  - Test power and speed on scrap; a piece that shifts during engraving is ruined.
  - Some plastics melt, burn or give off hazardous fumes; avoid materials not known to be safe.
  - Painted or coated surfaces can be marked by removing the coating.
  - Printing on wood benefits from sanding first and a clear primer for stronger colours.
  - A laser that is unknown in power class must be treated as dangerous; do not replicate a design with an unspecified beam.
  - Engraving a groove in a record is an experiment that gave faint or poor audio; treat it as a curiosity.
- **Evidence**: Practitioner; Position for experimental projects.
- **Trade-off**: Speed and finish against hazard.
- **Does not hold when**: The material is reflective or toxic to cut.

## 8.6 Reuse projects: converting old cases
- **Principle**: Old shells make attractive cases for new electronics; the old and the new often have different voltages and polarities.
- **How it works / sequence**: Plan power (battery, protection board, regulators), signal path and heat; build a prototype; test with a bench supply; then fit into the case.
- **Moves**:
  - Use a protection board with the battery; convert voltages with regulators; separate the amplifier supply from the digital supply to avoid noise.
  - Add a volume-limiting arrangement so that the device starts quietly.
  - Check wire gauge, short protection and polarity; a reversed battery on a board with no reverse protection destroys it.
  - Avoid permanent glue where the device will need service.
  - Heavy projects need two people to lift.
- **Evidence**: Practitioner
- **Trade-off**: Reuse is satisfying; results can be loud, noisy or fragile.
- **Does not hold when**: The device must meet formal safety rules for sale.

## 8.7 Mains-powered DIY and why to avoid it
- **Principle**: A home-built mains supply is a serious hazard.
- **How it works / sequence**: Use certified, enclosed mains adapters; do not wire mains onto bare boards without insulation, creepage and a fuse.
- **Moves**:
  - Cheap amplifier supplies connected directly to the mains with no ground plane and uninsulated joints exist; do not copy them.
  - Isolate boards from the enclosure and avoid humidity.
- **Evidence**: Practitioner
- **Trade-off**: Using a ready-made adapter adds a box and removes a risk.
- **Does not hold when**: The person has electrical training and the legal right to work on mains.
