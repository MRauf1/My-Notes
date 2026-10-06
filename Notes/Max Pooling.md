---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Max Pooling[^1]
> A [[Downsampling (Deep Learning)|downsampling]] operation that retains the maximum of each block of input values (typically $2 \times 2$), separately for each channel:
> $$
> \begin{align}
> h_{ij} = \max\{x_{2i-1,2j-1},\, x_{2i-1,2j},\, x_{2i,2j-1},\, x_{2i,2j}\}
> \end{align}
> $$

# Properties
- Induces some translation [[Invariant Function|invariance]]: if the input is shifted by one pixel, many of the maxima remain the same.[^1]
- Has no parameters; the gradient flows only to the maximal element of each block ([[Backpropagation]]).[^2]
- Can be reversed approximately by [[Max Unpooling]].
- On graphs, the element-wise maximum over a node's neighbours is a permutation-invariant [[Neighborhood Aggregation (Graph Neural Network)|aggregation]] operator.[^4]
- Wu & Gu (2015) adapted it for [[Dropout]] by sampling from a probability distribution over the constituent elements rather than always taking the maximum.[^3]

[^1]: [Prince, p. 172](zotero://open-pdf/library/items/BWT7FYX5?page=186&annotation=YWT9TXL4)
[^2]: Added from general knowledge.
[^3]: [Prince, p. 183](zotero://open-pdf/library/items/BWT7FYX5?page=197&annotation=V6VYB47L)
[^4]: [Prince, p. 258](zotero://open-pdf/library/items/BWT7FYX5?page=272&annotation=7RF6CS87)
