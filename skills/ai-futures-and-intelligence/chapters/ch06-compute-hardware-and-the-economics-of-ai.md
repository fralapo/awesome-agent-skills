# Chapter 6: Compute, Hardware and the Economics of AI

## Core Idea
In this model the pace of AI is set by a chain of physical and economic constraints (chips, memory, packaging, power, capital) and by how the economy absorbs the output. The binding constraint moves over time, so any "bottleneck" claim needs a date. Figures below are **dated snapshots (2026; some marked unverified)**: use them for the shape of the argument, re-check before relying on them. For GPU-memory arithmetic when serving a model see ch07 and `software-architecture` ch25.

## 6.1 Chip scaling: schedule risk beats ambition (position)
- **Thesis**: do not put too much innovation into one process node; the more new things at once, the harder the yield and the schedule, and the customer wants a predictable schedule.
- **Mechanism (dated example)**: a node was targeted for 2016 and started manufacturing in 2018 after very aggressive "hyper-scaling" done without a new lithography tool, because that tool was judged not ready. A competitor adopted extreme-ultraviolet lithography (13.5 nm light, about 14 times shorter wavelength than earlier tools) in volume in 2019 and another node in 2020, while the delayed firm's first such product came in 2023: about four years of extra experience for the rival. The lesson drawn was a *phase-gate*: maturity metrics a technology must hit to move from pathfinding to development.
- **For**: a clear causal story for a famous slip.
- **Against**: waiting for a tool to mature can also lose the race; the right amount of innovation per node is a judgement.
- **Falsified by**: evidence that the firms that bundle more novelty per node do not slip more often.
- **Does not hold when**: a tool is already mature; then adopting it early is cheap.

## 6.2 Lab to product takes about a decade (position)
- **Thesis**: a novel architecture (stacked transistors) or material (atom-thin conductors, new interconnect metals) needs a long tail of integration steps; a working lab device is not a product.
- **Mechanism**: failure modes include adhesion (nothing sticks to the film), unwanted gas interactions with later steps, non-hermetic capping, rising aspect ratios when stacking. Defects are found by in-line inspection of wafers and end-of-line electrical test, then cross-sectioned to locate the layer at fault.
- **Trade-off**: a simplified version that works may be no better than the incumbent; it must be evolved to beat it.
- **Use**: "a lab demo exists" implies years, not months, for product impact.

## 6.3 Edges, not area: communication limits (mechanism)
- **Mechanism**: doubling a chip's width and length gives four times the area for circuitry but only twice the edge for communication; many AI workloads are limited by data movement, not arithmetic. Hence stacking whole chips in one package and putting memory stacks on the chip's edge ("shoreline").
- **Snapshot (2026)**: one stack of the current high-bandwidth memory generation: about 2048 bits wide at about 10 giga-transfers per second, roughly 2.5 TB/s per stack, within about 13 mm of edge; a conventional DDR interface in the same edge length: 64-128 bits at 6.4-8 GT/s, about 64-128 GB/s. About an order of magnitude more bandwidth per edge.
- **Consequence**: a die has a maximum size, so edge is the scarce resource; adding cache helps but does not remove the limit.
- **Does not hold when**: the workload is compute-bound (large batches of dense matrix multiplication), where arithmetic units matter more.

## 6.4 Memory crunch and spillover (position, snapshot)
- **Position**: high-bandwidth memory takes several times the wafer area per bit of ordinary memory (about 4x; approximate, dated), so a bit for AI displaces about four bits for phones and laptops.
- **Snapshot claims (2026, conflicting, unverified)**: one analyst put memory at about 30% of large-cloud capital spending for the year (a third), another estimate put it at half (position); treat as "a very large share" and re-check. A worked consumer example: a phone with 12 GB; memory price per GB roughly tripled (from about $3-4 to about $12), so about +$100 for DRAM, about +$150 including flash storage, about +$250 at the shelf once the maker's margin is passed on.
- **Consequence (position)**: consumer devices improve more slowly or get worse; public sentiment toward AI sours as a side effect.
- **Against**: memory is a cyclical industry; price spikes invite capacity that later crashes; one-year extrapolations are weak.
- **Falsified by**: new memory capacity arriving faster than demand within the next one or two years.

## 6.5 Which bottleneck binds? It changes (position)
- **Thesis**: some years the limit is packaging, then power, then chips. Over a multi-year horizon the long-lead-time items bind.
- **Mechanism**: lead times differ. A data centre can be built in under a year (some in about 8 months); a fabrication plant takes about 2-3 years; tools have long lead times; packaging is simpler. Earlier shortfalls (packaging, power) were short-lead items that could be fixed; the chip supply chain itself is not. Capacity once shifted from phone and PC chips to data-centre chips is now largely used up: the largest customers of the leading foundry and of the largest memory maker are AI-chip companies.
- **For**: explains why the constraint kept changing and why a 5-year view points back to semiconductors.
- **Against**: a snapshot of what is scarce is a poor predictor; a shortage prompts investment that may remove it quickly (as for power purchase and turbine deposits placed years ahead).
- **Falsified by**: a multi-year period in which power or data-centre construction, not chips, is again the stated limit for most buyers.

## 6.6 Capacity arithmetic: revenue to gigawatts (a method)
- **Method**: translate revenue growth into compute. Example (one analyst's back-of-envelope, 2026): if a lab keeps adding about $6B of revenue per month for 10 months, that is about $60B; at the gross margin reported at the time, about $40B would be inference compute; at about $10B of rental cost per gigawatt-year that needs about 4 GW added, assuming training stays flat. Industry deployment was put at roughly 20 GW in the year.
- **Position on strategy**: a firm that was conservative on compute commitments (to avoid bankruptcy if revenue turned) may have to buy later from lower-quality or newer providers; a firm that signed very large deals early gained access but created credit-market fear that the end buyer could not pay, until fundraising answered it.
- **For**: shows how revenue claims constrain capex and power claims.
- **Against**: margins, prices per token and efficiency change fast; straight-line revenue extrapolation is arbitrary.
- **Use**: when told "revenue will grow X", ask for the implied gigawatts, chips and capital.

## 6.7 AI's share of the economy may fall as AI improves (position)
- **Position**: a share can shrink even as a technology gets better, when automated things become cheap and the economy's spending shifts to what remains scarce. Whether the machine-only economy forms a closed loop that shrinks the human-only share is the debate.
- **Mechanism**: structural change; automated goods get cheap, income goes to services (the "lump of labour" fallacy was the error of expecting a fixed amount of work). Early nineteenth-century worries that machines would cause mass unemployment were right about which jobs vanished and wrong about aggregate employment; the prime-age employment rate was, in 2026 figures, near its historical peak apart from around 2000.
- **Arguments for slow automation (position)**: (a) reliability: a complex good can be destroyed by one failing component, so a 9-in-10 success rate is not enough, "nines" matter; (b) automating nine tenths of a job at lower quality may not pay; (c) licensing, liability and ownership (someone must be answerable); (d) future production flows organised for fast machine-to-machine communication may make integrating humans costly even where humans retain a comparative advantage.
- **Arguments against slow automation**: frictions such as licensing and political reservations for humans are transitional; once AI-run systems are efficient, systems that adopt them outcompete others.
- **Evolutionary angle (position)**: the preferences of entities that survive determine what a large economy produces; the same may apply to AI agents and firms with AI components, even without catastrophic misalignment.
- **Epistemic point**: individual economists' forecasts disagree in every direction; the proposal is to build aggregate forecasts (prediction markets) and to collect missing data: demand elasticities, which tasks are created and destroyed (an occupational-task database was described as rarely updated and low quality).
- **Falsified by**: labour share falling toward zero while wages and employment fall (supports automation doom), or labour share and employment stable after broad task automation (supports structural change).
- **Does not hold when**: the model's assumption of substitutability between human and machine labour fails in either direction; check which tasks are complements.

## Checklist for this chapter
1. Which constraint binds in the horizon of the claim, and what is its lead time?
2. Are the figures dated, and is the original uncertainty preserved?
3. Is the claim about the absolute size of AI or about its share?
4. What reliability (how many nines) does the task need, and who is liable?
