---
tags:
  - computer_science
  - computer_vision
---

# Definition

> [!info] Definition 1 (Evolution Strategy)
> With $\eta$ as the learning rate, $\sigma$ as the sampling [[Standard Deviation|standard deviation]], $M$ as the number of samples[^1]
> for $k=0, 1, ..., K-1$ do
> ...	for $i=1, 2, ..., M$ do
> $$
> \begin{align}
> \dots \epsilon_i \sim \mathcal{N}(0, \mathbf{I}) \\
> \dots s_i = J(\theta + \sigma \epsilon_i) \\
> \theta^{(k + 1)} \leftarrow \theta^k - \eta \frac{1}{\sigma M} \sum_{i=1}^{M} s_i \epsilon_i
> \end{align}
> $$

Evolution Strategy is used when the [[Gradient Descent|gradient descent]] struggles, such as with functions with near-zero [[Gradient Vector|gradients]]. The algorithms tries different perturbations $\epsilon_i$ to see which one leads to the lower loss and moves towards the $\epsilon_i$'s that decrease the loss.

# Properties
- An alternative to using a [[Surrogate Loss Function]] for obtaining a useful update direction when the true gradient is zero almost everywhere or otherwise unhelpful, since most [[Gradient-Based Learning|gradient-based optimizers]] only require some locally loss-minimizing direction, not necessarily the true gradient.
- A form of [[Zeroth-Order Optimization]], since it estimates a useful update direction from cost values alone, without an analytical gradient.

[^1]: https://visionbook.mit.edu/gradient_descent.html