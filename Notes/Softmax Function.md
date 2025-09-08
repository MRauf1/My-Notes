---
tags: computer_science, deep_learning
---

# Definition

> [!info] Definition
> [[Function|Function]] $\mathrm{softmax}: \mathbb{R}^K \rightarrow \mathbb{R}^K$ where $\mathrm{softmax}(\mathbf{z})$
> $$
> \begin{align}
> \hat{y}_j = \frac{e^{-z_j}}{\sum_{k=1}^{K} e^{-z_k}}
> \end{align}
> $$
> The values in $\mathbf{z}$ are called the logits and are the unnormalized log [[Probability|probabilities]].[^1]

[^1]: https://visionbook.mit.edu/intro_to_learning.html