# Chapter 04: Payment Channels, Lightning and Payments

> Educational concepts, not investment, tax or legal advice.

## Core Idea
In this model, most payments need not touch the base ledger. Two parties can **net payments off-chain and settle once**, and a network of such channels can route payments between strangers. This lowers cost and latency for small payments, at the price of liveness, liquidity and backup requirements. On-chain fees depend on data size and congestion, not on the amount sent (ch01), which makes small payments uneconomical on the base layer.

## 4.1 Why small on-chain payments fail
A 3-unit-currency ice cream paid on-chain can cost around two units in fees if the network is congested; fees are an auction for limited block space. The cost is nearly irrelevant for a large settlement and prohibitive for a coffee. That asymmetry is the economic reason for a second layer.

## 4.2 A channel in four steps
- **Thesis**: a channel is a shared balance that two parties update by exchanging signed states.
- **Mechanism**: (1) fund a 2-of-2 multisig address on-chain. (2) *Before* broadcasting the funding transaction, both sign, without publishing, a **refund transaction** returning each party's share. Decide how to close before you open. (3) Each payment creates a new signed state with new balances. (4) Either party can close by publishing the latest state, or both can close cooperatively.
- **Trade-off**: instant payments with negligible fees versus capital locked in the channel.
- **Does not hold when**: the counterparty is unresponsive and the chain is congested at closing time.

## 4.3 Why an old state cannot be used (revocation)
- **Thesis**: every state is replaced by a newer one, and publishing a superseded state must be punishable.
- **Mechanism**: each state's closing transaction **delays the publisher's own funds** (for example by 24 hours) and lets the counterparty sweep everything if they know a per-state secret. On each update both parties reveal the previous secret. Worked example: balances 5-5, then 4-6, then 3-7. If the party at 3 publishes the old 5-5 state, the other has the secret for that state and takes all funds within the delay.
- **Trade-off**: security requires **watching the chain** during the delay window, or delegating that watch.
- **Does not hold when**: the user is offline longer than the delay and no watcher exists.

## 4.4 Routing across several hops
- **Thesis**: a payment between two people with no direct channel can pass through intermediaries without trusting them.
- **Mechanism**: the recipient picks a secret R and shares only its hash H. The payer offers the first hop a conditional payment: "pay if R is revealed, otherwise refund after 2 hours". That hop offers the next the same with a 1-hour deadline. The recipient reveals R to claim, each hop reuses R to claim from the previous one, and all balances update without any on-chain transaction. **Deadlines must decrease along the path** so each intermediary has time to collect upstream after learning R. If someone is offline, the payment simply reverts. Worked example: payer-hub channel 5-5 and hub-recipient 2-6; a payment of 1 gives 4-6 and 1-7; the hub's total is unchanged, and it may earn a small fee.
- **Trade-off**: trust-free routing versus failed payments when liquidity on a path is one-sided.
- **Does not hold when**: the amount exceeds the weakest channel's capacity in the needed direction.

## 4.5 Fees, units and the units arithmetic
Routing fees are a few **satoshi** (1 satoshi = 1/100,000,000 of the main unit). Fee in local currency = satoshi / 100,000,000 x price per whole unit. Worked example: 14 satoshi at a price of 27,000 per unit is about 0.0038, against about 2.17 on-chain for the ice-cream case. Fees rise with the number of hops; intermediaries compete, which keeps them low. A merchant interface that mistakenly offers the on-chain option instead of the channel option produces high fees.

## 4.6 Custodial and non-custodial front ends
- **Mechanism**: a **custodial** wallet gives instant onboarding and no channel management, but the provider holds the keys (ch03). A **non-custodial** wallet gives you the keys but needs channel funding, inbound liquidity and a plan for backups.
- **Trade-off**: convenience versus control; both can be right for small amounts.
- **Does not hold when**: the amounts are large; then fees on-chain are negligible compared with the size, and on-chain settlement is the simpler choice.

## 4.7 Backups and the danger of an outdated state
An outdated backup restored by mistake is **treated as fraud** by the protocol, because it re-publishes an old state. The rule: back up the **latest** state, or use a design where the watcher or the provider holds a consistent copy. This is why restoring a channel wallet from a three-month-old file is far riskier than restoring an on-chain wallet from its phrase.

## 4.8 Comparing payment rails
| Rail | Reversibility | Typical fee | Speed | Main risk |
|---|---|---|---|---|
| Card payment | Chargeback possible | Percentage borne by merchant | Seconds | Card fraud, account suspension |
| Bank transfer | Recall in limited cases | Low or none | Seconds to days | Misdirected payments |
| On-chain transfer | None after confirmations | Per byte, variable | Minutes to hours | Wrong address or network |
| Channel payment | None after settlement | A few satoshi | Seconds | Liquidity, liveness, backups |

## 4.9 Merchant and consumer perspective
For a merchant, a channel payment settles into the merchant's channel balance and must eventually be moved on-chain or to a provider; accounting treats each as a receipt at a value on that date (ch09). For a consumer, the practical limits are channel capacity, route availability and the need for the wallet to be online at the time of receipt in some designs.

## Common mistakes
- Opening a channel without deciding how to close it.
- Restoring an old backup.
- Assuming a failed payment loses money: it simply reverts.
- Confusing a custodial "lightning" account with a self-held channel.

## Links
- ch01 fees and multisig; ch03 custody; ch09 tax record-keeping; ch10 address and invoice scams.
