---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Jensen-Shannon Divergence[^1]
> A symmetrized, smoothed version of the [[Kullback-Leibler Divergence]] that measures each distribution against their equal-weight [[Mixture Distribution|mixture]] $m = \frac{1}{2}(p + q)$:
> $$
> \begin{align}
> D_{JS}\left[p \,\|\, q\right] &= \frac{1}{2} D_{KL}\left[p \,\Big\|\, \frac{p + q}{2}\right] + \frac{1}{2} D_{KL}\left[q \,\Big\|\, \frac{p + q}{2}\right] \\
> &= \frac{1}{2}\int p(\mathbf{x}) \log\left[\frac{2p(\mathbf{x})}{p(\mathbf{x}) + q(\mathbf{x})}\right] d\mathbf{x} + \frac{1}{2}\int q(\mathbf{x}) \log\left[\frac{2q(\mathbf{x})}{p(\mathbf{x}) + q(\mathbf{x})}\right] d\mathbf{x}
> \end{align}
> $$

# Properties
- Symmetric, $D_{JS}[p \| q] = D_{JS}[q \| p]$, and bounded: $0 \leq D_{JS} \leq \log 2$, with $0$ iff $p = q$ and $\log 2$ iff $p$ and $q$ have disjoint supports. Its square root is a [[Metric|metric]].
- Always finite, unlike the KL divergence, since $p$ and $q$ are both absolutely continuous with respect to the mixture.
- **Quality vs. coverage** (with $p = Pr(\mathbf{x}^*)$ the model and $q = Pr(\mathbf{x})$ the data):[^1][^2]
	- The first term is small if, wherever the sample density is high, the mixture is high: it penalizes samples where there is no real data, enforcing **quality**.
	- The second term is small if, wherever the true density is high, the mixture is high: it penalizes real data where there are no samples, enforcing **coverage**.
- **Saturates for disjoint supports**: once $p$ and $q$ do not overlap, $D_{JS} = \log 2$ regardless of how far apart they are, so it gives no gradient for bringing them closer; the [[Wasserstein Distance]] does not have this problem.[^3]
- The original [[Generative Adversarial Network|GAN]] objective with an optimal discriminator equals $\log 4 - 2 D_{JS}[Pr(\mathbf{x}^*) \| Pr(\mathbf{x})]$.[^1]

[^1]: [Prince, p. 282](zotero://open-pdf/library/items/BWT7FYX5?page=296&annotation=7IKS8BK7)
[^2]: [Prince, p. 283](zotero://open-pdf/library/items/BWT7FYX5?page=297&annotation=ZD6YAEMZ)
[^3]: [Prince, p. 283](zotero://open-pdf/library/items/BWT7FYX5?page=297&annotation=V9QJTZ5H)
