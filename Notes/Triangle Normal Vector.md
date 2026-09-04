---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!info] Definition 1 (Triangle Normal Vector)[^1]
> For a [[Triangle]] with vertices $\mathbf{a}, \mathbf{b}, \mathbf{c}$, its [[Normal Vector]] can be found by taking the [[Cross Product]] of any two vectors in the plane of the triangle. It is easiest to use two of the edges, for example
> $$
> \begin{align}
> \mathbf{n} = (\mathbf{b} - \mathbf{a}) \times (\mathbf{c} - \mathbf{a}).
> \end{align}
> $$

The triangle's (unsigned) area follows from the [[Cross Product Norm]]:[^2]
$$
\begin{align}
\mathrm{area} = \frac{1}{2}||\mathbf{n}||.
\end{align}
$$
This area is not signed, so it cannot be used directly to evaluate [[Barycentric Coordinates]]. However, a triangle with a clockwise vertex order has a normal vector pointing in the opposite direction to that of a triangle in the same plane with a counterclockwise vertex order, so orientation is still recoverable from the direction of $\mathbf{n}$.[^3]

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=63&annotation=TG4WP2JU)
[^2]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=63&annotation=W4JTGXBT)
[^3]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=63&annotation=ME5E3LN3)
