---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Imaging Matrix)[^1]
> The matrix $\mathbf{A}$ relating a camera's sensor measurements $\ell_s$ to the scene's light intensities $\ell_w$ in the [[Camera as Linear System|linear camera model]] $\ell_s = \mathbf{A}\ell_w$, representing the camera itself.

# Properties
- For a [[Pinhole Camera]] or conventional [[Lens|lens-based]] camera, where the observed intensities are directly an image of the reflected scene intensities, $\mathbf{A}$ is approximately an identity matrix, since each sensor measurement depends only on a single scene element.
- For more general [[Computational Camera|computational cameras]], $\mathbf{A}$ may differ substantially from an identity matrix, and $\ell_w$ must instead be estimated from $\ell_s$.
- May be non-invertible or ill-conditioned, particularly in the presence of noise, which motivates [[Regularized Image Reconstruction|regularizing]] its inverse.

[^1]: [MIT Vision Book - The Camera as a Linear System](https://visionbook.mit.edu/camera_as_linsys.html)
