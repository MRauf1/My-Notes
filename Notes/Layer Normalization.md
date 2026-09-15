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

[^1]: https://visionbook.mit.edu/neural_nets.html