# Chapter 14: Macro Indicators and How Shocks Reach Markets

> Educational reading guide, not investment advice. Every indicator value, consensus figure and policy rate is a dated snapshot; check the release, its revision history and its date before using a number.

## Core Idea
In this model, a macro indicator is **a measured quantity with a lag, a revision history and a theory of how it reaches prices**. Markets react to the difference between a reading and what was expected, and to changes in the expected path of policy, rather than to levels alone. The chapter gives a map: which family of indicator measures what, how rates and currencies carry a shock into asset prices, and which chains are contested. For the institutions themselves see ch02; for inflation measurement see ch03; for bond mechanics see `investing-and-financial-history` ch06.

## 14.1 Indicator families and what each measures
| Family | Typical examples | What it measures | Usual caveat |
|---|---|---|---|
| Activity | purchasing managers' surveys, payrolls, jobless claims, retail sales, industrial output | Current and near-term pace of the economy | Surveys are opinions; payrolls are revised |
| Prices | consumer and producer price indexes, price deflators, wage growth, inflation expectations | Price pressure and how persistent it is | Headline is distorted by energy and food; core is a choice |
| Rates and curve | policy rate, market-implied rate path, government bond yields | Cost of money and the expected policy path | Expected path can change faster than the policy rate |
| Credit | corporate spreads over government yield, bank lending surveys, default rates | Willingness and cost of lending, stress in credit | Spreads reflect liquidity as much as default risk |
| Liquidity | central bank balance sheet, money-market funds, repo rates | Availability of cash and collateral | Hard to aggregate; definitions differ |
| External | trade-weighted currency indexes, reserves, current account | Pressure from abroad and the external balance | Index weights change the answer |
| Positioning | fund positioning surveys, futures positioning (trading ch04) | Who holds what, with a delay | Describes holdings, not the cause of moves |

Release timing matters. A reading published late in the month describes the previous month. Revisions can reverse the sign of a change. An analyst who uses the first print must say so.

## 14.2 Level, change and surprise
- **Thesis**: markets price what they expect, so the reaction tracks the surprise, not the level.
- **Mechanism**: the consensus forecast is the reference. A reading above consensus is a hawkish surprise for an inflation indicator and a positive one for activity; a reading below consensus reverses the sign. Base effects matter: a year-on-year change can look high or low because the comparison period was unusual (ch03).
- **Trade-off**: surprise is the right concept for prices, but consensus is itself uncertain and differs between sources.
- **Counter-view**: a persistently high level can matter even with no surprise, because it changes the path of policy that markets must price.

## 14.3 Real rates and the discount rate
- **Thesis**: the rate that discounts future cash flows is set by the risk-free yield plus a risk premium. Real rates (nominal yield minus expected inflation) are the part that matters most for assets without coupons.
- **Mechanism**: a higher discount rate lowers the present value of distant cash flows more than near ones. Long-duration assets, such as growth shares whose earnings lie far ahead and long-dated bonds, lose more for the same rise in rates (`investing-and-financial-history` ch05 for the discounting arithmetic; ch06 for bond duration). Gold pays no coupon, so higher real rates raise its opportunity cost. Bitcoin and other non-yielding assets are argued to respond the same way (position).
- **Trade-off**: real rates are estimated, often from inflation-linked bonds or from surveys; the estimate depends on the inflation measure used.
- **Does not hold when**: the rise in real rates comes with stronger earnings growth that exceeds the discount effect, or the assets are cash-generating and short-dated.

## 14.4 Policy path and market-implied probabilities
- **Thesis**: futures on policy rates and rate-derivatives price the probability of each path. The prices change with data and with what central bankers say.
- **Mechanism**: the implied probability of a move at a meeting is read from the price of short-term contracts. A large move in the probability after one release shows that the market had a different view. Tone counts: a decision with unchanged rates and a restrictive message can tighten conditions through higher yields and a stronger currency, without a rate change (ch02, forward guidance).
- **Trade-off**: market-implied probabilities are informative but not forecasts. They include a term premium and a risk premium, so they are not pure expectations.
- **Does not hold when**: the market is thin, or the probability is taken as a certainty. A 70% probability still expects the other outcome three times in ten.

## 14.5 The yield curve: level, slope and steepening
- **Thesis**: the slope of the government yield curve (long minus short) carries information about the expected path of policy and about the risk premium.
- **Mechanism**: an inverted curve (short rates above long) has preceded many past recessions, but the episodes are few, and the timing varies widely; the signal is not a dated trigger (position). The shape can change in two ways. A *bull steepening* is short rates falling faster than long rates, typical when markets expect easing. A *bear steepening* is long rates rising faster, typical when investors demand more compensation for inflation or for supply of debt. The two imply different things about growth and about the credibility of the policy path.
- **Trade-off**: slope is a summary; the level of the long rate and the level of the short rate matter too.
- **Counter-view**: a steep curve can mean a healthy recovery or an inflation scare; the shape alone does not say which.

## 14.6 The currency channel and carry unwinds
- **Thesis**: exchange rates link policy in one economy to financial conditions in another.
- **Mechanism**: a carry trade borrows in a low-yield currency to invest in higher-yield assets. The position earns the rate gap as long as the funding currency does not rise. When the funding currency strengthens quickly, leveraged holders must close positions, and the closing sells the risky assets as well as the funding currency. Correlations between markets rise during such unwinds, which removes the diversification that the positions appeared to have. A change in the policy of the funding-currency central bank can start the move.
- **Trade-off**: carry earns steadily in calm markets and loses in bursts; the average return hides the tail.
- **Does not hold when**: positions are small, funded in a currency that does not move, or hedged.

## 14.7 Oil, inflation and the stagflation chain
- **Thesis**: an energy price rise feeds into inflation directly, and into demand indirectly.
- **Mechanism**: energy has a direct weight in consumer prices and an indirect effect through transport, fertiliser and input costs. If households and firms expect higher inflation, wages and prices can follow (second-round effects, ch03). A central bank that holds rates high to contain them slows activity. The combination of high inflation and weak growth is stagflation, and it is the chain most often cited as the worst case for equities (position).
- **Supply or demand**: an oil rise from a supply shock differs from one driven by demand. A supply shock tends to lower output and raise prices together; a demand boom raises both as well, but with stronger activity. Telling them apart needs the quantity data, not only the price.
- **Trade-off**: a price rise is visible on the day; its macro effect takes quarters.
- **Does not hold when**: the energy share of spending is small, or the rise is reversed quickly.

## 14.8 The dollar as a global financial condition
- **Thesis**: a large share of world trade, debt and reserves is priced in dollars, so the dollar's value shapes financial conditions outside the US.
- **Mechanism**: a stronger dollar tightens conditions for borrowers who owe dollars and for importers whose costs rise, and weakens the value of dollar assets when measured in local currency. A weaker dollar has the reverse effect. The dollar is involved in most foreign-exchange transactions and holds the largest share of reserves (general knowledge; check current data from the central bank and the international financial institutions).
- **Trade-off**: a weak dollar helps some exporters and hurts importers; the net effect depends on the country.
- **Does not hold when**: the question is about a single bilateral rate, where other currencies drive the move.

## 14.9 Shock taxonomy
Sort any shock before reading its effects. Four families, each with its own sign on inflation, activity and asset prices:
- **Demand shock**: spending rises or falls. Inflation and activity move together.
- **Supply shock**: productive capacity or input costs change. Inflation and activity move in opposite directions.
- **Financial shock**: credit tightens or liquidity is withdrawn. Spreads widen and activity falls, often ahead of inflation.
- **Policy shock**: tariffs, taxes, regulation or a change in the central bank's reaction function. The effect depends on its expected duration.

Most real episodes mix two or three. A reading that fits only one family is a hypothesis to test.

## 14.10 Reading an indicator: a checklist
1. Name the family and what it measures (14.1).
2. Use the first print and the revised print, and say which.
3. Compare with consensus, and with the previous reading, and check for base effects.
4. Ask whether the change is in level, rate of change or surprise (14.2).
5. Ask which rate it moves: the real discount rate, the policy path or the term premium (14.3 to 14.5).
6. Check the currency channel (14.6) if the market is foreign.
7. Sort the shock (14.9) before reading the asset response.
8. Write what would change the reading, and when the next release is due.

## Counter-view and open questions
- Whether leading indicators predict turning points reliably: the record is mixed, and the lead times vary too much to serve as dates.
- Whether markets lead the economy or follow it: both happen; the balance changes with the episode.
- Whether the policy path is credible when the central bank's independence is questioned: contested, and it changes the meaning of every long-rate move.

## Common mistakes
- Reading a level as news when the market reacts to the surprise.
- Treating an inverted curve as a dated event.
- Quoting a revised figure as if it were the first print.
- Assuming that a rise in one asset means a rise in all, without a currency or rate channel.
- Reading a 70% probability as a certainty.

## Links
- ch02 (rates, guidance, balance sheet), ch03 (inflation measurement and expectations), ch05 (exchange rates and regimes), ch06 (crises); `investing-and-financial-history` ch05 (valuation and discounting), ch06 (bonds and curve), ch11 (decisions under uncertainty), ch13 (reading studies); `trading-methods-and-technical-analysis` ch04 (positioning data).
