---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Camera as Linear System)[^1]
> Approximating the incoming light by a discrete, finite set of [[Light Ray|light rays]] rather than a continuous wave, the light intensities in the scene can be represented as a column vector $\ell_w$, whose $n$-th component gives the light intensity at position $n$ heading toward the camera, and the sensor measurements as a column vector $\ell_s$. If the camera's sensors respond linearly to the light intensity at each sensor, the measurements are a linear combination of the scene light intensities, given by the camera's [[Imaging Matrix]] $\mathbf{A}$:
> $$
> \begin{align}
> \ell_s = \mathbf{A} \ell_w
> \end{align}
> $$

![[Camera as Linear System.png]]

# Properties
- Discretizing the incoming light into a finite set of rays is what allows the imaging process to be described with linear algebra.
- Generalizes the [[Pinhole Camera]] and [[Lens|lens-based]] camera models, the special cases where $\mathbf{A}$ is approximately the identity matrix, to arbitrary [[Computational Camera|computational cameras]].
- Recovering the scene $\ell_w$ from sensor measurements $\ell_s$ is an [[Inverse Problem]], addressed by [[Regularized Image Reconstruction]] when $\mathbf{A}$ is not directly invertible.
- Also models biological imaging systems such as the eye's [[Retinal Image Formation|optics]], which are approximately [[Shift-Invariant System|shift-invariant]] near the [[Fovea]].

[^1]: [MIT Vision Book - The Camera as a Linear System](https://visionbook.mit.edu/camera_as_linsys.html)
