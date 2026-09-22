---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Rigid-Body Transformation)[^1]
> An [[Affine Transformation]] composed only of translations and rotations, with no scaling or shearing, so that it stretches or shrinks nothing: its linear part is a pure [[Rotation Matrix|rotation matrix]].

# Properties
- Preserves distances and angles between points, i.e., it is an [[Isometry]].
- Implemented in [[Homogeneous Coordinates]] as a matrix whose linear block is orthogonal with determinant $+1$ and whose translation column is otherwise unrestricted.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=147&annotation=8CNFJ6WM)
