---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Rademacher Complexity[^1]
> A measure of [[Model Capacity]]: the expected empirical performance of a model class, with optimally chosen parameters, on data with random labels. For a class $\mathcal{F}$ and $ samples, with independent random signs $\sigma_i \in \{-1, +1\}$,[^2]
> 761831
> \begin{align}
> \mathcal{R}_N(\mathcal{F}) = \mathbb{E}_{S, \boldsymbol{\sigma}}\left[\sup_{f \in \mathcal{F}} \frac{1}{N}\sum_{i=1}^N \sigma_i f(\mathbf{x}_i)\right]
> \end{align}
> 761831

# Properties
- Measures how well the class can correlate with pure noise; unlike the [[VC Dimension]], it depends on the data distribution.
- Neyshabur et al. (2017) derive a lower bound on the generalization error of neural networks in terms of it.

[^1]: [Prince, p. 134](zotero://open-pdf/library/items/BWT7FYX5?page=148&annotation=EYUEGV6I)
[^2]: Formal definition added from general knowledge of learning theory.
