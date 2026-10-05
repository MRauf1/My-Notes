---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] 1x1 Convolution[^1]
> A [[Convolutional Layer|convolution]] with kernel size one, whose weights have size $1 \times 1 \times C_i \times C_o$: each output element is a weighted sum of all $C_i$ input channels at the same position, repeated with different weights for each of the $C_o$ output channels,
> $$
> \begin{align}
> h_{ijc} = \mathrm{a}\left[\beta_c + \sum_{c'=1}^{C_i} \omega_{c'c}\, x_{ijc'}\right]
> \end{align}
> $$

# Properties
- Changes the number of [[Feature Map|channels]] between layers without spatial pooling, usually so that the representation can be combined with another parallel computation (e.g. residual or multi-branch architectures).[^1]
- With a bias and activation function it is equivalent to running the same fully connected network ([[Linear Layer]]) on the channel vector at every position.[^1]
- Lin et al. (2014), *Network in Network*, is an early example.[^2]

[^1]: [Prince, p. 174](zotero://open-pdf/library/items/BWT7FYX5?page=188&annotation=W2QKD4EC); [Prince, p. 171](zotero://open-pdf/library/items/BWT7FYX5?page=185&annotation=2BL7VV7Z)
[^2]: [Prince, p. 181](zotero://open-pdf/library/items/BWT7FYX5?page=195&annotation=GA9QQRVM)
