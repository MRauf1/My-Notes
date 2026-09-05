---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Perspective Projection)[^1]
> A form of linear perspective in which 3D objects are projected onto an image plane along lines that pass through a single point, the viewpoint, rather than along parallel lines, so objects farther from the viewpoint naturally become smaller. The view is determined by the choice of viewpoint and image plane.

![[Parallel and Perspective Projection.png]]

# Properties
- Objects are projected directly toward the eye and drawn where they meet a view plane in front of the eye; this simple rule automatically produces the classical rules of perspective drawing recognized by artists since the Renaissance.
- Contrasts with [[Parallel Projection]], which uses a fixed projection direction rather than a single viewpoint.
- As with parallel views, distinguished as oblique or non-oblique based on the projection direction at the center of the image.
- All perspective viewing rays share the same origin (the viewpoint) but have different directions, unlike [[Parallel Projection]].
- The [[Camera Frame]] and [[Focal Length]] (image plane distance) together determine the viewing rays of a perspective view.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
