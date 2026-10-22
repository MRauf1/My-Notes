---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Conformal Map[^1]
> A map $f$ is conformal if it preserves the angle between any two vectors. Concretely, $f: \mathbb{R}^2 \supset M \rightarrow \mathbb{R}^3$ is conformal if
> $$\begin{align}
> df(X) \cdot df(Y) = a \langle X, Y\rangle \quad \text{for all tangent vectors } X, Y,
> \end{align}$$
> where $a > 0$ is a positive function on $M$ and $\langle\cdot,\cdot\rangle$ is the usual inner product on $\mathbb{R}^2$. In practice one writes $a = e^u$ for a real-valued function $u$ (the *log conformal factor*), so positivity is automatic. (Many authors instead write $e^{2u}$, so that $e^u$ is the length-scale factor.)

Vectors can still be stretched, but only uniformly in all directions at a point: the surface is never sheared, so e.g. orthogonal vectors stay orthogonal.[^1] Equivalently, the [[Induced Metric]] is a pointwise multiple of the flat metric, $\mathrm{I} = e^u\,\mathrm{Id}$ (i.e. $E = G$, $F = 0$). Such a parameterization is said to use *conformal* (isothermal) coordinates.

**Conformal vs. isometric.** An [[Isometric Parameterization|isometry]] preserves lengths *and* angles ($a \equiv 1$); a conformal map preserves only angles ($a$ arbitrary). So every isometry is conformal, not conversely. Isometries also preserve [[Gaussian Curvature]], while conformal maps may change it.

# Properties
- Conformal coordinates always exist locally around any point of a smooth surface, guaranteed by the [[Uniformization Theorem]] (and local existence of isothermal coordinates); isometric parameterizations generally do not.[^2]
- Like arc-length parameterization of curves, it stores the least possible distortion information: one number $u$ per point rather than a whole [[Jacobian Matrix]].[^2] Often it suffices to know the parameterization exists, without constructing it.
- In the plane, [[Holomorphic Function|holomorphic functions]] with nonvanishing derivative are exactly the orientation-preserving conformal maps.

[^1]: [Crane, p. 31](zotero://open-pdf/library/items/9N6JDPI2?page=32&annotation=AM7IA3EU)
[^2]: [Crane, p. 31](zotero://open-pdf/library/items/9N6JDPI2?page=32&annotation=AW2AIQP5)
