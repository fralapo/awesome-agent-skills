# Chapter 5: Hi-Fi Audio: Turntables, Amplifiers, Mixers and Loudspeakers

## Core Idea
Audio equipment is forgiving to restore because its failures are typically understandable: speed errors, worn rubber and gears in turntables, noisy controls and electrolytic capacitors in amplifiers, hum from ground and supply faults, and aged suspensions in loudspeakers. In this model the useful discipline is to separate source, amplification and transducer, to test each with a reference signal, and to keep subjective listening as the last step, because a pleasant sound can hide a real fault. Valve equipment carries lethal voltages; read chapter 2 before opening any.

## 5.1 Turntable speed and drive
- **Principle**: Speed error is audible as wrong pitch and wow; it is measured, not guessed.
- **How it works / sequence**: Use a stroboscope pattern or a strobe lamp at mains frequency and check that the marks stay still at each speed; adjust the speed trimmers, or find the cause (worn drive belt or idler, hardened motor mounts, a failing regulator).
- **Moves**:
  - Belt-drive and idler-drive decks need fresh belts or wheels; check the platter bearing and clean and lubricate it sparingly.
  - Worn motor isolation rubbers can be replaced with new ones, and printed spacers have been used as a fix; choose thickness by test.
  - Auto-stop and return mechanisms often use small plastic gears that fail; a reproduced gear can restore operation.
  - A seized tonearm return mechanism may only need lubrication and time for the oil to spread.
  - Check that the unit's voltage selector matches the mains.
- **Evidence**: Practitioner
- **Trade-off**: Original parts preserve value; replicas let a deck run.
- **Does not hold when**: The platter is warped or the motor is failing mechanically.

## 5.2 Tonearm, cartridge and stylus
- **Principle**: The cartridge-stylus pair is a wear item; the tonearm sets how it tracks.
- **How it works / sequence**: Inspect the stylus under magnification for wear or bent cantilever; set the tracking force with the counterweight, the anti-skating, and the alignment with a protractor or template.
- **Moves**:
  - Use the cartridge maker's recommended tracking force as the starting point.
  - Mount the arm parallel to the record, check geometry with a template, and ensure the output cable cannot pull on the arm.
  - Replacement styli are available for many old cartridges; match the original type.
  - A turntable built from salvaged parts needs rubber feet or isolation to reduce feedback from the surface it stands on.
- **Evidence**: Practitioner
- **Trade-off**: A new stylus is cheap compared with a ruined record.
- **Does not hold when**: The cartridge itself has failed electrically or magnetically.

## 5.3 Records, cleaning and special formats
- **Principle**: Surface noise partly comes from dirt; ultrasonic cleaning can remove it, while real wear cannot be removed.
- **How it works / sequence**: Clean in a bath of purified water with a little isopropyl alcohol to reduce surface tension, limit cycle time so the bath does not heat up, and dry by air, not by hot air or a centrifuge.
- **Moves**:
  - Use a carbon-fibre brush grounded to reduce static.
  - Some record formats use noise-reduction encoding (a decoder is needed); played without decoding they sound poor. A software decoder can process a clean flat recording from the phono stage.
  - Phono preamplifiers can come from a mixer or a small dedicated unit when none is present.
- **Evidence**: Practitioner; Observational for the cleaning effect.
- **Trade-off**: Cleaning reduces crackle on healthy discs; heavy wear remains.
- **Does not hold when**: The disc is warped, cracked or delicate.

## 5.4 Hum, noise and grounding
- **Principle**: Hum at mains frequency or its double comes from ground loops, missing earth connections, misrouted cables, or failed filter capacitors.
- **How it works / sequence**: Establish whether the hum is present with the input shorted and the volume up; if so it is inside the amplifier; if not, look at cables and grounding.
- **Moves**:
  - Keep the mains lead away from the input stage; check that the shield and chassis grounds are connected where the schematic says.
  - Moving the mains cable or the switch position can reveal that a switch only interrupts part of the supply.
  - A ground loop between a recorder and a computer can be broken with audio isolation transformers.
  - Do not defeat safety earths to cure hum; use an isolation device or fix the wiring.
- **Evidence**: Practitioner
- **Trade-off**: Isolation transformers add a little signal loss and cost.
- **Does not hold when**: The hum is in the source (a microphone with the wrong impedance, for example).

## 5.5 Amplifiers and mixers: bench method
- **Principle**: Test with a defined signal and a safe load, not through valuable speakers.
- **How it works / sequence**: Power up under current limit; measure DC rails; check for DC on the output; feed a sine wave and observe the output on an oscilloscope into a dummy load or a pair of cheap speakers; compare channels.
- **Moves**:
  - Dual-supply units need balanced positive and negative rails; measure both before connecting signals.
  - Frequency response can be scanned with a function generator and an oscilloscope; compare with the specification and between channels (a channel with different gain can be a swapped resistor).
  - Missing channels in mixers are often dirty potentiometers or switches; clean or replace them.
  - Check the regulators for counterfeits (chapter 4) and the filter capacitors.
  - Do not trust the spec sheet's top figures without a measurement.
- **Evidence**: Practitioner
- **Trade-off**: Dummy loads and test gear cost time to set up and protect speakers.
- **Does not hold when**: The unit is a high-power amplifier where load and heat management need a proper test bench.

## 5.6 Valve (tube) equipment
- **Principle**: Valve circuits combine heater supplies, high-voltage anode supplies and bias, and are fragile where components are old.
- **How it works / sequence**: Inspect and replace perished wiring and leaky coupling and filter capacitors; test valves on a valve tester or by substitution; power up slowly; measure only if you can do so safely.
- **Moves**:
  - Check heater voltages and anode supply separately.
  - A magic-eye indicator and other special tubes wear out; replacements are scarce.
  - A heat camera shows valves and resistors running hotter than normal.
  - Some modern "valve" amplifiers use a solid-state stage in the signal path, so what you hear is not necessarily the valve. **Position** from sources; verify against the schematic.
  - Observe chapter 2: a unit with hundreds of volts and old capacitors is a job for a competent person.
- **Evidence**: Practitioner; Position for the sound claims.
- **Trade-off**: Valves give sound that some prefer, at the price of heat, maintenance and risk.
- **Does not hold when**: The unit uses a battery-level valve design.

## 5.7 Optical disc players
- **Principle**: Compact-disc players fail in the mechanism (tray belts, carriage), power, laser output, or servo adjustment.
- **How it works / sequence**: Check the mechanism and tray, check supply rails, confirm that the laser is emitting (with an infrared-sensitive camera), check the radio-frequency eye pattern and servo signals against the service manual; use a thermal camera to find abnormally hot parts.
- **Moves**:
  - Remove circuits one at a time to see which causes the heat.
  - Servo focus can be checked with a test tone and an oscilloscope in XY mode.
  - A transistor in the focus driver is a common failure.
  - Mechanical buttons that wear out can be rebuilt with micro switches.
  - De-emphasis, filtering and digital converter behaviour can be tested with special discs.
  - A converter board swap between two identical players can show where the fault is.
- **Evidence**: Practitioner
- **Trade-off**: Laser adjustment is risky and often unnecessary; avoid it unless the manual and measurements support it.
- **Does not hold when**: The laser is dead; replacing the optical block may not be possible.

## 5.8 Loudspeakers and drivers
- **Principle**: Driver faults are mechanical: aged surrounds, dried suspensions, rubbing voice coils, broken crossovers.
- **How it works / sequence**: Test each driver with a sine sweep or tone at a low level and listen for rubbing; check crossover parts; re-seal the cabinet properly; replace drivers in pairs to keep channels matched.
- **Moves**:
  - Sealed enclosures must be airtight; reinforcement and sealing are part of the design.
  - Keep crossover coils away from magnets; twist the leads.
  - Absorbing material such as wool or mineral wool needs gloves, a mask and care.
  - Replacement voice coils with centring guides exist for some tweeters; replace both for balance.
  - Printed cones and homemade drivers are experiments, and the sound is often modest.
  - Reusing driver parts in a project (small drivers in battery speakers) is feasible; match power and impedance.
- **Evidence**: Practitioner
- **Trade-off**: Repair keeps character; modern drivers are simpler.
- **Does not hold when**: The magnet is damaged or the voice coil is burnt.

## 5.9 Microphones and headphones
- **Principle**: Vintage microphones and headphones are impedance-sensitive devices.
- **How it works / sequence**: Match the impedance of the microphone with the input; a ribbon microphone needs a suitable input stage; a carbon microphone needs a bias supply and an audio transformer.
- **Moves**:
  - A low-impedance headphone adapted to a high-impedance source may need a matching transformer.
  - Reusing salvaged transducers in a new headphone needs listening tests, and tuning parts (acoustic damping, pad choice) are subjective.
  - Wireless adaptation of old headphones needs a battery, a charger and protection electronics; check polarity.
- **Evidence**: Practitioner; Position for tuning.
- **Trade-off**: Matching and adaptation cost effort and change the original.
- **Does not hold when**: The microphone is delicate (ribbon) and mishandled; then specialist service.
