---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Convolutional Layer[^1]
> A network layer that convolves its input with a learned **kernel** (or **filter**) $\boldsymbol{\omega}$, i.e. computes at every position a weighted sum of nearby inputs using the same weights everywhere, adds a bias $\beta$, and passes each result through an [[Activation Layer|activation function]] $\mathrm{a}[\cdot]$. In 1D with kernel size $K = 3$:
> $$
> \begin{align}
> h_i = \mathrm{a}\left[\beta + \omega_1 x_{i-1} + \omega_2 x_i + \omega_3 x_{i+1}\right]
> \end{align}
> $$
> In 2D with a $3 \times 3$ kernel $\boldsymbol{\Omega} \in \mathbb{R}^{3\times 3}$ the kernel is translated both horizontally and vertically across the input:
> $$
> \begin{align}
> h_{ij} = \mathrm{a}\left[\beta + \sum_{m=1}^{3}\sum_{n=1}^{3} \omega_{mn}\, x_{i+m-2,\, j+n-2}\right]
> \end{align}
> $$

The size of the region over which inputs are combined is the **kernel size**. Since it uses the same weights at every position, a convolutional layer processes each local region independently with parameters shared across the whole input; it uses far fewer parameters than a [[Linear Layer|fully connected layer]], exploits the statistical dependence of nearby pixels, and does not need to re-learn the interpretation of a pattern at every position.[^2]

# Types
- [[Dilated Convolution]]
- [[Transposed Convolution]]
- [[1x1 Convolution]]
- Members of the general family are distinguished by their [[Stride (Convolution)|stride]], kernel size, and dilation rate, and by their boundary handling ([[Padding (Convolution)]]).[^3]

# Properties
- **Translation [[Equivariant Function|equivariance]]**: translating the input translates the output in the same way.[^1]
- **Special case of a fully connected layer**: with $D$ inputs and $D$ hidden units a [[Linear Layer|fully connected layer]] has $D^2$ weights and $D$ biases, while the $K=3$ convolutional layer has 3 weights and 1 bias. A fully connected layer reproduces it exactly if most weights are set to zero and the rest are constrained to be identical, so its weight matrix is sparse and banded with repeated entries (a Toeplitz matrix); other variants (e.g. other strides) correspond to different sparse weight structures.[^4]
- **Channels**: a single convolution loses information (it averages nearby inputs, and a [[ReLU Function|ReLU]] clips negative results), so several convolutions are computed in parallel; each produces a [[Feature Map]] (channel).[^5]
- **Parameter count**: with $C_i$ input channels and $C_o$ output channels, each output channel is a weighted sum over all $C_i$ channels and all kernel entries plus one bias. In 1D with kernel size $K$ this needs $\boldsymbol{\Omega} \in \mathbb{R}^{C_i \times C_o \times K}$ and $\boldsymbol{\beta} \in \mathbb{R}^{C_o}$; in 2D with a $K \times K$ kernel it needs $C_i \times C_o \times K \times K$ weights and $C_o$ biases (e.g. an RGB image is a 2D signal with $C_i = 3$ channels). The count is independent of the spatial size of the input.[^6]
- **Inductive bias**: forcing every position to be processed in the same way embeds prior knowledge (e.g. that objects are translated templates), so the network searches a smaller family of plausible input/output mappings and generalizes better than a fully connected network on the same data; equivalently, the convolutional structure is a [[Regularization|regularizer]] that applies an infinite penalty to most solutions a fully connected network can describe ([[Inductive Bias]]).[^7]
- Stacking convolutional layers grows the [[Receptive Field]] of the hidden units, gradually integrating information across the input ([[Convolutional Neural Network]]).
- Output length along one dimension, for input length $N$, padding $P$ per side, kernel size $K$, stride $s$, and dilation $d$: $\left\lfloor \frac{N + 2P - d(K-1) - 1}{s} \right\rfloor + 1$.[^8]
- What deep learning calls convolution is, strictly, [[Cross Correlation|cross-correlation]] (the kernel is not flipped); since the kernel is learned, the distinction is immaterial.[^8]

[^1]: [Prince, p. 163](zotero://open-pdf/library/items/BWT7FYX5?page=177&annotation=CDIV2Z4I); [Prince, p. 165](zotero://open-pdf/library/items/BWT7FYX5?page=179&annotation=VVB64TAG); [Prince, p. 170](zotero://open-pdf/library/items/BWT7FYX5?page=184&annotation=HX4JTQUR)
[^2]: [Prince, p. 161](zotero://open-pdf/library/items/BWT7FYX5?page=175&annotation=TULQ84TG); [Prince, p. 161](zotero://open-pdf/library/items/BWT7FYX5?page=175&annotation=B4WFN4CF)
[^3]: [Prince, p. 164](zotero://open-pdf/library/items/BWT7FYX5?page=178&annotation=NIEYTC3F); [Prince, p. 165](zotero://open-pdf/library/items/BWT7FYX5?page=179&annotation=D2WUA2RM)
[^4]: [Prince, p. 165](zotero://open-pdf/library/items/BWT7FYX5?page=179&annotation=PTGIK5DM); [Prince, p. 166](zotero://open-pdf/library/items/BWT7FYX5?page=180&annotation=22MR9LUL); [Prince, p. 166](zotero://open-pdf/library/items/BWT7FYX5?page=180&annotation=M74JCW7C)
[^5]: [Prince, p. 165](zotero://open-pdf/library/items/BWT7FYX5?page=179&annotation=RR6LJUI2)
[^6]: [Prince, p. 167](zotero://open-pdf/library/items/BWT7FYX5?page=181&annotation=REWX9AMS); [Prince, p. 170](zotero://open-pdf/library/items/BWT7FYX5?page=184&annotation=IN8DPHQX)
[^7]: [Prince, p. 170](zotero://open-pdf/library/items/BWT7FYX5?page=184&annotation=ZKKHF27M); [Prince, p. 170](zotero://open-pdf/library/items/BWT7FYX5?page=184&annotation=EE2MMBYY)
[^8]: Added from general knowledge.
