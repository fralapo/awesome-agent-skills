# Chapter 03: Candlesticks, Chart Patterns, Ichimoku and Cycles

> Educational concepts, not investment or trading advice. No signals, no forecasts. Pattern names describe shapes; they carry no guaranteed outcome.

## Core Idea
In this model, patterns are **shapes that recur because participants tend to react alike in similar situations**. They are pieces of evidence to combine with trend, levels and timeframe, never stand-alone predictions. The useful skill is not knowing hundreds of names but recognising a few clear configurations, especially candles of unusual size, and knowing where each one is invalidated. Studies of candlestick patterns after costs are mostly unfavourable (3.9).

## 3.1 Candle volatility as the key variable
- **Thesis**: a candle matters in proportion to its range relative to the candles before it.
- **Mechanism**: wide-range candles (large body, small shadows; a "marubozu" in the extreme) show control by one side; when they break a level they confirm the move, and their highs and lows become later levels and stop references. Narrow candles are pauses and carry no signal. A spinning top (small body, long shadows on both sides) shows indecision and matters only near a level at the end of a trend. A shadow about twice the body is a visual cue of rejection in one method.
- **Trade-off**: size relative to recent history is a moving benchmark; what is "wide" on one instrument is ordinary on another.
- **Does not hold when**: a single candle is read in isolation from trend and level.

## 3.2 Single-candle reversal shapes
- **Thesis**: shadows show rejection; position in the trend gives the shape its meaning.
- **Mechanism**: a **doji** (open about equal to close): gravestone after a rise is bearish, dragonfly after a decline bullish, long-legged is strong indecision, a doji right after a break hints at a false break. **Hammer** (after a decline) and **hanging man** (after a rise) share a long lower shadow; **shooting star** and **inverted hammer** share a long upper shadow. Practitioners disagree on which shapes need confirmation: one view says hammer and shooting star do not, while the hanging man needs a close below its low; another adds the inverted hammer to those needing confirmation; a third requires, for all of them, a next candle closing beyond the pattern's extreme. **Inconsistent between practitioners**; the conservative reading is to require confirmation for all.
- **Does not hold when**: the shape appears mid-range, away from any level.

## 3.3 Multi-candle patterns
- **Thesis**: two- and three-candle patterns encode a shift of control.
- **Mechanism**: **engulfing**: a wide second candle that engulfs the first; it works in directional markets, not in ranges. **Morning star**: a wide bearish candle, a narrow one, then a wide bullish candle closing well into the first body; **evening star** mirrors it. Gaps between the candles are rare in round-the-clock currency markets and are not required. **Continuation**: a long candle, three small ones inside it, then a new candle in the trend direction. **NR4**: four candles of narrowing range, then expansion. In this model reversal patterns are more reliable than continuation ones, and fewer than ten patterns are enough.
- **Mechanism, coding**: a pattern decomposes into elementary conditions joined by AND. A bearish engulfing: previous bar up; current bar down; current open above the previous high; current close below the previous low (the strict version; looser versions compare bodies). Writing patterns this way is the first step to testing them (ch08).
- **Does not hold when**: the definition used in testing differs from the one used in trading.

## 3.4 Managing a candle signal
- **Thesis**: entries, stops and targets come from the signal candle itself.
- **Mechanism**: decisions are taken on closes, not on intraday shadows. Entry is aggressive (right after the signal) or conservative (on the break of the signal candle's high or low). The stop is a close beyond the opposite extreme of the signal candle. The trade is taken only if the distance to the next level offers an adequate reward-to-risk ratio (6.1); the target is the next resistance where shadows cluster across periods. The daily timeframe is, in this model, the most reliable.
- **Does not hold when**: the reward-to-risk is poor; then the signal is skipped, however clean.

## 3.5 Chart figures
- **Thesis**: figures are codified supply-and-demand configurations; projections give a price objective, not a date.
- **Mechanism**: **head and shoulders**: the neckline joins the two lows between the shoulders; after the break, price often retests the neckline; the objective is the head-to-neckline distance projected from the break point; the inverse figure is symmetric. **Triangle**: compression between buyers and sellers, usually resolved by a sharp move; in an ascending triangle sellers defend the same level while buyers raise lows; objective = height of the base projected from the break. Compression of volatility is followed by expansion, more often in the direction of the prior trend. **Double and triple tops/bottoms** and **rectangles** (sideways channels, objective = channel height) complete the common set.
- **Trade-off**: real figures are rarely perfect as in manuals; tolerance makes them easier to see and easier to see falsely.
- **Does not hold when**: the break fails and price returns inside the figure, which invalidates the projection.

## 3.6 Ichimoku: equilibrium at a glance
- **Thesis**: Ichimoku measures the distance of price from recent equilibrium and projects support and resistance forward.
- **Mechanism (standard settings 9-26-52)**: **Tenkan** = (highest high + lowest low) / 2 over 9 periods: close to price, a momentum line. **Kijun** = the same over 26 periods: the more reliable level, a magnet when flat, and the midpoint of the 26-period range (hence equivalent to a 50% retracement of that range). These are midpoints, not averages of closes, so flat stretches mark consolidations without new extremes. **Chikou** = the close shifted back 26 periods; above the price of 26 periods ago it supports a long reading. **Kumo** (cloud) = Senkou A ((Tenkan + Kijun) / 2) and Senkou B (52-period midpoint), both shifted 26 periods forward; it describes future support and resistance, not future price. Alternative settings (for example 7-22-44 for a shorter trading week) are single-practitioner positions.
- **Mechanism, signals as used**: Tenkan/Kijun cross, close out of the cloud, break of the Kijun, cloud twist; more agreeing signals raise confidence, but in this model a Kijun break is a warning, not an entry. A method built on it reads price first (range, then wide candles breaking out, strong impulses and weak pullbacks), confirms with a close through the cloud on a wide candle, then waits for a pullback to a zone for timing; the stop is a close below a price band rather than a single line.
- **Position**: some read Ichimoku only as an elastic: when price is far from Kijun and cloud, equilibrium must be partly restored before the trend resumes. Views differ on whether it suits currencies or indices better; the daily chart is treated as the minimum reliable timeframe by some.
- **Does not hold when**: the market is range-bound and price weaves through the cloud.

## 3.7 Impulse and retracement
- **Thesis**: continuation entries need a complete impulse-retracement shape.
- **Mechanism**: an impulse in the trend direction, a retracement to a technical zone (the extreme of a breakout candle, a wide candle, a support or resistance, the Kijun), an entry only once the shape is complete. First target = the end of the impulse. A protective stop sits beyond a level on a closing basis, with a further emergency stop at about 2 x ATR.
- **Does not hold when**: the retracement is deep and fast, which in this model reads as a possible change of trend.

## 3.8 Cycles, Fibonacci and time (position)
- **Thesis**: cycle analysis decomposes price into periodic components; it is a complementary view, not an exact forecast.
- **Mechanism**: a cycle has magnitude, period (low to low) and phase. Principles in the classic cycle model: summation, commonality, nominality, harmonicity (typical ratio 2:1), proportionality, plus variation (tendencies, not laws). An annual cycle of about 50 weeks would contain two half-year cycles of about 25. Cycles in phase produce clean trends; out of phase, ranges. One practice avoids the most correlated cycle ("already spent") and follows the next one, with a 13-period average as a filter. Fibonacci numbers (5, 8, 13) recur in averages; Fibonacci extensions are used for targets.
- **Rival view**: in this model too, Fibonacci and angle-based methods are criticised as too interpretive, since the analyst chooses the swing points; pivots are preferred by some for that reason (1.8). Elliott waves appear only as an eyeball reading and are not treated systematically here.
- **Does not hold when**: cycles are fitted to the same data used to "confirm" them.

## 3.9 Evidence on patterns (position)
In this model, patterns help structure decisions. Rival view (general knowledge): systematic tests of candlestick and chart patterns on liquid markets have generally found little or no predictive value after costs, with results sensitive to the exact definition; recognition by eye after the fact inflates apparent reliability (hindsight bias, `investing-and-financial-history` ch08, ch13).

## Common mistakes
- Learning a hundred patterns and testing none.
- Reading a figure before the break has closed.
- Treating the cloud as a price forecast.
- Choosing Fibonacci anchors after seeing where price reacted.

## Links
- ch01 levels, ch02 indicators, ch05 strategies, ch06 stops, ch08 testing.
