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

## 4.10 The perceptron: one neuron is one line
- **Thesis**: the atomic unit of every large network is a weighted sum of inputs plus a bias, with a decision on its sign; geometrically it draws one straight boundary.
- **Mechanism**: each input is multiplied by a dial (weight), the products and a bias are added, and a positive total means "yes". With two inputs the boundary is the line where the total is zero, with slope minus the first weight over the second and an intercept set by the bias; points on one side are positive. Big models stack millions of such units; an attention block can be read as a unit whose weights are produced by other units, so the data steers the computation.
- **Trade-off**: tiny, fast and easy to analyse; a single unit can only separate patterns that a line can separate.
- **Does not hold when**: the classes are not linearly separable in the input space (see 4.11), or you equate "neuron" with "biological neuron": it is a convenient arithmetic unit.

## 4.11 The perceptron learning rule and the exclusive-or wall
- **Thesis**: a simple error-driven rule is guaranteed to find a separating line if one exists, but one unit cannot learn exclusive-or.
- **Mechanism**: on a wrong answer, nudge every active weight by a fixed learning rate toward the correct sign (up for a missed positive, down for a false positive) and leave the weights alone on a correct answer; cycling through the examples converges when a separating line exists. Exclusive-or (positive when exactly one input is on) has no separating line, so the boundary keeps jumping. Two layers of three units solve it: the first layer draws two lines, the second combines them into a band. A period of pessimism followed, because a training rule for the multi-layer case was missing, and symbolic approaches dominated for years (historical position).
- **Trade-off**: guaranteed convergence in the separable case, silence in the other.
- **Does not hold when**: data are noisy and almost-separable (the rule never settles; a cost-minimising rule, 4.12, behaves better).

## 4.12 Least squares and the gradient of one neuron
- **Thesis**: instead of an ad hoc nudge, measure the error as a smooth cost and walk downhill on it.
- **Mechanism**: define the cost as half the sum of squared differences between target and output; for one neuron the derivative of the cost with respect to a weight is minus the error times the input that weight multiplies. The resulting update is the perceptron rule with the step multiplied by the current error, so large mistakes move the weights more. Scanning a grid of dial settings is hopeless beyond a few dials (ten values for each of sixteen inputs is about 10^17 evaluations), whereas the slope costs one formula.
- **Trade-off**: works on non-separable data and gives the right behaviour near the minimum; convergence still depends on the learning rate.
- **Does not hold when**: the output passes through a function with zero slope (4.13).

## 4.13 Why a binary step blocked multi-layer training
- **Thesis**: the all-or-nothing neuron of the early models made the chain rule useless, and replacing it with a smooth function unlocked deep learning.
- **Mechanism**: a step function has zero slope everywhere and an undefined slope at the jump, so the product of sensitivities (1.6) collapses to zero at the first layer boundary and the cost surface becomes flat plateaus and cliffs. Swapping in a sigmoid, and later a rectifier, gives a usable slope at every layer. Historically the gradient method was one small step from the full algorithm (position: the missing piece looks obvious in hindsight).
- **Trade-off**: smooth functions make learning possible; saturating ones (sigmoid) can still make slopes tiny far from the centre.
- **Does not hold when**: you want hard decisions at inference time; those can be applied after training.

## 4.14 Exact slopes versus numerical estimates
- **Thesis**: backpropagation gives the exact gradient of every parameter in one backward pass, whereas estimating slopes numerically needs a fresh forward pass per parameter.
- **Mechanism**: a numerical estimate changes one parameter, recomputes the loss and divides; it needs a step size and a forward pass for each of billions of parameters. The chain-rule version writes the slope of the loss with respect to a parameter as a product of local derivatives and reuses them across parameters, and the same formulas are applied as matrices for a whole layer. Gradient components have a sign convention: a negative slope means "increase this parameter"; the update subtracts the learning rate times the gradient. Numerical estimates remain useful as a check that an implementation of the formulas is correct.
- **Trade-off**: speed and accuracy against the need to implement and store intermediate values.
- **Does not hold when**: a part of the model is non-differentiable; then other estimators are needed.

## 4.15 High-dimensional loss landscapes are not valleys with traps
- **Thesis**: the picture of a ball rolling into a local valley misleads; in very high dimensions gradient descent usually finds low-loss regions.
- **Mechanism**: a landscape of a billion parameters can only be drawn as a two-dimensional slice, and that slice changes dramatically after even a tiny step in the full space, so the visual impression is of a path suddenly opening toward a low valley rather than a ball descending. Early researchers dismissed gradient descent for fear of local minima; in practice, with many parameters, genuine traps are rare and flat directions and saddles dominate. Training a model on a single short phrase drives the probability of the target token close to one very quickly.
- **Trade-off**: reliable training of big models against no guarantee of reaching the best solution.
- **Does not hold when**: models are small or poorly initialised; plateaus, bad learning rates and unstable depth (6.8) still stall training. Landscape pictures are shadows of the real process (position).

## 4.16 Depth, folding and universal approximation
- **Thesis**: stacked units with a nonlinearity can approximate any function, but the theorem says nothing about how to find the weights or how many units are needed.
- **Mechanism**: without a nonlinearity two linear layers collapse into one linear map. A rectifier clips negative heights to zero, which folds the plane along a line; two folding units create four regions, and a second layer folds the already folded surface, so two extra units can raise the count to ten regions with a piecewise-linear decision boundary. The universal approximation theorem (1989) guarantees that a two-layer network exists for any target function and precision. For a broad class of functions a shallow network needs exponentially more units than a deep one, so "one very wide layer" is not a free substitute for depth.
- **Trade-off**: expressive power against the search problem of finding good weights by gradient descent.
- **Does not hold when**: you read the theorem as a recipe; a wide network may contain a good solution that gradient descent never reaches.
