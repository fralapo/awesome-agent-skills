# Chapter 7: Scaling, Training, Serving, and Models versus Brains

## Core Idea
Scaling debates have two layers: a *mechanical* layer (how compute, memory and batching determine cost and speed) and an *interpretive* layer (what extra scale or extra inference buys in capability, and how that compares with brains). This chapter separates them. Positions are marked and dated; numbers are snapshots. Learning-theory background is in `ai-ml-concepts` ch07-ch08; memory arithmetic for quantised serving is in `software-architecture` ch25.

## 7.1 The roofline view of inference (mechanism)
- **Thesis**: time per step is at least the larger of the compute time and the memory time, which gives a strong predictor with a simple model.
- **Mechanism**: compute time is about batch size times active parameters divided by the chip's arithmetic throughput (attention compute is small and ignored). Memory time is the time to fetch *all* the weights (total parameters, not only active ones) plus the time to fetch each batch element's cached context (context length times bytes per token). Decoding grows a cache of past keys and values; each new token needs a pass through every layer and reads the whole cache.
- **Consequence**: batching many users shares the weight fetch across them; the economics of serving one user at a time can be about a thousand times worse than a well-batched service (one illustrative estimate). In a mixture-of-experts model only a fraction of the parameters is active per token (the dated example: about 37 billion active out of about 700 billion total).
- **Trade-off**: large batches raise throughput but add latency and cache memory; long contexts raise the cache term and eventually make memory, not arithmetic, the limit.
- **Does not hold when**: a different bottleneck dominates (network between chips, scheduling, prefill-heavy workloads).

## 7.2 Capacity: how many chips must hold the model (mechanism)
- **Mechanism**: memory demand is total parameters plus batch times context times bytes per token. Spread across the product of expert-parallel width and pipeline depth, per-chip demand is that total divided by the product.
- **Position**: because pipelining weights across several racks reduces the memory each chip needs, industry might get by with less memory per chip than it ships, so a world exists in which memory is both extremely scarce (consumer shortages) and arguably over-provisioned per chip.
- **Against**: pipelining adds latency and bubbles; capacity is also used for longer contexts and bigger batches, so demand fills any slack.
- **Falsified by**: a deployed system that serves frontier-size models at competitive cost with sharply less memory per chip.

## 7.3 In-context learning as learning (position)
- **Position**: attention can be viewed as gradient descent on the data in the context: in a linear-regression test, the loss after n examples in the prompt matched n steps of gradient descent, and n steps looked like n layers of in-context learning.
- **For**: unifies "learning in the forward pass" with training; suggests long-context training induces meta-learning.
- **Against**: shown in small, stylised settings; whether a frontier model implements anything like it is unverified.
- **Consequence (position)**: if the model "learns on the fly" from adversarial examples in a long prompt, safety training may be behaving like a different model than the one tested; many-example jailbreaks follow.
- **Falsified by**: mechanistic analyses of large models showing no gradient-like computation, or a prompt-based learning curve that does not match any optimisation procedure.

## 7.4 A very long context is already a superhuman capacity (position)
- **Position**: a model that ingests a million tokens (a whole code base) has a capacity no human has, even if it is less clever per token; what you want is breadth integrated into one answer.
- **Against**: long context is not the same as good use of it; recall and reasoning over a long context degrade.
- **Related claim (position)**: slow agent adoption is mainly a matter of reliability ("nines"), not of context length; long-horizon tasks multiply per-step error.
- **Falsified by**: agents with long context and low per-step error still failing long tasks (supports the context view) or the reverse.

## 7.5 Models are underparameterised: superposition (position + mechanism)
- **Mechanism**: when data are high-dimensional and sparse (any given feature appears rarely), even small models learn to pack more features than they have dimensions, accepting interference. Real-world data have this shape (one shirt, one can). Training on the whole internet puts a model in the *underparameterised* regime.
- **Consequence**: a larger model can keep representations cleaner, with less interference, so it learns more from the same data. This offers one explanation for why scaling helps beyond memorising more.
- **Against**: unit-level analyses mostly come from toy models; relationship to the overparameterisation story in learning theory is not settled (see `ai-ml-concepts` ch05).
- **Falsified by**: evidence that large models trained on the same data have no less feature interference than small ones.

## 7.6 Input-output curves: does AI beat diminishing returns? (position)
- **Mechanism**: look at how much input (researchers, capital) is needed per doubling of output. Over a period in which the compute per dollar rose about a million-fold, research effort needed rose about 18-fold; so each doubling of compute needed somewhat more researchers, but each doubling of *effective researchers* gave more than four doublings of compute (the figure comes from an older study; snapshot).
- **Position**: if AI systems can substitute for researchers, hardware that doubles also doubles the effective labour force, so more than one doubling of labour is available per doubling of need; the leftover accelerates progress. Software improvements and more hardware add to this.
- **Counter (bottlenecks)**: if some inputs cannot be automated (human decisions, experiments, scarce complementary resources), those inputs bound the whole; the slowest part of the system governs speed.
- **Reply**: automating tasks that humans do rarely but would be enormously valuable at scale (for example building tailored training curricula) can matter more than their current share of work; as AI takes over the most difficult parts, even the bottleneck falls.
- **Falsified by**: a sustained period of AI-assisted research in which output per unit of effective labour keeps falling faster than effective labour grows.
- **Does not hold when**: the new input is physically limited (energy, fabs; see ch06).

## 7.7 Brains and models: what is missing? (position)
- **Position A (omnidirectional prediction)**: a cortical area may be a general prediction engine that can predict any subset of variables from any other subset, rather than only the next token from the previous ones; this resembles probabilistic or energy-based models. A language model can mimic fill-in-the-middle only through emergent in-context behaviour.
- **Position B (a steering subsystem teaches attention)**: intelligence = a general world model plus an evolved subsystem that decides what is worth attending to and learning from; evolution may supply the "cost functions" at several levels; this is relevant for how different future intelligences might be (whether a pure single-goal maximiser could exist is left open; unverified).
- **Argument that cell machinery is implementation, not algorithm**: updating a synapse in a living cell requires a great deal of molecular machinery, whereas a digital system just changes a number; so the biological complexity may not add algorithmic content. A cited exception: timing of reflexes in the cerebellum appears partly stored in cell bodies, not only in synaptic connections.
- **Against**: absence of a known mechanism is not evidence of its non-existence; analogies with backpropagation remain unproven; how evolution encodes high-level desires has no good theory (unverified).
- **Falsified by**: a brain-inspired architecture with omnidirectional inference outperforming next-token models at equal compute, or a demonstration that the omitted biology is required.

## Checklist for this chapter
1. Is the limit compute time or memory time (and which memory: capacity or bandwidth)?
2. Does the cost claim assume batching that real traffic does not provide?
3. Is the scaling claim about capability or about cost?
4. Are non-automatable inputs named in any "intelligence explosion" argument?
