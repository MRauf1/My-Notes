---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Windowing Transformation)[^1]
> An [[Affine Transformation]] that maps one axis-aligned box to another axis-aligned box, by independently scaling and translating the coordinates along each axis so that the source box's extent along an axis maps onto the target box's extent along that same axis.

# Properties
- Implemented as a diagonal [[Scale Transformation|scale]] composed with a translation, expressed as a single matrix using [[Homogeneous Coordinates]].
- Used to implement the [[Viewport Transformation]] (canonical view volume to screen space) and the [[Orthographic Projection Matrix]] (orthographic view volume to canonical view volume), which are both instances of mapping one axis-aligned box to another.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=157&annotation=HXUEFWWG)
