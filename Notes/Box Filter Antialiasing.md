---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Box Filter Antialiasing)[^1]
> An antialiasing approach that sets each pixel's value to the average color of the image over the pixel's square area, rather than a single point sample; this requires treating every drawable entity (even a thin line) as having a well-defined area, e.g. a line as a one-pixel-wide rectangle.

# Properties
- Addresses [[Aliasing]] by replacing point sampling with area averaging.
- Better filters than the box filter exist, but a box filter suffices for all but the most demanding applications.
- Implemented in practice via [[Supersampling]] or [[Multisample Antialiasing]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=193&annotation=R3E2KIHX)
