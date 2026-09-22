---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Backface Culling)[^1]
> A [[Culling]] strategy that discards primitives facing away from the camera, i.e. whose outward-facing [[Triangle Normal Vector|surface normal]] points away from the viewer.

# Properties
- Valid for closed polygonal models (models bounding a closed space with no holes) with consistently outward-facing normals: any polygon facing away from the eye is guaranteed to be overdrawn by a polygon facing the eye, so such polygons can be culled before the pipeline even starts.
- Uses the same facing test later used for silhouette detection.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=195&annotation=ZKFFK2BY)
