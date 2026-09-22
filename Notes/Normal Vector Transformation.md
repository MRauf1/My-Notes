---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Normal Vector Transformation)[^1]
> When a surface is transformed by a matrix $M$, a tangent vector $\mathbf{t}$ transforms correctly as $M\mathbf{t}$ (remaining tangent to the transformed surface), but a surface [[Normal Vector|normal]] vector $\mathbf{n}$ transformed the same way, $M\mathbf{n}$, may no longer be perpendicular to the transformed surface. The matrix that correctly transforms normals is instead
> $$
> \begin{align}
> N = (M^{-1})^T
> \end{align}
> $$
> the transpose of the inverse of $M$.

# Properties
- Since a normal's length is not meaningful, $N$ may be scaled by any nonzero constant and still produce a correctly directed transformed normal; in particular, the division by the determinant in the [[Matrix Inverse|matrix inverse]] formula can be skipped, letting $N$ be built directly from the transpose of the cofactor matrix of $M$.
- Relevant whenever a non-[[Rigid-Body Transformation|rigid]] transformation (e.g., a nonuniform [[Scale Transformation|scale]] or [[Shear Transformation|shear]]) is applied to a surface whose normals (e.g., a [[Triangle Normal Vector|triangle's normal]]) are needed after the transform, such as for shading.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=141&annotation=NMSWY55A)
