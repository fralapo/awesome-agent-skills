# Chapter 5: Reading Benchmarks, Buying and Building, and Why Markets Move

## Core Idea
A benchmark is a measurement of one configuration, a purchase is a decision under a budget and a use, and a price is the result of supply and demand with some friction. In this model, good buying means matching the test to your use, comparing cost per performance within a tier, and understanding why availability and prices change so you do not mistake a shock for a trend. Specific products, prices and rankings go stale in months; the method does not.

## 5.1 What a benchmark number is
- **Thesis**: a number is a setup, a game, a scene and a run; it answers one question.
- **Mechanism**: average frame rate hides stutter, so read the low percentiles (1% lows) and frame-time plots; run each test several times and report the spread; sample variation between chips of the same model (the silicon lottery) and power limits change results; driver, firmware, memory configuration, case airflow and room temperature are part of the setup. Differences of one to three percent between runs are noise, and tuning tips that claim gains inside that band are not evidence. Open-source suites let you rerun the same test before and after an upgrade and compare with others.
- **Trade-off**: more runs and tools cost time but make a gain visible.
- **Does not hold when**: a gain is large and repeatable (a tuned memory change of tens of percent in a bound game).

## 5.2 Spotting a misleading benchmark
- **Thesis**: charts mislead by setup, not arithmetic.
- **Checks**: (1) resolution and settings: does it match your monitor and quality level (2.6)? (2) What was compared: native versus upscaled, with or without frame generation (3.3)? (3) Are the lows shown? (4) Test memory and power limits equal? (5) Were results taken at launch drivers? (6) A synthetic score versus the applications you run? (7) Sponsored or provided samples (note disclosure)? (8) Is there a different test that reveals the opposite? (9) Does the claim extrapolate from one title? (10) Is a "gaming" label hiding an application test that mixed workloads?
- **Operating-system tweaks**: claims that a deletion, a service change or a "booster" speeds up a PC mostly vanish under measurement (removing a small background program frees little memory; defragmentation helps spinning disks, not flash; indexing, prefetch and visual effects show no measurable change); a PC that "gets fast after cleaning" often had malware or too many background programs. The paging file should stay automatic; forced timer-resolution tweaks and V-Sync have trade-offs (V-Sync removes tearing and adds latency).
- **Trade-off**: skepticism costs time and can slide into denial; real gains exist.
- **Does not hold when**: you can reproduce the test yourself.

## 5.3 Buying method: use first, then tier, then price
- **Thesis**: decide what you do, at which resolution and refresh, on which monitor, then rank cards and processors by cost per performance within the segment.
- **Mechanism**: in a crowded mid-range tier, a dozen cards can have close prices and performance that does not scale with price. For a gaming build, put most of the budget into the graphics card and choose a processor that does not bottleneck it at your resolution; unbalanced allocation is deliberate. Buy for the use you have, not for a hypothetical later one; "future-proofing" with the next tier up rarely pays, because the replacement arrives with better value. Platform and memory choices (2.4, 2.7) fix the upgrade path.
- **Timing, two positions**: (a) wait and watch offers; day-one prices are usually the highest and festive periods raise them; the used market is cheapest soon after a new generation arrives; a common window is some months after launch. (b) Waiting for each part's offer often costs more than it saves: set a budget, buy the interdependent parts together, and do not defer the graphics card if stock is tight. Decision rule: wait when stock is plentiful and a new generation is near; buy together when supply is tight or prices are rising.
- **Trade-off**: patience against the cost of waiting for a part.
- **Does not hold when**: your current machine has failed and you need it now.

## 5.4 Used parts: how to buy safely
- **Thesis**: the used market rewards patience and verification.
- **Checks**: a compatible power supply and connectors; the history of the item; photos of the actual item (not stock images) and a demonstration; payment through a method with buyer protection, with the item described as working in writing (a listing "sold as faulty" removes protection); face-to-face testing for local sales; for graphics cards, a sustained stress test, fans, thermal paste and pads. The used market is good value at low budgets; at higher budgets (illustratively above a few hundred) the saving over new, with warranty, shrinks. Miners rarely dump stock in bulk.
- **Trade-off**: lower price against no warranty.
- **Does not hold when**: the seller is a business offering a warranty.

## 5.5 Compatibility and assembly checklist
- **Method**: socket and chipset match the processor; memory type and slot count; cooler height and case clearance; radiator and graphics-card length; power-supply connectors and wattage; storage interfaces and lanes; case airflow; firmware version for new processors on old boards; all cables native. Ordering mistakes cost days; one afternoon with the specification sheets saves them.

## 5.6 Why prices and availability move
- **Thesis**: price is the meeting point of demand and supply; shocks arrive from either side, and the part of the chain that earns the most margin gets production capacity first.
- **Mechanism**: a sudden demand spike (a new use that can run on graphics cards, such as proof-of-work mining, in 2017-2018 and 2020-2021, dated) can absorb orders at the factory before shops are served. A supply shock (a pandemic, a shipping bottleneck, factory closures around a holiday) lowers output at the same time; chips are also contested between industries. The distribution chain adds margin at every level, and a longer chain (for example in one country compared with another, reported) adds more. A software block meant to deter miners was bypassed within about two months; a durable segmentation needs hardware differences, hence separate products. When a demand spike ends, used stock floods the market and prices fall.
- **2022-2026 pattern (reported, dated)**: after the 2021 peak, shipments fell and the top-tier card price rose sharply, attributed to weak competition at the top and buyers who accepted it, not only inflation and exchange rates; in this model, concentrated supply (a single maker of advanced lithography machines, a single leading foundry, a single dominant card vendor) concentrates leverage; manufacturers shifted capacity and margin toward memory for data centres (margins on that segment were reported far higher than on consumer parts), and the consumer share of memory demand is small, so a buyer boycott does not move the market. A similar memory shift raised prices in 2017. In April 2025 tariffs exempted wafers and bare chips but not boards and cards (reported). Hypotheses worth stating as hypotheses: coordinated price-setting by memory makers (unverified); any date on which prices normalise (a forecast, not a fact); that entry-level cards will disappear because of integrated graphics (a forecast).
- **Trade-off**: understanding the cause tells you whether to wait; it does not predict the date.
- **Does not hold when**: a local factor dominates (a tariff, a currency swing).

## Common Mistakes
- Comparing numbers from different settings.
- Believing a gain inside the noise band.
- Waiting forever for a better offer, or buying on day one at peak.
- Treating a forecast of prices as a fact.

## Checklist
- [ ] Test matches your resolution and settings?
- [ ] Cost per performance compared within the tier?
- [ ] Compatibility sheet checked before ordering?
- [ ] Used item verified and payment protected?

## Connects To
ch02 (which part limits), ch03 (upscaling, frame generation), ch06 (scams); `economics-finance` (supply, demand and market structure), `ai-futures-and-intelligence` ch6 (memory crunch and AI compute demand).
