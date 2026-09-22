---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Field of View)[^1]
> The vertical field of view $\theta$ of a perspective camera: the angle subtended at the eye by the top and bottom of the [[View Frustum]]'s near plane, related to the near-plane half-height $t$ and near-plane distance $|n|$ by
> $$
> \begin{align}
> \tan\frac{\theta}{2} = \frac{t}{|n|}
> \end{align}
> $$

# Properties
- Distinguished from the horizontal field of view (angle between the left and right sides) and from the diagonal field of view (angle between opposite corners).
- If the window is symmetric ($l=-r$, $b=-t$) and pixels are constrained to be square (undistorted), then $n_x/n_y = r/t$; once the image resolution $(n_x, n_y)$ and the near-plane distance $n$ are fixed, choosing $\theta$ determines $t$ (and hence $r$), leaving no remaining degrees of freedom in the frustum's shape.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=170&annotation=NAC786GB)
