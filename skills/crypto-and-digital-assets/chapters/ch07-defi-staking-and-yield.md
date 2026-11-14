# Chapter 07: DeFi, Staking, Stablecoins and Yield (Risks)

> Educational concepts, not investment, tax or legal advice.

## Core Idea
In this model, decentralised finance replaces intermediaries with **programs that execute rules automatically**. That removes some counterparties and adds others: code bugs, oracle errors, bridge failures, governance attacks and the incentive design itself. A high advertised yield compensates for real, often hidden, risks; this chapter lists the mechanisms and what each risk is.

## 7.1 Smart contracts
- **Thesis**: a contract is code on the ledger that executes conditions without a trusted party.
- **Mechanism**: example: an insurance contract pays the passenger if the flight is cancelled and pays the airline if it lands. Contracts are **immutable** once deployed (or upgradable through a key held by someone, which is a trust assumption).
- **Trade-off**: no counterparty to trust versus bugs that cannot be fixed and can lock or leak funds.
- **Does not hold when**: contracts are audited, minimal and battle-tested, which reduces but does not remove risk.

## 7.2 Stablecoin peg mechanisms
- **Thesis**: a peg is only as good as its redemption or arbitrage mechanism.
- **Mechanism**: (1) **Issuer-backed**: the issuer promises 1:1 conversion into the reference currency; it works while reserves exist and are liquid; opacity of reserves is the main risk and the issuer can freeze addresses. (2) **Reserve-transparent** versions of the same. (3) **Over-collateralised on-chain**: each unit is backed by more than one unit of volatile crypto locked in a contract; hard to censor but correlated with the crypto market. (4) **Algorithmic**: a protocol mints or burns a sister token at a fixed rate to the peg. If the stablecoin trades at 0.90, buy it, convert it into one unit of sister token, sell the sister token: stablecoin supply shrinks and its price rises; volatility is exported to the sister token.
- **Trade-off**: capital efficiency versus fragility.
- **Does not hold when**: the sister token falls faster than arbitrageurs can sell it: the arbitrage turns loss-making, sister-token issuance explodes, and the structure collapses. This **death spiral** was seen in 2022, amplified by demand propped up by unsustainable yields.

## 7.3 Automated market makers and slippage
- **Thesis**: a pool and a pricing formula replace an order book.
- **Mechanism**: a pool holds two assets; the price follows from keeping the pool balanced after each trade. The simplest rule is the constant product x * y = k, where x and y are the two reserves and k stays fixed across trades (fees aside). Worked example: a pool of 100 units of asset A and 100,000 stable units gives k = 10,000,000 and a price of 1,000. Buying 10 units of A leaves 90 A, so the stable reserve must become 10,000,000 / 90 = 111,111; the buyer pays 11,111 (average price about 1,111) and the price at the end of the trade is 111,111 / 90 = about 1,235. The larger the trade relative to the pool, the worse the execution (**slippage**). Aggregators route across venues.
- **Trade-off**: always-on liquidity and no account versus slippage, fees and exposure to smart-contract bugs.
- **Does not hold when**: pools are thin; the quoted price then misleads.

## 7.4 Over-collateralised lending and liquidation
- **Thesis**: on-chain loans trade a safety margin for automation: no credit check, no humans, and no warning.
- **Mechanism**: deposit collateral, borrow up to a loan-to-value (LTV) share (1 unit worth 40,000 supports 30,000 at 75%). When debt over collateral crosses the liquidation threshold (typically 75 to 85%) anyone may repay part of the debt at a discount (5 to 10%) and seize collateral. **Liquidation price = loan / (collateral quantity x threshold).** Worked example: 0.74 units of collateral (about 1,942 per unit), a loan of 988 and an 85% threshold: liquidation at 988 / (0.74 x 0.85) = about 1,571 per unit, a drop of about 19% from 1,942. Interest raises the debt, so the liquidation price drifts upward. Rates rise steeply above roughly 80% pool utilisation. Protocol token rewards can make borrowing cost negative.
- **Trade-off**: liquidity without selling versus forced selling at the worst moment.
- **Does not hold when**: collateral is stable and the loan small, or the borrower monitors and tops up.

## 7.5 Yield farming: APR, APY, impermanent loss
- **Thesis**: high advertised yields compensate for real risks.
- **Mechanism**: liquidity providers deposit two tokens 50/50, receive a receipt token, and earn swap fees plus incentive tokens. **APR** is simple annual; **APY** includes reinvestment: an APR of 52% compounded monthly is about 67% APY, daily about 69%; compounding matters hugely for triple-digit rates and little at 20%. Each harvest costs fees, so there is an optimal frequency; aggregators batch it. **Impermanent loss**: if the two tokens' prices diverge, the pool position is worth less than holding them separately.
- **Further risks**: bugs in contracts and aggregators, bridge failure, unlimited token approvals, phishing sites (the dominant loss cause), incentive tokens that tend to lose value as everyone sells.
- **Does not hold when**: yields come from sustainable fees rather than printed incentives; risk is then lower but so is the rate.

## 7.6 Staking
- **Thesis**: in proof-of-stake systems, validators lock capital as the security budget and earn rewards.
- **Mechanism**: rewards come from new issuance and fees. Penalties (**slashing**) destroy part of the stake for misbehaviour or downtime. **Liquid staking** issues a receipt token that can be traded while the stake is locked; it adds smart-contract and de-peg risk. **Delegation** gives a validator control of the stake's voting, not its custody, in most designs, but terms vary.
- **Trade-off**: yield and network participation versus lock-up, slashing and extra layers.
- **Does not hold when**: staking is offered by a custodian that pools your assets; then ch05 counterparty risk applies.

## 7.7 Tokens, NFTs and the question of ownership
A contract maps a token ID to an owner. The image associated with a collectible is usually **referenced**, not stored, and anyone can copy it. Owning the token confers no copyright unless a licence says so. Collectibles form their own bucket in tax terms (ch09).

## 7.8 Intermediated yield (crypto lenders)
An intermediary paying 8 to 10% is not a fixed-income issuer; it invests clients' money in the same strategies the client could access directly. Client risk is **strategy risk plus intermediary risk**. See ch05, case card B.

## 7.9 Risk map
| Risk | Where it arises |
|---|---|
| Smart-contract bug | Any contract |
| Oracle failure | Lending, derivatives |
| Bridge exploit | Cross-chain transfers |
| Governance attack | Voting by token holders |
| Liquidation cascade | Lending in a fall |
| De-peg | Stablecoin or liquid staking token |
| Phishing, malicious approval | Wallet interactions |
| Regulatory | Everything |

## Common mistakes
- Reading APY as guaranteed.
- Granting unlimited token approvals.
- Ignoring that borrowing against a volatile asset can force a sale at lows.
- Treating a receipt token as the underlying.

## Links
- ch01 account model; ch05 counterparty cases; ch08 leverage and hedging statistics; ch10 phishing.
