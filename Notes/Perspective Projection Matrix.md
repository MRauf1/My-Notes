---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Perspective Projection Matrix)[^1]
> The matrix $P$ that maps the [[View Frustum]] onto the [[Orthographic View Volume]], implementing the perspective divide by which a point's projected size scales as $n/z$ (for a camera at the origin facing $-z$, using the near plane as the projection plane):
> $$
> \begin{align}
> P = \begin{bmatrix} n & 0 & 0 & 0 \\ 0 & n & 0 & 0 \\ 0 & 0 & n+f & -fn \\ 0 & 0 & 1 & 0 \end{bmatrix}
> \end{align}
> $$

# Properties
- Leaves points on the near plane $z=n$ unchanged, and maps the (large) far-plane rectangle of the frustum onto the (small) far-plane rectangle of the orthographic volume.
- Sends any line through the eye (the origin) to a line parallel to the $z$-axis.
- Cannot preserve the literal value of $z$ (since $x,y$ are now divided by $z$), but does preserve the relative order of $z$-values between the near and far planes, which is what later enables depth-based hidden-surface elimination.
- Produces no sign flips in $x$ or $y$, since both $n$ and $z$ are negative throughout the frustum.
- As a homogeneous-coordinate matrix it is only defined up to a nonzero scalar multiple, so a transformation's "inverse" need not be the literal matrix inverse; a convenient representative of the inverse transformation is
$$
\begin{align}
P^{-1} \sim \begin{bmatrix} f & 0 & 0 & 0 \\ 0 & f & 0 & 0 \\ 0 & 0 & 0 & fn \\ 0 & 0 & -1 & n+f \end{bmatrix}
\end{align}
$$
- Concatenated with the [[Orthographic Projection Matrix]] to give the full perspective projection transformation $M_{per} = M_{orth} P$; the complete [[Viewing Transformation]] pipeline is then $M = M_{vp} M_{orth} P M_{cam}$.
- Being a [[Projective Transformation]], it takes lines to lines and planes to planes, and hence triangles to triangles.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=165&annotation=ZCH96XKP)
