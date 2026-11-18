# PC Hardware Fundamentals: Cheatsheet

Figures are rules of thumb, standards or made-up illustrations; re-check against current specifications. "Position" = judgment, not fact. Chapter references in brackets.

## Where to Start
| Situation | First move |
|---|---|
| Frame rate lower than expected | Find the limit: processor, graphics card, memory, or settings; test at your resolution [ch02.6] |
| Stutter with good average frame rate | Check 1% lows and graphics-memory use; spill-over to main memory [ch03.1] |
| High temperatures | Read the chip's limits; refresh paste and check mounting before changing the case [ch04.3] |
| Random crashes after tuning | Back out the undervolt or memory profile; long stress test [ch02.5] |
| Fans at full speed, no picture | Power or power-delivery stage first; then software and memory [ch04.6] |
| Choosing a power supply | Measured review of the exact model; 12 V capacity with margin [ch01] |
| Which card or processor to buy | Use, resolution, budget; cost per performance inside the tier [ch05.3] |
| A chart looks too good | Setup, settings, upscaling or frame generation, lows, noise band [ch05.2] |
| Offer far below market | Assume scam or counterfeit until checked [ch06.1] |
| Unexpected "account" message | Do not click; contact the body through your own channel [ch06.3] |
| Files encrypted | Disconnect, keep the encrypted files, restore from offline copy [ch06.4] |

## Power (ch01)
| Item | Rule |
|---|---|
| Rating | A ceiling; judge by measured 12 V behaviour |
| Efficiency | Output over input: 300 W at 80% draws 375 W; at 90% about 333 W; says nothing about ripple |
| Rail tolerance | About 5%: 12 V between roughly 11.4 and 12.6 V; ripple limits commonly cited 120 mV on 12 V and 50 mV on small rails |
| Sizing | Sum of component peaks plus margin; allow for brief spikes of modern graphics cards |
| Connectors | Seat fully, gentle bend, native cable over adapter |
| Yearly cost | watts difference x hours per day x 365 / 1000 x all-in price per kWh |

## Processor and Memory (ch02)
| Item | Rule |
|---|---|
| IPC x clock x cores | All three; cores help only threaded software |
| Process node name | Partly marketing; compare density and results |
| Cache | Hit costs cycles, miss to memory costs hundreds |
| Memory | Two matched modules; platform sweet spot; enable profile; test |
| Power | Peak is not average; limits and undervolts cut heat, need long stress tests |
| Bottleneck | Low resolution or high frame rate: processor; high resolution: graphics card |

## Graphics (ch03)
| Item | Rule |
|---|---|
| VRAM | Capacity (fits?), bus and bandwidth (how fast?); 100% usage is not 100% compute |
| Spatial upscaler | One frame, any card, quality depends on base resolution |
| Temporal neural upscaler | Several frames plus network, dedicated hardware |
| Frame generation | Interpolated frames; displayed rate up, responsiveness set by real frames; adds latency |
| Two cards | Do not scale evenly; one stronger card is better |
| Local model memory | Weights about parameters x bytes per parameter (4-bit = 0.5 byte; 14 billion = about 7 GB) plus cache and overhead |

## Storage, Cooling, Faults (ch04)
| Item | Rule |
|---|---|
| Drives | Random performance matters; cache fills; labels are marketing |
| RAID | Availability, not backup |
| Throttling | Design feature; alarms are crashes, falling clocks, high idle |
| Airflow | In and out; check radiator and card clearances |
| Air vs liquid | Entry liquid not better than air at same price; watch pump and corrosion |
| Diagnosis | Symptom, most probable cause, software before hardware, backup before reflashing |

## Benchmarks and Buying (ch05)
| Item | Rule |
|---|---|
| Numbers | Averages hide stutter; read lows and frame times; run several times |
| Noise band | One to three percent between runs is not evidence |
| Tweaks | Most operating-system "boosters" vanish under measurement |
| Timing | Wait when stock is plentiful and a new generation is near; buy together when supply is tight |
| Used | Written "working" description, payment protection, stress test |
| Price moves | Demand spike or supply shock; capacity goes to the highest-margin segment; forecasts are hypotheses |

## Security and Backup (ch06)
| Item | Rule |
|---|---|
| Counterfeit card | Hardware-information tool, board versus sticker, memory chips versus capacity |
| Cheap mini PC | Wipe, reinstall clean, isolate until trusted |
| Phishing | Generic greeting, urgency, odd sender domain; contact via your own channel |
| Ransomware | Entry via weak or reused password, attachments, exposed services; keep encrypted files |
| Isolation | Default credentials changed; untrusted devices on a separate segment |
| Backup | 3 copies, 2 media, 1 off site; one offline; encrypt remotely; test restore |

## Do Not
Buy by wattage or badge alone · compare charts with different settings · treat RAID as backup · pay a ransom before preserving files · buy "for the future" · believe a gain smaller than the noise.
