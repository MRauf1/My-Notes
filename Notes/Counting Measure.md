---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Counting Measure[^1]
> Let $X$ be any nonempty set, $\mathcal{M} = \mathcal{P}(X)$, and $f : X \to [0, \infty]$. Then
> $$
> \begin{align}
> \mu(E) = \sum_{x \in E} f(x)
> \end{align}
> $$
> (an [[Unordered Sum]]) is a [[Measure (Measure Theory)|measure]] on $\mathcal{P}(X)$. With $f \equiv 1$, $\mu(E) = \operatorname{card}(E)$ (or $\infty$ for infinite $E$) is the counting measure.

The general weighted form shows that on any set, and in particular any countable set, every subset can be measured consistently: assign a nonnegative weight to each point and sum. The same name is used for the restriction to smaller $\sigma$-algebras on $X$.

# Types
- [[Dirac Measure]]: the case $f = \chi_{\{x_0\}}$.

# Properties
- The weighted measure is [[Semifinite Measure|semifinite]] iff $f(x) < \infty$ for every $x$, and [[Sigma-Finite Measure|$\sigma$-finite]] iff it is semifinite and $\{x : f(x) > 0\}$ is countable.[^1]
- Counting measure on $X$ is $\sigma$-finite iff $X$ is countable.
- Integration against counting measure is summation; the Radon–Nikodym derivative with respect to it is a [[Probability Mass Function]] ([[Absolutely Continuous Measure]]).

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=KZAMA5UJ)
