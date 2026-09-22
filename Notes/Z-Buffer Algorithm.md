---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Z-Buffer Algorithm)[^1]
> The standard [[Hidden Surface Removal]] algorithm: a depth buffer (or z-buffer) stores, for each pixel, the depth of the closest surface drawn there so far; a new [[Fragment]] overwrites the stored color and depth only if its own depth is closer, and is discarded otherwise.

# Properties
- Implemented in the [[Fragment Blending]] stage by comparing each fragment's depth against the z-buffer's current value at that pixel.
- The z-buffer is initialized to the maximum depth (the depth of the far plane), so the first fragment drawn at each pixel always passes the depth test.
- Because the same (closest) fragment wins the depth test regardless of draw order, the final image does not depend on the order in which surfaces are submitted to the pipeline (ties aside).
- A fragment's depth is obtained like any other attribute, by interpolating the $z$-coordinate across the primitive via [[Gouraud Interpolation]].
- In practice, depths are stored as nonnegative integers rather than floating-point values, since the fast memory needed for the z-buffer is comparatively expensive; this economy introduces some precision problems.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=188&annotation=TT9CS47R)
