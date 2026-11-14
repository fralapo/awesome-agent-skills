# Chapter 01: What a Blockchain Is, and the UTXO and Account Models

> Educational concepts, not investment, tax or legal advice.

## Core Idea
In this model, a blockchain is a **replicated public ledger whose order of entries is agreed without a central authority**. A digital payment needs three guarantees: the payer owns the coin, the payee can prove receipt, and the coin cannot be spent twice. Copyable data makes the third one hard. A central ledger solves it trivially; a decentralised one needs a consensus rule. Everything else in this skill (custody, fees, privacy, tax) follows from how that rule and the ledger's data model work.

## 1.1 Ownership as a signature
- **Thesis**: ownership of a coin is the ability to produce a valid digital signature, not a name in a database.
- **Mechanism**: a private key signs a transaction; the matching public key verifies it. The address is derived from the public key (one-way derivation). Anyone can check a signature; nobody can forge one without the private key. The ledger is public and every full node holds a copy.
- **Trade-off**: no intermediary can reverse or freeze a transfer, but no one can recover a mistake, a theft or a lost key either.
- **Does not hold when**: the user does not control the keys (custodial setups, ch03 and ch05); then ownership is a claim on a company.

## 1.2 Double spending and why consensus is needed
- **Thesis**: without a coordinator, two conflicting payments broadcast almost simultaneously could split the network into two beliefs.
- **Mechanism**: the system needs one agreed history. In the proof-of-work design (ch02) block production is costly and randomly assigned, so the network converges on one chain; a rational producer extends the longest valid chain because its reward exists only there. Other designs replace cost with locked stake (ch07); they trade a different set of assumptions.
- **Trade-off**: finality is probabilistic. A transaction becomes harder to reverse with each block built on it.
- **Does not hold when**: a coalition controls the majority of the scarce resource (hash power or stake): then history can be rewritten.

## 1.3 Hash functions in one paragraph
A hash function maps any input to a fixed-size number (256 bits in the main design). It is deterministic, changes completely if one character changes, and cannot be inverted in practice. Two consequences matter: (1) a block that commits to the previous block's hash makes any past edit force redoing all later work; (2) you can prove a document existed without revealing it (1.6).

## 1.4 The UTXO model
- **Thesis**: in the UTXO design a balance is not stored anywhere. It is the sum of **unspent transaction outputs** your keys can spend, like banknotes in a wallet.
- **Mechanism**: an output is spent whole. A transaction destroys inputs and creates new outputs: payment plus change (sent to a fresh address); the fee is inputs minus outputs. Worked example: you hold outputs of 7 and 3 and pay 4. You spend the 7, receive 3 back as change, and the network keeps the fee out of the remainder. Because outputs are independent, validation can run in parallel and the audit trail is clean.
- **Trade-off**: simple, auditable validation and good isolation of coins versus awkward user experience (change, many small outputs) and weak privacy (1.7).
- **Does not hold when**: the chain uses accounts instead (1.5).

## 1.5 The account model
- **Thesis**: account-based chains record a **balance per address**, like a bank ledger, and a transaction subtracts from one balance and adds to another.
- **Mechanism**: a per-account counter orders transactions and prevents replay. Programmable contracts (ch07) fit naturally, since contracts hold state and balances.
- **Trade-off**: expressive and compact versus stronger linkage between your payments (one address accumulates a visible history), and more shared state to secure.

| Feature | UTXO model | Account model |
|---|---|---|
| Balance | Sum of unspent outputs | Number stored per address |
| Transaction | Consumes outputs, creates outputs and change | Debits one balance, credits another |
| Replay protection | Outputs spent once | Per-account counter |
| Smart-contract fit | Limited, explicit | Natural |
| Typical privacy lever | Fresh address per receipt, coin control | Fresh account (links remain if funded from one source) |

## 1.6 Timestamping by hash commitment
- **Thesis**: a document can be proven to exist at a date by anchoring its hash, not the document, in a ledger.
- **Mechanism**: compute the file's hash and place it in a data-only output (a non-spendable output carrying a short message). The block time bounds the date within a window of about one block interval. Later, show the file; anyone recomputes the hash and finds it on the ledger. Because hashes cannot be inverted, nobody can fabricate a document matching an earlier hash.
- **Trade-off**: cheap, trust-minimised proof of prior existence versus no proof of authorship, no storage (lose the file, lose the proof), and possibly no acceptance as a certified timestamp in a legal setting.

## 1.7 The mempool, fees and fee replacement
- **Thesis**: confirmation speed is an auction for scarce block space.
- **Mechanism**: unconfirmed transactions sit in the **mempool** and miners pick the most profitable. Fees are quoted per byte of data (satoshi per byte in the main design), independent of the amount sent; a low-fee transaction can wait a long time. A sender may replace an unconfirmed transaction with another spending the same funds at a higher fee ("replace by fee"), and the two sides can keep outbidding until the fee consumes the funds. A **child** transaction with a high fee that spends an unconfirmed parent can pull the parent into a block, because miners evaluate the pair together.
- **Trade-off**: flexible fee market versus unpredictable cost at congestion.
- **Does not hold when**: nodes refuse replacement by policy, which is a node setting rather than a consensus rule (position: some merchants rely on this for zero-confirmation acceptance, and it is not a guarantee).

## 1.8 Privacy and chain analysis
- **Thesis**: the ledger is public, so privacy depends on how the user spends, not on the protocol alone. Addresses are pseudonyms, not anonymity.
- **Mechanism, analyst heuristics**: addresses co-spent as inputs of one transaction probably share an owner (**clustering**); of two outputs, the round-number one is usually the payment and the other the change. Ten withdrawals to a single address expose a growing visible balance; ten addresses give unlinked movements until the funds are merged. Merging many small outputs into one reveals common ownership.
- **Mechanism, defences**: coin control, fresh addresses and not recombining funds; collaborative transactions where several users build one joint transaction (the **anonymity set** is the number of participants you are mixed with). Centralised mixing services add counterparty risk (the operator can simply keep the funds) and may return coins that exchanges treat as tainted.
- **Trade-off**: more privacy costs effort, fees and sometimes legal friction with regulated venues.
- **Does not hold when**: you buy through a venue that records your identity; the link between identity and first address already exists off-chain.

## Common mistakes
- Treating an address as anonymous.
- Saying "the coins are in my wallet": the coins are on the ledger; the wallet holds keys.
- Assuming a fee depends on the amount sent.
- Confusing "no central operator" with "no operational risk".

## Links
- ch02 consensus economics and issuance; ch03 keys; ch04 off-chain payments; ch07 contracts and stake; ch10 phishing and address tampering.
