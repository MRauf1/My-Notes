---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Ray-Polygon Intersection)[^1]
> A case of [[Ray Intersection]] against a planar polygon with vertices $\mathbf{p}_1, \dots, \mathbf{p}_m$ and surface [[Normal Vector|normal]] $\mathbf{n}$: the ray is first intersected with the polygon's plane to find a candidate point $\mathbf{p}$, and the ray hits the polygon only if $\mathbf{p}$ lies inside the polygon.

# Properties
- Whether $\mathbf{p}$ is inside the polygon is decided by projecting the point and the polygon's vertices onto a 2D plane (chosen to avoid degenerate projections) and testing containment there, e.g., by counting crossings of a 2D ray with the polygon's boundary.
- A common alternative in practice is to avoid a general polygon test entirely by replacing the polygon with several triangles and using [[Ray-Triangle Intersection]] on each.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
