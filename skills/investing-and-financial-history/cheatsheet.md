# Investing and Financial History: Cheatsheet

Educational concepts and history, not advice or forecasts. Figures are dated snapshots; re-test. "Position" = contested view. Chapter references in brackets.

## Where to Start
| Question | First move |
|---|---|
| What is risk? | Separate volatility, loss probability and goal failure [ch01] |
| Which risk is paid? | Market risk yes; single-company risk no [ch01, ch04] |
| Can anyone beat the market? | Arithmetic of active management; persistence evidence [ch02] |
| Is value / a factor still working? | Reasons, persistence, cost, dated data, rival view [ch03] |
| How diversified am I? | Check correlations, shared factors, country, own business [ch04] |
| Is this stock cheap? | State what the price assumes; DCF with conservative inputs, multiple vs history and peers [ch05] |
| What does the yield curve say? | Expectations plus premium; imperfect timing [ch06] |
| What is a covered call really? | Capped upside sold for income [ch07] |
| Why do investors do that? | Name the bias, add a rule [ch08] |
| Why did the crash happen? | Ingredients, trigger, proposed causes, rival account [ch09] |
| Is this a Ponzi or fraud? | Verify independently, run the checklist [ch10] |
| Was the decision good? | Judge at decision time: risk, reason, expected outcome [ch11] |
| How do I compare two returns? | Same horizon, net of costs and tax, IRR on dated flows, annualised correctly [ch12] |
| Is this backtest reliable? | Count independent observations; survivorship; costs; effect size; how many rules tried [ch13] |
| How is a bond priced and what hurts it? | Present value at required yield; duration for rate risk; credit and call for the rest [ch06] |
| What is a leveraged or structured product really? | Daily reset and wipe-out threshold; barrier cliff and issuer risk [ch07] |
| How long will a withdrawal plan last? | Real net return, horizon-dependent rate, sequence risk, left tail [ch14] |
| Is a high yield or promised return real? | Name the risk paid; trace the counterparty; check for new-money dependence [ch06, ch10] |

## Figures to Keep in Mind (dated, context-bound)
| Statistic | Value | Where |
|---|---|---|
| Global long-run equity premium over safe assets | about 4.2% a year (since 1900) | ch01 |
| 10-year windows with stocks behind bills | about 6% (developed ex-US), 12% (Canada), 15% (US) | ch01 |
| Index fund fee vs active fund fee (Canada, about 2024) | about 0.19% vs 0.85% | ch02 |
| US funds beaten by an index before fees (1991-2020) | about 55% | ch02 |
| US funds beating an index after fees (1991-2020) | about 30% | ch02 |
| Lifetime US stocks beating bills / the market (1926-2016) | about 43% / 31% | ch03 |
| Large US stocks with a -70% never-recovered loss (1980-2020) | about 44% | ch03 |
| US value premium 1963-91 / 1991-2019 | about 4.9% / 1.2% a year (not significant) | ch03 |
| Chance of a negative value premium (simulated) | about 23% over 23 years, 9% over 10 | ch03 |
| Variance explained by factor models | one-factor about 60-80%, three-factor about 90%, five-factor about 90-95% | ch03 |
| Concentration threshold in a study | a single holding of about 10% | ch03, ch04 |
| 1987 one-day fall | about 22.6% | ch09 |
| Portfolio insurance share of sell volume on the day | about 19% (one estimate) | ch09 |
| House price rise 1998-2006 (US) | about 124% | ch09 |
| Recovery needed after a fall of 20% / 50% | +25% / +100% | ch12 |
| Non-overlapping five-year periods in 4,787 overlapping windows (25 years of data) | about 5 | ch13 |
| Cost of exit rules in one 25-year sample (5-year windows) | about 8-12 points of mean return | ch13 |
| Wipe-out day for a daily-reset product x2 / x3 / x5 | fall of 50% / 33% / 20% | ch07 |
| Duration 6, yield +1 point | price about -5.8% | ch06 |
| Initial withdrawal rate calibrated to 30 years / to 50 years (this model) | about 4% / about 2% or somewhat more | ch14 |

## Option Greeks
| Greek | Measures | Note |
|---|---|---|
| Delta | price change per 1 move in the underlying | 0 to 1 calls, -1 to 0 puts |
| Gamma | change of delta per 1 move | peaks near the strike |
| Theta | time decay | hurts the buyer, helps the writer |
| Vega | sensitivity to expected volatility (general knowledge) | |
| Rho | sensitivity to interest rates (general knowledge) | |

## Formulas
| Quantity | Formula | Where |
|---|---|---|
| Annualised return | `(1+R)^(1/years) - 1` | ch12 |
| Log return | `ln(final/initial)`; simple = `e^r - 1` | ch12 |
| Recovery after loss p | `1/(1-p) - 1` | ch12 |
| Modified duration | Macaulay duration / (1 + yield) | ch06 |
| Accrued interest | coupon x days since last payment / days in period | ch06 |
| Rights value | ex-rights price - subscription price | ch12 |
| Portfolio variance (2 assets) | `w1^2 V1 + w2^2 V2 + 2 w1 w2 Cov` | ch12 |
| Required capital | spending / withdrawal rate | ch14 |

## Fraud Quick Signs
Smooth high returns; opaque revenue; non-standard adjusted metrics; critics attacked; authority instead of evidence; urgency and secrecy; one person controls trading and settlement; dependence on new money; a fee to release funds; a famous face in an advertisement; a token that pays referrals.
