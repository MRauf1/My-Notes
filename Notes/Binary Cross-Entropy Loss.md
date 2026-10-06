---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Binary Cross-Entropy Loss[^1]
> For [[Binary Classification]] with $y \in \{0, 1\}$, model the output with a [[Bernoulli Distribution]] whose parameter $\lambda = \mathrm{sig}[f[\mathbf{x}, \boldsymbol{\phi}]]$ is obtained by passing the network output through the logistic [[Sigmoid Function|sigmoid]] $\mathrm{sig}[z] = \frac{1}{1 + \exp[-z]}$. The negative log-likelihood is
> $$
> \begin{align}
> L[\boldsymbol{\phi}] = \sum_{i=1}^I -(1 - y_i)\log\left[1 - \mathrm{sig}[f[\mathbf{x}_i, \boldsymbol{\phi}]]\right] - y_i \log\left[\mathrm{sig}[f[\mathbf{x}_i, \boldsymbol{\phi}]]\right]
> \end{align}
> $$

# Properties
- An instance of the [[Maximum Likelihood Loss Function Recipe]]; the sigmoid maps the unbounded network output to the valid range $\lambda \in [0, 1]$.
- Called cross-entropy because minimizing it is equivalent to minimizing the [[Cross-Entropy Loss|cross-entropy]] between the empirical and model distributions.
- The two-class special case of the multiclass [[Cross-Entropy Loss]] with a [[Softmax Function|softmax]]; equivalent to the loss of [[Binary Logistic Regression]].
- With labels $y \in \{-1, +1\}$ and margin $z = y f[\mathbf{x}]$, it equals the logistic loss $\log[1 + e^{-z}]$ ([[Loss Function Taxonomy]]).
- The discriminator of a [[Generative Adversarial Network|GAN]] minimizes it with real examples labelled $1$ and generated samples $0$, while the generator maximizes it.

[^1]: [Prince, Ch. 5](zotero://select/library/items/T3V9WVXD)
