# Chapter 1: Triage, Methodical Diagnosis and Evaluating Used Equipment

## Core Idea
Most vintage consumer electronics fail for ordinary, findable reasons, and the order in which you look decides whether the repair takes an hour or a month. In this model the sequence is: understand what the unit is and what was done to it before, look for mechanical and contact faults before electronic ones, power it up in a way that limits damage, measure instead of guessing, change one variable at a time, and write down what you did. The same discipline applies before a purchase, because shipping damage and earlier amateur repairs are common.

## 1.1 Mechanical and contact faults come first
- **Principle**: In aged equipment with moving parts the cheapest explanation is also the most frequent one: perished rubber, hardened lubricant, loose belts, dirty or oxidised contacts.
- **How it works / sequence**: Inspect and move every mechanism by hand (power off) and note what drags, slips or crumbles; clean contacts (connectors, slots, sockets, potentiometers, relays, switches) and reseat boards and memory; only then open the electronics.
- **Moves**:
  - Look for belts that are melted, stretched, missing or sticky, rubber rollers that are glazed or sticky, gears that have cracked, and old grease that has set.
  - Clean contacts with isopropyl alcohol and reseat plug-in cards; many "dead" or "unstable" machines are poor contacts.
  - Listen for what the mechanism does when it stops (a protection circuit often reacts to a mechanical or sensor fault, not to an electronic one).
- **Evidence**: Practitioner
- **Trade-off**: Mechanical work is cheap but slow to do well; skipping it and replacing electronic parts "to be safe" feels productive and often changes nothing.
- **Does not hold when**: The unit shows burnt smell, bulged or leaking capacitors or blown fuses on arrival; then the electronic fault is already visible.

## 1.2 Service documentation and what to do without it
- **Principle**: A service manual narrows the search more than any amount of inspection, and it also holds the alignment values.
- **How it works / sequence**: Identify the exact model and revision, find the schematic and adjustment procedure, check that the document matches the unit, then follow the signal or the supply from where it stops.
- **Moves**:
  - Expect manuals in another language or for a close sibling model; compare the board against the drawing before trusting it.
  - Without a schematic, reconstruct the circuit by following traces and use component datasheets to see where a pin should receive a supply.
  - Treat a datasheet as the way to identify an unmarked transistor or regulator (polarity, pin-out).
- **Evidence**: Practitioner
- **Trade-off**: Hunting for a manual can take longer than the repair; a wrong-revision manual can mislead.
- **Does not hold when**: The unit is a simple mechanical fault that is visible and fixable without a drawing.

## 1.3 Previous work, photographs and notes
- **Principle**: Before touching anything, learn what somebody else already touched.
- **How it works / sequence**: Inspect for modified wiring, replaced parts, jumpers moved, new fuses, missing screws and glue; photograph or note every connector and flat cable before removal; keep a log of what each step changed.
- **Moves**:
  - A reversed connector or a jumper moved to the wrong position by a previous owner can be the whole fault, and can burn a fuse as soon as power is applied.
  - Label connectors; take photographs before and after each disassembly stage.
  - Keep a record of values measured before and after, so that a regression is visible.
- **Evidence**: Practitioner
- **Trade-off**: Documentation costs minutes at each stage and saves hours at reassembly.
- **Does not hold when**: Never; the only variation is how formal the notes are.

## 1.4 Isolate variables and use known-good comparison
- **Principle**: Diagnosis is elimination: reduce the system until the fault stays on one side.
- **How it works / sequence**: Remove or disconnect one subsystem at a time (drive mechanism, boards, peripherals, an extra card, parallel components) and watch whether the symptom changes; compare with an identical unit or swap a board between two units to see whether the fault follows the board.
- **Moves**:
  - If a unit with its mechanism removed no longer runs hot or no longer trips protection, the fault is in what was removed.
  - A component in parallel with a short can be lifted to find the one that is shorted.
  - Test components cold: a coolant spray can reveal a part that fails only when warm, a heat camera shows which part is abnormally hot; a hot component that should not be hot is a lead.
  - When working on computers, power and test one machine at a time with other machines and storage disconnected.
- **Evidence**: Practitioner
- **Trade-off**: Swapping boards between two faulty units can create a second fault; use it only when one unit is known good.
- **Does not hold when**: The fault is intermittent and disappears when the unit is disturbed; then log conditions and use thermal and mechanical stress deliberately.

## 1.5 Measure rather than assume; do not replace by default
- **Principle**: A measurement beats a hunch, and a fault found is better than a part replaced.
- **How it works / sequence**: Measure supply rails first, then bias and signal points the manual lists; use a series current limiter or bench supply with a current limit for the first power-up; compare each reading with the expected value; only then decide on a component.
- **Moves**:
  - Check rail voltages before connecting signal cables.
  - A capacitor test in circuit with an equivalent series resistance (ESR) meter is quick; unsoldering and measuring out of circuit can make a bad electrolytic look better, so interpret it carefully.
  - Replacing every electrolytic capacitor is generally harmless and often wise on very old equipment, but it should not be mistaken for diagnosis: many units are found with capacitors that test good while the real fault is mechanical or a cold joint.
- **Evidence**: Practitioner; **Contested** on whether to replace capacitors wholesale as routine (see chapter 4).
- **Trade-off**: Wholesale replacement removes a class of faults and adds risk of assembly errors; selective replacement keeps the machine more original.
- **Does not hold when**: The unit has a known capacitor series with a bad reputation; then replacement is the baseline.

## 1.6 Cold joints, broken traces and cracked boards
- **Principle**: Intermittent faults are often a hairline fracture in a joint or trace, and a small repair is better than replacing the board.
- **How it works / sequence**: Inspect under magnification; flex gently while monitoring the symptom; resolder suspicious joints (large components, power connectors, bridge rectifiers); rebuild corroded or lifted traces with thin wire and resin.
- **Moves**:
  - Reflow joints at connectors, transformers and heavy parts first.
  - Where electrolyte from a leaking capacitor has eaten traces, clean the residue thoroughly before rebuilding the track.
  - A flat cable that has cracked can be the whole fault in a display that does not light.
- **Evidence**: Practitioner
- **Trade-off**: Repairs by wire jumpers are strong but are also visible and make later servicing harder.
- **Does not hold when**: Corrosion has spread under components; then the board may not be economical to save.

## 1.7 Knowing when a unit is not worth saving
- **Principle**: Not every machine is recoverable, and an honest stop is part of the method.
- **How it works / sequence**: Decide in advance what would make you stop: crumbling plastics, missing proprietary parts, no documentation and no donor, hours of work with no cause found.
- **Moves**:
  - Plastics that turn to wax or powder, brittle zinc-alloy parts and ruined proprietary mechanisms are often terminal.
  - A unit that cannot be repaired may still be useful for parts, or as a display object; keep the useful donor parts.
  - Some faults stay unsolved; recording that the cause is open is more useful than an invented explanation.
- **Evidence**: Practitioner
- **Trade-off**: Persistence teaches a lot; sunk time is not a reason to continue.
- **Does not hold when**: The unit is rare and has value in being preserved; then specialist help is the better route.

## 1.8 Evaluating a used unit before buying and shipping it
- **Principle**: Treat the description as a claim; most of the risk is in what the seller cannot see.
- **How it works / sequence**: Ask for photographs of the underside, internals, the mechanism and the serial plate; ask what has been done to it; check the current and voltage rating matches your mains; estimate the cost of belts, rollers and capacitors before agreeing to a price.
- **Moves**:
  - Machines described as "tested" may only have been switched on; ask what was actually tested.
  - Heavy machines are damaged in transit: demand double boxing, firm internal support and, for tape machines, a locked transport or removed tapes; photograph the unpacking before anything else.
  - For free or very cheap lots, budget for parts that cannot be sourced; keep the manual-less units as donors.
  - Assume stored data on computers and servers is private: take it seriously and delete or return it as the situation demands (chapter 7).
- **Evidence**: Practitioner
- **Trade-off**: Careful vetting reduces surprises and also loses some bargains.
- **Does not hold when**: The purchase is a deliberate gamble for parts, where the price already prices in failure.
