# Chapter 17: Economics of AI, Capex, Pricing and Bubble Tests

## Core Idea
Model quality is only half of the AI story. The other half is money: who pays for compute, how fast the bill comes due, what a user costs to serve, and what a price has to be true about the future to be justified. This chapter gives accounting and market mechanisms for reasoning about those questions and tests for claims about a "bubble". It is not investment advice. Figures in the sources behind this material are reported, dated and often unverified, so the chapter gives shapes and checks, not numbers. Per-agent token budgeting is covered in ch15 (15.19); open-weight definitions are covered in ch08 (8.9).

## 17.1 Cash flow is not profit
- **Thesis**: a company can report growing profit while its cash shrinks, because the heavy spending on data centres and chips is paid now and recorded over years.
- **Mechanism**: capital expenditure on hardware is an asset on the balance sheet; its cost reaches the income statement slowly through depreciation. Revenue and profit can look healthy while the cash spent on buildings and accelerators exceeds the cash coming in. Reading only one statement hides this. The depreciation schedule itself is an assumption: if the useful life of hardware is shorter than assumed, reported profit is overstated.
- **Practice**: read the income statement, the balance sheet and the cash-flow statement together; compare capital spending with operating cash flow over several periods; check the depreciation period and any change to it.
- **Trade-off**: heavy investment can be the correct strategy in a race; the question is whether it earns a return before the money runs out.
- **Does not hold when**: spending is funded from operating cash and the investment is small relative to income.

## 17.2 Commitments can sit outside the headline debt (hypothesis to check)
- **Thesis**: obligations to lease capacity, to purchase future compute or to finance facilities through partner entities may not appear as debt in the headline figures.
- **Mechanism**: lease liabilities, purchase commitments and special-purpose vehicles can be disclosed in notes rather than shown as borrowings. Their size is therefore a matter for the disclosure section, not the summary.
- **Practice**: read the notes on commitments and off-balance-sheet arrangements before comparing leverage across companies. Whether a particular company has a particular exposure is a factual question to check in filings, not a claim this chapter makes.
- **Trade-off**: none of this implies misconduct; disclosure rules allow many arrangements.
- **Does not hold when**: the company has no such arrangements, which the notes will show.

## 17.3 Unit economics: cost per user and per heavy user
- **Thesis**: the margin of an AI product depends on what one user costs to serve, and that cost is very uneven across users.
- **Mechanism**: each request consumes compute roughly in proportion to the amount of text read and generated, and agentic or reasoning workloads can consume far more per task. A flat subscription that suits average users can lose money on heavy users. The usual responses are usage limits, tiers, cheaper default models, or advertising. Each response changes the product the user actually gets.
- **Practice**: estimate the cost of a typical request and of a heavy user's month; compare with the price paid; look for how the provider limits usage.
- **Trade-off**: limits frustrate power users; flat pricing attracts users who may not be profitable.
- **Does not hold when**: the cost per unit of output falls faster than usage grows. This is the Jevons-style case discussed in ch15 (15.19): cheaper use can increase total consumption, so falling unit prices do not guarantee falling bills.

## 17.4 Launch pricing and dependence (position)
- **Thesis (position)**: a service can be priced below its cost to win users, and the price can rise once users depend on it and switching costs are high.
- **Mechanism**: subsidised prices work as customer acquisition. Dependence is built through habit, saved data, integrations and the disappearance of alternatives. When the price changes, the users who remain are those who could not easily leave, so the price rise is less sensitive than the price cut.
- **Trade-off**: subsidised prices widen access; they also make later increases look like a betrayal and can damage trust.
- **Does not hold when**: switching costs are low (open formats, portable data, interchangeable services), in which case price rises are constrained by competition.

## 17.5 Cheaper inference is not the same as cheap business
- **Thesis**: the cost of running a model for one request can fall while the cost of the business rises, because it includes training, research and competing with better-funded rivals.
- **Mechanism**: training a frontier model is a large fixed cost, spread over users only if usage and prices hold. Inference cost per token depends on hardware, model size and optimisation; these improve, but competitors also improve and lower the price users will pay.
- **Practice**: separate three costs: running one request, training the next model, and acquiring users. A business case that assumes only the first is falling is incomplete.
- **Trade-off**: fixed training costs can be a moat; they also make the business sensitive to a few large customers and to the timing of releases.
- **Does not hold when**: the provider sells capacity to customers who pay for it in advance, which shifts the risk to them.

## 17.6 Monetisation: subscription, advertising and commerce
- **Thesis**: an AI assistant that answers in text can be paid by subscription, by advertising, or by recommending products. Each changes the incentives of the answer.
- **Mechanism**: advertising inside an answer is harder to notice and to block than a separate banner. Disclosure rules and labelling are the main defence. When a summary answers the question, fewer users click through to the sources, which affects the publishers who relied on those clicks. Recommendation revenue (commissions, affiliate links) creates a conflict between the recommendation and the user's interest.
- **Practice**: ask what the business earns from each answer and whether the answer is labelled; compare the answer with a source that has no commercial link.
- **Trade-off**: advertising can keep a service free; subscriptions can make the service accountable to users. Neither removes the need to check claims.
- **Does not hold when**: the service is run by a public or non-profit body with a clear mandate; then the incentive question changes shape but does not disappear.

## 17.7 Who runs the models you depend on (open weights and the cost of running)
- **Thesis**: open weights reduce dependence on one provider only if you can afford to run them and you know how they were configured.
- **Mechanism**: fine-tuning a released model costs far less than training one from scratch, but hosting a large model still needs substantial memory and hardware. Quantisation reduces memory and can degrade smaller models more than larger ones. An implementation that differs from the reference setup (tokeniser, prompt format, sampling) can lower measured quality well below the published figure, so a benchmark on your own setup is the right test.
- **Practice**: measure quality and cost on your own tasks before choosing a host; keep the exact configuration with the results; compare hosted and local runs on the same tasks.
- **Trade-off**: local running gives control of data and cost at the price of hardware, maintenance and a slower path to new capabilities.
- **Does not hold when**: the workload is small or occasional; a hosted API is usually cheaper to operate.

## 17.8 Gatekeeping and concentration
- **Thesis**: when a few assistants mediate access to information, a few providers decide what appears first, which is the same concentration pattern seen in search ranking.
- **Mechanism**: a single assistant that summarises the web or recommends products shapes what users see without showing the ranking, so the criteria are hard to audit. Walled ecosystems that keep data inside one platform add switching costs. Open protocols that let data and identity move between services are one counterweight; their adoption is itself an economic question.
- **Trade-off**: a single well-run assistant can be simpler for users than many services; that simplicity is paid for in dependence.
- **Does not hold when**: many providers compete on the same data and users can switch in minutes.

## 17.9 Bubble tests: when is a price not justified?
- **Thesis**: a market price is in a bubble when it cannot be explained by any reasonable future outcome. Innovation can be real and prices can still be unjustified, so the two claims must be tested separately.
- **Mechanism**: the definition is a common one in market practice, not a formal theorem. Tests that make the claim checkable:
  1. **Revenue against capital**: is recognised revenue growing fast enough to pay for the spending within a stated period?
  2. **Margins at scale**: do margins improve as usage grows, or do heavy users make them worse?
  3. **Cost per useful output against price**: is the cost of a finished, useful unit falling faster than the price charged?
  4. **Substitutes**: if a free or cheap substitute matches the paid product, what happens to the price?
  5. **Price after dependence**: what do customers do if prices double?
  6. **Falsifiers**: what observable result would show the thesis wrong, and by when?
- **Evidence**: a reasoning checklist; no historical base rate is claimed here.
- **Trade-off**: the tests are slow and depend on disclosures; timing of a correction is not predictable from them.
- **Does not hold when**: the company is private and discloses nothing; then the uncertainty itself is the finding, and claims should be stated as unverifiable rather than as settled.

## 17.10 Energy and waste claims (position)
- **Thesis (position)**: claims that AI wastes energy need a per-task measure before they can be compared with alternatives.
- **Mechanism**: energy per answer depends on model size, hardware, batch size and the length of reasoning. A total figure for a data centre hides how much of the load is useful work and how much is training. The right comparison is energy per completed task against the same task done another way.
- **Trade-off**: per-task measures are harder to obtain and can be gamed by choosing favourable tasks.
- **Does not hold when**: the question is only about aggregate national demand, where totals are the right measure.

## Stay in lane
This chapter does not recommend investments, values companies or forecast prices or timing. Figures reported in the source material are not reproduced because they are unverified snapshots. Use filings and primary data before relying on any number.

## Cross-references
- ch08 (8.9) for open weights and open data; ch08 (8.18) for verifiability and where capability grows.
- ch15 (15.19) for token economics inside agents.
- `economics-finance` and `investing-and-financial-history` for general finance and market history.
- `scientific-thinking` for how to test a causal or market claim.
