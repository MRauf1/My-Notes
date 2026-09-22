---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Canonical View Volume)[^1]
> The cube containing all 3D points whose Cartesian coordinates are between $-1$ and $+1$, i.e. $(x,y,z) \in [-1,1]^3$: an arbitrary, conveniently-chosen ("canonical") region that all viewing transformations project visible scene geometry into before final display.

# Properties
- $x=-1$ and $x=+1$ map to the left and right edges of the screen; $y=-1$ and $y=+1$ map to the bottom and top edges.
- The [[Orthographic Projection Matrix]] maps the [[Orthographic View Volume]] into this cube directly, while the [[Perspective Projection Matrix]] first maps the [[View Frustum]] onto the orthographic view volume so the same orthographic machinery can then bring it into the canonical view volume.
- The [[Viewport Transformation]] maps this cube (its $x,y$ extent, while carrying $z$ along unchanged) into screen space.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=156&annotation=TY8AMD2M)
