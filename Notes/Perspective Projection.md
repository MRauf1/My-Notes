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
- The [[Perspective Projection Equations]] give the analogous quantitative projection for a [[Pinhole Camera]], relating world and camera-plane coordinates directly by similar triangles.
- The key quantitative property is that projected size scales as $1/z$: for an eye at the origin looking down $-z$, a point at distance $y$ along the image-plane axis, at depth $z$, projects to $y_s = (d/z)\,y$ on a plane at distance $d$.[^2] This underlies the [[Perspective Projection Matrix]] used within the [[Viewing Transformation]] pipeline.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=84&annotation=4U5WR7CJ)
[^2]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=161&annotation=KCQMUZQG)
