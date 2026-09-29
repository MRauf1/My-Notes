---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!abstract] Regression Function[^1][^2]
> Under squared loss, the expected loss $\mathbb{E}[L] = \iint \{y(\mathbf{x}) - t\}^2\,p(\mathbf{x}, t)\,d\mathbf{x}\,dt$ is minimized by the conditional average of $t$ given $\mathbf{x}$, called the regression function:
> $$
> \begin{align}
> y(\mathbf{x}) = \frac{\int t\,p(\mathbf{x}, t)\,dt}{p(\mathbf{x})} = \int t\,p(t | \mathbf{x})\,dt = \mathbb{E}_t[t | \mathbf{x}]
> \end{align}
> $$
> For a vector of targets, the optimum is likewise $\mathbf{y}(\mathbf{x}) = \mathbb{E}_{\mathbf{t}}[\mathbf{t} | \mathbf{x}]$.

> [!abstract] Decomposition of the Expected Squared Loss[^3]
> $$
> \begin{align}
> \mathbb{E}[L] = \int \{y(\mathbf{x}) - \mathbb{E}[t | \mathbf{x}]\}^2\,p(\mathbf{x})\,d\mathbf{x} + \int \mathrm{var}[t | \mathbf{x}]\,p(\mathbf{x})\,d\mathbf{x}
> \end{align}
> $$
> obtained by writing $y - t = (y - \mathbb{E}[t | \mathbf{x}]) + (\mathbb{E}[t | \mathbf{x}] - t)$; the cross-term vanishes on integrating over $t$.

# Properties
- Only the first term depends on $y(\mathbf{x})$ and vanishes when $y(\mathbf{x}) = \mathbb{E}[t | \mathbf{x}]$: the optimal least-squares predictor is the conditional mean ([[Conditional Expectation]]).
- The second term is the variance of $t$ averaged over $\mathbf{x}$: the intrinsic variability (noise) of the targets. It is independent of $y$, so it is the irreducible minimum of the expected loss; it is the $\mathrm{Var}[\epsilon]$ term of the [[Bias-Variance Tradeoff]].
- Other losses give other optimal point predictions: the [[Minkowski Loss]] yields the conditional median for $q = 1$ and the conditional mode as $q \to 0$.
- Learning $y(\mathbf{x})$ directly is the third of the [[Three Approaches to Decision Problems]] for regression.

[^1]: [Bishop, 2006, p. 46](zotero://open-pdf/library/items/5G99AZ8U?page=66&annotation=XPQUH6VU)
[^2]: [Bishop, 2006, p. 47](zotero://open-pdf/library/items/5G99AZ8U?page=67&annotation=6XQY9U9C)
[^3]: [Bishop, 2006, p. 47](zotero://open-pdf/library/items/5G99AZ8U?page=67&annotation=CWSF9YFJ)
