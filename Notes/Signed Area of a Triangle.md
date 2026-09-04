---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!info] Definition 1 (Signed Area of a Triangle)[^1]
> For a 2D [[Triangle]] with vertices $\mathbf{a} = (x_a, y_a)$, $\mathbf{b} = (x_b, y_b)$, $\mathbf{c} = (x_c, y_c)$, its signed area is
> $$
> \begin{align}
> \mathrm{area} = \frac{1}{2}\begin{vmatrix} x_b - x_a & y_b - y_a \\ x_c - x_a & y_c - y_a \end{vmatrix} = \frac{1}{2}\left(x_a y_b + x_b y_c + x_c y_a - x_a y_c - x_b y_a - x_c y_b\right).
> \end{align}
> $$

The sign of the area is positive if $\mathbf{a}, \mathbf{b}, \mathbf{c}$ are in counterclockwise order, and negative if they are in clockwise order.[^2] Besides encoding orientation, the signed area is the building block used to compute [[Barycentric Coordinates as Sub-triangle Areas|barycentric coordinates via sub-triangle areas]]. This notion of signed area is specific to 2D; in 3D, the analogous role is played by the [[Triangle Normal Vector]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=60&annotation=NUDU6YEC)
[^2]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=60&annotation=JPG2KFMX)
