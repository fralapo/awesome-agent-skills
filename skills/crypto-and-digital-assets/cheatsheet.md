# Crypto-Assets and Digital Assets: Cheatsheet

Educational concepts, not advice or forecasts. Figures are dated snapshots or worked examples; re-check. "Position" = contested view. Chapter references in brackets.

## Where to Start
| Question | First move |
|---|---|
| Who owns a coin? | The holder of the key that signs; custodial = a claim on a company [ch01, ch03] |
| Why can't a coin be spent twice? | Public ledger plus a cost-based ordering rule [ch01, ch02] |
| What is my balance? | UTXO: sum of unspent outputs; account chain: number per address [ch01] |
| Is it anonymous? | No, pseudonymous: clustering and change heuristics [ch01] |
| How secure is mining? | Cost of out-working honest hash power [ch02] |
| Do halvings move price? | Direct supply effect small; cycle claims rest on three events [ch02, ch08] |
| Where should keys live? | Compare failure modes: error vs counterparty [ch03] |
| What if a hop is offline? | The channel payment reverts [ch04] |
| Why did a platform fail? | Unsegregated assets, related-party exposure, unexplained yield [ch05] |
| Note vs fund vs asset? | Issuer risk vs custody vs key risk [ch06] |
| Where does the yield come from? | Fees, incentives or hidden risk [ch07] |
| Does this correlation prove anything? | Control for time; non-overlapping windows; few events [ch08] |
| Does high funding mean the move is over? | No: funding describes crowding, lags and differs by venue [ch11] |
| What does open interest show? | Commitment; rising with price means new positions; keep coin and currency units apart [ch11] |
| Is this a taxable event? | Disposal or income receipt, not holding or own-wallet transfers [ch09] |
| Is this a scam? | Unsolicited, urgent, irreversible, escalating fees [ch10] |

## Figures to Keep in Mind (dated, context-bound)
| Statistic | Value | Where |
|---|---|---|
| Supply cap | converges just below 21 million units | ch02 |
| Halving interval | every 210,000 blocks, about four years | ch02 |
| Block interval target | about 10 minutes; retarget about every two weeks | ch02 |
| Confirmation benchmark | six, traditional | ch02 |
| Daily issuance cut at the halving from 6.25 to 3.125 | about 450 units a day | ch02 |
| Seed phrase checksum (12 words, last word) | about 1 in 16 candidates valid | ch03 |
| Channel fee example | 14 satoshi, about 0.0038 vs about 2.17 on-chain | ch04 |
| Yield platform recovery (one reported case, uncertain) | roughly a quarter of liabilities | ch05 |
| Annual wrapper cost | up to about 2% | ch06 |
| APR 52% compounded monthly / daily | about 67% / 69% APY | ch07 |
| Typical liquidation threshold / discount | 75-85% / 5-10% | ch07 |
| Supply-price correlation / after controlling for time | +0.65 / small and negative | ch08 |
| Maximum drawdown, one-year windows of a volatile asset | average about 23%; 1 in 10 about 54%; worst about -80% | ch08 |
| Dip-buying backtest (equities) | buy-and-hold 13.9% vs wait-for-30%-drop 12.8% | ch08 |
| Value levy (Italy, snapshot 2023-2025) | 0.2% x final value x days/365 | ch09 |
| Substitute tax rate (Italy, snapshot 2025) | 26% through 2025; 33% scheduled from 2026 | ch09 |
| Step-up break-even (Italy, snapshot 2025) | price/cost basis > 3.25 | ch09 |
| Pyramid arithmetic | 5 invitees per member, level 10 = 9,765,625 people | ch10 |
| Recovery after a 70% fall | about +233% | ch11 |

## Formulas
- Liquidation price = loan / (collateral quantity x threshold) [ch07]
- Fee in local currency = satoshi / 100,000,000 x price per unit [ch04]
- Break-even annual-fee product: fee / cost rate. Over 10 years, 2% a year removes about 18% [ch06]
- Value levy = 0.2% x final value x days/365 [ch09]
- Leveraged daily-reset fund: +x then -x gives factor 1 - x^2; at leverage 2, 1 - 4x^2 [ch08]
- Annualised basis = (futures - spot) / spot x (365 / days to expiry) [ch11]

## Red Flags (any of these: verify before acting)
- Yield above the risk-free rate with no explanation [ch05, ch07]
- Withdrawal pauses, "fees to release" [ch05, ch10]
- Someone asks for your phrase [ch03, ch10]
- Urgency plus a private deal [ch10]
- Unlimited token approval request [ch07, ch10]
- "Proof of reserves" without liabilities [ch05]
- A liquidation map or a cycle date presented as an observed level or as certain [ch11]
