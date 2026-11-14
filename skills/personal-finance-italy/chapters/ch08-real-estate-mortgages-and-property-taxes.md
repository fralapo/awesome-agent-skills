# Chapter 08: Real Estate, Mortgages and Property Taxes

> Educational concepts, not investment, tax or legal advice. Rates and rules are snapshots (Italy, 2021-2026, year stated), to be re-checked against the rule in force.

## Core Idea
In this model, a home is a consumption good, a financing decision and an investment at the same time, and the three get confused. The mortgage is a recursion with a payment that brings the balance to zero; the choice between fixed and variable is an option question; buying versus renting is close to a draw once all owner costs are counted; and a let flat yields little net of tax, vacancies and works. Property taxes ("IMU", transfer taxes, "cedolare secca") change the arithmetic but not the structure.

## 8.1 Mortgage mechanics
- **Thesis**: a constant-payment loan: balance grows by interest and falls by payment.
- **Mechanism**: Balance(t+1) = Balance(t) x (1 + monthly rate) - payment. Payment = P x r/(1 - (1 + r)^-n). Three of rate, term, payment, principal determine the fourth. A payment below interest makes the debt grow. By convention Italian mortgages apply the nominal annual rate as nominal/12 per month; (1 + i)^(1/12) - 1 is the correct monthly rate only when the quoted rate is an effective annual rate, so nominal and effective rates must be told apart (verify against the contract). A fixed-principal schedule ("ammortamento all'italiana") has a falling payment but a heavier start; the constant-payment schedule ("ammortamento alla francese") has early payments mostly interest. The split between interest and principal matters to the bank's books and tax deductions, not to the borrower's cash flow, so "prepay early because you only pay interest" is a myth. A check on a quote: the IRR of the loan's cash flows, expressed on the same basis (nominal or effective) as the stated rate, must equal it.
- **Worked example**: 100,000 at 5% with payment 500: with a nominal 5% the monthly rate is 0.4167%, first-month interest about 417, principal about 83 (if 5% were an effective annual rate, the monthly rate would be 0.4074%, interest about 407). 200,000 over 20 years at 4%: 1,212 per month with nominal/12; 1,204 if 4% is read as an effective annual rate.
- **Trade-off**: lower first payment (longer term) versus total interest paid.
- **Does not hold when**: variable rates reset: the bank typically keeps the term and recomputes the payment on the residual balance.

## 8.2 Fixed with portability versus variable
- **Thesis**: a fixed-rate mortgage that can be transferred without penalty is a one-sided option.
- **Mechanism**: if rates rise, the fixed payment is unchanged; if rates fall, you switch to a lower fixed. In Italy the right to transfer a mortgage to another lender ("surroga") is statutory and the new lender bears the practical costs (general knowledge; Italy, snapshot 2026); the new lender may add about 20-30 basis points; small residual balances (below roughly 50,000-60,000) may be refused. Simulations on a long history show variable payments reaching 40-50% above the initial one, while fixed-with-portability rarely exceeds the starting payment. Sustainability means checking the maximum possible payment, not only the average. Rate futures predict poorly beyond a year.
- **Worked example (Italy, snapshot 2024)**: moving from a variable at 4.5% to a fixed at 2.8% saves money even after 0.2-0.3 points of extra spread.
- **Trade-off**: a slightly higher initial fixed rate versus protection and optionality.
- **Does not hold when**: the portability right is removed, the fixed spread is very large (about 2 points), or rates are at zero with easing programmes.

## 8.3 Buying versus renting the home you live in
- **Thesis**: financially close to a draw; the drivers are appreciation, the alternative return and the mortgage rate.
- **Mechanism**: renter pays rent (here about 6% of value, range 4-8%) and earns the after-tax return on the capital not spent. Owner has building costs, periodic renovation (about a third of value every 40 years), transaction taxes and notary fees on each move (amortised), plus the opportunity cost of capital. With a mortgage whose rate is below the investable return, buying wins on numbers; with no mortgage and a 5% net return, renting wins narrowly. A 1% annual appreciation gives +10.5% after 10 years and about x1.49 after 40.
- **Worked example**: 200,000 home, rent 12,000, investment 10,000: renter pays 2,000 more; owner extra costs about 2,800 a year.
- **Trade-off**: mobility and no capital tied up versus freedom to alter the home and security of tenure.
- **Does not hold when**: the renter cannot actually invest the capital productively, or the landlord market is closed to them.

## 8.4 Rental property: from gross to net yield
- **Thesis**: a second home to let usually yields little net of tax, vacancies, management and eventual renovation; headline returns come mostly from appreciation.
- **Mechanism**: purchase costs 6-13% above price (agent, notary, purchase taxes). Gross yield 4-6%. Subtract the flat tax on rent ("cedolare secca": 21%, or 10% for regulated rents; Italy, snapshot 2021-2026), service charges (up to 1-2 months a year plus extraordinary works), property tax ("IMU"), maintenance, vacancies (about 3 months per tenant turnover, tenants staying about 4.5 years), agent fees, legal and administrative time, and a renovation of about a third of value after about 40 years. Net yield ends near 1-3% before appreciation. An IRR must include renovation and extraordinary costs and the dated flows.
- **Sell or hold**: the neutral price is the capital that, in the alternative portfolio, yields the same net income. For a 50/50 mix expected at 8% and 4% (gross 6%) with 26% tax on equities and 12.5% on bonds (blended 20%), net is about 4.8%; net rent 6,710 on a 160,000 flat (4.2%) gives break-even 6,710/0.048 = about 140,000. Taxed distributions raise it (about 156,000); an accumulating fund with gradual drawdown lowers it. Owners tend to overestimate prices.
- **Worked example**: bought for about 23,000 and sold for 100,000 after 23 years is about 6.6% a year on capital; net rent adds about 3.7% on the sale value, but the gain came from two market bubbles.
- **Does not hold when**: appreciation is high, the owner enjoys the work or has expertise, or the purchase is at a deep discount.

## 8.5 Taxes that touch property (structural summary)
| Tax | Concept | Note |
|---|---|---|
| "IMU" | annual municipal tax on property | main home exempt except luxury categories; second homes taxed (general knowledge; Italy, snapshot 2026) |
| Transfer taxes | registration, mortgage and cadastral taxes, or VAT on new builds | reduced treatment for a "first home" ("prima casa") if conditions are met (general knowledge; Italy, snapshot 2026) |
| Flat tax on rent | "cedolare secca" 21% or 10% regulated | alternative to ordinary progressive taxation of rent |
| Capital gain on sale ("plusvalenza") | gain on sale of a property sold within five years of purchase, generally with exemptions for main homes and inherited property | optional substitute tax at 26% through the notary (general knowledge; Italy, snapshot 2026) |
| Mortgage interest deduction | limited credit on interest for the main home | cap and rate change by year (general knowledge) |

Treat every row as a pointer to check, not a ruling (ch12).

## 8.6 Energy-efficiency payback with opportunity cost
- **Thesis**: evaluate an upgrade as two capital paths (with and without), not total savings versus total cost.
- **Mechanism**: start with capital C. Without intervention: C grows at the net return and pays the heating bill (rising with the gas price). With intervention: C minus upfront cost, plus smaller bills, plus tax recovery (10 equal yearly shares, only while there is enough taxable income, zero under flat regimes, starting after payment and invoicing). Break-even is the first year the difference becomes positive. Only the variable part of the bill can be reduced; estimate heating gas as annual use minus summer use x 4. Inflation affects both paths and does not move break-even. The dominant variable is your own consumption; the investment return shifts break-even by only 1-2 years.
- **Worked example**: cost 30,610; saving about 830 a year: simple payback about 36 years; with 5.5% on capital and gas +5.36% a year, break-even about 2064 without tax recovery, about 2050 with 50% recovery; high consumption (about 900 a year) breaks even around 2037 (Italy, snapshot 2026).
- **Does not hold when**: consumption is low, the tax credit is unavailable, or the 60% saving assumption is optimistic (40% is prudent).

## 8.7 Securities-backed credit as an alternative to selling
A credit line against a pledge of securities (typically 50-60% of value) gives liquidity without realising gains; the cost is margin calls (a trigger at 85% of line/collateral means a roughly 29% fall if the line is 60% of value) and overuse. Leveraged, short, commodity and real-estate funds are ineligible; concentrated portfolios lose collateral value.

## Common mistakes
- Mixing nominal and effective rates when computing the monthly rate.
- Reading gross yield as net.
- Treating a mortgage's early interest as "lost money" and prepaying for that reason alone.

## Links
- ch04 reinvestment; ch09 inheritance of property; ch10 flat tax; `economics-finance` ch07 (housing, mortgages as economics).
