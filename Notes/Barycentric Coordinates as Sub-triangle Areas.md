---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!abstract] Theorem 1 ([[Barycentric Coordinates]] as Sub-triangle Areas)[^1]
> Given a [[Triangle]] with vertices $\mathbf{a}, \mathbf{b}, \mathbf{c}$ and [[Signed Area of a Triangle|signed area]] $A$, a point $\mathbf{p}$ divides the triangle into three sub-triangles of signed areas $A_a = \triangle \mathbf{pbc}$, $A_b = \triangle \mathbf{pca}$, and $A_c = \triangle \mathbf{pab}$, with $A = A_a + A_b + A_c$. The barycentric coordinates of $\mathbf{p}$ are then
> $$
> \begin{align}
> \alpha = \frac{A_a}{A}, \qquad \beta = \frac{A_b}{A}, \qquad \gamma = \frac{A_c}{A}.
> \end{align}
> $$
> This rule still holds for points outside the triangle if the sub-triangle areas are allowed to be signed.

Because $A = A_a + A_b + A_c$, the total area needs only two additions once the sub-triangle areas are known, rather than a full [[Signed Area of a Triangle|area]] computation. Expanding the signed area formula for each sub-triangle in terms of the $(x, y)$ coordinates of $\mathbf{p}, \mathbf{a}, \mathbf{b}, \mathbf{c}$ gives closed-form expressions such as[^2]
$$
\begin{align}
\gamma &= \frac{(y_a - y_b)x + (x_b - x_a)y + x_a y_b - x_b y_a}{(y_a - y_b)x_c + (x_b - x_a)y_c + x_a y_b - x_b y_a}, \\
\beta &= \frac{(y_a - y_c)x + (x_c - x_a)y + x_a y_c - x_c y_a}{(y_a - y_c)x_b + (x_c - x_a)y_b + x_a y_c - x_c y_a},
\end{align}
$$
with $\alpha = 1 - \beta - \gamma$. In practice only two of the three coordinates need to be computed this way, since the third follows from the constraint $\alpha + \beta + \gamma = 1$.

This method requires a 2D signed area and so only applies to a [[2D Barycentric Coordinates|2D triangle]]; the 3D analogue is [[Barycentric Coordinates as Sub-normal Ratios]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=63&annotation=GZD87MIA)
[^2]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=62&annotation=D9E2ILVK)
