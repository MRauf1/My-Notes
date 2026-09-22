---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Culling)[^1]
> Identifying and discarding geometry that cannot contribute to the final image before spending further processing time on it, in order to speed up [[Object-Order Rendering]] of complex scenes.

# Properties
- Compensates for a weakness of object-order rendering: its single pass over all scene geometry wastes effort on primitives that are invisible (e.g., behind other objects or behind the viewer), which can be the majority of a complex scene (e.g., a city model where only a few buildings are visible at once).
- Three commonly used strategies, often combined: [[View Frustum Culling]], [[Occlusion Culling]], and [[Backface Culling]].
- Testing primitives individually for culling can cost more than simply letting the rasterizer discard them; culling is most effective when applied to whole groups of primitives at once, e.g. via a bounding volume.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=194&annotation=M5W2M2AU)
