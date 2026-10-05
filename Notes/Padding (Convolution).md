---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Padding (Convolution)[^1]
> Extending the edges of the input of a [[Convolutional Layer|convolution]] with new values, so that outputs whose kernel extends beyond the input (e.g. the first and last outputs) can be computed as usual.

# Types
- **Zero-padding**: assumes the input is zero outside its valid range.
- **Circular padding**: treats the input as periodic.
- **Reflection padding**: reflects the input at the boundaries.
- **No padding (valid convolution)**: discard the output positions where the kernel exceeds the range of input positions.

# Properties
- Valid convolutions introduce no extra information at the edges of the input, but the representation shrinks with each layer (by $K-1$ per dimension for kernel size $K$ and stride one).[^1]
- With stride one and odd kernel size $K$, zero-padding by $(K-1)/2$ on each side preserves the spatial size ("same" convolution).[^2]

[^1]: [Prince, p. 164](zotero://open-pdf/library/items/BWT7FYX5?page=178&annotation=FKRMB93U)
[^2]: Added from general knowledge.
