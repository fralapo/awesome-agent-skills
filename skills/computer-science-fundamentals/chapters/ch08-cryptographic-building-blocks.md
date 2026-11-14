# Chapter 8: Cryptographic Building Blocks

## Core Idea
Cryptography converts computational asymmetry into security: operations that are cheap for the key holder and expensive for everyone else. In this model there are four tools (a one-way function, a public/private pair, a shared-key cipher, and fast exponentiation to make the pair usable), and security is a property of their combination, never of any single one.

## 8.1 Easy to do, hard to undo
- **Thesis**: public-key cryptography rests on problems where checking or forward computation is fast and the reverse is believed to be slow.
- **Mechanism**: multiplying two large primes is quick; recovering them from the product (factoring) has no known fast method. Telling that a number is not prime is often easy; finding its factors is not. Nobody has proved that a fast factoring method cannot exist (see ch1, P and NP), so the security is a belief backed by decades of failed attempts.
- **Trade-off**: key sizes must grow as attacks and hardware improve; a mathematical or quantum breakthrough would invalidate a whole family.
- **Does not hold when**: a larger machine of a new kind exists. On paper a quantum algorithm factors in polynomial time, but machines are far from the needed size; treat quoted records as short-lived.

## 8.2 Modular arithmetic: the clock
- **Thesis**: working "on a clock" keeps numbers bounded and gives operations with inverses.
- **Mechanism**: a result modulo n is the remainder after division by n (fifteen hours on a twelve-hour clock is three). A clock of 91 hours (91 is seven times thirteen) behaves like any other clock for addition and multiplication; the special property is that raising numbers to certain powers can be undone by raising to other powers.
- **Trade-off**: a clock with a prime size and one with a product of primes behave differently; the difference is what RSA exploits.
- **Does not hold when**: numbers are not reduced (they become astronomically large).

## 8.3 RSA: public-key encryption and signatures
- **Thesis**: choose exponents e and d so that raising to e and then to d on a clock of size n returns the original number; publish n and e, keep d secret.
- **Mechanism**: pick two large primes p and q; n = p times q is public. Compute (p minus 1) times (q minus 1); with the toy primes 7 and 13 this is 6 times 12 = 72. Pick e that shares no factor with that number (5 here). Find d with e times d equal to 1 on the clock of that size (5 times 29 = 145 = 2 times 72 plus 1, so d = 29), using the extended Euclidean algorithm, which is fast. Encrypt a message m as m to the e on the 91-hour clock (18 to the 5 gives 44), decrypt as the result to the d (44 to the 29 gives 18). Why it works: e times d minus 1 is a multiple of both p minus 1 and q minus 1, and Fermat's little theorem then collapses the power to one, leaving m. Why it is secure: computing (p-1)(q-1) requires p and q; the key owner multiplied two primes of about 300 digits each (a 2048-bit modulus of about 600 digits), then discarded them. A certificate shows the algorithm, the key size, the exponent and the modulus; the public exponent is small and usually 65537 (2^16 plus 1), while d is a roughly 2000-bit secret that cannot be searched. Signing reverses the roles: apply the private exponent to a hash of the message; anyone can verify with the public exponent (fast), which is a reason RSA verification stays popular next to elliptic-curve schemes (the other main family, which does not rest on factoring).
- **Trade-off**: slow compared with symmetric ciphers, so it is mainly used to sign and to agree on a symmetric key; real use needs padding and other safeguards (the toy example omits them and is not secure); large keys.
- **Does not hold when**: key generation is flawed (poor randomness, shared primes), the implementation leaks (see 8.4), or the key length is too short for the threat.

## 8.4 Square and multiply: fast modular exponentiation
- **Thesis**: computing a^k mod n by repeated multiplication takes k steps, which is impossible for a 2000-bit k; squaring makes the exponent double each step, so the cost is about its bit length.
- **Mechanism**: write the exponent in binary. Squaring a number doubles the exponent, which in binary appends a 0; multiplying the running result by the original base adds one, which turns that appended 0 into a 1. Process the exponent from its leading bit: for each remaining bit, square; if the bit is 1, also multiply by the base. Reduce modulo n after each operation so that no number exceeds n squared; in the worked example (three to the power 45 modulo seven) every intermediate value stays tiny instead of reaching a 22-digit figure. For 2^8 this takes three squarings instead of seven multiplications. A public exponent of 65537 has only two one-bits, so verification needs about sixteen squarings and one multiplication. A private exponent of 2000 bits needs about 2000 squarings and roughly half as many multiplications, on the order of three thousand big-number operations, feasible on any machine; the naive method would never finish. Also used in primality testing.
- **Trade-off**: the sequence of operations depends on the secret exponent. A timing or power measurement can show a square (and no multiply) versus a square plus a multiply, and so read the key bits off; keys with many zeros are faster, leaking their weight. Variants that always do a multiplication and are structured to take constant time close this channel.
- **Does not hold when**: the exponent is public (then the speed is the point) or the computation runs somewhere an attacker cannot measure.

## 8.5 AES: a symmetric block cipher built as a substitution-permutation network
- **Thesis**: encrypt a 128-bit block by repeating rounds that confuse (substitute) and diffuse (permute and mix) the data, with the key mixed in each round; the algorithm is public and only the key is secret.
- **Mechanism**: key length 128, 192 or 256 bits, giving 10, 12 or 14 rounds. The 16 bytes of a block are laid out in a 4-by-4 grid, column by column. First the block is combined with a round key by exclusive-or. Each round then does: SubBytes (every byte replaced by another through a fixed lookup table, the S-box, designed to be very non-linear, with no byte mapping to itself and none to its bitwise opposite); ShiftRows (row i shifted left by i places with wrap-around); MixColumns (each column multiplied by a fixed small matrix, so each output byte depends on all four input bytes of the column; combined with ShiftRows, a few rounds spread every input byte across the entire block); AddRoundKey (exclusive-or with that round's key). The last round skips MixColumns. A key schedule expands the short key into one round key per round and is designed to be fast. All arithmetic is in a finite field of 256 elements (one byte each): addition is exclusive-or, multiplication is defined modulo a fixed polynomial, so results never overflow and every step is invertible, which is what makes decryption possible by running the inverse operations. To an observer the result looks like a random permutation of blocks.
- **Trade-off**: fast in software and hardware because it is lookups and exclusive-ors; a block cipher alone gives no integrity and is used within a mode of operation that also detects tampering (general knowledge: integrity is provided by standard symmetric-key constructions on top of the cipher).
- **Does not hold when**: the key is guessable or reused incorrectly, or a side channel leaks table accesses.

## 8.6 Hash functions and digital signatures
- **Thesis**: a hash maps data of any size to a fixed-size digest in a way that cannot be reversed; two values can be checked for identity by comparing digests.
- **Mechanism**: a secure hash algorithm with a 256-bit output is the standard example. A signature hashes the message, signs the hash with the private key, and anyone verifies with the public key; any change to the message changes the hash and verification fails. A signature proves identity without revealing the private key and detects alteration, while the message itself can travel in clear.
- **Trade-off**: hashing is not encryption (nothing can be recovered); old hash functions are broken for security uses.
- **Does not hold when**: two different messages produce the same hash (a collision), which is why weak hashes are retired.

## 8.7 Hybrid use: public key to agree, symmetric key to talk
- **Thesis**: asymmetric operations are clumsy and slow, so they are used to establish a shared secret from which a fast symmetric key is derived.
- **Mechanism**: two parties exchange secrets using public keys (see ch9), derive a symmetric key from both, then use a cipher such as the one in 8.5 for all bulk data. The same pattern runs the secure web.
- **Trade-off**: one more step, and the derived key must be fresh for every session.
- **Does not hold when**: both parties already share a secret.

See also: ch9 (protocols that combine these tools and how they fail), `software-architecture` ch13 (TLS in practice) and ch16 (OAuth).
