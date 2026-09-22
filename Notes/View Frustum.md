---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (View Frustum)[^1]
> The perspective view volume: a frustum (a truncated pyramid) bounded by a near plane $z=n$, a far plane $z=f$, and left/right/bottom/top planes, analogous to the [[Orthographic View Volume]] but tapering toward the eye rather than having parallel sides.

# Properties
- Mapped onto the [[Orthographic View Volume]] by the [[Perspective Projection Matrix]], after which the ordinary orthographic pipeline ([[Orthographic Projection Matrix]] then [[Viewport Transformation]]) applies.
- Its tapering shape produces the characteristic $1/z$ size scaling of [[Perspective Projection]].
- Its near-plane half-height, together with the near-plane distance, is set via the [[Field of View]].
- Geometry lying entirely outside it can be discarded by [[View Frustum Culling]] before rendering, and any geometry that still crosses its boundary is handled by [[Clipping (Computer Graphics)|clipping]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=167&annotation=9BV4UXRN)
