---
tags: computer_science, computer_vision
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

Similar to [[L2 Normalization|L2 Normalization]], layer normalization also projects the input onto a unit [[Hypersphere|hypersphere]], but also centers and then potentially shifts and scales the inputs.
#TODO 
- Write layernorm in terms L2 normalization

[^1]: https://visionbook.mit.edu/neural_nets.html