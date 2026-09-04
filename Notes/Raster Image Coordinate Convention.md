---
tags:
  - computer_science
  - computer_graphics
---

# Definition

> [!info] Definition (Raster Image Coordinate Convention)[^1]
> A raster image with $n_x$ columns and $n_y$ rows is indexed by the pair $(i, j)$ giving the column and row of a pixel, counting from the bottom left, so the bottom-left pixel is $(0,0)$ and the top-right pixel is $(n_x - 1, n_y - 1)$. The rectangular domain of the image is centered on this grid, extending half a pixel beyond the last sample point on each side:
> $$
> \begin{align}
> R = [-0.5,\, n_x - 0.5] \times [-0.5,\, n_y - 0.5].
> \end{align}
> $$

# Properties
- These coordinates are a convention needed to specify pixel positions within a [[Coordinate System]] when implementing cameras and viewing transformations.
- Some APIs and file formats instead index rows top-to-bottom, so that $(0,0)$ is at the top left, for historical reasons tracing to analog television transmission.
- Some systems instead shift coordinates by half a pixel, placing sample points halfway between integers and the image edges at integers.
- The convention for indexing and bounding a [[Raster Image]].

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=68&annotation=6QKT4SFD)
