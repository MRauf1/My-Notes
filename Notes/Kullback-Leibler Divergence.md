---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Kullback-Leibler Divergence (Relative Entropy)[^1]
> The average additional information (in nats) needed to specify the value of $\mathbf{x}$ when it is coded using an approximating distribution $q(\mathbf{x})$ instead of the true distribution $p(\mathbf{x})$:
> $$
> \begin{align}
> \mathrm{KL}(p \| q) = -\int p(\mathbf{x}) \ln q(\mathbf{x})\,d\mathbf{x} - \left(-\int p(\mathbf{x}) \ln p(\mathbf{x})\,d\mathbf{x}\right) = -\int p(\mathbf{x}) \ln\left\{\frac{q(\mathbf{x})}{p(\mathbf{x})}\right\} d\mathbf{x}
> \end{align}
> $$

> [!abstract] Gibbs' Inequality[^2][^3][^4]
> $$
> \begin{align}
> \mathrm{KL}(p \| q) \geq 0, \quad \text{with equality if and only if } p(\mathbf{x}) = q(\mathbf{x}) \text{ for all } \mathbf{x}
> \end{align}
> $$
> *Proof.* $-\ln$ is [[Convex Function|convex]], so by [[Jensen's Inequality]] $f\left(\int \mathbf{x}\,p(\mathbf{x})\,d\mathbf{x}\right) \leq \int f(\mathbf{x})\,p(\mathbf{x})\,d\mathbf{x}$,
> $$
> \begin{align}
> \mathrm{KL}(p \| q) = -\int p(\mathbf{x}) \ln\left\{\frac{q(\mathbf{x})}{p(\mathbf{x})}\right\} d\mathbf{x} \geq -\ln\int q(\mathbf{x})\,d\mathbf{x} = 0
> \end{align}
> $$
> using the normalization $\int q(\mathbf{x})\,d\mathbf{x} = 1$. Strict convexity of $-\ln$ gives equality only when $q = p$.

# Properties
- Not symmetric: in general $\mathrm{KL}(p \| q) \not\equiv \mathrm{KL}(q \| p)$, so it is a measure of dissimilarity between distributions rather than a metric.[^1]
- The first term, $-\int p \ln q$, is the cross-entropy, so $\mathrm{KL}(p \| q) = \text{cross-entropy} - \mathrm{H}[p]$ ([[Cross-Entropy Loss]], [[Entropy]]).
- **Compression**: coding with the wrong distribution is necessarily less efficient, by at least $\mathrm{KL}(p \| q)$ on average ([[Noiseless Coding Theorem]]).[^5]
- **Equivalence with maximum likelihood**: fitting $q(\mathbf{x} | \boldsymbol{\theta})$ to data $\mathbf{x}_1, \dots, \mathbf{x}_N$ drawn from unknown $p$, the expectation over $p$ is approximated by a sample average,[^6]
$$
\begin{align}
\mathrm{KL}(p \| q) \simeq \frac{1}{N}\sum_{n=1}^N \left\{-\ln q(\mathbf{x}_n | \boldsymbol{\theta}) + \ln p(\mathbf{x}_n)\right\}
\end{align}
$$
  The second term is independent of $\boldsymbol{\theta}$ and the first is the negative log likelihood, so minimizing this KL divergence is equivalent to [[Maximum Likelihood Estimation|maximum likelihood]] ([[Density Estimation]]).
- [[Mutual Information]] is the KL divergence between a joint distribution and the product of its marginals.

[^1]: [Bishop, 2006, p. 55](zotero://open-pdf/library/items/5G99AZ8U?page=75&annotation=AU4JTTL2)
[^2]: [Bishop, 2006, p. 55](zotero://open-pdf/library/items/5G99AZ8U?page=75&annotation=RQNP4C83)
[^3]: [Bishop, 2006, p. 56](zotero://open-pdf/library/items/5G99AZ8U?page=76&annotation=9JI5Y8BL)
[^4]: [Bishop, 2006, p. 57](zotero://open-pdf/library/items/5G99AZ8U?page=77&annotation=DS4TLMUV)
[^5]: [Bishop, 2006, p. 57](zotero://open-pdf/library/items/5G99AZ8U?page=77&annotation=ZLT8Z9K5)
[^6]: [Bishop, 2006, p. 57](zotero://open-pdf/library/items/5G99AZ8U?page=77&annotation=SNY35FXQ)
