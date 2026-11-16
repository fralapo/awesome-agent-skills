# Chapter 02: Moving Averages, Oscillators and Volatility Measures

> Educational concepts, not investment or trading advice. No signals, no forecasts. Default parameters are conventions, not optimal values.

## Core Idea
In this model, **an indicator is a formula applied to price; it measures, it does not predict**. A moving average measures where price has been on average, an oscillator measures where the close sits inside a recent range or how up-closes compare with down-closes, a volatility measure gauges the size of normal moves. Knowing what each formula measures prevents the most common misreadings, such as treating "overbought" as "about to fall". Whether rules built on these measures beat a buy-and-hold baseline after costs is a separate, contested question (8.6).

## 2.1 Moving averages
- **Thesis**: a moving average smooths price and lags it by construction.
- **Mechanism**: a simple moving average (SMA) is the mean of the last N closes; an exponential one (EMA) weights recent closes more. Price above a rising average reads as an uptrend, below a falling one as a downtrend; the slope matters as much as the position. The 200-period average (about a trading year on daily data) is a convention for the long trend, 50 for the medium one. With three averages (say 50, 100, 200), price below all three describes a downtrend, and a change in the slope of the fastest is the first sign of change. In this model the 200-period line also acts as a dynamic level: price is drawn back to it, and breaking it can precede acceleration.
- **Trade-off**: longer averages are steadier and later; shorter ones are timelier and noisier.
- **Does not hold when**: the market is in a range, where price crosses the average back and forth.

## 2.2 Crossovers and the "right" period
- **Thesis**: averages describe the trend; using their crossovers as entry signals is weak.
- **Mechanism**: a crossover of two averages arrives late and, in ranges, produces a run of false signals; in this model it loses over time as an entry system, while working in strong trends. Two averages on a chart are enough; five add nothing. There is no secret period: 200 is convention, and searching for the period that "worked best" on one instrument (a fitted value such as 28 on one currency pair) is curve fitting unless tested out of sample (8.3).
- **Does not hold when**: used only as a trend filter for another entry rule.

## 2.3 Oscillators: what they measure
- **Thesis**: oscillators are bounded (usually 0 to 100) and were designed for ranges; trend-following indicators are unbounded.
- **Mechanism**: the **stochastic** places the close inside the recent range: with low 50, high 100 and close 90, `(90 - 50) / (100 - 50) = 0.8`, a reading of 80. The **RSI** (relative strength index, 14 periods by convention) compares the average up-close with the average down-close over N periods, rescaled to 0-100; 50 is the dividing line. The **MACD** (12-26-9 by convention) is the difference of two exponential averages with a signal line; it is unbounded and slower. Oscillators are close relatives of each other; in this model one is chosen and learned with default settings rather than several being stacked.
- **Trade-off**: bounded readings are easy to compare across instruments but saturate in strong trends.
- **Does not hold when**: a single oscillator is read without the trend context of a higher timeframe.

## 2.4 Overbought and oversold are not reversal signals
- **Thesis**: a high reading proves a strong trend in progress, not an imminent reversal.
- **Mechanism**: from the stochastic formula, a reading of 80 means the close sits near the top of its recent range, which is what an uptrend looks like. In this model the classic "overbought means sell" reading should be dropped; if anything, a move from oversold to overbought can mark the start of a rise. A variant uses the RSI as a regime filter: above roughly 40 in uptrends, below roughly 60 in downtrends, between 40 and 60 a range (5.1).
- **Position**: some practitioners still trade 70/30 extremes against the move in ranges (5.4); others treat them only as a pre-alarm. Both are rules of thumb without a stated base rate.
- **Does not hold when**: the market is genuinely range-bound and mean-reverting.

## 2.5 Divergences
- **Thesis**: a divergence is a loss of momentum, not an entry signal on its own.
- **Mechanism**: price makes a new high and the oscillator does not (bearish), or price makes a new low and the oscillator does not (bullish). Price and oscillator making extremes together describe a healthy trend. One confirmation method draws a trendline on the diverging swing and waits for its break and a pullback. In this model divergences are more reliable on higher timeframes, a third divergence weighs more than the first, and a divergence against the higher-timeframe trend (a bullish divergence on fifteen minutes inside a daily decline) is not a signal. Oscillators can also reveal patterns, such as head and shoulders, that are hard to see on price.
- **Does not hold when**: price has already fallen a long way and the oscillator sits at an extreme; divergences then appear repeatedly without a turn.

## 2.6 Momentum histograms and averaging systems
- **Thesis**: several popular tools are averages in disguise.
- **Mechanism (general knowledge)**: the **Awesome Oscillator** is a 5-period minus a 34-period simple average of the median price, drawn as a histogram; zero means the averages cross, colour changes show slowing momentum, and in this model divergences matter more than colour. The **Alligator** is three averages of the median price shifted forward (5 shifted 3, 8 shifted 5, 13 shifted 8): lines fanned out and ordered describe a trend, lines tangled describe a range, where the system fails. **Heikin Ashi** candles use `close = (O + H + L + C) / 4` and `open = (previous smoothed open + previous smoothed close) / 2`; they smooth noise and help hold a trend, but do not show real prices, so orders are placed on a normal chart.
- **Does not hold when**: used below about fifteen minutes, where smoothing lags most of the move.

## 2.7 Trend-strength and stop-style indicators
- **Thesis**: some indicators measure strength or trail price rather than direction.
- **Mechanism**: the **ADX** measures trend strength, not direction; one set of thresholds treats it as meaningful above about 20 for indices, currencies and commodities and above about 25 for shares (practitioner thresholds). The **Parabolic SAR** (step 0.02 by convention) and **Supertrend** trail price and flip side when touched; they are used as trailing stops or direction filters. **Bollinger bands** place bands at two standard deviations around a 20-period average; the middle band is a mean-reversion target in some methods (5.4).
- **Does not hold when**: a strength reading is mistaken for a direction call.

## 2.8 ATR: the unit of normal movement
- **Thesis**: the average true range (ATR, 14 periods by convention) is the instrument's own yardstick.
- **Mechanism**: ATR averages the true range (the larger of high minus low and the gaps from the previous close). It changes with instrument and timeframe: a currency pair may move around 70 points a day, 27 on four hours and 17 on one hour (illustrative proportions). Its uses in this model: stop distance in multiples of ATR (6.3), judging whether a candle is unusually wide (1.7), and comparing an option's break-even with typical daily movement (10.1). The expected volatility of a session is better judged from the calendar of scheduled events than from past ATR.
- **Does not hold when**: a regime change makes the trailing average stale.

## 2.9 What the evidence says about indicators (position)
- **In this model**: indicators are tools for describing trend, momentum and volatility, and for building consistent rules; they are not predictors.
- **Rival view (general knowledge)**: academic tests of simple moving-average and oscillator rules on long index histories have found apparent profits that shrink or vanish after accounting for data snooping (many rules tried), transaction costs and out-of-sample periods; the weak-form efficiency argument says past prices should not forecast future returns once costs are counted (`investing-and-financial-history` ch02). The strongest counter-evidence in favour of trend rules comes from diversified, long-horizon trend-following across many asset classes, where returns have been documented but are lumpy and regime-dependent (5.1).
- **Reading**: treat any indicator claim as a hypothesis to test with the checklist in ch08, and in `investing-and-financial-history` ch13.

## Common mistakes
- Treating overbought as a sell signal.
- Stacking several oscillators that measure the same thing.
- Optimising a period on one instrument and calling it "the right one".
- Placing orders on smoothed candles.

## Links
- ch01 structure, ch03 Ichimoku and patterns, ch05 strategy rules, ch06 ATR stops, ch08 evidence; `investing-and-financial-history` ch02, ch13.
