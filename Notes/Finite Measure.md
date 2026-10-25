---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Finite Measure[^1]
> A [[Measure (Measure Theory)|measure]] $\mu$ on $(X, \mathcal{M})$ is finite if $\mu(X) < \infty$.

# Properties
- If $\mu$ is finite then $\mu(E) < \infty$ for all $E \in \mathcal{M}$, since $\mu(X) = \mu(E) + \mu(E^c)$.[^1]
- Every finite measure is [[Sigma-Finite Measure|$\sigma$-finite]].
- Probability measures ([[Probability Space]]) are finite measures with $\mu(X) = 1$.
- For a finite measure, continuity from above holds without extra hypotheses ([[Measure Basic Properties]]).
- A finite [[Borel Measure]] on $\mathbb{R}$ is determined by its [[Cumulative Distribution Function|distribution function]] $F(x) = \mu((-\infty, x])$ ([[Lebesgue-Stieltjes Measure]]).

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=V62UTMST)
