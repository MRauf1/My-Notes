---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Camera Frame)[^1]
> The [[Orthonormal Basis|orthonormal]] [[Coordinate System]] from which all ray-generation methods start, denoted by the eye point (viewpoint) $\mathbf{e}$ and basis vectors $\mathbf{u}, \mathbf{v}, \mathbf{w}$, with $\mathbf{u}$ pointing rightward, $\mathbf{v}$ pointing upward, and $\mathbf{w}$ pointing backward (opposite the view direction), so that $\{\mathbf{u}, \mathbf{v}, \mathbf{w}\}$ forms a right-handed coordinate system.

![[Camera Frame.png]]

# Properties
- Constructed from the viewpoint $\mathbf{e}$, the view direction ($-\mathbf{w}$), and an up vector, using the [[Gram-Schmidt Algorithm|Gram-Schmidt-like]] process for building an orthonormal basis from two vectors; since $\mathbf{v}$ and $\mathbf{w}$ must be perpendicular, the up vector and $\mathbf{v}$ are generally not the same, but an up vector pointing straight upward in the scene orients the camera "upright."
- Used by [[Ray Generation]] to compute each pixel's viewing ray for both orthographic and perspective views.
- The image is positioned relative to $\mathbf{e}$ using the plane spanned by $\mathbf{u}$ and $\mathbf{v}$, bounded by left/right/bottom/top extents measured along $\mathbf{u}$ and $\mathbf{v}$.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=89&annotation=PUQPY4AM)
