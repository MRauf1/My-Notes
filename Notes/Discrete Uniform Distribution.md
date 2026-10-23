---
tags:
  - statistics
  - introduction_to_statistics
---

# Definition

> [!info] Definition 1 ([[Discrete]] [[Uniform Distribution]])[^1]
> Denoted as $Uniform(n)$, the [[Probability Mass Function]] is
> $$
> \begin{align}
> f(x) = \frac{1}{n}, x = 1, 2, \dots, n
> \end{align}
> $$
> and [[Cumulative Mass Function]] is
> $$
> \begin{align}
> F(x) = P(X \leq x) = \begin{cases}0 & x < 1 \\ \frac{k}{n} & k \leq x < k + 1 \\ 1 & n \leq x\end{cases}
> \end{align}
> $$

When the PMF is constant, the distribution is uniform.

# Properties
- Sampling by [[Inverse Transform Sampling|inversion]]:[^2] $X = \lfloor kU \rfloor$ is uniform on $\{0, \dots, k-1\}$ (safer: $\min\{\lfloor kU \rfloor, k - 1\}$ in case $U = 1$ occurs), and $X = \max\{1, \lceil kU \rceil\}$ is uniform on $\{1, \dots, k\}$. These depend on the high-order bits of $U$, which are usually more nearly random than the low-order bits of a [[Pseudorandom Number Generator]].

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=53)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=7&annotation=6Z4R43F6)
