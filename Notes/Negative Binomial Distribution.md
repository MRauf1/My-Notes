---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Negative Binomial Distribution[^1]
> In a sequence of independent [[Bernoulli Distribution|Bernoulli trials]] with success probability $p$, let $Y$ be the number of failures before the $r$th success ($r$ a fixed positive integer), so $Y + r$ trials are needed with the last one a success. Then
> $$
> \begin{align}
> p_Y(y) = \binom{y + r - 1}{r - 1} p^r (1 - p)^y, \quad y = 0, 1, 2, \dots
> \end{align}
> $$
> and zero elsewhere.

Derivation: $Y = y$ means exactly $r - 1$ successes occur in the first $y + r - 1$ trials (a [[Binomial Distribution|binomial]] probability) and the $(y + r)$th trial is a success. The name comes from $p_Y(y)$ being the general term of the negative-exponent binomial expansion of $p^r[1 - (1 - p)]^{-r}$.

# Types
- [[Geometric Distribution]]: the case $r = 1$.

# Properties
- [[Moment Generating Function|mgf]]: $M(t) = p^r[1 - (1 - p)e^t]^{-r}$ for $t < -\log(1 - p)$.
- $E(Y) = \frac{r(1-p)}{p}$ and $\text{Var}(Y) = \frac{r(1-p)}{p^2} > E(Y)$, so it models overdispersed counts ([[Probability Distribution Overdispersion]]).
- $Y$ is the sum of $r$ [[Independent and Identically Distributed|iid]] geometric variables, which is visible in the mgf being the $r$th power of the geometric mgf.
- Poisson-gamma mixture:[^2] if $X | \theta \sim$ [[Poisson Distribution|Poisson]]$(\theta)$ and $\theta \sim$ [[Gamma Distribution|Gamma]]$(r, (1-p)/p)$, the [[Mixture Distribution|compound distribution]] of $X$ is negative binomial$(r, p)$. This representation extends the family to non-integer $r > 0$ and explains its use for counts with heterogeneous rates (e.g. accident counts).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=175)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=236)
