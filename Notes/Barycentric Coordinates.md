---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!info] Definition 1 (Barycentric Coordinates)[^1]
> Given a [[Triangle]] with vertices $\mathbf{a}, \mathbf{b}, \mathbf{c}$ (in 2D or 3D), set up a nonorthogonal [[Coordinate System]] with origin $\mathbf{a}$ and [[Basis]] vectors $(\mathbf{b} - \mathbf{a})$ and $(\mathbf{c} - \mathbf{a})$. Any point $\mathbf{p}$ can then be written as
> $$
> \begin{align}
> \mathbf{p} = \mathbf{a} + \beta(\mathbf{b} - \mathbf{a}) + \gamma(\mathbf{c} - \mathbf{a}).
> \end{align}
> $$
> The ordered pair $(\beta, \gamma)$ gives the [[Coordinates]] of $\mathbf{p}$ with respect to this basis.

> [!example]- Example 1 (Barycentric Coordinates)[^2]
> The point $\mathbf{p} = \mathbf{a} + 2.0(\mathbf{b} - \mathbf{a}) + 0.5(\mathbf{c} - \mathbf{a})$ has coordinates $(\beta, \gamma) = (2.0, 0.5)$ with respect to this basis, even though $\mathbf{p}$ lies outside the triangle.

> [!info] Definition 2 (Barycentric Coordinates, Symmetric Form)[^3]
> Reordering the terms of Definition 1 and introducing $\alpha \equiv 1 - \beta - \gamma$ gives
> $$
> \begin{align}
> \mathbf{p}(\alpha, \beta, \gamma) = \alpha \mathbf{a} + \beta \mathbf{b} + \gamma \mathbf{c}, \qquad \alpha + \beta + \gamma = 1.
> \end{align}
> $$
> $(\alpha, \beta, \gamma)$ are the barycentric coordinates of $\mathbf{p}$ with respect to $\mathbf{a}, \mathbf{b}, \mathbf{c}$.

Since $\alpha, \beta, \gamma$ always sum to $1$, Definition 2 mixes the three vertices in a smooth way. The same coefficients can be reused to mix other quantities attached to the vertices, such as [[RGB Color Space|color]], which is how barycentric coordinates enable interpolation across a triangle. This representation and its mixing property hold regardless of whether $\mathbf{a}, \mathbf{b}, \mathbf{c}$ are 2D or 3D points, but computing $(\alpha, \beta, \gamma)$ from a query point $\mathbf{p}$ differs by dimension.

# Types
## 2D
- [[2D Barycentric Coordinates]]
## 3D
- [[3D Barycentric Coordinates]]

# Properties

## Triangle Membership
A point $\mathbf{p}$ with barycentric coordinates $(\alpha, \beta, \gamma)$ lies:[^4]
- inside the triangle if and only if $0 < \alpha < 1$, $0 < \beta < 1$, and $0 < \gamma < 1$;
- on an edge if exactly one of $\alpha, \beta, \gamma$ is $0$ and the other two are in $(0, 1)$;
- at a vertex if two of $\alpha, \beta, \gamma$ are $0$ (and the third is $1$).

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=60&annotation=BF4LAJ7I)
[^2]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=60&annotation=48DRKFGI)
[^3]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=61&annotation=MVVDRJZS)
[^4]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=61&annotation=KQFDABG7)
