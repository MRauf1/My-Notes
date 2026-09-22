---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Scale Transformation)[^1]
> A [[Geometric Transformation]] that scales each Cartesian coordinate independently along the coordinate axes, potentially changing a vector's length and, if a scale factor is negative, its direction:
> $$
> \begin{align}
> \text{scale}(s_x, s_y) = \begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}, \qquad \text{scale}(s_x, s_y, s_z) = \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & s_z \end{bmatrix}
> \end{align}
> $$

# Properties
- The inverse of $\text{scale}(s_x, s_y, s_z)$ is $\text{scale}(1/s_x, 1/s_y, 1/s_z)$.
- [[Reflection]] across a coordinate axis is the special case of a single negative scale factor.
- By the [[Spectral Theorem]], every symmetric matrix is geometrically a scale transformation along some (possibly non–axis-aligned) set of orthogonal directions, its eigenvectors; by the [[Singular Value Decomposition Theorem]], every matrix includes a scale by its singular values sandwiched between two rotations.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=125&annotation=I4DPHAAZ)
