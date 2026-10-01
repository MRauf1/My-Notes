---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Micro-Batching[^1]
> A method for reducing training memory (Huang et al., 2019) that subdivides a batch into smaller sub-batches and aggregates the gradients from each sub-batch before applying a single update to the network.

# Properties
- Produces the same update as the full [[Batch Size|batch]], since the gradient of a sum of per-example losses is the sum of their gradients, while storing activations for only one sub-batch at a time (also called gradient accumulation).
- Complementary to [[Gradient Checkpointing]].

[^1]: [Prince, Ch. 7](zotero://select/library/items/T3V9WVXD)
