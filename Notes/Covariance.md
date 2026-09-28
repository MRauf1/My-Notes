---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Covariance)[^1][^2]
> Let $(X_1, X_2)$ have a joint distribution with means $\mu_1 = E[X_1]$, $\mu_2 = E[X_2]$. The covariance of two [[Random Variable]] $X_1, X_2$ is
> $$
> \begin{align}
> Cov[X_1, X_2] &= E[(X_1 - \mu_1)(X_2 - \mu_2)] \\
> &= \sum_{x_1} \sum_{x_2} (x_1 - \mu_1)(x_2 - \mu_2) f(x_1, x_2)\ \text{(Discrete)} \\
> &= \int\!\!\int (x_1 - \mu_1)(x_2 - \mu_2) f(x_1, x_2)\,dx_1\,dx_2\ \text{(Continuous)}
> \end{align}
> $$

**Intuition.** Covariance measures how two random variables move together about their means. The product $(X_1 - \mu_1)(X_2 - \mu_2)$ is positive when both are above their means or both below, and negative when one is above and the other below. Covariance is the probability-weighted average of this product:
- positive covariance: large values of $X_1$ tend to occur with large values of $X_2$;
- negative covariance: large values of one tend to occur with small values of the other;
- zero covariance: no linear tendency either way.

It measures only linear co-movement: a perfect nonlinear dependence (e.g. $X_2 = X_1^2$ with $X_1$ symmetric about $0$) can have zero covariance. Its size depends on the units of both variables, so its magnitude alone says little about how strong the relationship is; the standardized version is the [[Correlation]] coefficient. Geometrically, covariance is an inner product of the centered variables $X_1 - \mu_1$ and $X_2 - \mu_2$, with [[Variance]] as the squared length.

Covariance is a one-number statistic of the joint relationship of the two random variables. It depends on the scale of both $X_1, X_2$.

# Properties
- Computational formula, by linearity of [[Expectation]]:[^3]
$$
\begin{align}
Cov[X_1, X_2] = E[X_1 X_2 - \mu_2 X_1 - \mu_1 X_2 + \mu_1 \mu_2] = E[X_1 X_2] - E[X_1] E[X_2]
\end{align}
$$
  equivalently $E[X_1 X_2] = E[X_1] E[X_2] + Cov[X_1, X_2] = E[X_1] E[X_2] + \rho \sigma_1 \sigma_2$: the expectation of a product is the product of expectations plus the covariance.
- $Cov[X, X] = Var[X]$ and $Cov[X_1, X_2] = Cov[X_2, X_1]$.
- Bilinear: $Cov[aX_1 + b, cX_2 + d] = ac\,Cov[X_1, X_2]$ and $Cov[X_1 + X_3, X_2] = Cov[X_1, X_2] + Cov[X_3, X_2]$.
- $Var[X_1 + X_2] = Var[X_1] + Var[X_2] + 2\,Cov[X_1, X_2]$; more generally, see [[Linear Combination of Random Variables]].
- [[Independent Random Variable|Independent]] $\implies Cov[X_1, X_2] = 0$ ([[Expectation of Product of Independent Random Variables]]); the converse fails.
- $|Cov[X_1, X_2]| \leq \sigma_1 \sigma_2$ ([[Cauchy-Schwarz Inequality]]), so $-1 \leq \rho \leq 1$.
- Arranged for all pairs of components of a [[Random Vector]], covariances form the [[Covariance Matrix]].
- Computable from the joint mgf: $Cov[X_1, X_2] = \frac{\partial^2 M(0, 0)}{\partial t_1 \partial t_2} - E[X_1] E[X_2]$ ([[Moment Generating Function of Random Vector]]).

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=24)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=141)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=142)
