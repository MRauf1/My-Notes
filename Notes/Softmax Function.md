---
tags:
  - computer_science
  - deep_learning
---

# Definition

> [!info] Definition
> [[Function|Function]] $\mathrm{softmax}: \mathbb{R}^K \rightarrow \mathbb{R}^K$ where $\mathrm{softmax}(\mathbf{z})$
> $$
> \begin{align}
> \hat{y}_j = \frac{e^{z_j}}{\sum_{k=1}^{K} e^{z_k}}
> \end{align}
> $$
> The values in $\mathbf{z}$ are called the logits and are the unnormalized log [[Probability|probabilities]].[^1]

# Properties
- Maps an arbitrary length-$K$ vector to a vector of the same length with elements in $[0, 1]$ that sum to one: the exponentials ensure positivity and the denominator normalizes. Used to obtain the parameters of a categorical distribution for [[Multiclass Classification]] in the [[Maximum Likelihood Loss Function Recipe]], giving the [[Cross-Entropy Loss]].[^2]
- Sign convention: some texts write $e^{-z_j}$ (treating $\mathbf{z}$ as energies); with the logits interpreted as unnormalized log probabilities, the standard form is $e^{z_j}$.

[^1]: https://visionbook.mit.edu/intro_to_learning.html
[^2]: [Prince, Ch. 5](zotero://select/library/items/T3V9WVXD)
