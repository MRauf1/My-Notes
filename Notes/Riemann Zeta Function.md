---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Definition 1 (Riemann Zeta Function)[^1]
> For $1 < s < \infty$,
> $$
> \begin{align}
> \zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}
> \end{align}
> $$

It is of great importance in the study of the distribution of [[Prime Number|prime numbers]].

# Properties
- Converges for $s > 1$ by the [[Infinite Series Integral Test]] ($p$-series), diverges at $s = 1$ (harmonic series).
- Integral representations, with $[x]$ the greatest integer $\leq x$:[^1]
$$
\begin{align}
\zeta(s) &= s \int_1^\infty \frac{[x]}{x^{s+1}} \, dx \\
\zeta(s) &= \frac{s}{s - 1} - s \int_1^\infty \frac{x - [x]}{x^{s+1}} \, dx
\end{align}
$$
  The first comes from writing the series as a [[Riemann-Stieltjes Integral]] $\int x^{-s}\,d[x]$ against the step function $[x]$ and integrating by parts. The integral in the second converges for all $s > 0$ (since $0 \leq x - [x] < 1$), so the right side extends $\zeta$ to $0 < s < 1$, with a simple pole at $s = 1$.
- Extends to a meromorphic function on $\mathbb{C}$ with only a simple pole at $s = 1$; the Euler product $\zeta(s) = \prod_{p \text{ prime}} (1 - p^{-s})^{-1}$ links it to the primes.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=150&annotation=Q6IVI6UC)
