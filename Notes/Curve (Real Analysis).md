---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Definition 1 (Curve)[^1]
> A continuous mapping $\gamma$ of a compact interval $[a, b]$ into $\mathbb{R}^k$ is called a curve in $\mathbb{R}^k$. To emphasize the parameter interval, $\gamma$ is called a curve on $[a, b]$.

The curve is the *mapping* $\gamma$, not its range: different curves can have the same range. Only continuity is assumed; no differentiability is required. This is unlike the differential-geometric [[Curve]] (a differentiable map on an open interval).

# Types
- [[Arc]]: $\gamma$ is one-to-one.
- [[Closed Curve]]: $\gamma(a) = \gamma(b)$.
- [[Rectifiable Curve]]: finite length $\Lambda(\gamma) = \sup_P \Lambda(P, \gamma)$.

# Properties
- Each of the three types, and the length, are invariant under reparameterization by a continuous one-to-one map of $[c, d]$ onto $[a, b]$ fixing the initial point ([[Rectifiable Curve]]).
- For $C^1$ curves, length is the integral of speed: [[Length of Continuously Differentiable Curve Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=145&annotation=B4BR6PHD)
