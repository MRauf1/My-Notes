---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Cumulant Generating Function[^1]
> For a [[Random Variable]] with [[Moment Generating Function]] $M(t)$, the cumulant generating function is
> $$
> \begin{align}
> \psi(t) = \log M(t)
> \end{align}
> $$
> and it satisfies $\psi'(0) = \mu$ and $\psi''(0) = \sigma^2$.

The $n$th cumulant is $\kappa_n = \psi^{(n)}(0)$, so $\psi(t) = \sum_{n \geq 1} \kappa_n t^n / n!$. Cumulants are the "linearized" version of [[Moment (Statistics)|moments]]: $\kappa_1 = \mu$, $\kappa_2 = \sigma^2$, $\kappa_3 = E[(X-\mu)^3]$, and $\kappa_4 = E[(X-\mu)^4] - 3\sigma^4$.

# Properties
- Additive over [[Independent Random Variable|independent]] sums: $\psi_{X+Y} = \psi_X + \psi_Y$, so every cumulant of a sum is the sum of the cumulants.
- $\psi_{aX+b}(t) = bt + \psi_X(at)$, so $\kappa_n$ for $n \geq 2$ is shift-invariant and scales by $a^n$.
- The [[Normal Distribution]] is the only distribution with finitely many nonzero cumulants: $\psi(t) = \mu t + \sigma^2 t^2/2$.
- $\kappa_3/\sigma^3$ is the [[Probability Distribution Skewness|skewness]] and $\kappa_4/\sigma^4$ is the excess [[Kurtosis]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=93)
