---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Orthographic Projection Matrix)[^1]
> The [[Windowing Transformation]] matrix $M_{orth}$ mapping the [[Orthographic View Volume]] $[l,r]\times[b,t]\times[f,n]$ to the $[-1,1]^3$ [[Canonical View Volume]]:
> $$
> \begin{align}
> M_{orth} = \begin{bmatrix} \frac{2}{r-l} & 0 & 0 & -\frac{r+l}{r-l} \\ 0 & \frac{2}{t-b} & 0 & -\frac{t+b}{t-b} \\ 0 & 0 & \frac{2}{n-f} & -\frac{n+f}{n-f} \\ 0 & 0 & 0 & 1 \end{bmatrix}
> \end{align}
> $$

# Properties
- Composed with the [[Viewport Transformation|viewport matrix]] $M_{vp}$ to project 3D points directly to screen space in one combined matrix, $M_{vp} M_{orth}$, carrying along the canonical $z$-coordinate (now in $[-1,1]$) for later use.
- Serves as the last stage of the perspective pipeline as well: the [[Perspective Projection Matrix]] first maps the [[View Frustum]] onto the orthographic view volume, after which $M_{orth}$ completes the mapping to the canonical view volume.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=158&annotation=X5JKG5C4)
