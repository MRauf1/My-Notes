---
tags:
  - computer_science
  - computer_vision
---

# Definition

> [!info] Definition 1 (Layer Normalization)
> $$
> \begin{align}
> x_{out}[i] = \gamma \frac{x_{in}[i] - \mu}{\sigma} + \beta
> \end{align}
> $$
> where $\gamma, \beta$ are learnable parameters to allow the layer be expressive enough to output values with non-zero mean and non-zero variance

[[Normalization Layer|Normalization layer]] that standardizes the input with respect to the [[Mean|mean]] and [[Variance|variance]] of the channels of each datapoint (note the difference between [[Batch Normalization|BN]].[^1]

Unlike BN, layer normalization does not contradict the iid assumption.

Similar to [[L2 Normalization|L2 Normalization]], layer normalization also projects the input onto a unit [[Hypersphere|hypersphere]], but also centers and then potentially shifts and scales the inputs; it can be written as [[L2 Normalization|L2 normalization]] applied after first centering the activations to zero mean, followed by scaling and shifting by $\gamma$ and $\beta$.

If a batch is stored as a [[Tensor]] $\mathbf{X} \in \mathbb{R}^{N_{batch}\times C}$, layer normalization looks like a "transpose" of [[Batch Normalization|batchnorm]]: batchnorm standardizes each element by the mean and variance of its column (over the batch), while layer normalization standardizes each element by the mean and variance of its row (over the channels of that datapoint).

![[Normalization Schemes.png]]

# Properties
- **Convolutional case**: avoids batch statistics by normalizing each data example separately, with statistics gathered across both the channels and the spatial positions; there is still a separate learned scale $\gamma$ and offset per channel (Ba et al., 2016).[^2]
- Special case of [[Group Normalization]] with a single group containing all channels.
- Used in the [[Transformer Layer]], where it normalizes each token embedding separately over its $D$ dimensions. Vaswani et al. (2017) preferred it to [[Batch Normalization|BatchNorm]] because NLP statistics vary greatly between batches; placing it after the residual addition (Post-LN) makes gradients shrink through the network (Xiong et al., 2020).[^3]

[^1]: https://visionbook.mit.edu/neural_nets.html
[^2]: [Prince, p. 203](zotero://open-pdf/library/items/BWT7FYX5?page=217&annotation=E94CD4T3)
[^3]: [Prince, p. 216](zotero://open-pdf/library/items/BWT7FYX5?page=230&annotation=89AW73IT); [Prince, p. 237](zotero://open-pdf/library/items/BWT7FYX5?page=251&annotation=X6CE7KIZ)
