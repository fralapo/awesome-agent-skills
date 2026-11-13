# Chapter 1: Math Foundations: Linear Algebra and Calculus

## Core Idea
Almost all of modern machine learning is two ideas stacked: **linear maps** (matrix times vector, over and over) and **calculus** (how much does the output move when a number is nudged). In this model, a reader who holds these two pictures can follow every later chapter without memorising formulas.

## 1.1 Matrices are transformations, not tables
- **Thesis**: a matrix is a machine that moves every vector of a space; the numbers are just where the basis vectors land.
- **Mechanism**: the columns of a matrix are the images of the basis vectors, so any vector is moved by the same recipe (a weighted sum of those columns). Composition of transformations is matrix multiplication; order matters. The determinant is the factor by which areas or volumes scale (zero means the space is flattened and the map cannot be undone). The inverse exists only when nothing is flattened; the column space is what the map can reach and the null space is what it crushes to zero.
- **Trade-off**: the geometric picture is exact in two or three dimensions and only an analogy in thousands; the algebra stays valid, the visual intuition is a guide.
- **Does not hold when**: the operation is not linear (activation functions, softmax, layer normalisation); then the matrix picture describes one stage, not the whole model.

## 1.2 Rows as questions, columns as directions
- **Thesis**: a matrix-vector product can be read two ways, and each reading is useful in a different place.
- **Mechanism**: row by row, every output entry is a dot product, so each row asks "how much does the input align with this direction?". Column by column, the output is a sum of columns scaled by the input entries, so each column says "if this input unit is on, add this direction". The first reading explains detectors (a row tuned to a pattern); the second explains writers (a column that adds a feature to the result). Both readings return in the feed-forward blocks of transformers (chapter 7).
- **Trade-off**: none in the math; the risk is over-reading: a row or column is only "a feature" if training happened to make it one.
- **Does not hold when**: features are spread across many rows or columns at once (superposition, chapter 11).

## 1.3 Dot product as similarity
- **Thesis**: the dot product of two vectors measures alignment; attention scores, embedding similarity and neuron activations are all dot products.
- **Mechanism**: positive when pointing the same way, zero when perpendicular, negative when opposed; dividing by lengths gives cosine similarity. A weighted sum of inputs is a dot product of the input with the weight vector.
- **Trade-off**: raw dot products grow with vector length and dimension, which is why scores are rescaled before a softmax (chapter 7).
- **Does not hold when**: magnitude carries meaning that cosine similarity throws away.

## 1.4 Eigenvectors: directions a map only stretches
- **Thesis**: for a given linear map, special vectors stay on their own line and are merely scaled; the scale factors are the eigenvalues.
- **Mechanism**: solve for scalars where the map minus that scalar times the identity flattens space (determinant zero). In a basis made of eigenvectors the map is diagonal, which makes repeated application (powers, and the exponential of a matrix used for linear differential equations) easy: each eigen-direction just grows or decays on its own. A fast check for two-by-two cases is that the eigenvalues have the trace as their sum and the determinant as their product.
- **Trade-off**: powerful for analysis of linear systems and stability; real deep networks are not linear, so eigen-analysis applies locally or to specific sub-blocks.
- **Does not hold when**: the map has no real eigenvectors (a pure rotation) or lacks a full set of them; complex values or a more general decomposition are needed.

## 1.5 Derivatives as sensitivity
- **Thesis**: a derivative is the ratio of a tiny output change to the tiny input change that caused it; it answers "how sensitive is the output to this input?".
- **Mechanism**: the slope of the tangent line at a point; the best linear approximation of a function near that point. The reasoning habit: nudge the input by a small step, see the output nudge, take the ratio.
- **Trade-off**: local information only; it says nothing about distant parts of the function.
- **Does not hold when**: the function has kinks or jumps (the derivative is undefined or zero there), which is why training prefers smooth functions or accepts sub-gradients.

## 1.6 The chain rule: sensitivities multiply along a path
- **Thesis**: when a quantity depends on another through a chain of intermediate quantities, its sensitivity is the product of the sensitivities along the chain.
- **Mechanism**: nudging a weight nudges a pre-activation, which nudges an activation, which nudges the cost; multiply the three ratios. When a quantity influences the result through several parallel paths, add the path contributions. This is the entire mathematical content of backpropagation (chapter 4).
- **Trade-off**: exact but requires storing intermediate values from the forward pass.
- **Does not hold when**: a step is non-differentiable (hard rounding, sampling); the chain breaks and needs a surrogate or a different estimator.

## 1.7 Gradient: the direction of steepest increase
- **Thesis**: for a function of many inputs, the gradient collects every partial sensitivity into one vector pointing uphill; its negative points downhill.
- **Mechanism**: each component is the sensitivity to one input. Its sign says whether to nudge that input up or down; its relative size says which inputs matter most "for the bang for the buck". Its length says how steep the slope is.
- **Trade-off**: tells you the best direction for a small step, not how far to go or where the global minimum lies.
- **Does not hold when**: the surface is flat in many directions or has saddle points: a zero gradient does not prove a minimum.

## 1.8 Integrals and expectations
- **Thesis**: an integral accumulates a quantity; the fundamental theorem links it to derivatives (accumulate the rate of change and you recover the total change).
- **Mechanism**: area under a curve as a limit of thin slices. In probability, an expectation is an integral (or a sum) of value times probability, which is why sampling can approximate it (chapter 12).
- **Trade-off**: exact integrals exist for few functions; most real ones are approximated numerically or by sampling.
- **Does not hold when**: the integrand is highly peaked or high-dimensional; naive slicing explodes in cost.

## 1.9 Why high dimensions behave differently
- **Thesis**: in a space with thousands of dimensions, almost all random vectors are nearly perpendicular, and exponentially many directions can be kept nearly perpendicular to each other.
- **Mechanism**: only n vectors can be exactly perpendicular in n dimensions, but if "89 to 91 degrees" is accepted, the number that fits grows exponentially with the dimension. This is why embedding spaces can hold far more features than they have axes (chapter 7) and why distance in high dimensions is less discriminating than intuition suggests.
- **Trade-off**: capacity gain is paid with interference: features overlap slightly, which makes them hard to read out one at a time.
- **Does not hold when**: dimension is low (two or three), where the geometric intuition is correct and the exponential room does not exist.
