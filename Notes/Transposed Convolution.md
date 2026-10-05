---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Transposed Convolution[^1]
> A learned [[Upsampling (Deep Learning)|upsampling]] operation that reverses the connectivity of a [[Stride (Convolution)|strided]] [[Convolutional Layer|convolution]]: instead of each output being a weighted sum of $K$ nearby inputs, each input contributes $K$ weighted values to the output, which has $s$ times as many positions. If the strided convolution is the matrix $\boldsymbol{\Omega}$, i.e. $\mathbf{h} = \boldsymbol{\Omega}\mathbf{x}$, the transposed convolution computes
> $$
> \begin{align}
> \mathbf{h}' = \boldsymbol{\Omega}^T \mathbf{x}'
> \end{align}
> $$

![[Transposed Convolution 1D.png]]
*1D, kernel size three, stride two: (a, b) downsampling convolution and its weight matrix; (c, d) the transposed convolution, whose weight matrix is the transpose of (b).*[^2]

# Properties
- It is the transpose, not the inverse, of the strided convolution; the transpose is also exactly the map that [[Backpropagation]] applies to propagate gradients through the strided convolution.[^3]
- Introduced by Long et al. (2015) for semantic segmentation; Odena et al. (2016) showed it can produce **checkerboard artifacts** (uneven overlap of the kernel's contributions when the kernel size is not divisible by the stride), so it should be used with caution, e.g. replaced by resize-then-convolve.[^4]
- Also (misleadingly) called "deconvolution" or "fractionally strided convolution".[^3]

[^1]: [Prince, p. 172](zotero://open-pdf/library/items/BWT7FYX5?page=186&annotation=VFLG5CND); [Prince, p. 174](zotero://open-pdf/library/items/BWT7FYX5?page=188&annotation=ALVJCEVQ)
[^2]: [Prince, p. 173](zotero://open-pdf/library/items/BWT7FYX5?page=187&annotation=ALL4XZK6); [Prince, p. 173](zotero://open-pdf/library/items/BWT7FYX5?page=187&annotation=UNBS8B2R)
[^3]: Added from general knowledge.
[^4]: [Prince, p. 181](zotero://open-pdf/library/items/BWT7FYX5?page=195&annotation=GA9QQRVM)
