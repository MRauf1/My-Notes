---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] $\sigma$-Finite Measure[^1]
> A [[Measure (Measure Theory)|measure]] $\mu$ on $(X, \mathcal{M})$ is $\sigma$-finite if
> $$
> \begin{align}
> X = \bigcup_{j=1}^\infty E_j, \qquad E_j \in \mathcal{M},\ \mu(E_j) < \infty \text{ for all } j.
> \end{align}
> $$
> More generally, a set $E$ is **$\sigma$-finite for $\mu$** if $E = \bigcup_1^\infty E_j$ with $E_j \in \mathcal{M}$ and $\mu(E_j) < \infty$.

Most measures arising in practice are $\sigma$-finite, which is fortunate since non-$\sigma$-finite measures tend to behave pathologically.[^2]

# Properties
- Every [[Finite Measure]] is $\sigma$-finite.
- Every $\sigma$-finite measure is [[Semifinite Measure|semifinite]], but not conversely.[^2]
- Every $\sigma$-finite measure is [[Saturated Measure|saturated]].
- [[Lebesgue Measure]] on $\mathbb{R}$ is $\sigma$-finite ($\mathbb{R} = \bigcup_n [-n, n]$) but not finite.
- A $\sigma$-finite [[Premeasure]] has a **unique** extension to a measure on the generated $\sigma$-algebra ([[Carathéodory Extension Theorem]]).
- $\sigma$-finiteness is the standing hypothesis of the Radon-Nikodym theorem ([[Absolutely Continuous Measure]]).

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=V62UTMST)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=7T6GDKAE)
