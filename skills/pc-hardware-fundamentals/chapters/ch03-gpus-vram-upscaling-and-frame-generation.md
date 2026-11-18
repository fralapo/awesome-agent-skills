# Chapter 3: Graphics Cards, Graphics Memory, Upscaling and Frame Generation

## Core Idea
A graphics card is thousands of simple units fed by a pool of fast memory. In this model most buying and diagnosis questions reduce to three: is the card compute-bound, bound by memory capacity, or bound by memory bandwidth, and which visual tricks (ray tracing, upscaling, frame generation) are in use, since they change what a frame-rate number means.

## 3.1 Graphics memory: capacity, bus width and bandwidth
- **Thesis**: capacity is the warehouse, bus width the door, and bandwidth the speed at which goods move; each limit fails differently.
- **Mechanism**: capacity decides whether the scene fits; bandwidth (bus width times memory speed) decides how quickly data reaches the cores. A narrow bus limits a card even when its capacity is large. A usage reading of 100% means the card is busy, not that its cores are computing: they may be waiting for memory. When capacity runs out the system spills into main memory over the slower bus; average frame rate may hold while 1% lows collapse, textures pop in, the game stutters or crashes. More memory does not cure a badly optimised game, but it removes a cliff.
- **Method**: check the graphics-memory use in the games and settings you actually run, add headroom, and recall that ray tracing, upscaling and frame generation raise use; three-dimensional modelling, rendering and local AI need more than gaming.
- **Trade-off**: capacity costs money; a modest card with too little memory ages badly.
- **Does not hold when**: you play older or well-optimised titles at modest settings.

## 3.2 Same name, different card
- **Thesis**: a product name does not fix the specification; compare cores, bus and memory.
- **Mechanism**: variants sharing a model name can differ in memory size and also in cores or bus width, so "the same card with more memory" is not guaranteed. Always read the specification sheet and independent benchmark of the exact variant. Faster memory chips with looser timings are not always faster in practice (hypothesis: higher frequency needs relaxed timings).
- **Trade-off**: reading takes minutes and prevents expensive mismatches.
- **Does not hold when**: the vendor publishes a single configuration.

## 3.3 Ray tracing, upscaling and frame generation: three different tricks
- **Thesis**: they solve different problems and trade quality, latency and compatibility differently.
- **Mechanism**: *Ray tracing* is an optics algorithm (follow light paths) that dedicated hardware can accelerate; at lower tiers it can cost around half the frame rate and is then paired with upscaling. *Spatial upscalers* enlarge one finished frame with a filter or algorithm: open, run on any card, quality depends on the starting resolution (better from a high base than a low one) and can add latency. *Temporal neural upscalers* use several frames, motion data and a trained network on dedicated hardware and can approach native quality. *Frame generation* inserts interpolated frames between real ones: displayed frame rate rises, but the game's responsiveness is still set by the real frames and interpolation adds latency (partly offset by latency-reduction modes); it works best when the base frame rate is already high, and multiplying to higher factors produces ghosting and smearing. A frame rate with frame generation on is therefore not comparable with one without it.
- **Trade-off**: smoother picture against responsiveness and artefacts; each feature may be vendor-specific or require developer support, not a driver switch.
- **Does not hold when**: the feature is turned off or the content is not interactive (film playback).

## 3.4 Several cards and "the next card for the future"
- **Thesis**: paired cards rarely scale and "buying for later" is rarely rational.
- **Mechanism**: work cannot be split evenly across two cards, so doubling the cards does not double performance and needs software support; one stronger card is the better route. The price of a card for tomorrow's games is better paid when those games exist (chapter 5).
- **Trade-off**: none worth the complexity.
- **Does not hold when**: a compute job is designed for multiple devices and splits cleanly.

## 3.5 Memory temperature and board cooling
- **Thesis**: memory and power stages need cooling like the main chip.
- **Mechanism**: a multi-level signalling scheme used by one fast memory type runs hot (temperatures near the top of their rating were reported on several models, with pads and heatsinks criticised); other designs run cooler. Poor thermal pads or low contact pressure make memory the hottest component long before the core. Ageing pads and dried paste are the usual cause of rising temperatures years later (chapter 4).
- **Trade-off**: heavier cooling adds cost and noise.
- **Does not hold when**: the card is lightly loaded.

## 3.6 Direct memory access for the processor
- **Thesis**: letting the processor address all graphics memory instead of a small window can speed some workloads.
- **Mechanism**: a feature (resizable base address register, branded variants) removes the small-window limit; reported gains are a few percent in some games and zero in others, and the idea existed earlier in other fields. Enable it in firmware if supported.
- **Trade-off**: small gain, no cost.
- **Does not hold when**: firmware or driver support is missing.

## 3.7 Compute, creative work and local AI
- **Thesis**: gaming speed and compute speed are different; AI workloads are limited by memory capacity first.
- **Mechanism**: a top-tier card can double the previous one in compute while adding less in games. A language model's weights need roughly bytes-per-parameter times the number of parameters: at 4-bit precision (half a byte per parameter) a 14-billion-parameter model needs about 7 GB for weights, plus memory for the context cache and overhead, so a mid-capacity card runs it comfortably; higher precision multiplies the need. Quantisation trades some quality for space (`ai-ml-concepts` ch7.12 for the cache). Speed in tokens per second depends on memory bandwidth more than on core count. A neural processing unit is a small low-power accelerator for low-precision work, not a graphics card; "TOPS" figures are not comparable across vendors because they may add several chips, and for a local model storage and memory matter more than the TOPS label. Data sent into a hosted model cannot be recalled.
- **Trade-off**: bigger models need more memory and more power; small models are weaker but cheap and private.
- **Does not hold when**: the model is run through a hosted service.

## 3.8 Software matters as much as silicon
- **Thesis**: frame rate varies with the program and the driver, not only the hardware.
- **Mechanism**: the same card at the same resolution can differ by tens of percent between two games; drivers can add double-digit gains in a specific title; a driver that offloads more work to the processor changes the processor-bound result. Causes of poor optimisation are usually unverifiable from outside because source code is closed (hypothesis). A compatibility layer that translates one graphics interface into another can make a vendor's cards more useful at the cost of completeness.
- **Trade-off**: waiting for a driver or patch is free; replacing hardware is not.
- **Does not hold when**: the title is mature and patched.

## Common Mistakes
- Equating 100% usage with 100% of the cores working.
- Comparing frame rates with and without frame generation.
- Buying two cards or a larger card "for the future".
- Assuming the same name means the same card.

## Checklist
- [ ] Graphics memory use measured in your games, with headroom?
- [ ] Exact variant specification read?
- [ ] Which of ray tracing, upscaling and frame generation are on in any comparison?
- [ ] Local AI sized by weights plus cache?

## Connects To
ch02 (which component limits), ch04 (thermals), ch05 (reading benchmarks); `ai-ml-concepts` ch7 (KV cache), `ai-futures-and-intelligence` ch6 (AI compute economics).
