---
name: pc-hardware-fundamentals
description: "Evergreen mechanisms of PC hardware and how to decide: power supplies (rating, efficiency vs quality, ripple, transients, burnt connectors, running cost), CPUs (IPC, cores, caches, memory latency, power limits and undervolting, bottleneck by resolution), GPUs (VRAM, bus, bandwidth, ray tracing, upscaling and frame generation, local-AI memory arithmetic), storage, airflow and liquid cooling, throttling, diagnosing faults, reading benchmarks and spotting misleading ones, buying and building method, used parts, why prices and shortages happen, hardware scams, phishing, ransomware, network isolation and 3-2-1 backups. Use when the user builds, upgrades or diagnoses a PC, asks about temperatures, power or stutter, compares CPUs or GPUs, interprets a benchmark, wonders why prices rose, or worries about a counterfeit or infected device. Gives method, not product picks."
allowed-tools:
  - Read
  - Grep
argument-hint: [component, symptom, benchmark, purchase, or chapter number]
---

# PC Hardware Fundamentals
**Chapters**: 6 | **Corpus**: ~190 practitioner talks on PC hardware, buying, markets and home security | **Generated**: 2026-11-18

## Role and Boundaries

This skill **explains how PC components work and how to decide about them**: what a measurement shows, which part limits performance, what a price or a shortage means, and which habits stop common losses. It gives mechanisms, checklists and decision rules; the user owns the budget and the choice.

| This skill decides | This skill hands off |
|---|---|
| Which component limits a workload; how to read a benchmark; how to size power and cooling; how to check a used or suspicious part; what makes a backup real | CPU cache theory, memory hierarchy, concurrency → `computer-science-fundamentals` ch4-5; network and cryptography theory → ch7-9 |
| Method for choosing between tiers (use, resolution, cost per performance, timing) | Model sizes, quantisation, KV cache, AI economics → `ai-ml-concepts` ch7, `ai-futures-and-intelligence` ch6 |
| Why prices and availability move, framed as mechanism | Market theory and investing → `economics-finance`; legal or tax advice → professionals |
| Home-user security habits and scam recognition | Deep forensics, incident response for a company, legal action → specialists |

**Stay in lane.** The skill names no products and gives no "best buy": models, prices, and rankings go stale within months. Any figure marked "dated" or "illustrative" is a snapshot or a made-up example; limits and standards (voltage tolerances, interface generations) should be rechecked against the current specification. Forecasts (when prices fall, which vendor wins) are hypotheses and are labelled so.

## Facts vs Positions

- **Mechanism / fact**: Joule heating in a connector, how cache hits cut latency, why frame generation adds latency, why RAID does not protect from deletion.
- **Reported result**: a measured figure from one test or one reviewer; dated, not independently verified here.
- **Position**: written "In this model..." or "(position)": for example "an entry-level liquid cooler is not better than air at the same price", "buy for the use you have".
- Every concept in the chapters has four fields: **Thesis**, **Mechanism**, **Trade-off**, **Does not hold when**. Read the last one before applying a rule. Where two positions conflict (for example "wait for offers" versus "buy together"), the chapter gives a decision rule.

## How to Use This Skill

Diagnose before prescribing: ask the workload (games, rendering, local AI, office), the resolution and monitor, the budget and time horizon, the current symptoms and measurements, and whether parts are new or used.

| Task | Start with | Then |
|---|---|---|
| Choose or check a power supply; burnt connector; electricity cost | [ch01](chapters/ch01-power-delivery-and-the-psu.md) | ch04 |
| Processor, memory configuration, power limits, "which part is the bottleneck" | [ch02](chapters/ch02-cpus-memory-and-the-platform.md) | ch05 |
| Graphics card, VRAM, upscaling, frame generation, local AI memory | [ch03](chapters/ch03-gpus-vram-upscaling-and-frame-generation.md) | ch05 |
| Temperatures, airflow, case, cooler, fans, drives, stutter or crashes | [ch04](chapters/ch04-storage-cooling-and-diagnosing-faults.md) | ch01, ch03 |
| Reading or doubting a benchmark; what to buy; used parts; why prices moved | [ch05](chapters/ch05-benchmarks-buying-and-market-dynamics.md) | ch02, ch03 |
| Counterfeit part, cheap mini PC, phishing, ransomware, isolation, backup | [ch06](chapters/ch06-scams-security-and-backup-for-home-users.md) | ch05 |
| Quick lookup | [cheatsheet.md](cheatsheet.md), [glossary.md](glossary.md) | |

## The Core Principles (recurrence order)

1. **Match the test to your use.** Resolution, settings and workload decide which component limits you.
2. **The slowest stage sets the speed.** Find the limit before spending.
3. **Latency often beats raw speed.** Caches, memory timing and bandwidth explain many "same clock, different speed" results.
4. **Labels are not measurements.** Wattage, efficiency tier, process node and "gaming" tags describe intent; measure the thing.
5. **Peak is not average.** Peak power, peak temperature and peak frame rate rarely describe daily use.
6. **Parts protect themselves by slowing.** Throttling is a feature; red flags are crashes and rising idle temperatures.
7. **Noise lives inside a band.** Differences of a few percent between runs are not evidence.
8. **Compare cost per performance inside a tier,** for the use you have, not for a hypothetical later.
9. **Prices are demand meeting supply.** Shocks and capacity allocation explain moves; forecasts of dates are hypotheses.
10. **Verify before you trust.** Seller, part, message, backup: test the claim directly.
11. **Redundancy is not backup.** A backup is a restored copy, one of which is offline.
12. **Isolate what you cannot trust.** Assume a device will fail or be breached and limit its reach.

## Chapter Index

1. [Power delivery and the power supply](chapters/ch01-power-delivery-and-the-psu.md)
2. [CPUs, memory and the platform](chapters/ch02-cpus-memory-and-the-platform.md)
3. [Graphics cards, graphics memory, upscaling and frame generation](chapters/ch03-gpus-vram-upscaling-and-frame-generation.md)
4. [Storage, cooling and diagnosing faults](chapters/ch04-storage-cooling-and-diagnosing-faults.md)
5. [Reading benchmarks, buying and building, and why markets move](chapters/ch05-benchmarks-buying-and-market-dynamics.md)
6. [Scams, security and backup for home users](chapters/ch06-scams-security-and-backup-for-home-users.md)

## Topic Index

- **Airflow, intake and exhaust, VRM cooling** → ch04 (4.4)
- **Air vs liquid cooling, corrosion, pump life** → ch04 (4.5)
- **Backup, 3-2-1, RAID is not backup, snapshots** → ch06 (6.6), ch04 (4.2)
- **Benchmark reading, 1% lows, noise band, misleading charts** → ch05 (5.1-5.2)
- **Bottleneck by resolution** → ch02 (2.6)
- **Caches, latency, stacked cache, memory tuning** → ch02 (2.3-2.4)
- **Compatibility checklist, clearances** → ch05 (5.5)
- **Counterfeit graphics card, fake listings, seller checks** → ch06 (6.1)
- **Electricity cost formula, surge protection, UPS** → ch01 (1.6)
- **Frame generation, upscalers, ray tracing** → ch03 (3.3)
- **Local AI, weights-plus-cache arithmetic, NPU, TOPS** → ch03 (3.7)
- **Market shocks, shortages, memory crunch, mining** → ch05 (5.6)
- **Network isolation, default credentials, wireless security** → ch06 (6.5)
- **Phishing, one-time codes** → ch06 (6.3)
- **Power limits, undervolting, stability testing** → ch02 (2.5)
- **PSU ripple, regulation, platform, sizing, transients** → ch01 (1.1-1.4)
- **Ransomware, decryptors, preserving encrypted files** → ch06 (6.4)
- **SSD sequential vs random, caches, HDD capacity, RAID** → ch04 (4.1-4.2)
- **Temperatures, throttling, paste and pads** → ch04 (4.3), ch03 (3.5)
- **Used parts, payment protection, stress tests** → ch05 (5.4), ch04 (4.6)
- **VRAM, bus, bandwidth, spill-over** → ch03 (3.1)
- **Processor-level flaws, trusted modules, drivers** → ch06 (6.7)

## Related Skills

- `computer-science-fundamentals`: the theory under caches, memory, concurrency, networks and cryptography.
- `ai-ml-concepts`: model memory, quantisation and the KV cache; `ai-futures-and-intelligence`: compute and memory economics of AI.
- `economics-finance`: how supply, demand and market structure work in general.
- `coding-with-agents`: safety and backups when agents run unattended.

## Scope & Limits

Distilled from many hours of practitioner commentary on PC components, buying, market swings and home security, from roughly 2017 to 2026. The commentators were hobbyists who measured with their own instruments, not laboratories; their simplifications are flagged, and conflicting positions are given with a decision rule. Not covered: specific products, prices or rankings, overclocking records, laptop repair procedures, legal or tax advice, and security work against targeted attacks. Treat the checklists as a method for verifying, not a substitute for current reviews with instruments.
