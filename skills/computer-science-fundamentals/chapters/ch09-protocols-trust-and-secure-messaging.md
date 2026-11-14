# Chapter 9: Protocols, Trust and Secure Messaging

## Core Idea
A protocol is a conversation between parties who do not trust the wire and sometimes not each other; correct cryptography is necessary and nowhere near sufficient. In this model every message must say who it is from, who it is for and which run of the protocol it belongs to, and a protocol is secure only against the attacker model it was analysed under: the attacker needs one overlooked combination, the defender must cover all of them.

## 9.1 The untrusted network and the man in the middle
- **Thesis**: a message on the internet crosses servers, routers and devices run by others, any of which may read or change it; the party who sits in the path is the man in the middle.
- **Mechanism**: analogy: you post a locked envelope; the postman may open, copy or replace it. Public keys let anyone lock a message that only the key holder can open, but a key is just a number: nothing in it says who owns it. Browsers show a padlock when a certificate ties a public key to a domain name through a trusted authority; the certificate's key information shows the algorithm, key size, exponent and modulus (ch8).
- **Trade-off**: trust moves from the network to the authority that signs certificates.
- **Does not hold when**: both ends already hold each other's keys through a separate trusted channel.

## 9.2 Proving who you are with a public key, and why it is subtle
- **Thesis**: "this party could decrypt my challenge" proves the holder of the private key is present, not that the party I meant to talk to is.
- **Mechanism**: challenge-response: lock a random secret with a claimed owner's public key and ask for it back. A malicious relay who receives a challenge does not need the key: it can forward the same challenge to the real owner, receive the correct answer, and return it as its own. You then believe the relay is the owner. The lesson: an ability to decrypt must be tied to a binding of identity and run.
- **Trade-off**: binding identity costs extra fields in each message.
- **Does not hold when**: the relay is not in the path or the challenge is bound to the intended identity (see 9.3).

## 9.3 The public-key authentication protocol with nonces, its flaw and its fix
- **Thesis**: a protocol that looks right and has a published proof can still fail when it is run in a situation the proof did not consider.
- **Mechanism**: the steps: (1) the first party creates a random secret number (a nonce), puts it with its own name in an envelope locked with the second party's public key, and sends it. (2) The second party opens it, learns the nonce and who asked, creates its own nonce, and returns both nonces locked with the first party's public key; getting its own nonce back proves to the first party that the reply came from the holder of the second private key. (3) The first party returns the second party's nonce locked with the second party's public key, proving it read the reply. Afterwards both know the pair of secrets and can derive a symmetric key from them (ch8). The flaw: suppose the first party legitimately starts the protocol with a malicious party (for example a dodgy website). That party can run a second protocol with a third party, replaying and relaying the same messages, so the third party believes it is talking to the first party. The relay uses the first party as an oracle. It went unnoticed for years because the proof only considered the first party wanting to talk to the intended partner. The fix: the second party's reply also includes its own identity; the first party, expecting to talk to the malicious party, sees a different name and aborts.
- **Trade-off**: the extra identity field is cheap; the real cost is the analysis effort.
- **Does not hold when**: modern protocols are designed with this attack in mind; the example is didactic (position).

## 9.4 Why protocol security is hard
- **Thesis**: attackers combine runs, roles and replays; defenders must show safety for every combination.
- **Mechanism**: an honest party may play several roles at once, may be tricked into starting a session with an attacker, and may be an oracle for other sessions. Typical defences: include the identities of both parties and a role marker in signed or encrypted content, use fresh nonces per run, never answer an unsolicited challenge without context, check that every message belongs to the expected step, and use formally analysed standard protocols instead of inventing new ones.
- **Trade-off**: each safeguard costs bytes or round trips.
- **Does not hold when**: the setting is closed and trusted (single machine, single process).

## 9.5 Asynchronous messaging: keys that change every message
- **Thesis**: in a chat where the other party may be offline for months, no single key should live long; each message gets a fresh key derived by one-way steps.
- **Mechanism**: the initial exchange is done asynchronously through pre-key bundles (public keys left on a server in advance) and a triple Diffie-Hellman combination, which gives both parties a starting shared secret without being online together. Using that one key for all messages would mean that breaking one message breaks all of them. A key-derivation ratchet turns the current key into the next key and a message key through a one-way function (like a hash), so a stolen key cannot be run backwards: past messages stay safe (forward secrecy). But the ratchet alone allows an attacker who has a key to compute all later keys; so Diffie-Hellman parameters carried in messages are used to re-seed the chain: once the parties exchange fresh parameters the attacker, who has not seen them, is locked out again (sometimes called future secrecy or self-healing). Combining the two gives the double ratchet. Each party keeps a Diffie-Hellman ratchet, a sending chain and a receiving chain; the sending chain of one is kept in step with the receiving chain of the other; when a new public value arrives it updates the Diffie-Hellman ratchet and resets the chains. In practice a new value is sent with every message. Out-of-order or lost messages: the message says how many were sent on this chain; the receiver advances the receiving chain, storing the skipped message keys temporarily, and deletes every key immediately after use. The derived keys drive a standard symmetric cipher with integrity protection, so voice, video and text all use the same mechanism. Delivered and read marks are application messages inside the encrypted channel.
- **Trade-off**: state to keep in sync, stored keys for missing messages, complexity; the benefit is that a device compromise reveals little.
- **Does not hold when**: the endpoint itself is compromised (the plaintext is available there), or the server is trusted with metadata (who talks to whom is not hidden by this mechanism, general knowledge).

## 9.6 Hash-linked ledgers and proof of work
- **Thesis**: a chain of records where each one contains the hash of the previous one makes tampering detectable; agreeing on one chain without a central authority needs a cost to propose a block.
- **Mechanism**: a transaction names an amount, a payer's and a payee's public key and is signed with the payer's private key; a wallet is a key pair (public key to receive, private key to spend). Transactions are grouped into blocks; each block holds the hash of the previous block, so changing an old block changes every later hash. The first block has no predecessor. Two simultaneous spends of the same coin (a double spend) must be resolved by agreement: many machines compete to find a proof of work, a problem hard to solve and easy to verify (ch1), the winner proposes the next block and is rewarded, and the others check and accept it. The result is a shared ledger without a trusted middleman, at the cost of heavy computation.
- **Trade-off**: tamper evidence and decentralisation against energy, latency and throughput; whether such a system is a durable store of value or a speculative bubble is contested (position).
- **Does not hold when**: a single organisation can be trusted; a conventional database is simpler and cheaper. See `software-architecture` ch02 for consensus.

## 9.7 Sessions versus tokens for web authentication
- **Thesis**: the question is where the login state lives, on the server (session) or with the client (token); each choice moves cost and risk.
- **Mechanism**: session: the client sends credentials; the server validates them, stores a session record, and returns a session identifier kept in a cookie; every later request carries it and the server looks it up. Token: the server creates a signed token (for example a JSON web token) with a private key and returns it; the client sends it in an authorisation header on each request; the server only checks the signature, with no lookup in another system.
- **Trade-off**: sessions are stateful: a lookup per request becomes a bottleneck when the service scales horizontally, and cookies invite cross-site request forgery (low risk with a modern framework). Tokens scale with no shared store, but a stolen token works until it expires, they are hard to revoke and cannot authenticate a user in the background on the server. Where tokens are stored in the browser is a contested choice (position; general knowledge: script-readable storage is exposed to script injection).
- **Does not hold when**: revocation must be immediate (keep a server-side list, which brings back state).

See also: ch8 (the tools), `software-architecture` ch16 (OAuth and gateways) and ch13 (TLS).
