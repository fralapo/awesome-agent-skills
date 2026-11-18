# Chapter 1: Power Delivery and the Power Supply

## Core Idea
Every component lives on the rails the power supply produces. In this model the supply is the one part whose failure can take other parts with it, so its quality is judged by how steady the voltages stay under load, not by the number on the label or the efficiency badge. This chapter covers what the label says, what it hides, how to size a supply, why connectors burn, and how to estimate running cost.

## 1.1 Rated power is a ceiling, not a quality
- **Thesis**: the watt figure on the box tells you the design target, not whether the unit delivers it cleanly or at all.
- **Mechanism**: a supply converts mains voltage to a few DC rails (a large 12 V rail and smaller 5 V and 3.3 V rails). Cheap units can print a big number and still fail to hold it: the primary-side capacitors may have a lower voltage rating than a quality design uses, an input filter may be missing, and cooling may limit sustained output. What counts is the power available on the 12 V rail, because that is where the processor and graphics card draw.
- **Trade-off**: spending more buys margin and protection circuits; past a sufficient level extra wattage buys nothing.
- **Does not hold when**: the unit is a known-good design from an established platform and the price merely reflects branding.

## 1.2 Efficiency badges measure waste heat, not quality
- **Thesis**: an efficiency tier says how much wall power becomes useful output at test points; it says nothing about ripple, regulation or protections.
- **Mechanism**: efficiency is output power divided by input power. At 80% efficiency a 300 W load draws 375 W from the wall; at 90% it draws about 333 W. The 42 W difference is heat the supply must shed and a small running cost (section 1.6). Tests are run on samples submitted by the manufacturer; a public certification database lets you check a suspicious badge. A mid-tier badge on a good platform can be better than a top tier on a poor one.
- **Trade-off**: higher efficiency reduces heat and noise slightly and raises price.
- **Does not hold when**: the machine runs near idle most of the time, where the efficiency curve and standby draw matter more than the peak figure.

## 1.3 What quality looks like: regulation, ripple and platform
- **Thesis**: a good supply holds each rail steady while the load changes quickly; the evidence is measured, not printed.
- **Mechanism**: the common desktop standard allows each rail to deviate by about five percent (so a 12 V rail stays roughly between 11.4 V and 12.6 V) and limits ripple, the fast residual wobble, to roughly 120 mV peak-to-peak on 12 V and 50 mV on the smaller rails (commonly cited limits, check the current standard). Measurement needs a reproducible load outside the PC, an oscilloscope for ripple and a power meter for efficiency; unboxing and switching on with no load say nothing. Other indicators: how far the 12 V rail sags at full load, and regulation under unbalanced load (cross-load). Most brands rebadge a handful of manufacturing platforms, so the same brand name can cover excellent and poor series; judge model by model, by teardown and measurement from reviewers with instruments.
- **Trade-off**: reading measured reviews takes time; it is the main protection against a bad unit.
- **Does not hold when**: no instrumented review of the exact model exists; then favour models from a proven platform with a long warranty.

## 1.4 Sizing: sum the peaks, add margin, mind the spikes
- **Thesis**: size by the components' maximum draw, plus margin, not by online calculators or by the size of the badge.
- **Mechanism**: add the maximum power of the processor and graphics card, then a margin for the rest of the system (a few tens of watts for drives, fans and memory; RGB lighting adds only a handful of watts and does not change frame rates). Modern graphics cards can briefly spike well above their average board power, for fractions of a millisecond; the supply must tolerate transients, so a unit sized with headroom or designed for them is safer. A supply is often most efficient in the middle of its load range, but that is a minor effect. For an ordinary build a quality unit in the lower hundreds of watts is enough; high wattage is needed only for high-power graphics cards or heavy overclocking.
- **Trade-off**: too small a unit trips protection or shuts down under spikes; too large costs more and gains little.
- **Does not hold when**: the build uses several high-power cards or a workstation processor; then follow the component maker's guidance.

## 1.5 Connectors, contact resistance and burning cables
- **Thesis**: a burnt connector is usually a high-resistance contact heated by a large current, not a mystery.
- **Mechanism**: heat is current squared times resistance (the Joule effect). A high-current graphics connector with a small contact area and a bend, or a partially inserted plug, raises the resistance of a few pins; those pins carry more current and heat further, a runaway. Adapters add a joint. Defences: seat the connector fully, avoid sharp bends near the plug, prefer a native cable from the supply to an adapter, and do not mix cable sets between supply models (pin-outs differ even when plugs fit).
- **Trade-off**: tidy cable routing versus bend radius; case width matters.
- **Does not hold when**: the load is low enough that the connector is far from its rating.

## 1.6 Running cost and protection against the mains
- **Thesis**: electricity cost is arithmetic; compare it with the purchase price before paying for efficiency.
- **Mechanism**: yearly cost = (difference in watts x hours per day x 365 / 1000) x price per kWh. Illustration with a made-up price: a 30 W difference for 4 hours a day is 43.8 kWh, which at 0.30 per kWh is about 13 per year, so between two components of the same tier the difference is small. Use the all-in price per kWh (energy plus fixed charges that scale with use), not the energy component alone; the bill also depends on contract terms. "Consumes 300 W" is a peak, not an average: measure a real session. Protection: a power strip with a surge protector, or a line-interactive or online unit with a pure sine output, protects against surges and brief outages. Cutting the supply with a switch at every shutdown causes an inrush current and stress on the input stage; "it never happened to me" is not a test.
- **Trade-off**: protection costs money and a surge protector wears out.
- **Does not hold when**: electricity is very cheap or the machine runs all day under heavy load (then efficiency matters more).

## Common Mistakes
- Buying by wattage and a badge without a measured review.
- Trusting online wattage calculators.
- Using an adapter where a native cable exists.
- Treating a tidy-looking cheap unit as safe.

## Checklist
- [ ] 12 V capacity above the sum of the peaks, with margin?
- [ ] Measured review of the exact model?
- [ ] Native cables, fully seated, gentle bends?
- [ ] Cost estimated with the all-in price per kWh?

## Connects To
ch04 (cooling inside the case), ch05 (buying method), ch06 (backup against power loss); `computer-science-fundamentals` ch4 (why components draw power).
