---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Isometric Parameterization[^1]
> A parameterization $f$ (of a curve or surface) is isometric if it introduces no stretching from the domain into $\mathbb{R}^3$:
> $$\begin{align}
> |df(X)| = |X| \quad \text{for all tangent vectors } X,
> \end{align}$$
> equivalently $df(X) \cdot df(Y) = \langle X, Y\rangle$, i.e. the [[Induced Metric]] equals the flat metric of the domain.

For curves $\gamma: I \rightarrow \mathbb{R}^3$ this is the [[Unit Speed Curve|unit-speed / arc-length]] parameterization: think of $\gamma$ as a completely relaxed rubber band. It is also the natural viewpoint in the discrete setting, where there is no base domain and the curve is assumed to sit in a relaxed state.[^2]

# Properties
- Every regular curve admits one ([[Arc Length Curve Reparameterization]]).
- For surfaces, an isometric parameterization does not always exist, not even locally.[^3] Since the domain is flat, a local isometric parameterization exists iff the [[Gaussian Curvature]] vanishes ($K = 0$, a [[Developable Surface]]), by Gauss's Theorema Egregium.
- The weaker substitute that always exists locally is a [[Conformal Map|conformal]] parameterization.
- An isometric map is a [[Conformal Map]] with conformal factor $1$. Compare [[Isometry]] (metric spaces) and [[Isometry (Linear Algebra)]].

[^1]: [Crane, p. 31](zotero://open-pdf/library/items/9N6JDPI2?page=32&annotation=E4XP97PP)
[^2]: [Crane, p. 35](zotero://open-pdf/library/items/9N6JDPI2?page=36&annotation=PHZZCDMR)
[^3]: [Crane, p. 31](zotero://open-pdf/library/items/9N6JDPI2?page=32&annotation=RH3CKCLQ)
