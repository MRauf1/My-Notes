---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!info] Definition 1 (3D Barycentric Coordinates)[^1]
> For a [[Triangle]] with 3D vertices $\mathbf{a}, \mathbf{b}, \mathbf{c}$, [[Barycentric Coordinates]] still represent a point $\mathbf{p}$ via
> $$
> \begin{align}
> \mathbf{p} = (1 - \beta - \gamma)\mathbf{a} + \beta \mathbf{b} + \gamma \mathbf{c}.
> \end{align}
> $$
> As $\beta$ and $\gamma$ vary, $\mathbf{p}$ sweeps out the [[Plane]] containing the triangle.[^2]

Unlike in 2D, there is no natural signed area in 3D, so computing $(\alpha, \beta, \gamma)$ requires the triangle's [[Triangle Normal Vector|normal vector]] in place of [[Signed Area of a Triangle|signed area]].

# Properties
- [[Triangle Normal Vector]]
- [[Barycentric Coordinates as Sub-normal Ratios]]

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=63&annotation=GTI95FRB)
[^2]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=63&annotation=BJ4GXBPT)
