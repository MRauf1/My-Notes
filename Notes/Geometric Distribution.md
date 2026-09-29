---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Geometric Distribution[^1]
> In a sequence of independent [[Bernoulli Distribution|Bernoulli trials]] with success probability $p$, the number of failures $Y$ before the first success has pmf
> $$
> \begin{align}
> p_Y(y) = p(1 - p)^y, \quad y = 0, 1, 2, \dots
> \end{align}
> $$
> and zero elsewhere. It is the [[Negative Binomial Distribution]] with $r = 1$.

Some texts instead count the trials up to and including the first success, $Y + 1 \in \{1, 2, \dots\}$, with pmf $p(1-p)^{k-1}$; the two conventions differ by a shift of $1$.

# Properties
- [[Moment Generating Function|mgf]]: $M(t) = p[1 - (1 - p)e^t]^{-1}$ for $t < -\log(1 - p)$.
- $E(Y) = \frac{1-p}{p}$ and $\text{Var}(Y) = \frac{1-p}{p^2}$.
- Tail: $P(Y \geq k) = (1 - p)^k$, the probability that the first $k$ trials all fail.
- Memoryless:[^2] $P(Y \geq k + j \mid Y \geq k) = P(Y \geq j)$ for nonnegative integers $k, j$; having already waited $k$ failures does not change the distribution of the remaining wait. It is the only memoryless distribution on $\{0, 1, 2, \dots\}$, the discrete counterpart of the [[Exponential Distribution]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=176)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=182)
