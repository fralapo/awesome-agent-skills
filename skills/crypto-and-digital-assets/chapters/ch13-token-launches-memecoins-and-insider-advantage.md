# Chapter 13: Token Launches, Memecoins and Insider Advantage

> Educational concepts on how newly issued tokens are controlled and traded, and on the patterns through which early holders gain at the expense of later buyers. Not advice, not a list of tokens and not an accusation against any project. Checks are prompts for verification, not proof of fraud.

## Core Idea
In this model, most newly launched tokens are first a set of contracts and pools, and only second an asset. Who can create supply, who controls the trading pool, who gets the first trades, and what fees run on each transfer determine who gains and who pays before any question of value arises. A token's displayed market value (price times total supply) is a number that only means something when the pool is deep and the supply is actually sellable. Memecoins compress these mechanics into one product, so they are the clearest place to see them.

## 13.1 Who controls supply
- **Thesis**: a token whose issuer can create more units can be diluted at will, whatever its story.
- **Mechanism**: token contracts may include a mint function (create units), a freeze or blacklist function (block addresses), an administrative key that can change the contract, or a fee setting that the owner can raise. Each is a control that the holder cannot see without reading the contract or the chain state. A mint right that is revoked is a fixed supply; one that is kept allows unlimited dilution, so market value can rise and then be diluted to nothing.
- **Trade-off**: some controls are legitimate (regulated stablecoins need freeze functions to comply with sanctions law); the point is to know which controls exist and who holds them.
- **Does not hold when**: the contract is verified, has no retained admin rights, and its supply is fixed; even then the other mechanics below still apply.

## 13.2 Liquidity pools, market cap and the exit
- **Thesis**: a token's displayed value assumes that its supply can be sold at the displayed price, which is true only if the pool behind the price is deep enough.
- **Mechanism**: a new token is usually paired with a base asset in a pool, with a formula that sets the price (ch07, 7.3). Whoever holds the pool's liquidity-provider tokens can withdraw the base asset, which leaves the remaining holders with tokens they cannot sell at the quoted price. Illustration: a pool holding 10 units of base asset and 10,000 tokens; a holder who controls the pool and withdraws the base asset leaves a price that no outside buyer will pay for the remaining supply. The displayed market value (price times total supply) can be large while the depth actually available is small.
- **Trade-off**: a shallow pool has low costs to launch and high price swings; a deep pool needs real capital and a locked liquidity commitment, which can be verified.
- **Does not hold when**: liquidity is held by independent providers under locks that can be read on chain, and the pool depth is large relative to the holdings.

## 13.3 Insider and sniper advantage at launch
- **Thesis**: the first trades after a listing are often executed by participants who acted before the public, so later buyers buy near the top.
- **Mechanism**: automated bots (sometimes called snipers) buy in the first blocks after a pool opens, and insiders can buy before public trading if they know the launch time. Their purchases push the price up, which attracts later buyers. Creator fees (royalties on each trade, set in the contract) pay the issuer on every transaction whether the buyer gains or not. Illustration: a 5% fee on each side of a trade costs about 9.75% on a round trip at a flat price, since 0.95 x 0.95 = 0.9025.
- **Trade-off**: the advantage is structural and does not require any news; the only protection is to be the one who checks the first trades, or to avoid the early market.
- **Position**: whether launch-stage bots are a fair part of market-making or extraction is contested. The rival view is that they transfer value from retail buyers without providing liquidity that persists.
- **Does not hold when**: the launch is fair (no pre-sale, no pre-listing purchases, a fixed and public start time), and the fee is low and disclosed.

## 13.4 Concentration and unlock schedules
- **Thesis**: a few wallets holding most of the supply can sell at once and move the price; scheduled unlocks create known supply shocks.
- **Mechanism**: check the share of supply held by the largest addresses (ignoring exchange and pool addresses, which hold on behalf of many) and whether the rest is locked by a contract with a stated release schedule. An unlock that releases a large share after a short period can coincide with a price drop, which is a mechanical effect of new supply, not a forecast.
- **Trade-off**: vesting aligns insiders with the long run only if the schedule is long and enforced by code; a schedule enforced by promise is a claim.
- **Does not hold when**: the supply is distributed widely and the largest holders are known to be independent; concentration then matters less.

## 13.5 The pump, promotion and exit pattern
- **Thesis**: a token promoted through many accounts at once, with rising price and falling liquidity, shows a pattern in which early holders sell into demand created by later buyers.
- **Mechanism**: promotion from many sources (paid posts, fake endorsements, AI-generated or celebrity-linked material, referral groups) creates buying pressure. Insiders and early wallets sell into that pressure; the price falls when demand stops. Prominent-person tokens add a verification problem: any name or image can be used without consent (ch10, 10.3). Warning signs include a sudden surge in unknown accounts, a rapid change of contract owner, and promotional deadlines.
- **Trade-off**: a promotion can be real and still end badly; a pattern is a risk indicator, not a proof of intent.
- **Does not hold when**: the asset is traded on a deep, regulated venue, with independent liquidity and no concentrated supply.

## 13.6 Launch checklist
1. Is the contract verified, and are mint, freeze and fee controls present, revoked or held by whom?
2. Who created the pool, what is its depth in base-asset units, and who holds its liquidity tokens and whether they are locked?
3. Were any wallets funded or bought before public trading? Check the first blocks of activity.
4. What fees apply to each transfer, and who receives them?
5. What share of supply is held by the largest independent addresses, and what is the unlock schedule?
6. Is the displayed market value backed by sellable depth at the displayed price?
7. Who is named in the promotion, and has that person confirmed through a channel you opened (ch10, 10.3)?
8. What would the position's total loss be, and is it inside the loss budget (ch11, 11.9)?

## Common mistakes
- Reading the displayed market value as a value that could be realised.
- Treating a fast price rise on a shallow pool as demand.
- Ignoring creator fees because they are small per trade; they compound over the round trip.
- Buying after promotion has already moved the price.
- Assuming a verified contract means a fair launch.

## Links
- ch01 (ledgers), ch03 (keys and wallets), ch07 (AMMs, pools and slippage), ch08 (weak tests and drawdown), ch10 (scams, impersonation and verification), ch11 (derivatives, flows and loss budget); `trading-methods-and-technical-analysis` ch10 (how a product's death event is found) and ch12 (liquidity and thin books).
