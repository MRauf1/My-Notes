---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Intrinsic Image Decomposition[^1]
> The decomposition of an image into images of its different physical causes, i.e. recovering intrinsic scene characteristics such as occlusions, depth, surface normals, [[Shading|shading]], reflectance, and reflections. Proposed by Barrow and Tenenbaum (1978).

# Properties
- The classic case is reflectance-shading separation, $\ell(x, y) = r(x, y) \times l(x, y)$, which is ill-posed (one observation, two unknowns per pixel) and requires priors on the structure of each component, e.g. the [[Retinex Algorithm]]'s smooth illumination and piecewise-constant reflectance.
- Building such image models is a major research theme in computer vision.

[^1]: [MIT Vision Book - Image Derivatives](https://visionbook.mit.edu/derivatives.html)
