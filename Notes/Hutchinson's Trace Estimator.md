---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Hutchinson's Trace Estimator[^1]
> Let $\boldsymbol{\epsilon} \in \mathbb{R}^D$ be a random vector with $\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T] = \mathbf{I}$ (e.g. standard normal $\mathrm{Norm}[\mathbf{0}, \mathbf{I}]$, or i.i.d. Rademacher $\pm 1$ entries). For any $\mathbf{A} \in \mathbb{R}^{D \times D}$,
> $$
> \begin{align}
> \operatorname{trace}[\mathbf{A}] = \mathbb{E}\left[\boldsymbol{\epsilon}^T\mathbf{A}\boldsymbol{\epsilon}\right] \approx \frac{1}{I}\sum_{i=1}^I \boldsymbol{\epsilon}_i^T\mathbf{A}\boldsymbol{\epsilon}_i, \qquad \boldsymbol{\epsilon}_i \sim Pr(\boldsymbol{\epsilon})
> \end{align}
> $$

*Proof.*[^1]
$$
\begin{align}
\operatorname{trace}[\mathbf{A}] &= \operatorname{trace}\left[\mathbf{A}\,\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T]\right] = \operatorname{trace}\left[\mathbb{E}[\mathbf{A}\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T]\right] = \mathbb{E}\left[\operatorname{trace}[\mathbf{A}\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T]\right] \\
&= \mathbb{E}\left[\operatorname{trace}[\boldsymbol{\epsilon}^T\mathbf{A}\boldsymbol{\epsilon}]\right] = \mathbb{E}\left[\boldsymbol{\epsilon}^T\mathbf{A}\boldsymbol{\epsilon}\right]
\end{align}
$$
using $\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T] = \mathbf{I}$, linearity of [[Expectation]] ([[Expectation of Random Matrix]]), linearity of the [[Trace|trace]], invariance of the trace to cyclic permutation ([[Trace of Matrix Multiplication]]), and that the argument is a scalar.

# Properties
- **Unbiased**, and requires only matrix-vector products $\mathbf{A}\boldsymbol{\epsilon}$, never $\mathbf{A}$ itself: useful when $\mathbf{A}$ is implicit, e.g. a power of a network [[Jacobian Matrix]] evaluated via repeated vector-Jacobian products.
- **Variance**: for symmetric $\mathbf{A}$, a single Gaussian probe has variance $2\|\mathbf{A}\|_F^2$, while a Rademacher probe has variance $2(\|\mathbf{A}\|_F^2 - \sum_d A_{dd}^2)$, the minimum among probes with $\mathbb{E}[\boldsymbol{\epsilon}\boldsymbol{\epsilon}^T] = \mathbf{I}$.
- Used to approximate the traces in the power-series log-determinant of contractive [[Residual Flow|residual flows]].[^1]

[^1]: [Prince, p. 317](zotero://open-pdf/library/items/BWT7FYX5?page=331&annotation=HZ8DDNJ8)
