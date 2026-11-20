# Chapter 15: Money Forms, Payments and Central Bank Digital Currency

> Educational reading guide, not advice. Designs and project status of specific digital currencies change; check the central bank's and the legislators' current publications before quoting any status.

## Core Idea
In this model, money is a set of claims with a named issuer, a redemption promise and a way of transferring it. Digital money changes the transfer layer and sometimes the issuer. The useful questions are: who issues the claim; who can refuse or delay a transfer; who earns fees on the rails; and what happens to bank funding if a new claim is easier to hold than a bank deposit. Chapter 01 covers how bank deposits are created; chapter 02 covers reserves and central bank tools.

## 15.1 Forms of money and their issuers
- **Thesis**: money in use is mostly bank deposits, which banks create when they lend (ch01). Cash is a central bank liability. Privately issued tokens are a third form, and their safety depends on what backs them.
- **Mechanism**: cash pays no interest and does not record who holds it. A bank deposit is a bank liability, usually insured up to a limit in many systems and convertible to cash at par. Reserves are deposits held at the central bank and used to settle between banks. Electronic money from non-banks is redeemable at par into bank money, and its safety depends on the backing and the redemption rules. A privately issued token (a stablecoin) is safe only as far as its reserves are liquid, valued correctly and redeemable on demand. Technology and custody of tokens are covered by `crypto-and-digital-assets`.
- **Trade-off**: each form trades safety, interest, anonymity, convenience and reach differently.
- **Does not hold when**: a form is fully backed, redeemable on demand and its reserves are transparent and audited.

## 15.2 Payment networks and market power
- **Thesis**: payments are a network business. Network effects concentrate rails in a few providers, and fees follow concentration.
- **Mechanism**: a payment method is valuable when many merchants accept it and many users hold it (two-sided network effects). An incumbent with both sides is hard to challenge, and a newcomer faces a chicken-and-egg problem. Schemes charge interchange and network fees, which merchants usually pass into prices. Dependence on a few private circuits, or on providers outside the country, can give those providers control over a domestic flow of payments (position on how much this matters).
- **Trade-off**: scale lowers unit costs and improves reliability; it also concentrates pricing power and dependence.
- **Counter-view**: concentration can be contestable when rails interoperate and switching is cheap. The usual remedies are fee caps and interoperability mandates, each with its own costs.
- **Does not hold when**: several rails are interoperable and switching costs are low.

## 15.3 Cash: independence, privacy and social cost
- **Thesis**: cash is the only money that needs no intermediary and leaves no record. That is a benefit to the holder and a cost to the public.
- **Mechanism**: cash keeps payments possible without a bank account and without a payment provider. It also supports informal and illegal activity, and handling it costs the economy (printing, storage, security, collection). A decline of cash moves control of payments to whoever runs the rails.
- **Trade-off**: privacy for users against traceability for enforcement, and the handling costs of cash against the dependence on providers.
- **Position**: some argue that a digital instrument that behaves like cash, introduced gradually and without dominant intermediaries, could keep independence while cutting handling costs. Others argue that privacy can be given by account-based systems with safeguards, or that cash should be kept as a backstop for outages. Both are positions.
- **Does not hold when**: there is no practical alternative to cash for people without bank access, or the cash system is already cheap and reliable.

## 15.4 Central bank digital currency: design choices
- **Thesis**: a central bank digital currency (CBDC) is a central bank liability in digital form. Its design decides its effects on banks, privacy and policy.
- **Mechanism** (general knowledge; the design options are the main content, not any project's status):
  - *Retail or wholesale*: retail is held by the public; wholesale is held by banks and used for settlement, as reserves are now.
  - *Account-based or bearer-like*: an account ties units to an identified holder; a bearer-like instrument transfers value without identifying the payer.
  - *Online or offline*: offline transfers need no connection but raise counterfeiting and privacy questions.
  - *Holding limits*: a cap on balances limits the scope for deposits to move to the central bank; it also limits usefulness.
  - *Remuneration*: a zero rate makes the CBDC cash-like; a positive rate makes it an attractive place to hold savings.
  - *Operation*: the central bank can run the ledger itself or use private providers for access and service, which keeps some competition and adds dependence.
- **Trade-off**: the more attractive a retail CBDC is as a store of value, the more it can draw deposits away from banks. The more it is restricted, the less it competes with private money.
- **Does not hold when**: the central bank offers no retail accounts and the design is limited to wholesale settlement.

## 15.5 Deposit flight and bank funding
- **Thesis**: a risk-free store of value that is easy to use can pull deposits out of banks during stress, which changes the speed and channel of a bank run (ch06).
- **Mechanism**: a deposit is cheap and sticky funding for a bank. If holders can move money into a central bank claim quickly, the stickiness falls. Banks can respond by paying higher deposit rates, holding more liquidity or borrowing from the central bank, and each response changes lending. Holding limits, remuneration and transfer rules shape the size of the effect. The scale of the effect is contested; the design features are meant to limit it.
- **Trade-off**: a safe public alternative supports confidence in a crisis, and it adds a channel through which a run can happen.
- **Does not hold when**: the design keeps holdings small and remuneration low, so that the central bank claim works as a means of payment rather than a savings product.

## 15.6 Motives and their trade-offs (position)
- **Thesis**: proposals for digital money are justified by several motives that pull in different directions.
- **Mechanism**: motives typically include a public alternative to private rails, resilience to outages, access for people without bank accounts, and the transmission of policy. Some proposals also state a capital-markets aim, such as moving savings from current accounts into investment; that aim is contested. Privacy and surveillance concerns arise with account-based designs, and programmable payments (conditional or time-limited money) can be a benefit or a tool of control, depending on rules.
- **Trade-off**: each motive adds a constraint (holding limits, privacy safeguards, interoperability), and the constraints weaken the others.
- **Counter-view**: critics ask whether the stated problem is one a new currency solves, and whether private and public solutions could be combined more cheaply.
- **Does not hold when**: each motive is named, costed and tested against its own evidence.

## 15.7 Checklist for reading a proposal
1. Which problem is named, and is it the main one?
2. Who issues the claim, and who runs the ledger and collects fees?
3. Retail or wholesale; account-based or bearer-like; online or offline?
4. What are the holding limits and the remuneration?
5. What happens to bank deposits and bank lending in a stress?
6. What are the privacy and data rules, and who can see the transfers?
7. How do people without bank accounts or devices get access?
8. What is the status of the project today, and what would change it?

## Common mistakes
- Treating a stablecoin, a CBDC and a bank deposit as equivalent because all are "digital money".
- Assuming a CBDC creates money for households in the same way as QE (ch02 explains that QE buys assets).
- Judging a retail design without its effect on bank funding.
- Judging payment fees without looking at market structure.
- Stating a project's status from an old article.

## Links
ch01 (money and banks), ch02 (reserves, QE, central bank tools), ch06 (bank runs and deposit flight), ch10 (market power and monopoly), ch14 (money-market rates and the policy path). `crypto-and-digital-assets` for token technology and custody; `investing-and-financial-history` ch10 for fraud signs in payment and yield products; `personal-finance-italy` for one country's payment products.
