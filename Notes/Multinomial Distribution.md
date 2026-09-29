---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Multinomial [[Probability Distribution]])[^1]
> Denoted as $X \sim Multinomial(n, p_1, \dots, p_c)$
> $$
> \begin{align}
> P(n_1, \dots, n_c) &= \frac{n!}{n_1! \dots n_c!} p_1^{n_1} \dots p_c^{n_c}, \sum_{j} n_j = n
> \end{align}
> $$
> Trial $i$ in category $j$ is denoted as $X_{ij}$

Distribution for seeing $n_1$ successes of 1st category, $\dots$, $n_c$ successes of $c$th category in $n$ multi-variant observations (e.g. $c$ categories).

Since $n_c$ is [[Linearly Dependent]] on the preceding $n_j$, the input can be $(c-1)$-dimensional with $n_c = n - (n_1 + \dots + n_{c - 1})$. Same is true for the probability $p_c$.

> [!info] Definition 2 (Multinomial Distribution, $k - 1$ Free Counts)[^2]
> Repeat an experiment $n$ independent times, each with exactly one outcome in one of $k$ categories $C_1, \dots, C_k$ with constant probabilities $p_i$. With $X_i$ the count in $C_i$, $X_k = n - X_1 - \dots - X_{k-1}$ is determined, so the joint pmf of $(X_1, \dots, X_{k-1})$ is
> $$
> \begin{align}
> P(X_1 = x_1, \dots, X_{k-1} = x_{k-1}) = \frac{n!}{x_1!\cdots x_{k-1}!\,x_k!}p_1^{x_1}\cdots p_{k-1}^{x_{k-1}}p_k^{x_k}
> \end{align}
> $$
> for nonnegative integers with $x_1 + \dots + x_{k-1} \leq n$, where $x_k = n - \sum_{j<k} x_j$ and $p_k = 1 - \sum_{j<k} p_j$.

The joint mgf is[^3] $M(t_1, \dots, t_{k-1}) = \left(\sum_{i=1}^{k-1} p_i e^{t_i} + p_k\right)^n$, by factoring out $m^n$ with $m = \sum_{i<k} p_i e^{t_i} + p_k$ and recognizing a multinomial pmf that sums to $1$. (The printed text has "$+ p_{k-1}$"; it should be $+p_k$, as the $t = \mathbf{0}$ check $M(\mathbf{0}) = 1$ confirms.)

# Types
When $c = 2$, it is the [[Binomial Distribution]].

# Properties
## Basic Statistical Properties
- [[Multinomial Distribution Expectation]]
- [[Multinomial Distribution Variance]]
- [[Multinomial Distribution Covariance]]
- [[Multinomial Distribution Row Sum]]
- [[Multinomial Distribution Column Sum]]
- Marginals:[^3] $M(0, \dots, t_i, \dots, 0) = (p_i e^{t_i} + 1 - p_i)^n$, so $X_i \sim$ [[Binomial Distribution|$b(n, p_i)$]]; any pair $(X_i, X_j)$ is multinomial (trinomial) with parameters $n, p_i, p_j$.
- Conditional distribution:[^3] $X_2 \mid X_1 = x_1 \sim b\left(n - x_1, \frac{p_2}{1 - p_1}\right)$: given $x_1$ outcomes in $C_1$, the remaining $n - x_1$ trials fall in $C_2$ with renormalized probability.
- Correlation:[^3] $E(X_2 | X_1) = (n - X_1)\frac{p_2}{1 - p_1}$ is linear with slope $-p_2/(1 - p_1)$, so by the [[Linear Conditional Expectation Theorem]], $\rho_{12} = -\sqrt{\frac{p_1 p_2}{(1-p_1)(1-p_2)}}$. The negative correlation reflects the constraint $x_1 + x_2 \leq n$.

## [[Maximum Likelihood Estimation]]
- [[Multinomial Distribution Maximum Likelihood Estimation]]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=24)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=176)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=177)
