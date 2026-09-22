---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Gouraud Interpolation)[^1]
> Interpolating a per-vertex attribute value across a [[Triangle]] using the [[Barycentric Coordinates]] of a point: if the vertices have colors $c_0, c_1, c_2$, the color at a point with barycentric coordinates $(\alpha, \beta, \gamma)$ is
> $$
> \begin{align}
> c = \alpha c_0 + \beta c_1 + \gamma c_2
> \end{align}
> $$
> Named for its inventor, Gouraud (1971).

# Properties
- Used by the [[Rasterization|rasterizer]] to fill in any per-vertex attribute (color, depth, normals, texture coordinates, etc.) at every covered pixel from only the primitive's vertex values.
- Underlies [[Per-Vertex Shading]] (Gouraud shading), where the interpolated attribute is itself a color already computed by evaluating a shading equation at each vertex.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=179&annotation=TLU7LEWF)
