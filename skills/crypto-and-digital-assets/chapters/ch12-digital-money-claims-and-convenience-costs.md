# Chapter 12: Digital Money, Claims on Issuers and Convenience Costs

> Educational concepts on what a digital balance is, how digital cash is designed, and what convenience costs. Not advice, not a product comparison and not a forecast. Design choices of public digital currencies are described as options, because several are still being decided; re-check current status.

## Core Idea
In this model, a digital balance is always one of two things: a **claim** on someone (a bank, a payment company, an exchange, a central bank), or **bearer value** that the holder controls with a key. Most confusion about crypto-assets, stablecoins and "digital euro" style projects comes from treating a claim as if it were bearer value, or the reverse. The second idea is that digital cash must solve a copying problem, and the solution has costs in speed, privacy and offline use. The third is that convenience has a price, which shows up as spreads and fees.

## 12.1 Claim on an issuer versus bearer value
- **Thesis**: a balance shown in an app is an entry in someone else's records unless the holder controls the keys that can move it.
- **Mechanism**: three forms recur. (a) A bank deposit is a claim on a licensed bank, often covered by a deposit guarantee scheme up to a limit. (b) An electronic-money or wallet balance is a claim on the issuing company; the company may or may not be a bank, and the guarantee may not apply (check the regime). (c) Bearer value on a ledger is held by whoever controls the signing key; no company stands between the holder and the value, but nobody stands behind it either. A wallet interface on top of a bank account is still form (a) or (b): the interface changes, the claim does not.
- **Trade-off**: claims are reversible, recoverable by identity and protected by regulation; bearer value is final, private and unrecoverable if the key is lost (ch03). Each protection of the first form is a point where the holder depends on someone else's solvency.
- **Does not hold when**: a claim is fully segregated, held at a regulated institution with a guarantee, and redeemable at par on demand; the risk is then small but not zero.

## 12.2 Double spending and why offline digital cash is hard
- **Thesis**: a digital token can be copied. Online systems prevent this by checking a shared record before accepting a payment; offline systems must accept payments without that check.
- **Mechanism**: a public ledger orders transactions with a cost-based rule (ch01, ch02), so a second spend of the same output is visible to all. A payment between two devices with no network cannot consult the ledger, so the payee must rely on secure hardware, limits on amounts, and later reconciliation. Double spending offline can succeed until the records are reconciled, after which the duplicate is detected and the loss falls on whoever accepted the copy or on the issuer, depending on the design (position: prevention by hardware is contested, because hardware can be attacked).
- **Trade-off**: offline use gives payments without connectivity and some privacy; it accepts a bounded fraud loss and requires a dispute process. Online use gives finality and a clear record, and depends on connectivity and on a central checkpoint.
- **Position**: whether a digital currency needs offline payment as a design goal is debated. Proponents see it as parity with cash; critics see it as an unnecessary new risk that a bank-linked online system avoids.
- **Does not hold when**: payments happen only where a connection is always available, in which case the offline problem does not arise.

## 12.3 Money functions and volatility
- **Thesis**: money has three functions: a medium of exchange, a unit of account, and a store of value. An asset can perform one of them well and the others badly.
- **Mechanism**: a unit of account needs a stable reference, because contracts and prices written in it must stay comparable over time. A volatile asset can be used as a medium of exchange by a community that accepts it, but prices expressed in it move with its own volatility, which makes it a poor unit for long contracts. A stablecoin meets the first two functions only as far as its reserves and redemption rights hold (ch07, 7.2).
- **Trade-off**: a volatile asset can serve as a store of value for a holder who accepts the swings, but it fails the unit-of-account test for wages, rents and debts.
- **Does not hold when**: a closed community uses one asset with prices fixed in the same unit for a long period; the stability is then social, not market-based, and it can end abruptly.

## 12.4 Convenience channels and their spreads
- **Thesis**: the spread between buying and selling is the cost of immediacy. Convenience channels charge more of it.
- **Mechanism**: a cash-to-crypto kiosk or an instant-buy feature quotes a price above the market mid for buying and below it for selling. One reported kiosk spread is about 10% (snapshot, re-check). Round-trip loss on a flat market: if you buy at 5% above mid and sell at 5% below mid, one unit costing 1.05 returns 0.95, a loss of about 9.5% before any fee. The loss is incurred on entry and on exit, so a short holding period amplifies it.
- **Trade-off**: a convenience channel saves time and a bank account; it costs the spread every time it is used. A venue with a narrow spread requires more steps and a verified account.
- **Does not hold when**: the channel is the only way to acquire the asset in the holder's situation and the holding period is long enough that the spread is small relative to the expected use.

## 12.5 Central-bank digital currencies and bank-linked wallets (position)
- **Thesis**: a digital currency issued by a central bank is a claim on the central bank, a different instrument from a wallet that holds a bank deposit, even when both look the same on a phone.
- **Mechanism**: design choices include whether the currency works offline, whether holdings are capped, whether it pays interest, whether it can be programmed, and how privacy is handled. Each choice trades off fraud resistance, privacy, bank funding and financial stability. A widely held central-bank currency could reduce deposits at commercial banks, which is one reason some designs cap holdings or keep a bank intermediary (position).
- **Trade-off**: fraud resistance and public access versus privacy and the role of banks. Designs that give the central bank more data reduce privacy; designs that keep banks in the middle preserve deposits but keep the bank-claim structure from 12.1.
- **Position**: whether a tokenised bank deposit is preferable to a central-bank digital currency is contested. The rival views differ on the role of banks and on the risks of a public, programmable money.
- **Does not hold when**: the design is final and its legal status is set; check the official documentation of the issuing institution, since these projects change.

## Common mistakes
- Calling a bank-linked wallet "crypto" and assuming bearer protection.
- Assuming that a digital money is final, private and recoverable at the same time.
- Judging a stablecoin as money without checking the redemption right and the reserves.
- Ignoring the spread of a convenience channel in a short-term plan.
- Assuming offline payments are as safe as online ones.

## Links
- ch01 (ledgers and double spending), ch02 (proof of work and finality), ch03 (keys and recovery), ch05 (claims on venues and counterparty failure), ch07 (stablecoin pegs and redemption); `economics-finance` for central banks, deposits and monetary policy; `personal-finance-italy` for the regulatory treatment of balances in Italy (snapshot, re-check).
