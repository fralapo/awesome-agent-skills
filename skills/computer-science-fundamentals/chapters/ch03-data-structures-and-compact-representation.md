# Chapter 3: Data Structures, Representation and Compact Coding

## Core Idea
Data structures decide which operations are cheap; representation decides how many bits a value costs and what damage a flipped bit can do. In this model the question is never "which structure is best" but "which operation dominates, and what does the hardware do with that access pattern", and the answer is checked by measurement.

## 3.1 The seven basic structures
- **Thesis**: almost everything is built from seven shapes, each a trade between access, change and memory.
- **Mechanism**: array (numbered cells, direct access by index, size fixed at creation); linked list (each node holds a pointer to the next; grows and shrinks by re-pointing; a null pointer ends it); hash table or dictionary (keys point to values); stack (last in, first out); queue (first in, first out); tree (hierarchy, often faster to traverse than a line); graph (nodes plus edges for arbitrary relations). A data structure is a way to organise data so you can create, read, update and delete it efficiently.
- **Trade-off**: the cost of the operation you do most decides the choice: random access favours arrays; frequent insertion in the middle favours lists (when you already hold the position); membership by key favours hashing; ordered lookup favours trees or sorted arrays.
- **Does not hold when**: the data is tiny; any structure then works and clarity wins.

## 3.2 Array versus linked list: the answer depends on the machine
- **Thesis**: asymptotic analysis says the two are equivalent for a full traversal; in practice a traversal of an array is usually much faster than a list because of how memory is fetched, and that was measured, not assumed.
- **Mechanism**: an array stores elements one after another; a list scatters nodes in memory and needs an extra pointer per node. Summing one field over about 125,000 elements, repeated 100 times, a comparison was run on several kinds of machine. On an old machine whose memory was as fast as its processor and which had no cache, the list was slightly faster (roughly ten per cent) and a backward array loop beat the forward one, because the instruction set had a decrement-test-branch instruction. On a machine of the same family with a cache, the array became faster. On a modern small computer and on a desktop machine the array won by about a factor of two to five; part of the large factor came from the compiler unrolling the array loop. The reason: with a cache, instructions come from the instruction cache and an array element arrives with its neighbours in one cache line, so each element needs about one real memory access; a list needs two (the value and then the next pointer), and the next node may be anywhere.
- **Trade-off**: arrays win scans and random access; lists win when the program already holds a position and inserts or removes there, and when elements cannot be moved.
- **Does not hold when**: the list nodes happen to be allocated contiguously, the element is large, or the access is a single lookup (for one random element an array always wins; for the first element they tie). The general lesson: you cannot assume how a CPU runs code, even within one processor family; write a test and collect data.

## 3.3 Trees for storage: B-tree, radix tree, rope
- **Thesis**: when the data lives on slow storage, minimise the number of block reads; when keys share prefixes or strings are edited, shape the tree to that.
- **Mechanism**: a binary search tree turns quadratic work into n log n but has only two children per node, so it is deep. A B-tree lets each node hold many sorted keys and many children; internal nodes are signposts, leaves hold data or pointers to data; the height is small, so a lookup reads few disk blocks. Databases and file systems mostly use a variant that keeps data in the leaves. A radix tree merges chains of single-child nodes, which suits keys with shared prefixes such as network addresses. A rope breaks a long string into chunks joined by nodes that record chunk lengths, so editing a large document changes a few nodes instead of copying everything.
- **Trade-off**: more complex insertion and rebalancing in exchange for fewer I/Os or cheaper edits.
- **Does not hold when**: everything fits in memory and keys are random (a hash table or a plain sorted array can be simpler and faster).

## 3.4 Probabilistic and constant-time structures: Bloom filter, cuckoo hashing
- **Thesis**: sometimes the cheapest answer is "definitely not" or "found in a fixed number of probes".
- **Mechanism**: a Bloom filter is a fixed array of bits and several hash functions. To add an item, set the bits its hashes point to; to test, check those bits. If any bit is zero the item is definitely absent; if all are set it is probably present (false positives are possible, false negatives are not). Cuckoo hashing gives each key two or more candidate slots; inserting into an occupied slot evicts the occupant to its alternate slot, like the bird that takes over another's nest; lookups probe a fixed few places, so the worst case is constant.
- **Trade-off**: a Bloom filter cannot list or delete members (in its basic form) and its false-positive rate grows as it fills; cuckoo insertion can cascade and may require a resize.
- **Does not hold when**: a false positive is unacceptable and there is no cheap second check behind it.

## 3.5 Huffman coding: shortest prefix code for known frequencies
- **Thesis**: if symbols have different probabilities, give frequent ones shorter codes; the Huffman procedure builds the best such code.
- **Mechanism**: order the symbols by probability; repeatedly merge the two lowest-probability items into a node whose probability is their sum, until one node (probability 1) remains; this builds a tree. Label every left branch 0 and every right branch 1 (the opposite convention gives a different but equally good code); a symbol's code is the path from the root. When ties occur, apply one consistent rule. The average code length L can be compared with the entropy H, the sum over symbols of p·log2(1/p): efficiency is H/L. Four equally likely weather states give two-bit codes, entropy two bits, efficiency 100 per cent. For probabilities one third, one third, and three of one ninth, the entropy is about 2.113 bits, average length about 2.222 bits, efficiency about 95.1 per cent.
- **Trade-off**: it reaches the entropy limit only when probabilities are negative powers of two; with other probabilities a whole number of bits per symbol wastes a little. It needs the probabilities up front or a first pass to count them. Codes that are not prefixes of one another can be decoded without separators (general knowledge).
- **Does not hold when**: the symbols are nearly equally likely (little to gain), or the statistics change quickly (use adaptive methods).

## 3.6 Error detection and correction: parity, Hamming, Reed-Solomon
- **Thesis**: add structured redundancy and the receiver can detect, locate and repair damage.
- **Mechanism**: a parity bit makes the count of ones even or odd and detects a single flipped bit. A Hamming code adds several check bits so that one wrong bit can be located and corrected: protecting two data bits with three check bits makes a five-bit codeword in the example given. Reed-Solomon codes treat each position as a symbol (for example a byte) instead of a bit, so they cope with bursts of errors, such as a scratch on a disc that ruins a stretch of consecutive bits but damages only a few symbols. The check symbols at the end are computed so that, for an intact word, a set of remainders called the syndrome is zero; a non-zero syndrome signals damage, and from its values the damaged positions and corrections can be computed. The arithmetic is done in a finite field (a Galois field) of 2^8 elements, where each element is a byte; addition modulo 2 is exclusive-or, every non-zero element has a multiplicative inverse, and operations never leave the field. Discs use two layers of the code, one backing up the other.
- **Trade-off**: redundancy costs space and computation; stronger correction needs more check symbols.
- **Does not hold when**: errors exceed what the code can fix (the word is then wrongly decoded or flagged as uncorrectable), or the channel can simply retransmit (then detection alone may be cheaper, as in ch7).

## 3.7 Bits, bytes, text and numbers
- **Thesis**: the machine stores only bits; meaning is a convention.
- **Mechanism**: a bit is a transistor switch state; eight bits form a byte with 256 values; a character is mapped to a number by an encoding such as ASCII or UTF-8; hexadecimal writes four bits per digit. Integers can be signed or unsigned; non-integers use floating point, a form of scientific notation with limited range and precision (a double doubles the width); text is a string of characters. Byte order in memory is big-endian (most significant byte at the lowest address) or little-endian. Source code is converted into machine code, the binary instructions the CPU decodes. Variables name data in memory; a pointer is a variable that holds the address of another.
- **Trade-off**: fixed widths overflow; floating point rounds; byte order matters when data crosses machines.
- **Does not hold when**: a language hides these details; they reappear in file formats, networks and bugs.

See also: ch4 (why layout matters for speed), ch7 (how bits are put on a wire), `software-architecture` ch04 (storage engines, Bloom filters in practice).
