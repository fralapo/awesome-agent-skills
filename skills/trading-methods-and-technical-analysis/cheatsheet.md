# Trading Methods and Technical Analysis: Cheatsheet

Educational concepts, not advice, signals or forecasts. Parameters are conventions; figures are worked examples or dated snapshots; re-check. "Position" = contested view. Chapter references in brackets.

## Where to Start
| Question | First move |
|---|---|
| Is it going up? | Ask "on which timeframe?"; read higher timeframe first [ch01] |
| Is it a trend? | Higher highs and higher lows, or the reverse; otherwise a range [ch01] |
| Is this a real breakout? | Judge the close and the candle's size against normal range; watch the retest [ch01] |
| RSI is 80: will it fall? | No: a high reading describes a strong trend [ch02] |
| Is this divergence a signal? | Only with higher-timeframe agreement and a structural break [ch02] |
| Which pattern matters? | Few clear shapes at levels, confirmed on close [ch03] |
| Does seasonality say buy? | It is a bias; needs timing, a stop, and a check against chance [ch04] |
| What does the COT say? | Long-term bias with three days' delay; no timing [ch04] |
| Which strategy fits? | Identify the regime first: trend, range, expansion, relation [ch05] |
| How big should the position be? | Stop first, then size = risk / (stop x value per point) [ch06] |
| Is this track record credible? | Fixed rules, out-of-sample, costs, number of trades, seller's interest [ch08] |
| Is this company solid? | Ratios and scores as hints, sector-relative, not for banks [ch09] |
| How does this leveraged product die? | Barrier, reset, margin call or issuer default [ch10] |

## Figures to Keep in Mind (conventions and worked examples)
| Item | Value | Where |
|---|---|---|
| Common settings | SMA 50/200; RSI 14; MACD 12-26-9; ATR 14; Bollinger 20, 2 sd; SAR 0.02 | ch02 |
| Ichimoku settings | 9 / 26 / 52, cloud shifted 26 | ch03 |
| RSI regime filter (one method) | 40-100 up, 0-60 down, 40-60 range | ch02, ch05 |
| ADX meaningful (practitioner thresholds) | above about 20 (indices, currencies), 25 (shares) | ch02 |
| Break-even win rate at 1:1 / 1:2 / 1:3 | 50% / 33% / 25% | ch06 |
| ATR stop / target (one convention) | 2 x ATR / 6 x ATR | ch06 |
| Risk per trade (practice, inconsistent) | 1-2%, up to 3%; outliers 5-6% | ch06 |
| Ten losses in a row at 1% / 2% / 5% risk | about -10% / -18% / -40% | ch06 |
| Recovery after -20% / -33% / -50% | +25% / +50% / +100% | ch06 |
| Chance of 7+ of 10, 14+ of 20 positive years by luck | about 17%, about 6% | ch04 |
| Trades to show 55% vs 50% at ~2 standard errors | about 400 | ch08 |
| European retail leverage (snapshot) | 30:1 major pairs, 20:1 major indices | ch06 |
| Altman zones (original model, inconsistent across practitioners) | >2.99 / 1.81-2.99 / <1.81 | ch09 |
| Beneish zones (inconsistent across practitioners) | >-1.78 flag; -2.22 to -1.78 grey | ch09 |
| Piotroski "strong" | above 6 of 9 | ch09 |
| Fixed 7x, underlying +2% then -2% | underlying 99.96, product 98.04 | ch10 |
| Binary 81 win / 100 loss | break-even win rate about 55% | ch10 |

## Formulas
- Break-even win rate = 1 / (1 + R); expectancy = p x average win - (1 - p) x average loss - costs [ch06]
- Size = (account x risk %) / (stop distance x value per point) [ch06]
- Leverage = 100 / margin % [ch06, ch10]
- Recovery needed after drawdown d = 1 / (1 - d) - 1 [ch06]
- Two equal risks r with correlation ρ: combined = r x sqrt(2 + 2ρ) [ch06]
- Pivot P = (H + L + C) / 3; R1 = 2P - L; S1 = 2P - H [ch01]
- Stochastic = (close - low N) / (high N - low N) x 100 [ch02]
- Turbo long price = (underlying - strike) / (parity x FX); leverage ≈ 100 / distance-to-barrier % [ch10]
- Certificate sizing: notional = max loss / accepted move; capital = notional / leverage [ch10]
- Range binary yield = (10 - price) / price [ch10]
- Present value = amount / (1 + rate)^years [ch09]
- Shareholder yield = dividend yield + net buyback yield + net debt reduction [ch09]

## Red Flags (any of these: verify before relying on a method)
- A result from one account, one period or one month [ch08]
- No out-of-sample test, or thousands of parameter sets tried [ch08]
- High hit rate with no stop or with averaging down [ch06, ch08]
- "Each confirmation adds ten points" [ch08]
- Seasonal win rate with no count of windows scanned [ch04]
- Barrier chosen far away "to avoid being stopped" [ch10]
- Performance shown by the seller of the product or indicator [ch08]
