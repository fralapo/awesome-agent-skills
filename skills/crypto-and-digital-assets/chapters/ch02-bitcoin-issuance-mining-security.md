# Chapter 02: Bitcoin Issuance, Halving, Mining and Security

> Educational concepts, not investment, tax or legal advice. Figures are snapshots.

## Core Idea
In this model, the main proof-of-work design is a **machine that turns electricity into an unforgeable record of order**, and pays the people who run it with newly issued units and fees. Its monetary policy is fixed in advance. This chapter explains how mining works, how issuance is scheduled, what security means quantitatively, and what the supply schedule does and does not imply (price drivers are in ch08).

## 2.1 Mining step by step
- **Thesis**: mining is repeated guessing whose only cheap-to-check output is a valid block.
- **Mechanism**: a miner bundles pending transactions plus a reward transaction, adds a number used once (the **nonce**), hashes the header and checks whether the binary result begins with enough zeros. If not, change the nonce and retry. Each additional required zero roughly **doubles** expected work. The block commits to the previous block's hash, so a rival block with a double spend cannot be prepared in advance, and editing history forces redoing all later work.
- **Trade-off**: verification is trivial for everyone, production is expensive for one: that asymmetry is the security.
- **Does not hold when**: hardware or energy becomes so concentrated that a few operators decide ordering.

## 2.2 Difficulty adjustment
- **Thesis**: block time stays near a target regardless of total hash power.
- **Mechanism**: difficulty retargets about every two weeks so that blocks arrive on average every 10 minutes. If miners join, difficulty rises; if they leave, it falls. This keeps issuance on schedule and makes security a function of the cost of the hash power, not of its quantity at any one time.
- **Trade-off**: the schedule is stable, but a sudden exit of miners leaves slow blocks until the next adjustment.
- **Does not hold when**: a fork changes the rule, as happened when rival chains split off with different parameters.

## 2.3 Longest chain, confirmations and reversal
- **Thesis**: reversing a confirmed payment requires out-working the honest chain.
- **Mechanism**: if two miners find blocks almost together, nodes follow the longest chain and the shorter branch is abandoned (its transactions return to the mempool). One or two confirmations are already hard to reverse; six is the traditional benchmark and more is used for very large amounts. Reversing requires controlling more than half of global hash power over the relevant period.
- **Trade-off**: waiting for more confirmations buys certainty but delays a payment.
- **Does not hold when**: a payee accepts zero-confirmation transactions, which can be replaced (ch01, 1.7), or a chain has very little hash power.

## 2.4 Supply schedule and halving
- **Thesis**: the reward halves every 210,000 blocks, roughly every four years (slightly less when blocks arrive faster than 10 minutes).
- **Mechanism**: rewards of 50, 25, 12.5, 6.25, 3.125... form a geometric series that converges just below **21 million** units (rounding at the smallest unit, the satoshi, lowers the total slightly). Supply inflation falls with each halving (see the table: about 1.8% a year after the third halving and about 0.85% after the fourth, roughly halving again in each later era) but never turns negative: the asset is **disinflationary, not deflationary**. Rewards vanish around the year 2140, after which miners live on fees.
- **Trade-off**: predictable issuance versus no discretionary response to shocks.
- **Does not hold when**: consensus rules change. This is not expected, but it is possible through a coordinated fork (position: supporters regard the schedule as socially locked; critics point out that rules are only as fixed as participants' agreement).

| Era | Reward per block | Approx. annual new supply as a share of existing supply |
|---|---|---|
| Early | 50 | very high, falling |
| Third halving | 6.25 | about 1.8% (Bitcoin, snapshot 2025) |
| Fourth halving | 3.125 | about 0.8-0.9% (Bitcoin, snapshot 2025) |

## 2.5 The fee question after rewards fade
- **Thesis**: long-run security must be paid for by fees (position, widely discussed, unresolved).
- **Mechanism**: fee revenue is the price of block space. If space is capped, fees rise with demand. If rewards shrink while fees stay low, the total payment to miners falls and so does the cost of attacking the chain.
- **Trade-off**: low fees help users now; high fees fund security later.
- **Does not hold when**: second-layer networks (ch04) move most small payments off-chain and base-layer fees come mainly from large settlement transactions.

## 2.6 Energy and concentration
- **Thesis**: the energy cost is not a side effect, it is the security budget.
- **Mechanism**: an attacker must outspend honest miners in hardware and electricity. Mining concentrates where power is cheap, and miners join **pools** that smooth income, which concentrates block-template decisions in a few pool operators even if hash power is spread among many members.
- **Trade-off (position)**: critics point to the energy use and the industrial concentration; supporters argue the energy secures a settlement system and uses stranded or surplus power. Neither claim is settled by the protocol itself.
- **Does not hold when**: another consensus design is chosen (ch07, staking), where the cost is locked capital rather than electricity.

## 2.7 What a halving does to selling pressure
A halving reduces new issuance. A worked check of the size: from 6.25 to 3.125 units per block, at 6 blocks per hour, means 3.125 x 6 x 24 = **450 units a day** less newly issued. Against a daily traded volume that has been of the order of a million units across venues (snapshot), that is a few hundredths of a percent. In this model the direct supply effect is therefore small; anything beyond it would have to come from expectations (ch08, which also treats the opposing position).

## 2.8 Attacks and failure modes in plain terms
| Failure | Meaning | Mitigation |
|---|---|---|
| 51% attack | Majority hash power rewrites recent history | Cost of renting or buying hash power; more confirmations |
| Selfish mining | Withholding blocks to gain advantage | Needs substantial hash share |
| Pool concentration | Few operators choose block contents | Members can switch pools |
| Software bug | Consensus rule error splits the chain | Conservative upgrades, many independent clients |
| Regulatory or energy-policy shock | Mining relocates | Geographic spread |

## Common mistakes
- Saying the supply is "capped at 21 million" and forgetting that lost keys remove units from practical circulation.
- Calling the asset deflationary.
- Treating the halving date as a causal event rather than a scheduled one.

## Links
- ch01 ledger basics; ch04 second-layer payments; ch07 staking alternatives; ch08 cycles and small samples.
