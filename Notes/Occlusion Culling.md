---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Occlusion Culling)[^1]
> A [[Culling]] strategy that discards geometry lying within the view volume but fully hidden (occluded) behind other geometry closer to the camera.

# Properties
- Addresses the same underlying goal as [[Hidden Surface Removal]] (not showing hidden geometry), but avoids processing occluded geometry at all, rather than resolving visibility per pixel only after it has already been rasterized.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=194&annotation=M5W2M2AU)
