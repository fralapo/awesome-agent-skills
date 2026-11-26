# Chapter 2: Safety and When to Stop

## Core Idea
This chapter gives the reasoning behind the precautions that experienced restorers use, not a licence to work on live equipment. Old consumer electronics can hold mains voltage, stored charge long after switch-off, kilovolt supplies in tube displays and amplifiers, toxic fumes, corrosive electrolyte, lasers and sharp or heavy parts. **This skill does not guarantee safety, and it is not a substitute for training, for the unit's own service documentation, or for a qualified technician.** For high-voltage circuits, cathode-ray tubes, valve (tube) supplies and any unit whose design you do not understand, the correct move is to stop and hand the work to a qualified person.

## 2.1 Mains is the first hazard
- **Principle**: Any appliance connected to the wall can kill; a fault current limiter reduces damage to the equipment but does not make the chassis safe to touch.
- **How it works / sequence**: Unplug before opening; do not work with the unit connected unless the procedure requires it and you have the training; when a powered test is required, use a means of limiting current and isolating the unit from the mains, and keep one hand away from the chassis.
- **Moves**:
  - Many classic chassis are connected to the mains with no isolation; a metal part can be at line potential even when the unit is off at the switch, because the switch may open only one side or only part of the supply.
  - A mains isolation transformer separates the unit from the grid reference; an incandescent lamp in series limits current into a fault but is not isolation.
  - Check cords, plugs, strain reliefs and fuses; replace perished cables; use the fuse value the manual specifies.
  - Missing earth connections, moved or removed earth pins and modified mains plugs are real hazards, not cosmetic choices.
- **Evidence**: Practitioner
- **Trade-off**: Isolation and current limiting add equipment and slow the work; they are cheap compared with the damage they prevent.
- **Does not hold when**: The work is only on a low-voltage battery or a regulated bench supply, where the main hazards are shorts and heat.

## 2.2 Stored charge: capacitors and supplies
- **Principle**: Large capacitors keep their charge after the unit is unplugged, and some do so for a long time.
- **How it works / sequence**: Unplug, wait, then discharge each large capacitor through a suitable resistor or a tool designed for the purpose, and confirm with a meter that the voltage is zero before touching. For tube equipment and any high-voltage section, follow the service manual or hand the job to a specialist.
- **Moves**:
  - A direct short across a capacitor can weld the tool and damage the part; a controlled discharge is the usual approach.
  - Never assume a capacitor is discharged because the unit has been off for some time.
  - Photographic flash and switch-mode supplies also store energy.
- **Evidence**: Practitioner
- **Trade-off**: Discharging takes minutes and prevents burns and shocks.
- **Does not hold when**: Never; if the discharge path is unclear, do not open the unit.

## 2.3 Valves (tubes) and high-voltage supplies
- **Principle**: Valve equipment commonly uses hundreds of volts on the anode supply, with the potential for lethal shock, even when no hum is heard.
- **How it works / sequence**: Treat the whole power section as live and charged; do a first power-up only with a current-limiting arrangement and a known-good fuse; measure only if you know where the dangerous points are; expect the unit to hold charge until bled down.
- **Moves**:
  - Test heater and anode supply separately where the design allows.
  - Be aware that old high-voltage capacitors can fail violently, and that rebuilding a unit from scratch changes its safety margins.
  - A pre-owned valve amplifier or jukebox is a reasonable project only for someone competent in high-voltage work.
- **Evidence**: Practitioner
- **Trade-off**: These units reward patience and caution; they punish confidence without training.
- **Does not hold when**: The unit is valve-based but battery-powered at low voltage, which still needs normal care.

## 2.4 Cathode-ray tubes and television chassis
- **Principle**: A CRT display holds a very high voltage on the tube (tens of kilovolts in larger sets) and a large vacuum; both can injure.
- **How it works / sequence**: The deflection and high-voltage stages can keep charge on the tube after power-off, and in monochrome and some colour sets part of the circuitry may be live. Discharge, handling and servicing of the tube and its high-voltage stage belong to a qualified technician.
- **Moves**:
  - Do not touch the tube's anode area, the high-voltage cable or the circuit board of a CRT unit unless you have been taught; the tube can implode if broken.
  - Treat the chassis ground of old television sets as potentially live.
  - Small tubes reused in projects (viewfinders, small monitors) carry lower but still dangerous voltages; discharge following the unit's documentation, and keep the high-voltage section isolated.
  - A set with sparks or arcing inside should not be run.
- **Evidence**: Practitioner
- **Trade-off**: A skilled technician makes the work routine; an unskilled attempt makes it hazardous.
- **Does not hold when**: Never for large tubes; the only decision is whether to hand the job on.

## 2.5 Heat, fumes, chemicals and batteries
- **Principle**: Soldering, cleaning and battery work release substances that are harmful in poor ventilation.
- **How it works / sequence**: Ventilate or extract fumes when soldering and using solvents; wear gloves and eye protection with acids, battery electrolyte and fibreglass or mineral wool; keep toner and fine dust away from the lungs; keep flammable solvents away from heat.
- **Moves**:
  - Leaking batteries and lead-acid batteries release corrosive material; remove them early and neutralise and clean their traces.
  - Glued-in battery packs can be dangerous to pry out; swollen lithium packs should not be punctured or heated.
  - Never connect a battery with reversed polarity; many devices have no protection and will be damaged.
  - Electrolysis and plating at high current can react violently; keep currents low and stay with the work.
  - Cutting some plastics with a laser can burn and give off fumes; only cut materials known to be safe to cut.
- **Evidence**: Practitioner
- **Trade-off**: Protective habits slow you down a little and prevent lasting harm.
- **Does not hold when**: The task is a few seconds of soldering on a lightly used board, where basic ventilation is enough.

## 2.6 Static electricity and handling
- **Principle**: Electrostatic discharge damages integrated circuits and memory without visible signs.
- **How it works / sequence**: Touch an earthed point on the equipment before handling cards and chips; use an anti-static mat or strap where parts are sensitive.
- **Moves**:
  - Do not use static as a "test" for a component.
  - Store boards in anti-static bags.
  - Be careful of floor and clothing conditions in dry weather.
- **Evidence**: Practitioner
- **Trade-off**: Strap and mat cost little compared with a ruined board.
- **Does not hold when**: Handling rugged, discrete mechanical parts.

## 2.7 Lasers, light and moving parts
- **Principle**: Invisible infrared light from an optical drive, and visible light from a laser module, can damage eyes.
- **How it works / sequence**: Do not look into the beam of an optical pickup; use an infrared-sensitive camera to see whether a laser is on; use eye protection rated for the wavelength with higher-power lasers used to cut, engrave or project.
- **Moves**:
  - Verify the power class of any laser you reuse; unknown classes are treated as hazardous.
  - Keep hands and hair away from belts and pulleys during tests, and keep spring-loaded parts under control.
  - Heavy cabinets and loudspeakers need two people and a safe lifting plan.
- **Evidence**: Practitioner
- **Trade-off**: Safety equipment is cheap; eyes are not replaceable.
- **Does not hold when**: Never.

## 2.8 Data, privacy and shared responsibility
- **Principle**: Salvaged computers can hold other people's data; the safe default is to protect it.
- **How it works / sequence**: Do not copy, publish or sell personal data found on discarded machines; wipe or destroy drives, or return them; tell the owner if data is found.
- **Moves**:
  - Treat any machine from a business as potentially holding customer or employee data.
  - Document what you did when you handed the data back or destroyed it.
- **Evidence**: Position
- **Trade-off**: Handling data carefully takes time, and it avoids harm to others.
- **Does not hold when**: The machine was wiped by its owner and you can verify it.

## 2.9 A stop-and-hand-off list
Stop and refer to a qualified technician when:
- the unit has a CRT with a large tube, or any exposed high-voltage section;
- there are sparks, burning smells, arcing, or a fuse that blows repeatedly;
- you cannot isolate the unit from the mains or confirm an earth connection;
- you do not understand a circuit well enough to say where a hazardous voltage is;
- mains-connected parts were modified by someone else;
- a laser or battery unit has unknown specifications.

In this model, being able to say "this is beyond what I can do safely" is the most valuable repair skill, and a good result is an unhurt person first, a working machine second.
