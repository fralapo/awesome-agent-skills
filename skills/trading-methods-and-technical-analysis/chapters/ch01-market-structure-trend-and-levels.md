# Chapter 01: Market Structure, Trend and Price Levels

> Educational concepts, not investment or trading advice. No signals, no forecasts. Price levels in examples are generic illustrations, not quotes.

## Core Idea
In this model, technical analysis starts from one premise: **price already contains the news, and it is formed by the meeting of supply and demand**. Past prices are studied to interpret the present, not to know the future. The basic vocabulary is structural: a trend is a sequence of highs and lows, a level is a zone where orders gathered before, and every statement about direction must carry a horizon. Whether any of this earns money after costs is contested (ch08, and `investing-and-financial-history` ch02).

## 1.1 Price, candles and the horizon
- **Thesis**: direction has no meaning without a timeframe.
- **Mechanism**: a line chart records only closes; a candlestick records four prices (open, high, low, close). The body shows open-to-close, the shadows (wicks) show the extremes reached and rejected. Each timeframe is a zoom of the same series: one daily candle splits into 24 hourly ones. An instrument can be falling on the daily chart and rising on the five-minute chart at the same time, so "is it going up?" is incomplete until "within when?" is answered. Price is the only quantity that is the same across chart types and timeframes; every indicator is a formula applied to it.
- **Trade-off**: lower timeframes give more entries and more noise; higher timeframes give fewer, slower, more reliable readings.
- **Does not hold when**: the question is about value rather than price path (ch09).

## 1.2 Top-down reading ("nested dolls")
- **Thesis**: the longer timeframe sets the context, the shorter one sets the timing.
- **Mechanism**: read monthly or weekly for the background trend, daily and four-hour for zones, hourly or lower only for execution. Levels and patterns found on higher timeframes outweigh those on lower ones; a weekly pattern beats a four-hour one. When timeframes disagree, the method waits for the lower one to realign with the higher (for example, a pullback in a weekly uptrend ends with an hourly turn up). A frequent beginner layout in this model: analysis on weekly, operations on daily, nothing below one hour; below that, false signals multiply.
- **Trade-off**: waiting for alignment skips many moves.
- **Does not hold when**: the strategy is explicitly intraday and the higher context is flat (ch05, 5.8).

## 1.3 Trend as structure (Dow theory)
- **Thesis**: an uptrend is a series of higher highs and higher lows; a downtrend, lower highs and lower lows; anything else is a range.
- **Mechanism**: the trend is read on the chart, not computed. A quick check: join the first and last visible closes; the slope gives the direction on that window. A healthy uptrend shows wide trend candles and small pullback candles nearly contained inside them; a pullback that fails to produce a new high afterwards means the trend is no longer up. Market phases in this model: accumulation (sideways after a decline), participation (the trend), distribution (sideways after a rise), then reversal.
- **Trade-off**: structure is unambiguous only in hindsight; in real time the last swing is always provisional.
- **Does not hold when**: the market is in a range, where "higher high" and "lower low" alternate without follow-through.

## 1.4 Reversal: suspicion versus confirmation
- **Thesis**: a reversal is a hypothesis until a key level breaks.
- **Mechanism**: after a decline, the first warning is a low that is not lower and a high that exceeds the previous one; confirmation is a close above the prior swing high, and often a return to the broken level, which flips from resistance to support. After a violent fall, lows are usually tested several times with long lower shadows before turning. Anticipating a reversal in free fall is, in this model, a common error.
- **Does not hold when**: a discontinuous event (a gap through all levels) makes the structure irrelevant.

## 1.5 Trendlines
- **Thesis**: a trendline describes the slope of a trend and its end.
- **Mechanism**: one drawing method uses closes only (a line chart helps): start from the highest close for a downtrend line and join it to the next close that keeps every close below the line; the anchor must be a swing consistent with the trend. Others draw on shadows: a difference of style, not of truth. Many lines on one chart signal a method not yet understood; when the first line is far from price, a new, steeper one is drawn. A line touched several times gains weight. A break obliges a review of the scenario; the break point often acts as a magnet, with price returning to test it (pullback). A common target after a break is the previous, steeper trendline or, failing that, the swing from which the first line started.
- **Position**: one rule of thumb holds that breaking a trendline born after N periods signals a turn in a cycle of about 2N periods. It is a personal heuristic without a measured base and gives no target.
- **Does not hold when**: price chops around the line; a break followed by a doji and an opposite pattern is a common shape of a false break.

## 1.6 Support, resistance and the level as a zone
- **Thesis**: a level is where orders accumulated, and it is a band, not a line.
- **Mechanism**: support is where price bounced up before, resistance where it was pushed back; a level that worked several times tends to be watched again and can swap roles once broken. Round numbers matter, especially if they already turned price. Long shadows mark price areas with many resting orders. The width of the band comes from the shadows around the level; on a volatile pair a "level" can be a band of a hundred points or more. In this model, extremes of unusually wide candles become later supports, resistances and stop references, and the midpoint of a very wide candle is itself a reference.
- **Trade-off**: a band is honest about uncertainty but makes stop placement wider.
- **Does not hold when**: a level has been tested so many times that, in this model, the next test is more likely to break than hold.

## 1.7 Breakout: valid or false
- **Thesis**: a break is judged on closes and on the size of the breaking candle, not on a touch.
- **Mechanism**: look for levels on high timeframes, then judge the break on the daily chart. One criterion: after a range, a candle whose open-to-close range is far larger than the recent average closes decisively beyond the level, and the method waits for a confirming close. A close just beyond the level with long shadows and a small body is not confirmed; a level broken and quickly regained, or a doji right after the break, often marks a false break. A broken resistance tends to become support. Comparing the candle's range with the instrument's own normal volatility tells whether the break is unusual.
- **Trade-off**: waiting for confirmation gives a worse price; entering on the touch takes more false breaks. Two entries are both used: on the retest or directly.
- **Does not hold when**: the range is wide and noisy; in this model many methods simply stand aside then (ch05, 5.5).

## 1.8 Pivot points
- **Thesis**: pivots are mechanical levels, so they remove the choice of swing points.
- **Mechanism (classic version, general knowledge)**: from the previous day's high `H`, low `L` and close `C`: `P = (H + L + C) / 3`; `R1 = 2P - L`; `S1 = 2P - H`; `R2 = P + (H - L)`; `S2 = P - (H - L)`; `R3 = H + 2(P - L)`; `S3 = L - 2(H - P)`. Variants include volatility. They are known from the start of the session and fixed for the day; they say nothing about direction and are areas rather than exact prices. A cluster of daily and weekly pivots is treated as the stronger level. On the first session of the week, the previous trading day's values are used.
- **Trade-off**: objective, but objectivity is not predictive power.
- **Does not hold when**: a scheduled data release dominates the session (ch05, 5.4).

## 1.9 Volume and the phases of supply and demand (thin coverage)
- **Thesis**: where real volume exists, it is read as confirmation of a break or as effort versus result.
- **Mechanism**: on exchange-traded futures and shares, a "good" breakout in this model shows a strong candle with volume around twice its average, a retest on low volume, and a false break on thin volume followed by a heavy-volume return inside (a bull trap). Over-the-counter contracts for difference and spot currencies have no centralised volume; tick counts are only a proxy, and one view holds that volume carries little meaning in currencies. The Wyckoff schema (general knowledge) names four phases (accumulation, markup, distribution, markdown) and reads divergences between effort (volume) and result (price progress): price making new lows while a demand measure rises suggests accumulation; new highs with falling demand suggest distribution. These readings are context, not timing.
- **Does not hold when**: the instrument has no reliable volume, or volume is distorted by index rebalancing and expiries.
- Coverage note: the material behind this skill treats volume and Wyckoff only in passing; the schema above is general knowledge to re-check against a primary text.

## Common mistakes
- Stating a direction without a timeframe.
- Drawing levels as thin lines and stops one tick beyond them.
- Calling a break on an intraday touch instead of a close.
- Reading volume on instruments that have none.

## Links
- ch02 indicators, ch03 patterns, ch05 strategies, ch06 stops; `investing-and-financial-history` ch02 on what efficiency implies for chart reading.
