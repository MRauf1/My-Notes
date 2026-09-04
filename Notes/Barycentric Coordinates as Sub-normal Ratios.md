---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!abstract] Theorem 1 ([[Barycentric Coordinates]] as Sub-normal Ratios)[^1]
> Given a [[Triangle]] with vertices $\mathbf{a}, \mathbf{b}, \mathbf{c}$ and [[Triangle Normal Vector|normal vector]] $\mathbf{n} = (\mathbf{b} - \mathbf{a}) \times (\mathbf{c} - \mathbf{a})$, define the sub-triangle normals at a point $\mathbf{p}$
> $$
> \begin{align}
> \mathbf{n}_a = (\mathbf{c} - \mathbf{b}) \times (\mathbf{p} - \mathbf{b}), \quad \mathbf{n}_b = (\mathbf{a} - \mathbf{c}) \times (\mathbf{p} - \mathbf{c}), \quad \mathbf{n}_c = (\mathbf{b} - \mathbf{a}) \times (\mathbf{p} - \mathbf{a}).
> \end{align}
> $$
> The barycentric coordinates of $\mathbf{p}$ are then
> $$
> \begin{align}
> \alpha = \frac{\mathbf{n} \cdot \mathbf{n}_a}{||\mathbf{n}||^2}, \quad \beta = \frac{\mathbf{n} \cdot \mathbf{n}_b}{||\mathbf{n}||^2}, \quad \gamma = \frac{\mathbf{n} \cdot \mathbf{n}_c}{||\mathbf{n}||^2}.
> \end{align}
> $$

This is the 3D analogue of [[Barycentric Coordinates as Sub-triangle Areas]]: each [[Dot Product]] $\mathbf{n} \cdot \mathbf{n}_a$ recovers the signed area of the corresponding sub-triangle scaled by $||\mathbf{n}||$, using agreement in direction with the reference normal $\mathbf{n}$ in place of a 2D signed area's sign.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=64&annotation=3AZMWTDM)
[^2]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=64&annotation=RJQ63TYK)
