---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!info] Definition (Point Sample)[^1]
> A point sample of an image is a pixel value that measures the local average color of the image over a small area around a grid point; finding value $x$ at a pixel means "the value of the image in the vicinity of this grid point is $x$."

# Properties
- A camera or scanner pixel is a measurement of the average color of the image over a small area around that pixel; a display pixel is designed so that its red, green, and blue subpixels reproduce that same average color over the face of the pixel.
- Point samples are what a [[Raster Image]] stores at each grid location.
- "A pixel is not a little square!"—Alvy Ray Smith (A. R. Smith, 1995), emphasizing that a pixel value describes a sample of the image rather than a small colored square.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=68&annotation=6QKT4SFD)
