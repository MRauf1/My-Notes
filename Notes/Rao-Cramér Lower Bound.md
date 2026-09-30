---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Rao-Cramér Lower Bound[^1]
> Let $X_1, \dots, X_n$ be iid with pdf $f(x; \theta)$, $\theta \in \Omega$, satisfying the [[Maximum Likelihood Regularity Conditions|regularity conditions]] (R0)-(R4). Let $Y = u(X_1, \dots, X_n)$ be a [[Statistic]] with $E(Y) = k(\theta)$. Then
> $$
> \begin{align}
> \text{Var}(Y) \geq \frac{[k'(\theta)]^2}{nI(\theta)}
> \end{align}
> $$
> where $I(\theta)$ is the [[Fisher Information]].

> [!abstract] Corollary 1 (Unbiased Estimators)[^2]
> If $Y$ is an [[Unbiased Estimator]] of $\theta$, so $k(\theta) = \theta$, then
> $$
> \begin{align}
> \text{Var}(Y) \geq \frac{1}{nI(\theta)}
> \end{align}
> $$

> [!abstract] Multiparameter Version[^3]
> For $\boldsymbol{\theta} \in \Omega \subseteq \mathbb{R}^p$ with [[Fisher Information Matrix]] $I(\boldsymbol{\theta})$, if $Y_j$ is unbiased for $\theta_j$, then $\text{Var}(Y_j) \geq \frac{1}{n}[I^{-1}(\boldsymbol{\theta})]_{jj}$.

Proof idea: $k'(\theta) = \text{Cov}(Y, \partial \log L/\partial\theta)$ by differentiating $E(Y)$ under the integral sign, and the [[Cauchy-Schwarz Inequality]] gives $[k'(\theta)]^2 \leq \text{Var}(Y)\,\text{Var}(\partial \log L/\partial\theta) = \text{Var}(Y)\,nI(\theta)$.

No unbiased estimator can be more precise than $1/(nI(\theta))$: the information in the sample limits how well $\theta$ can be estimated. An estimator attaining the bound is an [[Efficient Estimator]].

# Properties
- $[I^{-1}]_{jj} \geq 1/I_{jj}$, with equality when the information matrix is diagonal; not knowing the other parameters can only raise the bound.
- The bound can fail to be attainable for any unbiased estimator, and it does not apply when the regularity conditions fail (e.g. a support depending on $\theta$).
- Biased form: if $E(Y) = \theta + b(\theta)$ with bias $b(\theta)$, then $k'(\theta) = 1 + b'(\theta)$ and
$$
\begin{align}
\text{Var}(Y) \geq \frac{(1 + b'(\theta))^2}{nI(\theta)}, \qquad E[(Y - \theta)^2] \geq \frac{(1 + b'(\theta))^2}{nI(\theta)} + b(\theta)^2
\end{align}
$$
  An estimator attaining it for a given bias function is a locally efficient biased estimator. When $b'(\theta) < 0$ (shrinkage), the variance floor falls below $1/(nI(\theta))$, and the [[Mean Squared Error]] can fall below that of any unbiased estimator, including the [[Minimum Variance Unbiased Estimator|MVUE]] ([[James-Stein Estimator]]).
- An [[Efficient Estimator]] is the MVUE, but the MVUE need not attain the bound.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=381)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=382)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=405)
