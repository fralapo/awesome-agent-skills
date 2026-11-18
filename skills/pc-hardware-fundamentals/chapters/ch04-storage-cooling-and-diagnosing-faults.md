# Chapter 4: Storage, Cooling and Diagnosing Faults

## Core Idea
Storage trades speed, capacity and price; cooling trades noise, size and reliability. In this model parts slow themselves down before they damage themselves, so a hot reading is a prompt to look at airflow and contact, not to panic, and fault-finding should start from the most probable cause and from software tests before hardware work.

## 4.1 Memory versus storage, and what "fast" means
- **Thesis**: main memory and drives are different tiers; sequential speed is the number printed, random access is the one that feels fast.
- **Mechanism**: main memory answers in nanoseconds and loses its contents without power; flash drives answer in microseconds and keep data; a spinning disk answers in milliseconds. The machine needs working memory before it can load a storage driver, so the tiers cannot be swapped. A cheap solid-state drive can post good sequential speeds and much worse random performance (controller and flash quality), and a drive can slow once its fast cache is full. Labels such as "for gaming" or "for the operating system" are marketing; a newer interface generation mainly raises the sequential ceiling. A direct-storage interface moves decompression of game assets to the graphics card and shortens loading (reported around a third) without raising the frame rate.
- **Trade-off**: speed costs money per terabyte; for many uses a mid-range drive is indistinguishable.
- **Does not hold when**: the workload is heavy random writes or sustained large transfers (film editing, databases).

## 4.2 Hard disks, caches and RAID
- **Thesis**: spinning disks still win on capacity per price; tiering with a flash cache helps loading but not frame rate and adds risk.
- **Mechanism**: a flash cache in front of a disk speeds repeated reads and can lose data if it fails before write-back; overlapping-track (shingled) disks suit archives and can stall under random writes; a home network storage box on gigabit Ethernet delivers roughly 110-120 MB/s, the link's ceiling. RAID zero spreads data across drives and doubles the failure risk; redundancy (mirror, parity) keeps a service running after a drive dies, which is availability, not backup (chapter 6).
- **Trade-off**: cache and RAID add complexity and failure modes.
- **Does not hold when**: data can be recreated cheaply.

## 4.3 Temperature: throttling, limits and what is alarming
- **Thesis**: modern chips lower their clocks as they approach a limit; being near the limit under load is often by design.
- **Mechanism**: each chip has a published maximum temperature and a throttling behaviour; some processor families are designed to run close to their limit under load because they boost until they hit it. Red flags are crashes, clocks dropping below what the chip should sustain, temperatures that are high at idle, and rising temperatures over months. Read the vendor's limits for the exact model. Before changing the case or cooler, refresh the thermal paste and check mounting pressure, because the contact is the most common cause.
- **Trade-off**: lower temperatures mean less noise and slightly higher sustained clocks; chasing them past that gains little.
- **Does not hold when**: the machine is in a hot room or sealed enclosure; then ambient temperature is the first problem.

## 4.4 Airflow: intake, exhaust and the parts nobody watches
- **Thesis**: a case needs a path for cool air in and warm air out; components that sit outside the main stream overheat first.
- **Mechanism**: a rear and top exhaust with front intake is the typical pattern; with a closed front panel, intake from the rear and exhaust from the top works better. Power-delivery components around the processor socket are cooled by the case airflow; when they overheat they limit the power available to the processor. Assembly mistakes: a front radiator that blocks the graphics card, a card mounted vertically against glass with no intake gap, a cooler too tall for the case, no check of clearances. Fans are judged by airflow, static pressure (needed through radiators and filters), noise, bearing type and control method; direction and grilles change the real flow.
- **Trade-off**: positive pressure keeps dust out and needs filters; maximum airflow is loud.
- **Does not hold when**: the case is open on a bench.

## 4.5 Air versus liquid
- **Thesis**: a cheap all-in-one liquid cooler is not better than an air cooler at the same price; a custom loop is the real step up.
- **Mechanism**: an air cooler has fewer points of failure and holds up under long sustained loads; a liquid unit absorbs short spikes well and moves heat to a radiator that can sit where there is room. Failure modes of sealed loops: pump wear (a typical life of a few years), permeation, and corrosion when aluminium and copper meet in a conductive liquid (galvanic corrosion creates deposits that clog and strain the pump). Many brands share a few manufacturers. A liquid unit whose fans stop does not stay stable. A modest air cooler is enough for most processors in normal use, and a large radiator can hold a hot processor within its limits.
- **Trade-off**: quietness and looks against lifetime and maintenance.
- **Does not hold when**: space or memory-clearance constraints force one choice.

## 4.6 Diagnosing a fault
- **Thesis**: start from the symptom, study the effect, test the most probable causes first, do software tests before hardware work.
- **Mechanism**: fans at full speed with no picture often point to power or the power-delivery stage; artefacts on screen suggest memory or heat, and lowering clocks or reflashing firmware (after backup) can confirm; software tests and driver cleanups precede maintenance; routine cleaning and new paste every year or two prevents many faults; reballing or heating a board with a heat gun needs real skill and an oven is a bad idea. A used card with a past of continuous load is judged like any used part: check fans, paste and pads, and run a sustained stress test of tens of minutes. Hypothesis: a card kept at a steady temperature suffers less solder fatigue than one that repeatedly heats and cools, because fatigue comes from thermal cycling.
- **Trade-off**: diagnosing takes patience; swapping parts blindly costs money.
- **Does not hold when**: a part is under warranty (then return it, do not open it).

## 4.7 Screens and cables
- **Thesis**: the screen sets what resolution you can use and the cable sets what the port delivers.
- **Mechanism**: pixel density depends on size and resolution, so a sensible panel size grows with resolution (a rule of thumb: a smaller panel for full HD, larger for higher resolutions, adjusted by viewing distance). Response-time figures are not comparable between vendors; very high refresh rates only help competitive play where the system can sustain them. A television and a monitor differ in latency and processing. A USB-C connector can carry only the slowest protocol; speed and power depend on the cable and the port.
- **Trade-off**: higher resolution demands a stronger card.
- **Does not hold when**: use is mostly text or film.

## Common Mistakes
- Panicking at a hot reading without checking limits.
- Replacing the case before refreshing the paste.
- Treating a RAID array as a backup.
- Buying a drive for its label instead of its random performance.

## Checklist
- [ ] Limits read for this exact chip?
- [ ] Airflow path in and out, clearances checked?
- [ ] Paste and pads refreshed on a schedule?
- [ ] Faults tested in software first?

## Connects To
ch01 (power-delivery heat), ch03 (memory temperature), ch06 (backup); `computer-science-fundamentals` ch4 (memory hierarchy), ch3 (storage structures).
