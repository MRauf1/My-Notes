---
tags: computer_science, computer_vision
---

# Definition

> [!info] Definition
> $$
> \begin{align}
> x_{out}[i] = \gamma \frac{x_{in}[i] - \mathbb{E}[x_{in}[i]]}{\sqrt{Var[x_{in}[i]]}} + \beta
> \end{align}
> $$
> where $\gamma, \beta$ are learnable parameters to allow the layer be expressive enough to output values with non-zero mean and non-zero variance

[[Normalization Layer|Normalization layer]] that standardizes the input with respect to the [[Mean|mean]] and [[Variance|variance]] of the batch of the inputs per channel.[^1]

Due to the reliance on the batch for each datapoint, it violates the assumption that the datapoints are processed independently and identically (iid).

At test time, the standard approach is to aggregate the statistics from the training dataset, but using test batch statistics can be useful to achieve invariance to changes in the statistics from the training data to the test data.

[^1]: https://visionbook.mit.edu/neural_nets.html