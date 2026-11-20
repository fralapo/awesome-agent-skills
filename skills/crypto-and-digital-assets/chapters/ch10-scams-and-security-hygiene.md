# Chapter 10: Scams and Security Hygiene

> Educational concepts, not investment, tax or legal advice.

## Core Idea
In this model, most losses in digital assets are **not technical hacks of the protocol but social engineering and operational errors**. Because transfers are irreversible (ch01), a scammer only needs one successful instruction from the victim. Scams share a small set of mechanics: unsolicited contact, urgency, irreversible payment and escalating fees. Cheap, mechanical checks defeat most of them.

## 10.1 Irreversibility changes the game
Card payments and bank transfers can be disputed or recalled in some cases; a confirmed on-chain transfer cannot. This is why custody and fraud risk dominate price risk for beginners. A new withdrawal address that waits 24 hours at serious venues gives time to cancel a scam (ch03).

## 10.2 Anatomy of a financial scam
- **Thesis**: scams run on a pipeline: contact, trust, small gain shown, escalating deposits, blocked exit, fees to release, recovery scam.
- **Mechanism**: a fake endorsement (cloned profile, deepfaked advertisement, group chat) leads to a platform showing invented gains; withdrawals require "tax" or "fee" payments that grow (100, 200, 50...) until the victim stops. **Sunk-cost thinking** makes victims pay one more fee, and loss-chasing makes them seek risky recovery. Poorly written mass emails select naive targets on purpose, because the victims who respond are those who are cheapest to convert. Later waves target the same victim: recovery services asking advance fees, tax release, customs release. Romance scams invest months because attacker time is cheap.
- **Worked example**: a "tax release" asks 20% of 3,000 = 600 before paying out. Genuine withholding is deducted from payment, never prepaid.
- **Does not hold when**: contact was initiated by you with an authorised intermediary.

## 10.3 Impersonation and deepfakes
- **Thesis**: a face, voice, verified badge or professional-looking page is no longer evidence of identity.
- **Mechanism**: cloned social profiles of known figures, synthetic voice and face in live calls, fake support accounts that reply to public complaints, spoofed caller identity, and look-alike domains. A public figure is almost never offering you a private deal in a direct message.
- **Mitigation**: verify through a channel you opened yourself; two confirmations through the same channel are one confirmation; ask a question only the real person could answer; agree on a family code word for emergency requests.

## 10.4 Pyramid and Ponzi structures in the crypto setting
- **Thesis**: they fail by arithmetic regardless of the label.
- **Mechanism**: with 5 invitees per member, level 10 requires 5^10 = 9,765,625 people. A scheme paying earlier members from later deposits needs ever-growing inflows; yields advertised as coming from "trading", "arbitrage" or "staking" with no verifiable source are the standard cover. Tokens with an inside controller, withdrawal limits and referral rewards fit the pattern.
- **Does not hold when**: a product's yield comes from a transparent fee or revenue source that can be checked independently.

## 10.5 Verification heuristics
| Check | Why |
|---|---|
| Nobody seeks you to offer profitable investments | Genuine offers are not cold-called |
| Urgency is the lever | Real opportunities survive a night |
| Hang up and call a number you looked up | Defeats spoofed caller identity |
| Search "name + scam" | Cheap and often decisive |
| Read the real domain from the first single slash backwards | Defeats look-alike URLs |
| Guaranteed returns above about 10% are impossible | Guaranteed returns track low-risk rates (3-4% gross in Italy, snapshot 2023) |
| Check the intermediary in an official registry | Many scam entities are unregistered |
| A transfer's bank name is not checked against the IBAN | Attackers exploit this |
| Test the exit with a small withdrawal | A platform that blocks withdrawal is failing |

Would you hand cash to a stranger who made the same offer on the street? A 50% deposit for a holiday rental requested to a third party's account fails that test.

## 10.6 Technical hygiene
- **Second factors.** A second factor must not transfer automatically to a new device. A six-digit code with three attempts has a 3-in-a-million guess chance. App-based or hardware keys resist SIM-swap attacks better than SMS. Backup codes belong offline.
- **Phishing sites.** The dominant loss cause in DeFi (ch07). Bookmark official addresses; never click links from messages; treat unexpected "signing" requests as hostile; read what a signature authorises; avoid unlimited token approvals and revoke old ones.
- **Clipboard and addresses.** Check the first and last characters after pasting; send a test amount (ch03).
- **Software.** Official sources only, verify signatures, avoid cracked software, keep an offline device for large holdings.
- **Phrase handling.** Never enter a phrase into a website, chat or "support" form. No legitimate service asks for it.
- **Accounts.** Unique passwords per service from a password manager; separate email for financial services.

## 10.7 VPNs and anonymising networks
- **Thesis**: each tool moves trust somewhere; none removes risk.
- **Mechanism**: a VPN encrypts traffic to the provider, hiding it from the local network, but shifts visibility to the provider (look for a no-log policy) and does not stop phishing or inspection after the exit. Anonymising networks relay through several hops so each node sees only its neighbours; exit nodes are often blocked by mainstream sites and the network is slow. Illegal marketplaces rely on escrow and untraceable coins and are largely scams. Worked example: a 100 MB download took 43 s without a VPN, 44 s with a nearby server, about 99 s with a distant one.
- **Does not hold when**: services already use end-to-end encryption on a trusted network.

## 10.8 Account suspensions and the bank interface
Banks and card issuers can freeze or close accounts on risk grounds, and the cause is often undisclosed. Anti-money-laundering rules force periodic document requests, delivered inside the secure area rather than by email. Declared income wildly inconsistent with inflows, or expired identity documents, trigger blocks. For people moving money between crypto venues and banks, large inflows may prompt questions; keep documents ready (ch09). Redundancy (a second account, a second card) limits damage. Remote suspensions often happen at weekends when support is closed despite "24/7" claims.

## 10.9 Recovery scams and what to do after a loss
Do not pay anyone who promises to recover lost funds for an advance fee. Stop sending money, preserve evidence (addresses, transaction identifiers, chat logs), report to the platform and the relevant authorities, and expect that recovery is rare. Seek qualified advice before any new payment.

## 10.10 Threat model by amount
| Holdings | Main threats | Typical controls |
|---|---|---|
| Small | Phishing, fake apps | Official software, 2FA, test transfers |
| Medium | Phrase loss, SIM swap, malware | Hardware device, tested backups, app-based 2FA |
| Large | Targeted attacks, coercion, succession | Multi-signature, geographic spread, legal planning |

## 10.11 Compounding arithmetic in promises
- **Thesis**: a promised daily or monthly rate, once compounded, produces numbers that no real strategy sustains; the arithmetic is a faster test than any due diligence.
- **Mechanism**: a daily rate `d` compounds to `(1 + d)^365 - 1` over a year: 1% a day gives about 3,678% (37.8 times the capital). Working back, a claim that 4,000 became 13,000 in nine days implies a daily growth of `3.25^(1/9) - 1`, about 14% a day. Compounded, that rate would turn a small sum into an impossible one within weeks. A claim that gains of a few percent a day are "normal" is therefore a claim about the payer's cash flow, which must come from new deposits (10.4) or from a source that can be checked.
- **Trade-off**: the arithmetic reveals the promise, not the intention of the promoter, and it does not check whether a real but smaller return exists.
- **Does not hold when**: the figure is not compounded (a simple one-time gain on a fixed amount, stated as such and verifiable with statements).

## Common mistakes
- Believing support staff who contact you first.
- Trusting a screenshot of "profits".
- Paying "taxes" to release funds.
- Reusing passwords.

## Links
- ch01 irreversibility; ch03 custody; ch05 platform warning signs; ch07 approvals; `investing-and-financial-history` ch10 for fraud cases.
