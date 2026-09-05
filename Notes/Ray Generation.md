---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Ray Generation)[^1]
> The first stage of [[Ray Tracing]]: computing the origin and direction of each pixel's viewing ray from the camera geometry, using the [[Camera Frame]] and the image plane position of the pixel.

# Properties
- A viewing ray is represented as a 3D parametric line $\mathbf{p}(t) = \mathbf{e} + t(\mathbf{s} - \mathbf{e})$ from an origin toward a point $\mathbf{s}$ on the image plane; $t = 0$ gives the origin, $t = 1$ gives $\mathbf{s}$, larger $t$ (for $t>0$) is farther from the origin, and $t < 0$ lies behind the origin.
- In an **orthographic** [[Parallel Projection|parallel view]], all viewing rays share the fixed direction $-\mathbf{w}$, and each ray's origin is the corresponding point on the image plane spanned by $\mathbf{u}, \mathbf{v}$ at $\mathbf{e}$.
- In a **perspective** view, all viewing rays share the same origin $\mathbf{e}$ (the viewpoint), and each ray's direction points from $\mathbf{e}$ toward the pixel's position on an image plane offset by the [[Focal Length]] $d$.
- Oblique views (parallel or perspective) are produced by allowing the image plane normal to be specified separately from the view/projection direction.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=89&annotation=PUQPY4AM)
