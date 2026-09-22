---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Viewport Transformation)[^1]
> The final stage of the [[Viewing Transformation]] pipeline: a [[Windowing Transformation]] that maps the $[-1,1]^2$ extent of the [[Canonical View Volume]] to the pixel rectangle $[-0.5,\, n_x-0.5] \times [-0.5,\, n_y-0.5]$ of an $n_x \times n_y$ image,
> $$
> \begin{align}
> M_{vp} = \begin{bmatrix} \frac{n_x}{2} & 0 & 0 & \frac{n_x-1}{2} \\ 0 & \frac{n_y}{2} & 0 & \frac{n_y-1}{2} \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
> \end{align}
> $$

# Properties
- Also called the windowing transformation for this specific mapping. Depends only on the size and position of the output image.
- The $z$-row and $z$-column are included as an identity so the canonical-volume $z$-coordinate (now in $[-1,1]$) is carried through unchanged, even though it does not affect where a point projects on screen; this preserved $z$ is later used for depth ordering (e.g., $z$-buffer hidden-surface algorithms).
- Produces coordinates matching the [[Raster Image Coordinate Convention]] for indexing pixels.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=157&annotation=HXUEFWWG)
