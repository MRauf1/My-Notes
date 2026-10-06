---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Gradient Checkpointing[^1]
> A method for reducing the memory needed by [[Backpropagation]] (Chen et al., 2016): during the forward pass the activations are stored only every $N$ layers, and during the backward pass the missing intermediate activations are recomputed from the nearest checkpoint.

# Properties
- Drastically reduces memory at the computational cost of performing the forward pass twice.
- Needed because training is memory-intensive: the parameters and the pre-activations of every hidden unit for every batch member must be kept for the backward pass.
- Alternatives: [[Micro-Batching]], and reversible networks ([[Residual Flow]]), in which the previous layer's activations can be computed from the current layer's, so nothing needs to be cached.

[^1]: [Prince, Ch. 7](zotero://select/library/items/T3V9WVXD)
