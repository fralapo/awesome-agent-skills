# Chapter 25: Serving LLMs: Memory and Quantization

## Core Idea
Serving a language model is first an exercise in **memory arithmetic**: the weights must sit in accelerator memory before a single token is produced, and the numbers that fill that memory are far more precise than inference needs. In this model, quantization is the main lever that trades a controlled loss of precision for memory and speed, and the architecture question is where it is applied (weights ahead of time, cache entries on the fly). Capabilities, prices and formats change quickly; figures here are illustrations, and anything marked "general knowledge" is background knowledge. The retrieval and agent layers around a served model are in ch10 and ch11.

## 25.1 Weights set a hard memory floor
- **Thesis**: before any request is served, parameters times bytes per parameter must fit in memory.
- **Mechanism**: a parameter is a floating-point number; at 4 bytes each (32-bit), a one-billion-parameter model needs about 4 GB just to be loaded, and that excludes the **KV cache** and the other runtime overhead. Models are usually published in 16-bit formats (two common variants differ in how many bits go to exponent versus mantissa); training needs this precision because the loss is minimised through very small updates.
- **Trade-off**: bigger models fit fewer replicas per device; every halving of bytes per weight roughly doubles what fits.
- **Does not hold when**: the model is small relative to memory and the limit is compute or request rate instead.

## 25.2 Why integers: space and arithmetic
- **Thesis**: representing weights as small integers cuts memory and makes the multiply-and-add inner loop cheaper.
- **Mechanism**: a floating-point number is stored as a mantissa and an exponent, so adding two of them needs the parts handled separately and the result renormalised (stated as several cycles) while integer addition is one cycle and cheaper in energy (the cycle counts are an illustration, not a benchmark). Quantization maps a continuous range onto a small set of integer levels: for example the range of a layer's weights onto 16 levels for 4-bit values (16 levels, general knowledge). The map is lossy: many floating-point values share one level.
- **Trade-off**: memory and speed against rounding error.
- **Does not hold when**: the hardware has no fast low-precision path, so the integer form is converted back to floats anyway (the saving is then memory only; general knowledge).

## 25.3 Why the loss is tolerable at inference
- **Thesis (position)**: precision matters during training but mostly washes out in inference.
- **Mechanism**: inference is a chain of matrix multiplications; small rounding errors in individual weights tend to cancel inside the dot product, so the output changes little. Training needs the fidelity because the optimiser works with tiny differences.
- **Trade-off**: some quality loss grows as the bit width shrinks; the acceptable width depends on the model and the task.
- **Does not hold when**: a task is sensitive to small differences (reasoning, long chains, rare tokens) or when a few weights carry outsized influence (outliers); verify on your own evaluation set rather than assuming.

## 25.4 Where to quantize: after training, during training, not at serving time for weights
- **Thesis**: quantize weights once, ahead of time; quantize the cache on the fly.
- **Mechanism**: **post-training quantization** converts a published high-precision model into a quantized variant; some publishers also release quantized variants themselves. **Quantization-aware training** adds the rounding noise during training so the model adapts (untested here; general knowledge). Quantizing the weights *at inference time* defeats the purpose: you would still stream the full-precision weights across the memory bus for every token and hold them in memory, so no bandwidth or memory is saved. What *can* be quantized on the fly is the **KV cache**, because those vectors are generated during serving.
- **Trade-off**: an offline conversion step and a separate artifact per bit width, against a leaner serving path.
- **Does not hold when**: you serve a model that is already published in the target precision.

## 25.5 Symmetric versus asymmetric mapping, and the scale factor
- **Thesis**: the mapping must use all the available integer levels, and must be undone by one real-valued factor.
- **Mechanism**: in **symmetric** quantization real zero maps to integer zero and the range is mirrored (for 4-bit signed, about minus 7 to plus 7); if the real values only occupy one side, half the levels are wasted. **Asymmetric** quantization chooses where real zero falls, from the observed distribution, so all levels are used (useful with activation functions whose outputs are non-negative). A **scale factor** (a real number, such as 0.0038) says how much real value one integer step represents. Quantized values are multiplied and summed as integers, and the scale is applied **once to the finished dot product**, not to every weight, so the floating-point step happens once per row rather than once per multiplication.
- **Trade-off**: asymmetric mapping uses the range better but needs a stored offset and a little extra arithmetic.
- **Does not hold when**: the distribution is already centred and bounded, where symmetric is simplest.

## 25.6 Capacity thinking for a serving tier (general knowledge)
- **Thesis**: size memory as weights plus KV cache plus overhead, and size throughput by what the memory can hold.
- **Mechanism**: the KV cache grows with context length and with the number of concurrent sequences, so after the weights are placed, the remaining memory sets how many requests can be in flight; quantizing weights frees memory for more of them, and quantizing the cache stretches it further. Always measure on real prompts: peak memory depends on context length distribution, batch policy and the serving engine.
- **Trade-off**: a lower bit width increases concurrency and may lower answer quality; a higher one does the reverse.
- **Does not hold when**: requests are few and short, so memory is not the constraint.

## 25.7 Checklist
1. Compute weight memory (parameters x bytes per parameter) and compare with the device.
2. Pick a bit width from a quality test on your own task, not from a headline benchmark.
3. Quantize weights offline; consider quantizing the cache at serving time.
4. Re-measure memory, latency and quality after each change; keep the original model as the reference for evaluation (see the evaluation section of ch10).
