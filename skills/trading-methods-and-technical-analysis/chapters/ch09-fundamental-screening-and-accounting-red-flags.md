# Chapter 09: Fundamental Screening, Fair Value and Accounting Red Flags

> Educational concepts, not investment advice. No stock is recommended. Thresholds are practitioner conventions; where practitioners disagree, the disagreement is stated.

## Core Idea
In this model, fundamental screening answers **"what is worth watching"** and technical or statistical tools answer **"when"**. Screens combine growth, profitability, leverage, solvency scores and a rough fair value; each number is an indicator, not a verdict, and each has a domain where it does not apply (banks, insurers, loss-making firms). Valuation theory in depth (discounting, multiples, mean reversion of multiples) sits in `investing-and-financial-history` ch05; this chapter covers the screening toolkit used by active traders and its weak points.

## 9.1 Reading the statements, not the headline
- **Thesis**: headline revenue and profit can hide the reason for a result.
- **Mechanism**: the balance sheet is a photograph (assets minus liabilities = equity), the income statement a film (revenue minus costs = profit), the cash-flow statement the cash actually generated. A short press release can omit what a full annual report explains in its notes. A method: compare every income-statement line with the prior year and follow each line's note number to the notes of the consolidated accounts (note numbers are not page numbers). Illustration: an airline with growing revenue reported a net loss because one non-recurring line, a change to employee pension plans, swung from a small gain to a charge of nearly two billion; the core business was not the cause. The reading criterion is to separate a loss in core operations from a non-operating, one-off item.
- **Does not hold when**: "one-off" items recur every year.

## 9.2 Core revenue and quality of earnings
- **Thesis**: prefer businesses whose profit comes from their main activity.
- **Mechanism**: remove ancillary revenue and check whether a loss remains. A carrier earning a third of its revenue from fees and extras may show a profit only because of them. Other quality checks: margins by division (revenue streams shift: a segment can go from minority to most of revenue), and operating cash flow above net profit.
- **Does not hold when**: the "ancillary" line is in fact the business model.

## 9.3 Profitability, leverage and multiples
- **Mechanism**: profit margin = pre-tax profit / revenue; return on equity (ROE) = net profit / equity. One screen from the material treats ROE above 15% and net margin above 7% as profitable. Debt/equity = total debt / equity. Leverage raises ROE: a property bought for 100,000 earning 12,000 a year returns 12% with own money, but about 120% on 10,000 of equity with a 90,000 mortgage, before interest, which is always due and rises with rates. Warning sign: debt rising fast while margins and returns stay flat or fall. EV/EBITDA (lower is cheaper, compared with history and peers); ROIC (return on invested capital; high and stable suggests a durable advantage); free-cash-flow yield = free cash flow / market capitalisation; forward PEG = P/E / expected earnings growth (P/E 30 with 30% growth gives 1), built on analysts' estimates.
- **Inconsistent thresholds**: debt/equity below 1 "comfortable", 1-2 "acceptable", above 2 "dangerous" in one presentation; above 1 already a red flag in another; below 1 simply "more equity than debt" in a third. Read them as sector-relative indications, not absolute limits. Ratios do not apply to funds or index baskets.

## 9.4 Trailing twelve months and growth acceleration
- **Thesis**: the sum of the last four quarters shows the year "as if it ended today".
- **Mechanism**: trailing-twelve-month (TTM) profit above the last annual figure suggests improving momentum; below, deterioration; for loss-makers, "less negative" with rising revenue. A variant compares 5- and 10-year growth rates on annual data with the same rates on TTM data: rising rates mean accelerating growth; a stock whose growth is decelerating is dropped even if it looks "undervalued". Overlaying profit and price on one chart to argue that gaps close is, as one practitioner concedes, comparing different scales.
- **Position**: one view says price follows earnings "most of the time" and that the P/E should be abandoned; neither claim is tested here.

## 9.5 Solvency and quality scores
- **Altman Z-Score** (bankruptcy risk from accounts). Zones used in the material: above 2.99 safe; 1.81-2.99 grey; below 1.81 distress; the trend matters as much as the level. One presentation also mentions "above 1.8" and "1.1" as thresholds: **inconsistent**. A plausible reconciliation (general knowledge, re-check): the original model for listed manufacturers is `Z = 1.2 X1 + 1.4 X2 + 3.3 X3 + 0.6 X4 + 1.0 X5` (working capital, retained earnings, operating profit, market value of equity over liabilities, sales; all but X4 scaled by total assets) with zones 1.81/2.99, while a later variant for non-manufacturers uses different weights and zones 1.1/2.6. Mixing versions produces mixed thresholds. Not for financial firms. An anomalous value (zero, or an extreme yield beside it) may be a data error or a firm in decline.
- **Piotroski F-Score** (0-9, nine pass/fail tests): profitability (positive net income, positive operating cash flow, rising return on assets, cash flow above net income); leverage and liquidity (lower debt, higher current ratio, no new shares); efficiency (rising gross margin, rising asset turnover). Above 6 is called the "strong zone". Better on industrial and service firms than on financials; a low score does not exclude recovery.
- **Beneish M-Score** (eight indices from the accounts, built to flag earnings manipulation): an indication, not proof. Zones in one presentation: above -1.78 red flag; -2.22 to -1.78 grey; below -2.22 no apparent problem. Another presentation drops the grey zone ("below -1.78 low risk"). **Inconsistent**; general knowledge suggests -1.78 belongs to the eight-variable model and -2.22 to an earlier five-variable version, re-check before use. Indices include days of receivables, gross-margin change, asset quality, depreciation rate and leverage. Example of the depreciation lever: stretching a 1,000,000 machine's life from 5 to 20 years cuts annual depreciation from 200,000 to 50,000 and lifts reported profit. Quarterly data surface anomalies earlier; a jump in receivables is not fraud by itself. Not for banks and insurers.
- **General limit**: all three are probabilistic hints. Claimed backtests of score-based portfolios are discussed in ch08 (8.1).

## 9.6 Fair value as an average of rough models
- **Thesis**: fair value is discounted future cash; the formula is easy, the inputs are not.
- **Mechanism**: present value = future amount / (1 + rate)^years; at 5% a year, 100 in five years is worth about 78.4 today; a higher risk-free rate lowers every fair value. Rate = risk-free yield plus a risk premium (at least 4-5 points for a single company, in one view). Future earnings may be projected with linear and logarithmic regressions of history instead of personal guesses; analysts differ because projections differ, not formulas. Three methods are often averaged: discounted cash flow; economic value added (operating profit after tax minus cost of capital times invested capital); and the growth-equals-P/E rule of thumb (a fairly valued firm's P/E roughly equals its growth rate; half of growth is "attractive"). For prudence some drop the highest of the three. Read in reverse, a P/E is the growth the market is pricing in.
- **Does not hold when**: earnings are negative (growth rules and automatic fair values are meaningless), or the firm is a bank (cash-flow models need different inputs). An index can be valued by aggregating its largest members, but the output is a model, not a fact.

## 9.7 Dividends, buybacks and shareholder yield
- **Mechanism**: dividend yield = annual dividend per share / price; it rises when price falls and collapses when the dividend is cut; yields above 10-15% are more often warning than opportunity. Shareholder yield = dividend yield + net buyback yield + net debt reduction. Screen: shareholder yield positive and above dividend yield, otherwise the dividend is financed by new debt or new shares (dilution). Buybacks reduce share count; issuing shares to repair accounts is a negative sign. A growing dividend with a falling price is flagged for a closer look, not bought on sight.

## 9.8 Insider transactions and other screens
- **Mechanism**: in the US, insiders report trades on a standard form within days; open-market purchases with own money (code P) are the most informative; awards, option exercises and sales (often for taxes or personal spending) much less. Clusters of several insiders buying, small capitalisations, a fallen price and growing fundamentals are the combination studies tend to highlight (general knowledge). Screens add minimum capitalisation (liquidity), positive earnings, debt limits and positive margins; a first profitable quarter is a moment to analyse, not a signal. A qualitative ten-question scorecard for intangible-heavy firms (hard to copy, word of mouth, crisis survival, R&D above marketing, low turnover, succession, recurring revenue, pricing power, steady growth, room to grow) addresses the accounting fact that R&D is expensed at once, understating earnings of heavy investors.
- **Does not hold when**: scores are produced by a tool or a language model without inspection of the inputs.

## Common mistakes
- Treating a threshold from one presentation as a standard.
- Applying solvency or manipulation scores to banks and insurers.
- Averaging fair-value models whose inputs share the same optimism.
- Reading a high yield without the shareholder yield.

## Links
- ch08 claimed results; `investing-and-financial-history` ch05 (valuation), ch03 (factors), ch10 (fraud warning signs).
