# Chapter 14: Self-Supervised Learning, Representations and World Models

## Core Idea
Labels are scarce and data are abundant, so most modern systems learn first by predicting part of the data from other parts and later adapt to tasks. In this model the key design questions are: what is predicted (the next token, a masked token, a paired view, an embedding), how the model is stopped from cheating with a trivial answer (collapse), and how the learned representation is reused (fine-tuning, a prompt, a probe, planning).

## 14.1 Word vectors from prediction
- **Thesis**: training a shallow model to predict context words yields vectors in which meaning has geometry.
- **Mechanism**: the skip-gram objective predicts neighbouring words from a centre word. Computing a full softmax over a large vocabulary is expensive, so alternatives are used: a tree-structured softmax, noise-contrastive estimation, and negative sampling, a simplification that drops the likelihood approximation and just asks a logistic classifier to tell true context pairs from random ones. Very frequent words are subsampled. The vectors support analogy tests (a consistent direction relates related pairs) and phrases can be added as units. Careful, efficient code that ran on one machine contributed as much to adoption as the idea.
- **Trade-off**: fast static vectors (one vector per word, no context) against no handling of word senses; the negative-sampling trick became a cornerstone of contrastive learning.
- **Does not hold when**: context decides meaning; contextual models (14.3) take over.

## 14.2 Contrastive learning: positives, negatives and their cost
- **Thesis**: to learn a representation without labels, pull together views of the same thing and push apart different things.
- **Mechanism**: two augmented views of one item should map to similar embeddings, other items to dissimilar ones. If only positives were used, the network would map everything to one vector (collapse); negatives prevent it. It works on images, video and text-image pairs but needs large batches or many negatives, and a critic's argument is that in the worst case the number of negatives needed grows exponentially with the embedding dimension (position).
- **Trade-off**: simple objective against heavy compute and sensitivity to how negatives are chosen.
- **Does not hold when**: you can regularise the embedding statistics directly (14.7).

## 14.3 Autoregressive versus bidirectional pre-training
- **Thesis**: predicting the next token and predicting a masked token learn different things and suit different tasks.
- **Mechanism**: a decoder-only model predicts left to right, so its representation of a token sees only the past; it generates text and can be prompted. A bidirectional encoder masks random tokens and predicts them from both sides, adds a sentence-relation task, uses word pieces, three embeddings (token, segment, position) and a special classification token, and is then fine-tuned with a small task head (for example a per-token classifier for entities). Ablations showed that removing the sentence task lowered scores and restricting to left-to-right context lowered them much more, so the gain came from two-sided context, not only from size and data.
- **Trade-off**: encoders are strong at understanding tasks after fine-tuning; decoders generate and handle new tasks through prompts (chapter 8.10) but cannot condition on the right-hand side.
- **Does not hold when**: you need generation from an encoder, or sentence-level tasks the pre-training objective does not cover.

## 14.4 Zero-shot classifiers from paired text and images
- **Thesis**: training an image encoder and a text encoder to agree on image-text pairs yields a classifier whose classes are chosen at inference time as text.
- **Mechanism**: a contrastive objective on a very large set of image-text pairs; at test time each candidate label is turned into a sentence ("a photo of X, a type of Y"), embedded, and the image is assigned the nearest label. The text encoder is a transformer using the end-of-sentence token's vector; the image encoder is a residual network or a vision transformer, and compute, data and model size are scaled together. Prompt wording matters, and averaging over several prompt templates raises accuracy at no training cost. Zero-shot, it beat a fully supervised linear probe on a ResNet-50 baseline on 16 of 27 datasets (as reported at the time), while using no labels from those sets.
- **Trade-off**: flexible categories and broad robustness against weak performance on fine, specialised or counting tasks and dependence on the statistics of the paired text.
- **Does not hold when**: label sets include loaded categories: adding a "child" class sharply cut the misclassification of young people into other categories, and including categories such as criminal or non-human labels exposed bias, so the label list is a design decision with ethical weight.

## 14.5 Self-distillation without negatives
- **Thesis**: a student can learn to match a teacher that is just a slowly moving copy of itself, if collapse is prevented.
- **Mechanism**: take two augmented views, global and local crops, feed one to a student network and the other to a teacher with the same architecture whose weights are a moving average of the student's; the loss makes the student's output distribution over K learned dimensions match the teacher's, with no gradient into the teacher. Centring the teacher's outputs prevents one dimension from dominating, and sharpening (a low softmax temperature) prevents the uniform distribution; together they avoid collapse. The output dimensions act as self-chosen pseudo-classes. Resulting attention maps of a vision transformer segment objects without segmentation labels, and the features support nearest-neighbour classification and retrieval.
- **Trade-off**: no negatives, no labels; relies on hand-designed augmentations and on datasets whose pictures have a subject, so human attention is smuggled in as implicit supervision (a critical reading).
- **Does not hold when**: the data are arbitrary non-curated signals with no such structure.

## 14.6 Collapse and how to avoid it
- **Thesis**: any objective that only asks two embeddings to agree has a trivial solution (a constant), so each method needs a safeguard.
- **Mechanism**: safeguards: negatives (14.2), asymmetry with a moving-average teacher plus stop-gradient (14.5), centring and sharpening, and explicit regularisation of the embedding statistics (14.7). A generative objective is immune because reconstructing a specific input forces information, but it wastes capacity on unpredictable detail.
- **Trade-off**: each safeguard adds hyperparameters or compute.
- **Does not hold when**: your downstream task is trivially solved by the collapsed embedding (a bad probe can hide collapse).

## 14.7 Joint-embedding predictive architectures
- **Thesis**: predict the embedding of one part of the data from the embedding of another, not the data themselves, and keep the embeddings informative by regularisation.
- **Mechanism**: two encoders produce embeddings of an input x and a target y; a predictor, possibly with a latent variable for what cannot be known, predicts y's embedding from x's. The energy is low for compatible pairs and high for incompatible ones. To avoid collapse, regularise rather than use negatives: maximise the information content of the embeddings (for example keep the variance of each dimension above a floor and decorrelate dimensions, which can be done on a mini-batch) and minimise the information in the latent variable. Prediction heads can bias the embedding toward useful tasks. Predicting in latent space ignores unpredictable details (the motion of leaves in a driving video) and allows many correct paraphrases of an answer to map to similar targets, whereas a generative target penalises a correct answer that is phrased differently from the training example. A vision-language variant, trained under the same encoder, data and settings as a standard vision-language model, learned faster in one controlled report (as reported at the time; magnitude not stated here).
- **Trade-off**: efficiency and abstraction against a decoder-free system that is harder to inspect, and weaker demonstrated capability so far.
- **Does not hold when**: you must produce pixels or text; a separate decoder (used only for inspection) is then needed.

## 14.8 World models and planning in latent space
- **Thesis**: an agent that predicts the consequences of its actions can plan by searching over actions instead of reacting.
- **Mechanism**: train a predictor that takes the embedding of the current observation and an action and returns the embedding of the next observation; chaining it gives a learned simulator that can be inspected by a decoder. In a toy pushing task, eighteen steps in the learned model matched the real environment well with some drift (as reported at the time). Planning at inference minimises a cost over action sequences by optimisation or search (model-predictive control, re-planning as it goes). A first, reactive policy is cheap; a deliberate plan costs compute, and plans can be distilled into the reactive policy, like a skill becoming habit. Hierarchy helps: a high level predicts coarse states that serve as sub-goals for a low level with detailed short-term prediction; two levels extended a toy planning horizon from five to fifteen steps (as reported). Detailed predictions diverge quickly, so far-ahead plans must use fewer details.
- **Trade-off**: reliability and safety checks from foreseeing consequences against the effort to learn an accurate model and to search.
- **Does not hold when**: the learned model drifts or the real world has details the embedding drops; demonstrated robot capability of such systems lags the end-to-end alternatives (position: their advocates expect that to reverse; the claim is a forecast).

## 14.9 Robot brains as vision-language-action models
- **Thesis**: a multimodal language model trained to output robot actions can use web knowledge to handle objects and concepts absent from robot demonstrations.
- **Mechanism**: a staged history: a transformer imitating human control demonstrations; a language model also trained on vision-language tasks and on breaking tasks into steps; then the same model trained to emit actions. A demonstration moving a can onto a picture of a celebrity showed generalisation to concepts not in the robot data. A current design encodes each camera image into hundreds of embedding vectors, adds the text prompt tokens, runs a language model, and passes its cached keys and values to a flow-matching action expert (chapter 13.8); the robot acts a few steps and repeats.
- **Trade-off**: rapid progress on messy household tasks against limited generalisation beyond demonstration-like tasks, no explicit planning step and a black-box policy (criticisms from the world-model camp, a position; whether generalisation will become broad enough is open).
- **Does not hold when**: tasks need long-horizon planning or safety guarantees; demos remain demos.

## 14.10 Data construction is part of the learning signal
- **Thesis**: what pictures, descriptions and text people choose to produce already tells the model what matters.
- **Mechanism**: photographs have a subject because people take pictures of things they care about; descriptions pair salient content with words; filtered web text reflects editors' choices. Self-supervised methods therefore inherit human attention without any label.
- **Trade-off**: free supervision against built-in bias.
- **Does not hold when**: data come from sensors with no human selection; behaviour on such data should be tested, not assumed.
