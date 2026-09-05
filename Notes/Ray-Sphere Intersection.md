---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Ray-Sphere Intersection)[^1]
> A case of [[Ray Intersection]] against the implicit surface of a [[Sphere|sphere]] with center $\mathbf{c}$ and radius $R$, $(\mathbf{p} - \mathbf{c}) \cdot (\mathbf{p} - \mathbf{c}) - R^2 = 0$. Substituting the ray $\mathbf{p}(t) = \mathbf{e} + t\mathbf{d}$ yields a quadratic equation in $t$, solvable with the [[Quadratic Formula]].

# Properties
- The [[Quadratic Formula|discriminant]] of this quadratic determines how many intersections exist: negative means the ray misses the sphere, zero means the ray grazes it at one point, and positive means it enters at one $t$ and exits at another.
- If only whether the ray hits the sphere is needed (e.g., when a sphere is used as a bounding volume), checking the sign of the discriminant alone suffices.
- The [[Normal Vector]] at an intersection point $\mathbf{p}$ is given by the gradient $2(\mathbf{p} - \mathbf{c})$, whose [[Unit Vector|unit]] form is $(\mathbf{p} - \mathbf{c})/R$.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
