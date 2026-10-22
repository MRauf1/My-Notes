---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Osculating Circle[^1]
> At a point $p$ of a smooth [[Plane Curve]] $\gamma$, the osculating circle $S$ is the circle that best approximates $\gamma$: it has the same tangent direction $T$ and the same curvature vector $\kappa N$, i.e. it agrees with $\gamma$ up to second order (first and second derivatives equal). Its radius $r = 1/\kappa$ is the *radius of curvature* and its center is the *center of curvature*.[^2]

It always exists (when $\kappa \neq 0$): take the circle of radius $1/\kappa$ tangent to $T$. Equivalently, it is the limit of circles through $p$ and two neighboring points of $\gamma$ approaching from either side, since three shared points yield consistent finite-difference approximations of $T$ and $\kappa N$.[^1]

For a curve in $\mathbb{R}^3$, the same construction lives in the *osculating plane* spanned by $T$ and $N$ (which contains both the tangent and curvature vector).[^2]

# Properties
- The curvature of a circle is the reciprocal of its radius: $\kappa = 1/r$ ([[Curvature Function on Curve]]).[^3]
- [[Normal Curvature]] of a surface in direction $X$ is the curvature of the osculating circle of the normal section; see image there ($1/\kappa_n$).

[^1]: [Crane, p. 37](zotero://open-pdf/library/items/9N6JDPI2?page=38&annotation=YSC7X2Z8)
[^2]: [Crane, p. 37](zotero://open-pdf/library/items/9N6JDPI2?page=38&annotation=RJSBDHRD)
[^3]: [Crane, p. 36](zotero://open-pdf/library/items/9N6JDPI2?page=37&annotation=MI485UKQ)
