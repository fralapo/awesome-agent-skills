# Chapter 13: Backtesting and Historical Evidence: How to Read a Study

> Educational concepts, not investment, tax or legal advice.

## Core Idea
In this model, a backtest is a **story told by a short, overlapping, survivor-filtered sample**. It shows what would have happened in one history, not what is likely in the next. The honest questions are: how many independent observations are there, what was left out, how big is the effect against costs, and how many rules were tried before this one was shown. Track-record reading in general is in ch03 (3.6); decisions about forecasts are in ch11 (11.6).

## 13.1 Rolling windows and why they overlap
- **Thesis**: a price chart is one case; the investor's experience is the distribution over all entry dates.
- **Mechanism**: start a hypothetical investment every day or month, hold `K` years, annualise, and study mean, median, deviation, worst percentile and share of positive windows. A "return from entry date" line is not the market path: when it falls, later entrants earn less than earlier ones, not necessarily a loss. Shifting entry by a month can change a total from +130% to +60%; peaks before crises give low outcomes, troughs high ones. Successive windows overlap, so they are far from independent samples: 4,787 five-year windows from a 25-year dataset contain only about five non-overlapping five-year periods.
- **Mechanism, reading**: total variance splits into between-market and within-market (across time) parts; when the within part dominates, picking the "best" market matters less than expected. Dispersion shrinks as `K` grows, faster for heterogeneous baskets.
- **Does not hold when**: the history is short or one regime; "worst historical case" is not "worst possible case".

## 13.2 Data pitfalls
- **Survivorship**: using today's index members drops failed firms and inflates history; removing failed banks flatters every candidate equally and so fixes nothing. Sampling by market cap across a wider universe mitigates it.
- **Price versus total return**: price indices omit dividends worth roughly 2 to 2.5 points a year for large-cap equity (dated, context-bound); total return reinvests dividends gross, net total return after withholding. An equal-weight index built by hand must average **returns**, not prices, or winners drift in weight.
- **Currency**: an index in another currency embeds exchange-rate risk; five-year windows of the same index can be positive in one currency and negative in another. A country index only approximates currency exposure, since small markets host exporters earning in dollars or euros. A fund's quotation currency does not remove exposure (ch04, 4.11).
- **Back-filled series**: recently listed assets are often reconstructed from index data, which biases results. Flat price segments from non-trading days are not stability.
- **Quality checks**: plot every series; look for spikes, gaps, flats; inspect anomalous cases, which expose data or instruction errors; start from a theory, because with many variables and many points almost anything is significant and collinearity yields nonsensical coefficients.

## 13.3 Small-sample markets and rare events
- **Thesis**: a handful of crises or inversions cannot support a statistical claim.
- **Mechanism**: signals and events that each recur every 5 to 7 years will line up eventually without causation; a signal with as many false positives as true ones has zero predictive value. The yield-curve inversion example in this model: counting gives crises without prior inversion and inversions without a crisis, roughly 50-50; the correlation of the slope with the next 12-month mean log return was about 0.14; after an inversion the mean monthly log return was still positive (about 0.13% against 0.70% after a positive slope), so shorting after inversion lost money, and a long/short rule gave about +325% against about +365% for buy-and-hold (sum of log returns, one dataset; varying the delay never beat holding). A recurring-cycle claim in a young asset is similar: with 3-5 events, a "boom after each halving" pattern is what chance produces when two periodic series are placed side by side (see `crypto-and-digital-assets`).
- **Does not hold when**: a mechanism exists and has been tested out of sample in many markets.

## 13.4 Tests: what they can and cannot say
- **Thesis**: a significant result can be irrelevant, and a non-significant one is not proof of equality.
- **Mechanism**: a **paired t-test** on differences needs enough independent pairs and approximate normality; a p-value above 5% says only that the data cannot show a difference. A **sign test** counts wins against a binomial with `p = 0.5` and needs few assumptions (3,230 wins in 6,534 trials has a cumulative probability of 18.3%, not significant; 54 of 90 has 3.6%, significant). A rank-based test compares medians without normality. A **z-test** on mean return per trade needs a reasonably large sample. At a 5% threshold about 1 in 20 skill-less strategies pass; at 1%, 1 in 100; testing many rules and reporting the best multiplies false positives. Hindsight bias makes past charts look predictable and memory keeps the hits.
- **Mechanism, overlap**: 23-day returns computed daily multiply the apparent sample by about 23 and falsely shrink p-values.
- **Mechanism, hit rate versus expectancy**: many small wins and a few large losses give a high hit rate and a negative mean; judge by average return per trade, not by share of correct calls. Because equities and bonds drift up by construction, most strategies show positive average returns, which proves nothing; compare with the always-invested alternative.
- **Does not hold when**: samples are selected after the fact or test assumptions fail.

## 13.5 Significance versus effect size
- **Thesis**: always ask "by how much", then compare the effect with costs.
- **Mechanism**: with very large samples a correlation of 0.003 can reach p near 10^-14 while explaining nothing; a correlation of 0.29 neither means "29% explained" nor causation, since a common factor may drive both. Mean matters for someone who lives many periods; median for someone who draws one period.
- **Does not hold when**: the effect is large and persistent in many markets.

## 13.6 Fitted rules and overfitting
- **Thesis**: a complex rule that is perfect in the past usually fails out of sample.
- **Mechanism**: a CAPE-based exit rule (leave equities when excess yield falls below a level) fired about once, in the late 1990s, and missed 2008 unless its threshold was loosened. Buying last year's worst performer from a handful of annual observations collapsed to no edge when the reference month shifted. "Hold the best of the last five years" did not beat an equal-weight basket on equities. Mean reversion after a bad year occurred in fewer than half of cases, and in about half of those the rebound did not recover the loss; the rebound needed after a return `x` is `1/(1+x) - 1`. Rules that buy more after a fall (ladders, value averaging) lower dispersion and the mean together (ch04, 4.9).
- **Trade-off**: out-of-sample tests, many markets and a stated reason reduce the risk but cannot remove it.
- **Does not hold when**: the rule has a mechanism, is simple and was fixed before testing.

## 13.7 Market timing and the cost of being out
- **Thesis**: escaping each crisis needs recognising both its start and its end, and neither is knowable in advance.
- **Mechanism**: simulated exit rules (leave 10% under a 30-day high and re-enter after a 10% rebound; leave when 30-day volatility doubles) cost, over rolling 5-year windows with taxes, roughly 8 to 12 points of mean return and about 20 points of median (about 3.7% a year) in one 25-year sample, against an expected 7-8% a year. Volatility signals arrive late (they need a month of data) and stay high in turbulent rallies. Large drops occur at known frequencies: counting days with a fall below a level and multiplying by about 262 trading days gives events per year; in one dataset a one-day global fall of 6% occurred in about 0.08% of days (about one year in five) and an emerging-market fall of 7.3% about once in thirteen years. Worst 4-5 day drawdowns matter because other time zones react a day later. That a handful of days produce most of the return, so that being out for them is costly, is general knowledge about skewed daily returns; the size depends on the market and period and should be checked, not quoted.
- **Does not hold when**: the downturn is a regime break; the market that sets the pace may show a record the others do not.

## 13.8 Reading a study: checklist
1. How many **independent** observations, not windows?
2. Was the universe fixed ex ante, with failed members included?
3. Price or total return; gross or net of costs and taxes; which currency?
4. Is the benchmark the closest style, or an easy one?
5. How many rules or parameters were tried? Is there a stated mechanism?
6. Effect size against costs; confidence interval, not only p-value.
7. Is it replicated in other markets and periods, and with shifted start dates?
8. What is the worst outcome in the data and what could be worse?
9. Is it a story told after the fact (cherry-picked winner, ch03, 3.6)?
10. Does the conclusion survive a pessimistic change to the main input?

## Common mistakes
- Treating overlapping windows as independent samples.
- Testing on today's index members.
- Reporting the one rule that worked out of many tried.
- Calling an insignificant result "no difference".

## Links
- ch02 efficiency, ch03 track records, ch04 entry rules, ch11 forecasts, ch12 maths, `scientific-thinking` for method.
