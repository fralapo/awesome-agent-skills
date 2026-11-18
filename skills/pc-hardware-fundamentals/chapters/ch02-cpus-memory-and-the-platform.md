# Chapter 2: CPUs, Memory and the Platform

## Core Idea
A processor's speed is the product of how much work it does per cycle, how fast the cycles run, how many cores there are, and how quickly it can be fed with data. In this model the last factor, latency to memory, is often the hidden limit, which is why caches and memory tuning matter. The platform (motherboard, chipset, lanes) matters less than its price suggests for most users.

## 2.1 Clock, cores and work per cycle
- **Thesis**: clock speed alone is a poor predictor; compare work per cycle and the software's use of cores.
- **Mechanism**: instructions per cycle (IPC) is how much a core completes each tick, so an older design at a high clock can lose to a newer one at a lower clock. More cores help only software that runs several threads at once; a game that is limited by one main thread gains little. Simultaneous multithreading shares a core's resources between two threads and is worth less than a real core. Hybrid designs mix large and small cores; the operating system's scheduler decides where threads run, so behaviour depends on scheduler and driver support.
- **Trade-off**: more cores cost area and power; faster cores cost more per unit of single-thread gain.
- **Does not hold when**: the workload is embarrassingly parallel (rendering, compilation); then cores dominate.

## 2.2 Process node names are partly marketing
- **Thesis**: "7 nm" or "5 nm" no longer measures a physical dimension; compare density, power and measured results.
- **Mechanism**: the node name started as a feature size but drifted into a generation label; two makers' nominally different nodes can have similar transistor density. Architecture and design choices (cache, voltage curves) matter as much as the label. Manufacturing difficulty (multiple patterning, yields) and a split between designing and fabricating chips explain why one company can lead another on node for years. Illustrative, dated: around 2020 one maker's 14 nm-class and another's 7 nm-class processes were less far apart in density than the names suggest.
- **Trade-off**: a better node lowers power at the same speed but raises cost per wafer.
- **Does not hold when**: comparing two chips on the same foundry process; then the label is a fair proxy.

## 2.3 Caches, latency and why memory is the bottleneck
- **Thesis**: a cache keeps recently used data close to the core, cutting the wait for main memory.
- **Mechanism**: a small fast cache per core, a larger second level, and a big shared third level; each level trades size for speed. A hit costs a few cycles, a miss that reaches main memory costs hundreds (`computer-science-fundamentals` ch4). Stacking extra cache vertically on a chip raises the hit rate for cache-hungry games and costs heat and clock headroom; where only some core groups get the stacked cache, the scheduler, chipset driver and firmware must place threads on the right group. At very high frame rates the limit is often this chain of processor, memory and latency, so memory tuning (frequency and timings) can raise frame rates by a few percent to a sizeable share depending on the platform (reported, varies widely); an inexpensive processor with tuned memory can beat a pricier one that is left at defaults in such cases.
- **Trade-off**: more cache raises cost; tuning takes time and risks instability.
- **Does not hold when**: the game is limited by the graphics card, as it usually is at high resolution (see 2.6).

## 2.4 Memory configuration: channels, rank, frequency and generation
- **Thesis**: use at least two matched modules in the proper slots, then buy by the platform's sweet spot instead of the highest number.
- **Mechanism**: dual-channel doubles the path to memory; a single module halves bandwidth. Some platforms tie memory speed to an internal fabric clock, so memory speed affects performance more there; other designs decouple them. A vendor-recommended kit for a platform usually sits where the fabric and memory run in step; frequency beyond it brings less. The newer memory generation wins some workloads and not others (and a cheaper previous generation can be better value for a limited budget); the choice of platform also fixes the generation and the upgrade path. Memory profiles (XMP, EXPO type) are manufacturer-certified overclocks and may need enabling in firmware. More capacity avoids paging; speed rarely replaces it.
- **Trade-off**: a newer generation costs more now and offers longer platform life.
- **Does not hold when**: memory prices swing sharply (chapter 5) and the cheaper generation is the only affordable one.

## 2.5 Power, heat and voltage: peak is not average
- **Thesis**: heat and consumption follow voltage and clock; limiting power can cost little performance.
- **Mechanism**: dynamic power rises with the square of voltage and linearly with clock, so the last few percent of speed cost disproportionate power. "Draws 300 W" describes a peak under a synthetic load; in a session the average is much lower, and in one large set of tests a processor given a power limit drew on average about 30% below that limit, because everyday loads rarely reach it (reported). Where default voltages are set high, an undervolt or a power limit can cut heat and power with minimal loss, but stability must be proven with long stress tests; a system that passes a short run can still crash in a rare load. Sustained high voltage is also what degrades silicon over years; when a vendor ships a processor family with excessive default voltage, the cost is both heat and trust (reported, dated example from 2023-2024: one processor family with high default voltages and a later microcode and firmware fix cycle).
- **Trade-off**: tuning gains efficiency and risks silent instability.
- **Does not hold when**: warranty terms forbid changes or the system must run unattended; then keep defaults.

## 2.6 Which component limits you: the resolution and settings rule
- **Thesis**: the slowest stage sets the frame rate, and which one it is depends on resolution and settings.
- **Mechanism**: at low resolution and high frame rate the processor and memory become the limit; at high resolution the graphics card saturates first and many processors give nearly the same result. A "gaming processor" ranking built at low resolution and lowest settings exaggerates differences that disappear in your configuration. Prefer frame-time data and real-application tests over peak figures in a narrow setting.
- **Trade-off**: matching the test to your setting costs reading time.
- **Does not hold when**: you play competitive titles at very high refresh rates where the processor genuinely limits.

## 2.7 Platform: chipset, lanes, form factors
- **Thesis**: pay for the platform features you will use.
- **Mechanism**: a higher chipset tier adds lanes, ports and power-delivery headroom; for a gaming budget the money is better spent on the graphics card. Newer interface generations (PCIe) help mainly storage; a graphics card on a slower generation or on fewer lanes (each halving of lanes, and each step back a PCIe generation, halves the bandwidth) can lose performance, especially when it runs out of graphics memory and spills over the bus. A cheap mini PC can carry soldered memory and storage, weak cooling, a questionable power brick and preinstalled software; reinstall the system from clean media (chapter 6). Compact laptops with hybrid cores depend on the cooling design of the single model; the same chip varies with chassis.
- **Trade-off**: future-proof slots cost today.
- **Does not hold when**: you need many drives, add-in cards or heavy I/O.

## Common Mistakes
- Comparing processors by clock or core count alone.
- Running one memory module in a dual-channel platform.
- Treating a peak power figure as running cost.
- Believing a low-resolution ranking applies to your monitor.

## Checklist
- [ ] Which component limits the target resolution and settings?
- [ ] Two matched memory modules, profile enabled, long stress test passed?
- [ ] Platform features matched to real needs?

## Connects To
ch01 (power), ch04 (cooling), ch05 (reading benchmarks, buying); `computer-science-fundamentals` ch4 (caches, memory) and ch5 (threads).
