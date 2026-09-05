---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Specular Reflection)[^1]
> Ideal specular (mirror) reflection in [[Ray Tracing]]: a viewer looking from direction $\mathbf{d}$ toward a surface sees what is in the reflected direction $\mathbf{r}$, obeying the [[Law of Reflection]],
> $$
> \begin{align}
> \mathbf{r} = \mathbf{d} - 2(\mathbf{d} \cdot \mathbf{n})\mathbf{n}
> \end{align}
> $$
> where $\mathbf{n}$ is the surface [[Normal Vector|normal]] at the point of reflection.

![[Specular Reflection.png]]

# Properties
- Implemented by recursively tracing a reflection ray from the intersection point in direction $\mathbf{r}$ and adding its resulting color, tinted by a mirror reflectance color $k_m$, to the shaded color; this lets colors shift on reflection (e.g., gold reflecting yellow more efficiently than blue).
- Like a [[Shadow Ray]], the reflection ray's [[Ray Intersection]] test excludes a small interval near its origin to avoid the ray immediately re-hitting the surface that generated it.
- Because a reflection ray can itself generate further reflection rays, recursion must be bounded by a maximum recursion depth to guarantee termination (e.g., for rays bouncing inside an enclosed room).

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=102&annotation=C8DSEJFJ)
