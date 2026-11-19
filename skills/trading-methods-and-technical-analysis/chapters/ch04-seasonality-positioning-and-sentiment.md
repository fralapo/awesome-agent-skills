# Chapter 04: Seasonality, Positioning (COT) and Sentiment

> Educational concepts, not investment or trading advice. No signals, no forecasts. Seasonal statistics and positioning readings are snapshots that change every year.

## Core Idea
In this model, seasonality, positioning data and crowd sentiment are **context filters for direction**, not timing tools and not forecasts. A seasonal profile is an average of past years, a positioning report is a delayed photograph of who holds what, and a sentiment reading is a head count of small traders. Each is useful only combined with structure (ch01) and with a stop, and each is exposed to the statistics of small, overlapping samples (4.5, ch08).

## 4.1 What a seasonal profile is
- **Thesis**: a seasonal curve is the average path of the same calendar window over N past years, like a city's average temperature.
- **Mechanism**: take the same window in each of the last N years (5, 7, 10, 15, 20), rescale each year to a common base, and average. A correct calculation aligns trading days rather than stepping back 365 calendar days. Per window, the useful statistics are: share of years positive (win rate), mean return long and short, and largest rise and fall in the window (to see whether a few extreme years drive the mean). A detrended version removes the long-run drift; the correlation between the current year's path and the profile measures how well the profile is tracking now. The one-year "profile" is not an average and is excluded when combining horizons.
- **Trade-off**: more years give a smoother curve with smaller average amplitude; fewer years track recent regimes but rest on tiny samples.
- **Does not hold when**: the asset's history is short or its structure changed (a young asset, a market whose composition changed).

## 4.2 Reading rules
- **Thesis**: the profile says tendency and timing, not price level or exact day.
- **Mechanism**: highs and lows can shift by days or weeks; a shift of a few days is tolerable, of a month it weakens the profile. The profile is redrawn with several horizons and only features present in all of them are trusted; if horizons diverge, the tendency is uncertain. A practice aligns the live chart with the curve by shifting it until highs and lows match; events that distort the previous year's scale are ignored. The period around the year-end holidays is a blind spot with little usable data.
- **Positions that disagree**: one view prefers recent horizons (1-5 years) because regimes change, and treats a profile that fits too well for nine months as suspect; another prefers horizons above three years; a third chooses whichever horizon correlates best with recent price. One threshold reported: use a profile only when its correlation with the current path exceeds about 70%. These thresholds are **inconsistent between practitioners** and none is backed by a published test.
- **Does not hold when**: a sudden event (a crash, a war, a policy shock) breaks the pattern; a stop is the only defence.

## 4.3 Seasonality is never a stand-alone signal
- **Thesis**: in this model, opening a position on seasonality alone is a wrong shortcut.
- **Mechanism**: seasonality gives the bias; a technical tool gives the timing (a trendline break, a divergence, a pullback to a level); fundamentals and central-bank stance can veto it. If seasonality points down but the trend and policy point up, the short is not attempted. Technical signals against the seasonal bias are ignored only if they look like pullbacks. A bearish divergence inside a seasonally weak window counts as two independent pieces of evidence, which overstates independence (8.4). Seasonality also says when to stay out. One view adds a personal rule: never trade against a twenty-year seasonal statistic.
- **Does not hold when**: instruments with weak seasonality are forced into the method; in this model single shares (quarterly earnings), some national indices and young assets show weak or unstable profiles, while some commodities and currency crosses show stronger ones.

## 4.4 Rule-based seasonal setups (described, not endorsed)
- **Monthly**: pick the month; trade only if one direction wins on both win rate (above about 60%) and mean return; enter at the close of the second consecutive session against that direction; target = historical mean return; stop = half the target (reward-to-risk 2:1, break-even win rate 33%). A warning sign: the favoured side wins often but the other side, when it wins, wins bigger on average.
- **Weekly and daily**: the same logic on the current week (exit at week end) or day; a daily variant requires 10, 15 and 20-year win rates all above 70% in the same direction.
- **Calendar tables and election-year cycles**: monthly share of positive closes, kept only if it holds as the history extends from 10 to 15 and 20 years; election-cycle statistics computed only on years of the same type and only for the market concerned.
- **Stop/target conflict**: within the same family of methods some use stop = target (1:1, "the edge is in the probability") and others stop = half target. **Inconsistent between practitioners**; each choice changes the break-even win rate (6.1).

## 4.5 The statistics of seasonal filters
- **Thesis**: high win rates over 10 or 20 years are often what chance alone produces when many windows are scanned.
- **Mechanism (worked)**: with no real effect (each year a coin flip), the chance that a given window shows at least 7 positive years out of 10 is 176/1024, about 17%; at least 8 of 10, about 5.5%; at least 14 of 20 (70%), about 5.8%. Scan 250 trading days on 40 instruments (10,000 windows) and several hundred will pass a "70% over 20 years" filter by luck. The 10-year sample sits inside the 20-year one, so agreement across horizons is not independent confirmation. An asset with upward drift is positive in most months anyway, so a "65% positive month" may be barely above its own baseline (general knowledge: broad equity indices have historically been up in roughly six months out of ten). Calendar effects documented in academic work have tended to weaken after publication (general knowledge).
- **Does not hold when**: a seasonal effect has a physical or institutional mechanism (harvests, heating demand, fiscal-year flows) and has been tested out of sample (`investing-and-financial-history` ch13).

## 4.6 The Commitments of Traders report
- **Thesis**: the weekly positioning report shows who holds futures, with a delay.
- **Mechanism**: the US futures regulator publishes positions by category each Friday, reflecting Tuesday's data (about three days of lag). Legacy categories: commercials (hedgers), non-commercials (large speculators, funds), non-reportable (small traders); a disaggregated or financial version splits dealers, asset managers, leveraged funds and managed money. Net position = longs minus shorts, plotted around zero. It covers only regulated futures; currency positions come from currency futures, not from the much larger spot market. A cross without its own future needs a "synthetic" reading built from its two legs.
- **Trade-off**: long history and objectivity against delay and indirectness.
- **Does not hold when**: the market has no liquid US future.

## 4.7 Reading positioning
- **Mechanism**: (1) **divergence**: price makes a new low while the net position of speculators rises (possible bottom), or the reverse at tops; trend and positioning moving together describe a healthy trend. (2) **Extremes**: historical extremes act like overbought/oversold, because large holders eventually close or reverse. (3) **Open interest**: a sharp fall during a trend shows positions that fed it being closed; size is judged relative to total (a drop of 12,000 contracts is about 8% of 155,000 but under 1% of 1.5 million). (4) **Commercials in commodities** are structurally short for hedging; when they stop being so, in this model, price may be low relative to producers' needs. (5) A gap between commercial and speculative positions at historical extremes often coincided with turning points in past samples.
- **Positions**: reading only the speculative category is called a common error; at least two categories should be compared. One view ranks positioning above seasonality when they conflict; another uses it only as a long-term bias.
- **Does not hold when**: used for timing: there is no standard lag between a positioning extreme and price; large players are wrong too; and a net short in hedgers is not a bearish forecast, since futures exist to hedge.

## 4.8 Retail sentiment as a contrarian filter (position)
- **Thesis**: when most small traders sit on one side, some practitioners lean the other way.
- **Mechanism**: aggregated broker data on the share of retail accounts long or short; extreme readings (three-quarters or more on one side) are used as a contrarian hint. The logic offered: many small traders do not use stops and hold losers, so a crowded losing side must eventually close.
- **Rival view**: crowding can persist through long trends; the data come from a subset of brokers and accounts; and the claim that "retail always loses" is not tested here. It is an opinion, not a demonstrated rule.
- **Does not hold when**: a strong trend is driven by flows that retail does not see.

## 4.9 Sector rotation as a risk-appetite gauge (position)
Comparing a broad index with its sectors: cyclical consumer sectors leading suggest risk appetite, defensive sectors leading suggest caution; an index at new highs not confirmed by cyclical or financial sectors is read as a divergence. Proponents say tops are found more easily than bottoms; the evidence offered is a handful of cases, not a statistical test.

## 4.10 Analog statistics: matching a recent path to history (position)
- **Thesis**: if the recent path resembles some past windows, the outcomes that followed them describe a distribution of possibilities, not a forecast.
- **Mechanism**: take a recent pattern (commonly one to three months of daily or weekly returns), normalise it, and search the history of the same instrument, and sometimes of related ones, for windows of similar shape. Record what happened over the following three to six months. Report the number of analogs, the share ending positive, the median and the spread, and how close each analog is to the current pattern. Tools that present such results as "probabilities of a path" are, in this model, conditional historical frequencies, and must be read with their sample size attached.
- **Robustness criteria (inconsistent)**: a minimum number of analogs (counts vary widely between practitioners); a share above roughly 60-70% in one direction; an outcome that is coherent across analogs rather than driven by one large episode; a close match to the current shape. None of the thresholds is shown to be optimal.
- **Trade-off**: using the whole history gives more samples, against the risk that the market's structure changed. Overlapping windows mean that ten "analogs" can be one episode seen ten times (4.5; ch08, 8.4).
- **Does not hold when**: the analogs are few, the instrument's structure changed, or the pattern length was chosen after trying several lengths, which is multiple testing (ch08, 8.3). Analogs chosen after the outcome is known are not analogs.
- **Rival view**: an analog study is a historical average with no explanation attached. Its value depends on whether the same mechanism repeats, which must be argued separately and cannot be read off the match.

## 4.11 Composite sentiment readings and their components
- **Thesis**: a composite oscillator averages several readings on different scales, so that one number reads "overbought" or "oversold".
- **Mechanism**: typical components are a deviation of price from a statistical average, a measure of buyers against sellers taken from bar structure, and the speed of price change. Each is rescaled to a common range and averaged. Zones are set by convention (extremes near plus or minus one hundred, for example). Practitioners often read the composite's trend, and the sign of its momentum, more than its level; a divergence is a disagreement between price and composite.
- **Pitfalls**: the components are correlated (speed and deviation move together), so the average counts one idea more than once (ch08, 8.4); the rescaling window changes the zones; and zone boundaries are conventions. Two presentations of the same composite that give different zones are inconsistent, not one correct and one wrong.
- **Trade-off**: a composite smooths noise and hides which component drives the reading. Read the components when the composite and the price disagree.
- **Does not hold when**: the composite is used as a timing tool inside a trend it does not follow. The single-oscillator limits of ch02 apply in full.
- **Rival view**: a composite is a rescaled indicator, and its value is no larger than that of its best component unless it has been tested out of sample.

## Common mistakes
- Opening a trade because "the season says so".
- Counting nested horizons (10 inside 20 years) as independent confirmations.
- Using a delayed weekly report for intraday timing.
- Treating a hedgers' net short as a bearish call.

## Links
- ch01 structure, ch05 strategies, ch06 stops, ch08 statistics; `investing-and-financial-history` ch13; `scientific-thinking` for multiple testing.
