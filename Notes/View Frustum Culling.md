---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (View Frustum Culling)[^1]
> Also called view volume culling: a [[Culling]] strategy that discards geometry lying entirely outside the [[View Frustum|view volume]], since it would produce no fragments when rasterized.

# Properties
- Especially effective when applied to a bounding volume enclosing many triangles grouped into one object: if the bounding volume lies entirely outside the view volume, every triangle inside it can be culled at once without testing them individually.
- Distinct from [[Clipping (Computer Graphics)|clipping]]: culling discards an entire primitive that is invisible before it reaches the pipeline, whereas clipping cuts away the invisible portion of a primitive that is only partially outside the view volume.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=194&annotation=VIXZX6UR)
