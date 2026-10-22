---
tags:
  - mathematics
  - differential_geometry
---

# Definition
> [!info] Gauss Map[^1]
> For an [[Orientable Surface]] $f: M \rightarrow \mathbb{R}^3$, the Gauss map is the continuous map
> $$\begin{align}
> N: M \rightarrow S^2
> \end{align}$$
> sending each point to its unit [[Surface Normal]], viewed as a point on the unit [[Sphere]] $S^2 \subset \mathbb{R}^3$.

![[Gauss Map.png]]

Since $S^2 \subset \mathbb{R}^3$, $N$ can be treated exactly like the immersion $f$: it is another map from $M$ into $\mathbb{R}^3$, and its differential $dN$ (the [[Weingarten Map]]) pushes tangent vectors forward. The pair $(f, N)$ captures the most fundamental ideas about the geometry of surfaces.[^1]

# Properties
- Differential: [[Weingarten Map]] $dN$, which measures how the normal turns; this is the source of all surface curvature ([[Shape Operator]], [[Normal Curvature]]).
- The [[Gaussian Curvature]] $K = \det S$ is the signed local area-stretch factor of the Gauss map: area swept on $S^2$ per unit area of surface.

[^1]: [Crane, p. 30](zotero://open-pdf/library/items/9N6JDPI2?page=31&annotation=KXR94S9R)
