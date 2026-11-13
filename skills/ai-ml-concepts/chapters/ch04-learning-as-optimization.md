# Chapter 4: Learning as Optimization

## Core Idea
A neural network is a function with many adjustable numbers. "Learning" means choosing those numbers to make a cost small, using the gradient to step downhill. In this model, this single picture explains training, its failures (local minima, plateaus, confident nonsense) and why data and cost design matter more than the optimizer detail.

## 4.1 A network is a function with knobs
- **Thesis**: a layered network is a long composition of matrix products, shifts (biases) and simple nonlinear functions; for a small digit classifier it has on the order of thirteen thousand parameters, for a large language model hundreds of billions.
- **Mechanism**: each layer takes a weighted sum of the previous layer's activations, adds a bias, and applies a nonlinearity. Activations in the first layer are the input; in the last layer, a score for each class. The weights decide which patterns a neuron detects; the bias decides how strong the evidence must be before it activates. The older squashing function (sigmoid) has largely been replaced by a clipping function (ReLU) that trains more easily in deep networks.
- **Trade-off**: more parameters give more expressive power and more risk of overfitting (chapter 5) and cost.
- **Does not hold when**: the hoped-for story ("layer two finds edges, layer three finds loops") is taken as fact: after training, hidden units can look almost random.

## 4.2 The cost function
- **Thesis**: the cost turns "performance on the examples" into a single number that depends on all the parameters.
- **Mechanism**: squared differences between output and target for regression-style setups; cross-entropy for classification and language (chapter 3). Average over the training set. Smooth, continuous activations make the cost smooth, so small changes in a parameter produce small changes in the cost.
- **Trade-off**: you get what you measure: a cost that rewards confident answers on a narrow world produces a network that is confident about everything, including noise.
- **Does not hold when**: the true goal cannot be written as a differentiable per-example cost (use preference or reward learning, chapter 8).

## 4.3 Gradient descent
- **Thesis**: repeatedly stepping against the gradient finds a local minimum of the cost.
- **Mechanism**: compute the gradient, take a small step downhill, repeat; steps proportional to the slope shrink near a minimum and reduce overshoot. Components of the gradient show which parameters matter most. In one dimension the picture is a ball rolling into a valley; in thousands of dimensions the geometry is unimaginable, but the algorithm is identical.
- **Trade-off**: step size too small is slow, too large oscillates or diverges; no guarantee of reaching the global minimum.
- **Does not hold when**: the cost surface is rugged or the gradient is noisy beyond use; then momentum, adaptive step sizes, or better initialisation are needed.

## 4.4 Backpropagation: efficient gradients by the chain rule
- **Thesis**: backpropagation computes the gradient for all parameters in about the cost of two passes through the network, by reusing intermediate results.
- **Mechanism**: forward pass stores activations. Backward pass starts at the output: for each output neuron, how much should it change and in which direction (proportional to its error). That "desire" is pushed back to the previous layer in proportion to the connecting weights, summed over every neuron it influences; at each layer, the weight gradient is that desire times the incoming activation (a loose echo of "neurons that fire together wire together"). Averaging the desired nudges over all examples gives the gradient of the average cost.
- **Trade-off**: memory for stored activations; vanishing or exploding signals in very deep stacks without careful design.
- **Does not hold when**: parts of the pipeline are discrete or non-differentiable (sampling, search); then reinforcement-style estimators are used.

## 4.5 Stochastic gradient descent and mini-batches
- **Thesis**: a gradient from a small random batch is a noisy but good estimate of the full gradient and is much cheaper.
- **Mechanism**: shuffle the data, split into batches of tens to thousands of examples, step on each batch. The path is erratic ("a stumbling walk downhill") but progresses faster per unit of compute; noise can even help escape poor regions.
- **Trade-off**: batch size trades noise against hardware efficiency and generalisation.
- **Does not hold when**: batches are very small and unrepresentative, or the data is not shuffled (ordered data biases each step).

## 4.6 Local minima, plateaus and what "found a solution" means
- **Thesis**: the optimiser finds a point where the cost is low on training data; this need not be the best or the only solution, and it need not resemble the human-designed solution.
- **Mechanism**: with a huge parameter space, many different settings give similar cost; reported observations suggest the minima reached are often of similar quality when the data has real structure, and that training on structured labels converges much faster than on random labels. A network can nevertheless reach the same training accuracy on completely shuffled labels (it memorises), showing that low training cost alone does not prove learned structure.
- **Trade-off**: flexibility to fit anything is also the risk of fitting nothing meaningful.
- **Does not hold when**: you read the final weights as an explanation: interpretation needs separate evidence (chapter 11).

## 4.7 Optimization in general
- **Thesis**: optimisation means choosing variables to minimise or maximise an objective; many problems (a bridge with minimal material, a recipe, a network) are cast this way, and the real question is whether they can be solved quickly and reliably.
- **Mechanism**: variables, objective, constraints; gradient descent is the simplest optimiser; hand-designed optimisers are mostly written by experts. Research has shown that an optimiser itself can be learned, outperforming hand-made ones on a set of specialised problems.
- **Trade-off**: learned optimisers can win on a narrow family and may not transfer.
- **Does not hold when**: the objective is poorly specified: the optimiser will exploit the gap (chapter 10).

## 4.8 Classical alternatives: trees and boosting
- **Thesis**: many weak learners combined by scoring can beat one big model on tabular data, and are inspectable.
- **Mechanism**: a shallow decision tree is only slightly better than chance; boosting adds trees one after another, each fitted to the errors of the committee so far, and sums their scores. Gradient-boosted trees are a common winner on structured data.
- **Trade-off**: transparent decisions and good accuracy on tables; poor fit for raw images, audio and text, where learned representations win.
- **Does not hold when**: the data is unstructured or very large and sequential.

## 4.9 Data labels are the bottleneck
- **Thesis**: supervised learning needs a lot of labelled data, and getting labels is often harder than training.
- **Mechanism**: labelled sets (such as a standard digit set) made progress possible; modern pre-training avoids human labels by using the next token as the label (chapter 8); preference learning uses fewer, cheaper judgements (chapter 8).
- **Trade-off**: label quality caps what can be learned; errors in labels become errors in models and in benchmarks (chapter 9).
- **Does not hold when**: the task can be self-supervised from raw data.
