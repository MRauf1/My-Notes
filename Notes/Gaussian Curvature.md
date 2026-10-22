---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Gaussian Curvature[^1]
> The Gaussian curvature $K$ of a surface at a point is the product of the [[Principal Curvature|principal curvatures]] (the square of their [[Geometric Mean]]):
> $$\begin{align}
> K = \kappa_1 \kappa_2.
> \end{align}$$

Interpretation: Gaussian curvature is like a logical "and": is there curvature along *both* directions?[^2] Its sign classifies the local shape: $K > 0$ (bowl/sphere-like, both principal curvatures bend the same way), $K < 0$ (saddle-like), $K = 0$ (flat in at least one direction).[^3]

# Types
- $K \equiv 0$: [[Developable Surface]].

# Properties
- $K = \det S$ ([[Shape Operator]]) $= \frac{\det \mathrm{II}}{\det \mathrm{I}}$ ([[Second Fundamental Form]], [[First Fundamental Form]]).
- Signed area-distortion factor of the [[Gauss Map]].
- *Theorema Egregium* (Gauss): $K$ is intrinsic, i.e. it depends only on the [[Induced Metric]], so it is preserved by bending without stretching. Consequently a surface with $K \neq 0$ has no local [[Isometric Parameterization]] over the plane.
- Independent of the sign choice of the normal (flipping $N$ negates both $\kappa_i$).
- Together with [[Mean Curvature]] it determines the principal curvatures, and is often easier to obtain in practice.[^4]

[^1]: [Crane, p. 40](zotero://open-pdf/library/items/9N6JDPI2?page=41&annotation=484ZHDMR)
[^2]: [Crane, p. 40](zotero://open-pdf/library/items/9N6JDPI2?page=41&annotation=CIL7UXAJ)
[^3]: [Crane, p. 41](zotero://open-pdf/library/items/9N6JDPI2?page=42&annotation=CCECNLTT)
[^4]: [Crane, p. 41](zotero://open-pdf/library/items/9N6JDPI2?page=42&annotation=JMI9Q9XC)
