# Chapter 4: Power Supplies, Electrolytic Capacitors and Parts That Fail

## Core Idea
After mechanics, the power section is the next place faults concentrate: filter capacitors, rectifiers, regulators, fuses, batteries and connectors. In this model the aim is to find which part failed and why, rather than to replace everything on suspicion. A failed part often has a cause upstream (a short, wrong voltage, a previous repair), and putting a new part into the same condition simply kills it again. All procedures here involve circuits that can be dangerous; read chapter 2 first.

## 4.1 First power-up: limit the current, raise the voltage gradually
- **Principle**: The first minutes of power on an unknown aged unit are the most likely moment for a new fault.
- **How it works / sequence**: Inspect, discharge, check the fuse and the cord; connect through a current limiter (a lamp in series with the mains, a current-limited bench supply for low-voltage units); watch for a lamp that glows steadily bright; measure rails before connecting signals.
- **Moves**:
  - A lamp in series limits fault current: if it lights at full brightness with the unit connected, there is a heavy load or short; a dim glow is a normal start.
  - A variable transformer ("variac") lets you raise mains voltage slowly, commonly up toward the nominal value in steps; some practitioners use a variac plus a lamp; both are damage-limiting measures, not isolation, so shock risk remains.
  - Bench supplies with a current limit are the safest first source for low-voltage devices; set the limit near the expected draw.
  - Check mains voltage setting and the voltage selector against local mains before first use (a 110/220 selector in the wrong position destroys parts).
  - Measure supply rails with the signal cables unplugged.
- **Evidence**: Practitioner
- **Trade-off**: A slow, careful start adds an hour; a first blind power-up can add a month.
- **Does not hold when**: The unit is battery-powered at low voltage, where reversed polarity and shorts are the main risks.

## 4.2 Electrolytic capacitors: ageing, tests and replacement
- **Principle**: Wet electrolytic capacitors dry out, bulge, leak and lose capacity; leaking electrolyte corrodes boards.
- **How it works / sequence**: Look for bulged tops, brown residue and discoloured boards; measure suspicious parts with a capacitance and ESR meter; replace those that fail, and clean corrosion.
- **Moves**:
  - ESR (equivalent series resistance) is the best quick screen for an electrolytic; a part that tests in circuit may be fine or may be hiding a problem; unsoldering a capacitor can let it re-form and give a better reading than in service.
  - Tantalum capacitors are not measured the same way with an ESR meter; use the manual.
  - Choose replacement values matching the original capacitance, with a voltage rating at or above the original and a temperature rating suitable for the position; matching physical size and lead spacing helps mechanical fit.
  - Check polarity on the board and on the part; a reversed capacitor can burst.
  - When an exact value is missing, series and parallel combinations are a method, subject to voltage sharing.
  - A part that warms up in operation is suspicious; if a capacitor runs hot, find out why before swapping.
- **Evidence**: Practitioner; **Contested** on replacing all electrolytics in a unit (a common routine versus a diagnosis-led approach). The sources agree that replacement seldom hurts and often does not fix the actual fault.
- **Trade-off**: Wholesale replacement costs parts and may remove originality; selective replacement takes more measurement.
- **Does not hold when**: A known bad batch series, in which routine replacement is sensible.

## 4.3 Filter capacitors, hum and unusual stress
- **Principle**: The main filter capacitors smooth the rectified supply; when they age, hum increases and rails sag.
- **How it works / sequence**: Hum that appears at twice the mains frequency points to filtering; measure rail ripple with an oscilloscope; replace filter capacitors that are out of tolerance.
- **Moves**:
  - In a valve unit the filter capacitors are high-voltage parts; see chapter 2 and chapter 5.
  - Deflection circuits in displays stress their capacitors heavily; a part of low rating may fail again, and the correct replacement may need a much higher voltage rating than first guessed. A rating chosen by trial in a repair is a position, not a rule; follow the manual.
  - A capacitor that is physically failing may fuse and short the supply.
  - On computer power supplies, a dead supply sometimes resumes with a replaced filter capacitor; check the rails with a meter first.
- **Evidence**: Practitioner
- **Trade-off**: Higher-rated parts are larger and may not fit.
- **Does not hold when**: Hum comes from grounding or wiring rather than filtering (chapter 5).

## 4.4 Rectifiers, regulators, zener diodes and fuses
- **Principle**: Rectifiers, voltage regulators and reference diodes fail short or open from heat, overload and age; fuses blow for a reason.
- **How it works / sequence**: Test rectifiers out of circuit or with the diode range of a meter; test regulators by measuring input and output; replace fuses only with the specified value and type after finding why they blew.
- **Moves**:
  - Fixed positive and negative regulators in a series look similar but have different pin-outs; check the datasheet before fitting; a reversed or wrong regulator burns fuses.
  - Counterfeit or poorly marked regulators exist; a part that gives a wrong output voltage may be a fake. Buy from reputable sources.
  - A burnt zener or reference can be replaced by a regulator and diodes when an exact part is not available; check the resulting voltage.
  - Never replace a fuse with a bigger one or a wire to "make it stay on".
  - Jumpers and selector links that choose voltage should be checked after anyone has handled the unit.
- **Evidence**: Practitioner
- **Trade-off**: A substitute regulator saves a project but changes the original.
- **Does not hold when**: The fuse is blowing because of a hidden short; do not keep replacing it.

## 4.5 Batteries, backup cells and charging circuits
- **Principle**: Memory and clock batteries leak and die; leaked chemicals destroy traces and parts.
- **How it works / sequence**: Remove aged cells immediately; clean corrosion with the appropriate neutraliser; replace with the correct type; check any series diode or charging circuit that the manual specifies.
- **Moves**:
  - A flat backup cell in computers produces strange symptoms: lost settings, a drive not recognised, memory errors, keyboard glitches.
  - Soldered-in cells can be replaced by a holder with a correct cell or an external pack; check that the charging circuit does not try to charge a non-rechargeable cell.
  - Lead-acid and old rechargeable packs can leak or swell; handle with gloves; replace with an equivalent chemistry or a properly managed pack with protection electronics.
  - Replacing a battery with a different chemistry needs a matching charge circuit; do not assume that physical fit means electrical match.
- **Evidence**: Practitioner
- **Trade-off**: Modern cells give longer life; the charging scheme may need changes.
- **Does not hold when**: The unit is mains-only and has no backup cell.

## 4.6 Connectors, switches, potentiometers and relays
- **Principle**: Mechanical contacts oxidise and wear; a dirty contact can mimic a failed component.
- **How it works / sequence**: Operate the control while watching for crackle; clean with a contact cleaner suited to the part; replace if worn.
- **Moves**:
  - Potentiometers often need cleaning to stop noise; if track wear is visible, replace.
  - Relays that click but do not conduct often have oxidised contacts; clean them.
  - Reseat plug-in boards; clean the edge connector.
  - Applying general-purpose penetrating spray to controls is common but discouraged; if used, it can leave residue and affect plastics. **Contested**.
- **Evidence**: Practitioner
- **Trade-off**: Cleaning is quick; replacement of a custom part may be impossible.
- **Does not hold when**: The part is physically broken.

## 4.7 Cables, wiring and insulation
- **Principle**: Old cloth-covered and rubber-insulated wiring perishes; insulation that crumbles is a fire and shock risk.
- **How it works / sequence**: Inspect all internal wiring and mains cables; replace perished leads with suitable modern equivalents (shielded where the original was).
- **Moves**:
  - Mains-side heat-shrink on switch terminals is a basic safety improvement.
  - Poor insulation next to hot parts points to a deeper problem such as a part running hot.
  - Wiring changed by previous owners should be traced against the manual.
- **Evidence**: Practitioner
- **Trade-off**: Rewiring is slow but removes a class of hidden faults.
- **Does not hold when**: Wiring is sound and original and the unit is intended to stay unmodified.

## 4.8 Substitute and counterfeit parts
- **Principle**: A replacement part is only as reliable as its source.
- **How it works / sequence**: Prefer parts from established suppliers; verify markings, values and behaviour; test a part before fitting it.
- **Moves**:
  - Unmarked or oddly marked components are suspect.
  - Keep a bin of working donor parts from dead units.
  - A modification that fixes a symptom (a different lamp type, a replaced selector) should be documented as a change, so later work knows it is there.
- **Evidence**: Practitioner
- **Trade-off**: Cheap parts from unknown sources save money and introduce risk.
- **Does not hold when**: The part is a trivial passive with wide tolerances, where the risk is small.
