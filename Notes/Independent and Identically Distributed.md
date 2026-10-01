---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Independent and Identically Distributed (iid)[^1]
> Random variables $X_1, \dots, X_n$ are independent and identically distributed (iid) if they are [[Mutually Independent Random Variables|mutually independent]] and all have the same distribution. With common pdf $f$, their joint pdf is
> $$
> \begin{align}
> f(x_1, \dots, x_n) = \prod_{i=1}^n f(x_i)
> \end{align}
> $$

iid variables model repeated performances of the same [[Random Experiment]] under identical conditions; an iid collection is a [[Random Sample]] from the common distribution.

# Properties
- Sum of iid variables: if each has mgf $M(t)$ for $-h < t < h$, then $T = \sum_{i=1}^n X_i$ has mgf
$$
\begin{align}
M_T(t) = [M(t)]^n, \quad -h < t < h
\end{align}
$$
  a corollary of the mgf formula for linear combinations of independent variables ([[Moment Generating Function Technique]]).
- $E\left(\sum_i X_i\right) = n\mu$ and $\text{Var}\left(\sum_i X_i\right) = n\sigma^2$, since the [[Covariance]] terms vanish.
- The joint distribution is [[Exchangeability|exchangeable]]: invariant under permutations of $(X_1, \dots, X_n)$.
- The setting of the [[Strong Law of Large Numbers]] and the central limit theorem.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=156)
