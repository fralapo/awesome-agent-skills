# Chapter 13: Generative Models: Adversarial Games, Diffusion and Flow Matching

## Core Idea
A generative model learns a distribution over data so that new samples can be drawn. Three families dominate image-like data: adversarial pairs (one network generates, one judges), denoising diffusion (learn to undo small amounts of noise, sample by repeated denoising) and flow matching (learn a velocity field that carries noise to data). In this model they differ in what they train, how many steps sampling takes, and what can go wrong.

## 13.1 What "learning a distribution" asks for
- **Thesis**: a good generator must cover all kinds of data (diversity) and make each sample plausible (fidelity), and the two goals pull apart.
- **Mechanism**: the generator maps random noise to a sample; there is no single correct output for a given input, so training signals are about the whole distribution: a judge, a likelihood bound, or a matching of velocities. Quality is measured by distribution-level distances (for example a feature-space distance between generated and real image statistics) plus human looks.
- **Trade-off**: sharp samples may cover only part of the data; full coverage can be blurry.
- **Does not hold when**: you assume low distance between statistics guarantees every individual sample is good or novel (memorised training images are a risk).

## 13.2 The adversarial game
- **Thesis**: train a generator to fool a discriminator while the discriminator learns to tell real from generated.
- **Mechanism**: a minimax objective: the discriminator outputs the probability that a sample is real; the generator never sees real data directly, only the discriminator's gradient. In the original recipe the discriminator takes one step per generator step. At the idealised optimum the generated distribution equals the data distribution and the discriminator outputs one half everywhere. The generator is a smooth network, which makes memorising the training set hard; no inference procedure over latent variables is needed during training. Conditional versions feed a class label to both networks, and an extra encoder can map data back to noise.
- **Trade-off**: sharp samples and fast single-pass sampling against unstable training.
- **Does not hold when**: the discriminator is too weak or too strong: the generator then gets no useful gradient.

## 13.3 Mode collapse
- **Thesis**: the adversarial objective can reward producing the easiest few kinds of samples.
- **Mechanism**: the objective penalises different kinds of error differently, so the generator can settle on a part of the data the discriminator finds hard to reject and ignore the rest; the result is high-quality but narrow output. Later work added regularisers and different objectives.
- **Trade-off**: fidelity against coverage.
- **Does not hold when**: diversity is enforced by design (many noise samples scored jointly) or another family is used.

## 13.4 Denoising diffusion: undo small noise, repeat
- **Thesis**: instead of one jump from noise to image, learn many tiny reverse steps.
- **Mechanism**: the forward process adds a little Gaussian noise at each of thousands of steps until the image is pure noise; the network sees a noisy image and a step number and predicts how to remove noise, modelling the previous, slightly cleaner image as a Gaussian; that Gaussian assumption is acceptable only because the steps are tiny. Training samples a random step, noises a clean image to that level in one go and regresses the noise (the "simple" objective, with the variational bound as a variant). Sampling starts from pure noise and applies the network repeatedly. The relation to a variational autoencoder is that the chain of steps is the encoder and its reverse the decoder.
- **Trade-off**: stable training, high quality and diversity against many network evaluations per sample; more compute per sample can be spent on purpose.
- **Does not hold when**: latency is critical and a few-step or one-step sampler is unavailable.

## 13.5 Making training and sampling efficient
- **Thesis**: details of the loss and the sampler matter as much as the architecture.
- **Mechanism**: most of the variational loss comes from the earliest steps, so sampling steps uniformly gives an unbiased but noisy estimate; importance sampling over steps smooths training curves. Learning the covariance as well as the mean, mixing the variational and simple objectives, and using a deterministic sampler tied to score matching let an image model be sampled in about 25 steps instead of about 4000 (as reported at the time) with little loss in quality.
- **Trade-off**: fewer steps against a possible loss in diversity or detail.
- **Does not hold when**: you change the data modality: the schedule and importance weights were tuned on images.

## 13.6 Guidance: steering with a classifier
- **Thesis**: a classifier's gradient can steer a diffusion sampler toward a class, trading diversity for fidelity.
- **Mechanism**: at each step the gradient of the log-probability of the wanted class, computed on the noisy image, is added to the denoising direction, scaled by a guidance weight; a larger weight sharpens the conditional distribution, so samples look more typical of the class and vary less. Class information can also be fed into normalisation layers. In the original comparison, such a model beat a large adversarial model on the distance metric of the time and its samples were checked against the training set for copies (as reported at the time).
- **Trade-off**: tunable fidelity versus diversity; needs a classifier trained on noisy inputs (or a joint network).
- **Does not hold when**: no class labels exist, or the weight is so large that outputs become caricatures.

## 13.7 Flow matching: learn a velocity field
- **Thesis**: instead of a stochastic denoising chain, learn a vector field whose flow moves a simple distribution to the data distribution.
- **Mechanism**: a flow is the trajectory of every point moving along a time-dependent vector field; pushing the starting density through the flow gives a path of densities ending at the data. To sample, draw noise and integrate the field's ordinary differential equation from time 0 to 1 with a numerical solver. Directly regressing the unknown field is hard, so condition on one data point at a time: choose a path from the noise sample to that point (Gaussians with a mean and standard deviation that depend on time), whose velocity is known in closed form; averaging over all data points gives the aggregate field, and the conditional loss has the same gradients as the intractable one. Diffusion is the special case of curved Gaussian paths; the simplest alternative is a straight line from noise to data point, whose velocity does not depend on time, easier to learn and to integrate in few steps.
- **Trade-off**: a unifying, simpler framework and often fewer sampling steps against less mature tooling; the paths must still be chosen.
- **Does not hold when**: your problem needs stochastic dynamics or a likelihood that is easier under another formulation.

## 13.8 Generating actions: flow matching outside images
- **Thesis**: the same machinery produces smooth trajectories for robots.
- **Mechanism**: a robot policy built on a vision-language model adds a separate "action expert" that starts from random action trajectories and iteratively denoises them into a path, attending to the language model's cached keys and values (computed once per observation and reused at every denoising step). The robot executes a few steps, re-observes and repeats.
- **Trade-off**: smooth, multi-step outputs and efficient reuse of the cache against dependence on demonstration data (chapter 14.9).
- **Does not hold when**: the situation is far from the demonstrations.

## 13.9 What generators still get wrong
- **Thesis**: realism does not imply a correct model of the world.
- **Mechanism**: generated video and images can look right and break physics or object permanence over time; training objectives reward matching pixel statistics, and predictions of unpredictable details (leaves in the wind) absorb capacity. Predicting in an abstract space instead is an alternative bet (chapter 14.8).
- **Trade-off**: visual quality against consistency and cost.
- **Does not hold when**: the use is purely visual (art, concept exploration), where consistency is not required.
