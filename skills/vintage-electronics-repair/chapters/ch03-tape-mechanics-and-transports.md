# Chapter 3: Tape Mechanics and Transports

## Core Idea
Cassette, reel-to-reel, digital tape (DAT, ADAT, DCC), cartridge and video-tape transports fail mainly because rubber, lubricants and plastics age. In this model, restoring a tape machine is first a mechanical job (belts, pinch rollers, idlers, gears, springs, brakes, heads), second a cleaning and demagnetising job, and only then an electronic alignment job. A machine that looks dead is often just stuck, and a machine that plays is not necessarily aligned.

## 3.1 Belts
- **Principle**: Rubber belts degrade into goo, stretch or snap, and a transport with a bad belt may turn the motor freely while nothing moves.
- **How it works / sequence**: Identify every belt path (capstan, reel, counter, loading, tray); remove residue completely from pulleys; fit a replacement of the right section and length; check tension and path with the mechanism cycling.
- **Moves**:
  - If the correct length is unknown, try several nearby sizes: too long slips, too short loads the motor and bearings.
  - Clean pulleys with isopropyl alcohol before fitting a new belt.
  - A printed flexible-material belt is sometimes used as a temporary replacement; treat it as a stop-gap and replace it with a proper belt.
  - A loose belt may also be a symptom of a drive or tensioner problem; check that the pulleys and idlers are not seized.
- **Evidence**: Practitioner
- **Trade-off**: A stop-gap belt keeps the unit working for tests but may not hold speed accuracy.
- **Does not hold when**: The unit uses direct-drive motors, where a belt is not the cause.

## 3.2 Pinch rollers and capstans
- **Principle**: The pinch roller presses tape against the capstan; if the rubber is hard, glazed or dissolved, tape speed becomes unstable or tape is not pulled.
- **How it works / sequence**: Inspect the roller under magnification for cracks, glazing and tackiness; clean the capstan; replace the roller if the rubber has failed or if the roller is out of round.
- **Moves**:
  - Practitioners differ on cleaning rubber with alcohol: some use only a dry or lightly damp cloth, because solvents can harm the surface or a multi-layer roller. **Contested**: the safest route is to follow the service manual and test on a spare.
  - When pausing, the roller usually backs off the capstan so that the capstan can be cleaned.
  - Replacement rollers that are slightly different in width can be compensated with washers; a soft cable sleeve has been used as a makeshift capstan rubber; both are repairs of last resort.
  - Check the roller's spring and pressure against the manual; a weak spring gives wow and slip, a stronger spring may add wear.
- **Evidence**: Practitioner; **Contested** on alcohol on rubber.
- **Trade-off**: Rejuvenating products may buy time for rare machines but rarely restore a roller permanently.
- **Does not hold when**: The roller is cracked, then replacement is the only option.

## 3.3 Gears, cams, springs and brittle parts
- **Principle**: Plastic gears, cams and levers crack with age, and certain zinc-alloy and old plastic parts crumble or turn waxy.
- **How it works / sequence**: Inspect gears and cams with the mechanism removed; if a tooth is broken, source a donor part, or reproduce the gear by design and 3D printing; do not drill or machine fragile alloy parts.
- **Moves**:
  - Controlled reproduction of small gears needs measured tooth count, module and base diameter, and a fine nozzle for sharper teeth; test-fit and iterate, because early prints are often slightly off.
  - Cams and levers that move a switch should be inspected even in a machine that seems to work; a worn one will fail at a bad moment.
  - Springs lose force; a rewind spring that is unhooked or tired is a common reason for failed rewind or auto-stop.
  - Missing plastic from a part can make a machine lose its position and stop unexpectedly.
- **Evidence**: Practitioner
- **Trade-off**: A printed gear is fast and often good enough; a metal or injection-moulded original is stronger.
- **Does not hold when**: The part is a high-load drive gear or a part with sliding wear; plastic printing may not last.

## 3.4 Lubrication
- **Principle**: Too little lubricant causes stiction, too much attracts dirt, flows onto rubber and creates slip.
- **How it works / sequence**: Clean old grease; apply a small amount of the right lubricant only to the points that move under load; wait and retest.
- **Moves**:
  - A single drop on a stuck lever is often enough; resist lubricating everything.
  - Light oils free solenoids, arms and tray mechanisms that are seized rather than faulty.
  - General-purpose penetrating spray on plastics, rubber and contacts is widely used and widely discouraged; use a lubricant suited to plastic and keep it off belts, rollers and tape paths.
  - Some designs are meant to be dry; follow the manual (a drive that sheds tape when oiled is a real outcome).
- **Evidence**: Practitioner; **Contested** on which products are best (names in transcripts are unreliable).
- **Trade-off**: A little lubricant can revive a machine; too much shortens its life.
- **Does not hold when**: The seized part is corroded or deformed.

## 3.5 Heads, demagnetising and cleaning
- **Principle**: Heads accumulate oxide, become magnetised and wear; dirty or magnetised heads dull the sound and erase high frequencies.
- **How it works / sequence**: Clean heads, capstans, guides and tape path with isopropyl alcohol; demagnetise with a proper demagnetiser, approaching slowly, moving it across the heads and withdrawing slowly before switching off; check heads for wear grooves.
- **Moves**:
  - A demagnetiser used too near and removed quickly can leave heads magnetised.
  - Worn heads (a groove where tape runs) need replacement; where parts are not available, a compatible head may fit with a careful mounting.
  - Do not touch sealed head assemblies and factory-sealed adjustments without a reason; many repairs are completed by leaving them alone.
  - On video and digital tape machines, particles near the drum or heads can lift the tape and wreck playback.
- **Evidence**: Practitioner
- **Trade-off**: Cleaning is cheap and frequent; replacement is rare and expensive.
- **Does not hold when**: The tape path uses specialised head cleaning cassettes that the manual prescribes.

## 3.6 Speed, azimuth and alignment
- **Principle**: Alignment is measurement against a reference, not listening.
- **How it works / sequence**: After mechanical work, check speed with a reference tone and a meter or a strobe; check azimuth with a high-frequency test tape; check levels, bias and equalisation per the service manual.
- **Moves**:
  - Speed: play a reference tone tape (for example 1 kHz) and compare the reading; adjust the motor trimmer.
  - Azimuth: use a high-frequency tone (around 10 kHz) and adjust for maximum level or for the cleanest phase relationship; an oscilloscope in XY mode (left on one axis, right on the other) shows phase as a line, and a line close to a diagonal means the channels are in phase.
  - Bias and equalisation need the correct test tape or a calibrated machine; if you do not have them, leave factory seals alone.
  - Do not touch alignment when the unit plays well and shows no clear fault.
- **Evidence**: Practitioner
- **Trade-off**: Alignment takes hours and requires reference tapes; skipping it risks dull sound or tapes that cannot be played on other machines.
- **Does not hold when**: The unit is a toy-grade or a mono dictation device without adjustment points.

## 3.7 Digital tape, digital audio formats and noise reduction
- **Principle**: DAT, ADAT, DCC and similar formats are mechanically complex helical or multi-track transports, and their electronics are less forgiving of misalignment than analogue.
- **How it works / sequence**: Clean and lubricate mechanisms, check rollers, belts and connectors (wrong-way connector insertion by a previous repairer has caused faults), then test read and write with a known tape; format blank tape where the machine requires it before recording.
- **Moves**:
  - Machines connected to computers may require specific firmware, drivers and a suitable interface; documentation gaps are common.
  - Recording copy-protection flags may block digital cloning on some paths.
  - Noise reduction systems (several types) need matched decode on playback: an encoded tape played without decoding sounds different, and some types sound far worse than others when undecoded. **Contested**: opinions differ on which systems are tolerable undecoded.
  - Format claims in old marketing material (dynamic range, tape length designations) can be misleading; read the markings on the cassette.
- **Evidence**: Practitioner for mechanics; Position for sound comparisons.
- **Trade-off**: Digital formats offer clean copies and have fewer spare parts.
- **Does not hold when**: The unit is only for playback of existing tapes where a modern interface is not needed.

## 3.8 Handling old tapes
- **Principle**: Tapes stored in poor conditions can shed, stick or grow mould; playing them risks harming the tape and the machine.
- **How it works / sequence**: Inspect tapes visually; clean dry with a soft brush or purpose-built tape-cleaning machine; for sticky tapes, seek specialist advice, because heat treatments are controversial and not generally recommended by sources here.
- **Moves**:
  - Dry-clean mouldy tapes with a soft microfibre pass in both directions and check the cleaning pad for residue.
  - Do not bake a tape using improvised heat sources such as a radiator.
  - If a tape is stuck in a machine, free the mechanism instead of tearing the tape.
  - Cassette shells can be opened and the tape rewound in a new shell.
- **Evidence**: Practitioner; **Contested** on thermal treatment.
- **Trade-off**: Cautious cleaning may not rescue a tape; improvised treatments may destroy it.
- **Does not hold when**: The tape is irreplaceable, then use a specialist.
