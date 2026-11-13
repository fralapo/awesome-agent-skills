# Chapter 3: Information, Entropy, Compression and Signals

## Core Idea
Information theory gives machine learning its main loss function and its deepest analogy: **predicting well is the same as compressing well**. Signal tools (frequency decomposition, convolution) explain how structure is separated from a mixture. In this model these ideas are read as engineering limits, not as metaphors.

## 3.1 Information content: surprise in bits
- **Thesis**: an event with probability p carries minus log base two of p bits of information; rare events are more informative.
- **Mechanism**: halving the possibilities costs one bit, so the number of bits is "how many times you must halve to single out this event". For independent events the information adds, so the log turns products of probabilities into sums.
- **Trade-off**: the result is usually fractional, which is meaningful: it is the average cost over long messages, not the length of one codeword.
- **Does not hold when**: probabilities are unknown; then information is relative to a model and the model can be wrong.

## 3.2 Entropy: the average surprise and the compression limit
- **Thesis**: the entropy of a distribution is the expected information per symbol, and it is the lowest average code length any lossless code can reach for that source.
- **Mechanism**: an optimal code gives each symbol about minus log2 of its probability bits (for a source with probabilities one half, one quarter, one eighth, one eighth, lengths one, two, three, three). Entropy is largest for uniform distributions and zero for certainty. Visual form: a bar chart whose bar widths are probabilities and heights are code lengths; entropy is the total area.
- **Trade-off**: reaching the limit needs a good model of the source; real codes pay overhead for block lengths and model cost.
- **Does not hold when**: loss is acceptable (lossy compression trades fidelity for size) or the source is not stationary.

## 3.3 Cross-entropy: the price of using the wrong model
- **Thesis**: cross-entropy is the average code length when data follow distribution P but the code was built for distribution Q; it is never below the entropy of P and equals it only when Q matches P.
- **Mechanism**: weight each symbol's code length under Q by its true frequency under P. It is asymmetric: swapping the roles changes the number (an example with a 90/10 and a 50/50 source costs about 1.0 bits one way and about 1.74 the other). The excess over the entropy is the divergence between the distributions, a non-negative measure of mismatch.
- **Trade-off**: minimising cross-entropy is a clean, differentiable training target; it rewards calibrated probabilities, not only the right top answer.
- **Does not hold when**: the goal is not probability estimation (ranking, decisions with asymmetric costs), where a different loss may fit better.

## 3.4 Why cross-entropy trains language models
- **Thesis**: training a model to predict the next token with cross-entropy loss is the same as training it to compress text; a lower loss is a shorter code.
- **Mechanism**: the true next token acts as P (one-hot), the model's output probabilities act as Q, and the loss is minus log of the probability assigned to the true token. Distillation (teaching a small model with a large model's full probabilities) uses the same formula with soft targets. A classic demonstration: general file compression, used on pairs of documents, can cluster languages and recover family trees because co-compression is cheap when the patterns are shared.
- **Trade-off**: compression-quality is a strong proxy for modelling the data distribution, but it is not the same as usefulness: a model can compress web text well and still answer badly (chapter 8 on post-training).
- **Does not hold when**: you need properties the data distribution does not reward (truthfulness, safety), which must be added by other objectives.

## 3.5 Error-correcting codes: redundancy done cleverly
- **Thesis**: reliable storage and transmission over noisy channels needs redundancy, but far less than naive repetition if the redundancy is structured.
- **Mechanism**: repeating each bit three times wastes two thirds of the space and gives weak guarantees. A Hamming-style code places parity bits so that each one checks a different subset of positions; the pattern of failed checks spells out, in binary, the position of a single flipped bit, so it can be flipped back. A block of 256 bits can carry 247 data bits and 9 parity bits, correcting one error and detecting two. The one-line implementation is an exclusive-or over the positions of the set bits.
- **Trade-off**: more parity corrects more errors but lowers the rate; correction of one error is guaranteed, more than that is not.
- **Does not hold when**: errors come in long bursts (other codes, or interleaving, are used).

## 3.6 Frequency decomposition
- **Thesis**: any signal can be written as a sum of pure frequencies; the Fourier transform gives the amount and phase of each.
- **Mechanism**: wind the signal around a circle at a trial frequency and look at the centre of mass of the wound-up curve; it is far from the origin only when the signal contains that frequency. Used for audio, images, compression, and solving equations (derivatives become multiplications).
- **Trade-off**: a signal localised in time is spread over frequencies and vice versa, so no single view is both sharp in time and in frequency.
- **Does not hold when**: the signal is strongly non-stationary and a windowed or learned representation fits better.

## 3.7 Exponentials and the Laplace transform
- **Thesis**: the Laplace transform generalises the Fourier transform to growing and decaying exponentials, turning linear differential equations into algebra.
- **Mechanism**: complex exponentials with a negative real part decay while rotating; a transform that tests a signal against all of them reveals poles that govern stability and response. Solving: transform, solve the algebraic equation, transform back.
- **Trade-off**: elegant for linear time-invariant systems; it is mainly relevant for control and physics-style modelling in this domain.
- **Does not hold when**: the system is nonlinear or time-varying.

## 3.8 Logarithms and dynamic range
- **Thesis**: taking logarithms turns multiplicative structure into additive structure; it appears in information, in losses and in visualising wide ranges.
- **Mechanism**: log probabilities add, so products of many small probabilities do not underflow; a log of an image compresses brightness range and turns multiplicative lighting into additive differences.
- **Trade-off**: log of zero is undefined, so probabilities are floored or models use log-sum-exp tricks.
- **Does not hold when**: the quantity can be negative or zero by nature.
