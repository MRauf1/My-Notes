---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Regularized Image Reconstruction)[^1]
> Because a camera's [[Imaging Matrix]] $\mathbf{A}$ may be non-invertible or ill-conditioned, recovering the scene $\ell_w$ from noisy sensor measurements $\ell_s$ is [[Regularization|regularized]] by minimizing an objective that trades off explaining the observations against a preference for a small $\ell_w$:
> $$
> \begin{align}
> E = \lVert \ell_s - \mathbf{A}\ell_w \rVert^2 + \lambda \lVert \ell_w \rVert^2
> \end{align}
> $$
> which yields the reconstruction $\ell_w = \mathbf{B}\ell_s$, where
> $$
> \begin{align}
> \mathbf{B} = (\mathbf{A}^T\mathbf{A} + \lambda \mathbf{I})^{-1}\mathbf{A}^T
> \end{align}
> $$
> is the **regularized inverse** of the imaging matrix.

# Properties
- The regularization parameter $\lambda$ determines the trade-off between explaining the observations ($\ell_s \approx \mathbf{A}\ell_w$) and satisfying the regularization term (favoring small $\ell_w$).
- An instance of recovering the input to an [[Inverse Problem]] from its output, needed whenever a camera's [[Imaging Matrix]] is not directly, or not well-conditionedly, invertible.

[^1]: [MIT Vision Book - The Camera as a Linear System](https://visionbook.mit.edu/camera_as_linsys.html)
