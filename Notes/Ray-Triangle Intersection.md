---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Ray-Triangle Intersection)[^1]
> A case of [[Ray Intersection]] against a [[Triangle]] with vertices $\mathbf{a}, \mathbf{b}, \mathbf{c}$: the ray $\mathbf{e} + t\mathbf{d}$ hits the triangle's plane at a point expressible in [[Barycentric Coordinates]], $\mathbf{e} + t\mathbf{d} = \mathbf{a} + \beta(\mathbf{b} - \mathbf{a}) + \gamma(\mathbf{c} - \mathbf{a})$, and the intersection lies inside the triangle if and only if $\beta > 0$, $\gamma > 0$, and $\beta + \gamma < 1$.

# Properties
- Solving the vector equation for $t, \beta, \gamma$ is a linear system, solvable analytically (e.g., via Cramer's rule).
- No solution means either the triangle is degenerate or the ray is parallel to the triangle's plane.
- [[Barycentric Coordinates as Sub-triangle Areas|Barycentric coordinates]] also allow interpolating other per-vertex quantities (e.g., color, [[Triangle Normal Vector|normal]]) across the hit point.
- Polygons with more than three vertices are commonly handled by triangulating them into several triangles and testing each (see also [[Ray-Polygon Intersection]]).

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
