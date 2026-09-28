---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Linear Combination of Random Variables[^1]
> For a [[Random Vector]] $(X_1, \dots, X_n)^T$ and constants $a_1, \dots, a_n$, the linear combination
> $$
> \begin{align}
> T = \sum_{i=1}^n a_i X_i = \mathbf{a}^T \mathbf{X}
> \end{align}
> $$

> [!abstract] Theorem 1 (Mean of a Linear Combination)[^1]
> If $E(X_i) = \mu_i$ for $i = 1, \dots, n$, then
> $$
> \begin{align}
> E(T) = \sum_{i=1}^n a_i \mu_i
> \end{align}
> $$

> [!abstract] Theorem 2 (Covariance of Two Linear Combinations)[^1]
> Let $T = \sum_{i=1}^n a_i X_i$ and $W = \sum_{j=1}^m b_j Y_j$. If $E[X_i^2] < \infty$ and $E[Y_j^2] < \infty$ for all $i, j$, then
> $$
> \begin{align}
> \text{Cov}(T, W) = \sum_{i=1}^n \sum_{j=1}^m a_i b_j\,\text{Cov}(X_i, Y_j)
> \end{align}
> $$

> [!abstract] Corollary 1 (Variance of a Linear Combination)[^2]
> Provided $E[X_i^2] < \infty$ for all $i$,
> $$
> \begin{align}
> \text{Var}(T) = \text{Cov}(T, T) = \sum_{i=1}^n a_i^2\,\text{Var}(X_i) + 2\sum_{i<j} a_i a_j\,\text{Cov}(X_i, X_j)
> \end{align}
> $$

> [!abstract] Corollary 2 (Uncorrelated Case)[^2]
> If $X_1, \dots, X_n$ are [[Mutually Independent Random Variables|independent]] with $\text{Var}(X_i) = \sigma_i^2$, then
> $$
> \begin{align}
> \text{Var}(T) = \sum_{i=1}^n a_i^2 \sigma_i^2
> \end{align}
> $$
> It suffices that $X_i, X_j$ are uncorrelated for all $i \neq j$.

Theorem 1 is linearity of [[Expectation]]. Theorem 2 is bilinearity of [[Covariance]], and Corollary 1 is Theorem 2 with $W = T$. Corollary 2 follows because independence gives $\text{Cov}(X_i, X_j) = 0$ for $i \neq j$ ([[Correlation]]).

# Properties
- Matrix form: with $\boldsymbol{\mu} = E[\mathbf{X}]$ and $\Sigma = \text{Cov}(\mathbf{X})$ ([[Covariance Matrix]]), $E(\mathbf{a}^T\mathbf{X}) = \mathbf{a}^T\boldsymbol{\mu}$, $\text{Var}(\mathbf{a}^T\mathbf{X}) = \mathbf{a}^T\Sigma\mathbf{a}$, and $\text{Cov}(\mathbf{a}^T\mathbf{X}, \mathbf{b}^T\mathbf{X}) = \mathbf{a}^T\Sigma\mathbf{b}$.
- Positive correlations inflate the variance of a sum and negative correlations reduce it; this is the principle behind variance reduction with antithetic variates.
- Applied to a [[Random Sample]], it gives the mean and variance of the [[Sample Mean]].
- The distribution (not just the moments) of $T$ for independent $X_i$ follows from the [[Moment Generating Function Technique]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=167)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=168)
