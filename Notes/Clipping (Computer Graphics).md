---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Clipping)[^1]
> Removing the part of a geometric entity that lies on one side of a cutting plane. For example, clipping a triangle against the plane $x=0$ cuts it into two parts whenever the vertices' $x$-coordinates do not all share the same sign; in most applications the portion on the "wrong" side is discarded.

# Properties
- Must precede [[Rasterization]], because simply transforming primitives into screen space and rasterizing them does not work by itself: primitives extending outside the view volume — particularly behind the eye — can otherwise be rasterized incorrectly.
- The "wrong" side, for rendering, is the side outside the view volume. Clipping against all six planes bounding the [[View Frustum|view frustum]] is always safe, but many systems clip only against the near plane.
- Implemented either (1) in world coordinates, using the six planes bounding the truncated viewing pyramid, or (2) in the 4D transformed space before the [[Homogeneous Coordinates|homogeneous divide]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=184&annotation=RRK8ANRY)
