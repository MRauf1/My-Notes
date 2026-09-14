---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Image Coordinate System)[^1]
> The pixel coordinates $(n, m)$ of a point in a captured image, typically measured in pixels, where $n$ indexes the pixel row and $m$ indexes the pixel column. They relate to the [[Camera Coordinate System|camera coordinates]] $(x, y)$ of the virtual camera plane by an affine transform,
> $$
> \begin{align}
> n &= -ax + n_0 \\
> m &= ay + m_0
> \end{align}
> $$
> where $a$ is a constant scaling factor and $(n_0, m_0)$ are the image coordinates of the camera's optical axis.

# Properties
- The $x$ coordinate is negated in this transform because the virtual camera plane's $x$ axis points opposite to the direction in which the pixel row index $n$ increases.
- Comparable to the [[Raster Image Coordinate Convention]] used in computer graphics, though that convention instead indexes pixels from the bottom-left corner of the image rather than relative to a principal point $(n_0, m_0)$ on the optical axis.

[^1]: [MIT Vision Book - Imaging](https://visionbook.mit.edu/imaging.html)
