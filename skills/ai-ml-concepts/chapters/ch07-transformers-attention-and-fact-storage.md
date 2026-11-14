# Chapter 7: Transformers, Attention and How Facts Are Stored

## Core Idea
A transformer turns text into vectors, lets the vectors exchange information (attention), lets each vector be refined independently (feed-forward blocks), repeats this many times, and reads a probability over the next token from the last vector. In this model, almost every step is a matrix-vector product, and the open questions are about what the learned numbers mean.

## 7.1 Tokens and embeddings
- **Thesis**: text is cut into tokens (word pieces) and each token becomes a high-dimensional vector; directions in that space can carry meaning.
- **Mechanism**: an embedding matrix has one column per vocabulary entry (tens of thousands); values start random and are learned. Famous regularity: a consistent direction relates pairs such as masculine and feminine nouns. A position signal is added so that order is known.
- **Trade-off**: token splitting shapes behaviour (counting letters in a word, arithmetic on long numbers) because the model sees pieces, not characters.
- **Does not hold when**: you assume the vector means one fixed thing: the same token has the same initial vector in all contexts; context enters through attention.

## 7.2 The unembedding and softmax
- **Thesis**: the last vector is turned into a score per vocabulary item, and a softmax converts scores to probabilities.
- **Mechanism**: one more matrix; softmax exponentiates and normalises. A temperature parameter divides the scores before softmax: low temperature concentrates probability on the top token, high temperature spreads it. Sampling from the distribution (not always taking the top token) makes output varied; the model itself is deterministic, the sampling is not.
- **Trade-off**: greedy decoding is repeatable but can lock into a wrong first choice; sampling gives variety and can be combined with voting (chapter 8).
- **Does not hold when**: you need a guaranteed answer; probabilities express the model's belief, not truth.

## 7.3 Attention: queries, keys and values
- **Thesis**: attention lets each token pull relevant information from other tokens.
- **Mechanism**: every embedding is multiplied by three learned matrices to give a query ("what am I looking for?"), a key ("what do I contain?") and a value ("what would I add to someone who attends to me?"). Dot products of queries with keys give a grid of scores; a softmax per query turns them into weights; the weighted sum of values is added to the embedding. Scores are divided by the square root of the key dimension for numerical stability. Many heads run in parallel, each with its own matrices, and their outputs are combined.
- **Trade-off**: flexible and parallel across the sequence; cost grows with the square of the context length.
- **Does not hold when**: contexts get very long and the quadratic grid becomes the bottleneck; variants reduce it (chapter 7.8).

## 7.4 Masking: no peeking at the future
- **Thesis**: when training on text, each position predicts the next token, so a token must not see later ones.
- **Mechanism**: scores for later positions are set to minus infinity before softmax so their weights become zero and the rest stay normalised. One passage then trains many predictions in parallel.
- **Trade-off**: efficient training; the model cannot use right-hand context when generating left to right.
- **Does not hold when**: tasks are bidirectional encodings (other model families omit the mask).

## 7.5 The feed-forward block: where capacity lives
- **Thesis**: most parameters sit in the feed-forward (multi-layer perceptron) blocks, which process each token's vector independently.
- **Mechanism**: multiply by a wide matrix (about four times the model width), add bias, apply a clipping nonlinearity, multiply by a narrow matrix back to the model width, add to the input (a residual connection). In a large model of about 175 billion parameters (as reported at the time), roughly two thirds of the parameters were in these blocks across nearly a hundred layers.
- **Trade-off**: very high capacity at low architectural complexity; interpretation is hard.
- **Does not hold when**: you assume attention does all the knowledge work: attention moves information between positions, the feed-forward blocks transform and store.

## 7.6 A toy account of storing a fact
- **Thesis**: a feed-forward block can, in principle, store an association with an AND gate followed by a write.
- **Mechanism**: suppose one direction encodes "first name Marta" and another "last name Quillon" (an invented player). A row of the first matrix equal to their sum has dot product two only when both are present; with a bias of minus one and a clipping function the neuron fires if and only if both are present (the AND). A column of the second matrix encodes the "basketball" direction; when the neuron fires, that column is added to the vector. Attention must first have moved the information so that both names are in one position.
- **Trade-off**: the example is a teaching device. Direct evidence shows that facts live largely in these blocks, but a full mechanistic account is unsolved.
- **Does not hold when**: you expect a real neuron to represent a single clean fact: individual neurons rarely do.

## 7.7 Superposition: more features than neurons
- **Thesis**: a high-dimensional space can hold many more nearly independent features than it has axes, so features are stored as overlapping patterns.
- **Mechanism**: exactly perpendicular directions number only as many as the dimensions, but nearly perpendicular directions (say 89 to 91 degrees) number exponentially many. A model could therefore probe far more features than it has neurons, each feature appearing as a combination of neurons. This may help explain why performance scales well with size and why the model is hard to read; sparse autoencoders are a tool for extraction (chapter 11).
- **Trade-off**: capacity vs interference and readability.
- **Does not hold when**: features are dense or strongly correlated, where overlapping codes interfere too much.

## 7.8 Context length and alternatives to full attention
- **Thesis**: the quadratic cost of attention motivates cheaper sequence mixers and longer-context engineering.
- **Mechanism**: variants of attention and state-based sequence models aim for near-linear cost; as reported at the time, at small scale a transformer needed substantially more compute to match one such alternative on language modelling, with unknown behaviour at larger scale. Longer context also substitutes partly for learning from experience: place the domain material in the prompt (in-context learning).
- **Trade-off**: speed and memory against recall precision and maturity of tooling.
- **Does not hold when**: tasks need exact recall of arbitrary earlier tokens, where full attention remains strong.

## 7.9 Prediction as the only primitive
- **Thesis**: a chat assistant is a next-token predictor wrapped around a script of "user and assistant".
- **Mechanism**: the text of a hypothetical dialogue is the prompt; the model predicts the assistant's next word, appends it, and repeats. Behaviour such as helpfulness is added afterwards by training on preferences (chapter 8).
- **Trade-off**: simple and general; the model has no state between calls except the text you supply.
- **Does not hold when**: tools and memory are wrapped around the model, in which case the system is more than the bare predictor.

## 7.10 Attention replaced recurrence by shortening paths
- **Thesis**: instead of squeezing a sequence through a hidden state updated step by step, let every position look directly at every earlier position.
- **Mechanism**: a recurrent network reads tokens one at a time, each step combining the previous hidden state with the current input; training the whole sentence is one long chain of backpropagation, and information from far back must survive many updates. With attention each output token is one training example, the computation per step is a fixed number of projections, and the path length between any two positions is one. Because there is no step order, position is injected: sinusoids at several frequencies give each position a code like a continuous binary counter, letting the network compare which of two tokens comes first or how far apart they are. Keys act as addresses into a memory of values; queries ask. Encoder-decoder models add cross-attention where the decoder's queries read the encoder's keys and values.
- **Trade-off**: parallel training and short paths against quadratic cost (7.3).
- **Does not hold when**: sequences are so long that memory, not modelling power, limits you (7.12).

## 7.11 Query-key scoring is a low-rank bilinear form
- **Thesis**: scoring how well two vectors match can use a learned matrix between them, and splitting that matrix saves parameters.
- **Mechanism**: an early attention score multiplied the two vectors with a full matrix in the middle, letting the score weight some coordinates more than others. Write the matrix as a product of two low-rank matrices, apply one to each vector and take a dot product, and you obtain the same score with far fewer parameters and cheaper computation; this is the query and key projection of the modern block (an account given by a researcher involved in the early work; the history of such ideas is diffuse).
- **Trade-off**: parameter efficiency against a rank limit on the kinds of relations expressible per head; many heads compensate.
- **Does not hold when**: you need a score that is not well approximated by a bilinear form.

## 7.12 The key-value cache: compute becomes memory
- **Thesis**: generating one token at a time can reuse earlier keys and values, making per-token attention cost linear, at the price of memory.
- **Mechanism**: with a causal mask, when token n+1 arrives the first n rows of keys and values are unchanged and only the new row of queries is needed, so the keys and values are stored (queries are not). Storage is 2 times tokens times head size times heads times layers numbers. For a configuration with 128 heads and 61 layers in 16-bit numbers, that is on the order of four megabytes per token, hundreds of gigabytes read per new token at a 100,000-token context (illustrative, as reported). The bottleneck is memory bandwidth.
- **Trade-off**: speed for memory; very long contexts become a hardware problem, not a model-quality problem.
- **Does not hold when**: the prompt is short, where the cache is small and compute dominates.

## 7.13 Sharing keys and values: multi-query, grouped-query, latent attention
- **Thesis**: compressing the cache by letting heads share or compress their keys and values trades some specialisation for memory.
- **Mechanism**: multi-query attention uses a single key and value matrix for all heads (cache shrinks by the number of heads, quality drops since heads cannot specialise); grouped-query attention lets groups of heads (for example eight) share (cache shrinks by the group size, smaller drop). Multi-head latent attention projects the input into one compressed latent shared across heads and caches only that, then up-projects with per-head matrices to keys and values; a linear-algebra rearrangement absorbs the up-projection into the query and output weights, so no extra compute is paid at inference. In one developer report the cache fell from roughly four megabytes to about seventy kilobytes per token (a 57-fold reduction), with generation more than six times faster and quality not worse (a developer-reported result; re-check).
- **Trade-off**: cache size, speed and quality; each scheme changes what each head can store.
- **Does not hold when**: you treat the numbers as universal: they hold for one architecture and one implementation.

## 7.14 Selective state-space models: a fixed-size memory that chooses what to keep
- **Thesis**: a recurrent state with input-dependent update rules gives linear cost in sequence length while recovering some of attention's ability to select.
- **Mechanism**: attention can address any past token but costs the square of the length; a classic recurrent net keeps a fixed-size hidden state but only sees the last state and the current input. Linear state-space models update h = A h + B x with parameters fixed for the whole sequence, which allows the unrolled form to be computed as a convolution and is efficient, but cannot decide per token what to remember, and did poorly on language. The selective variant makes the step size and the input and output maps functions of the current token, so it can choose to propagate or forget; that breaks the convolution shortcut, so a hardware-aware scan limits memory traffic. A block is: input projection, short convolution, nonlinearity, selective recurrence, gate, output projection.
- **Trade-off**: linear time and constant memory against a bounded state that cannot hold arbitrary past tokens exactly (general knowledge: exact recall of far-back items stays an attention strength).
- **Does not hold when**: tasks need exact lookup in very long inputs; hybrids that keep some attention layers address this.
