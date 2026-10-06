---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Multivariate Normal Density Product[^1]
> The product of two [[Multivariate Normal Distribution|multivariate normal]] densities in the same variable $\mathbf{w}$ is an unnormalized normal density:
> $$
> \begin{align}
> \mathrm{Norm}_{\mathbf{w}}[\mathbf{a}, \mathbf{A}]\cdot\mathrm{Norm}_{\mathbf{w}}[\mathbf{b}, \mathbf{B}] = \kappa \cdot \mathrm{Norm}_{\mathbf{w}}\left[(\mathbf{A}^{-1} + \mathbf{B}^{-1})^{-1}(\mathbf{A}^{-1}\mathbf{a} + \mathbf{B}^{-1}\mathbf{b}),\; (\mathbf{A}^{-1} + \mathbf{B}^{-1})^{-1}\right]
> \end{align}
> $$
> with constant $\kappa = \mathrm{Norm}_{\mathbf{a}}[\mathbf{b}, \mathbf{A} + \mathbf{B}]$ independent of $\mathbf{w}$. Precisions add, and the new mean is the precision-weighted average of the two means.

> [!abstract] Gaussian Change of Variables[^1]
> A normal density in $\mathbf{v}$ whose mean is linear in $\mathbf{w}$ is, as a function of $\mathbf{w}$, proportional to a normal density in $\mathbf{w}$:
> $$
> \begin{align}
> \mathrm{Norm}_{\mathbf{v}}[\mathbf{A}\mathbf{w}, \mathbf{B}] \propto \mathrm{Norm}_{\mathbf{w}}\left[(\mathbf{A}^T\mathbf{B}^{-1}\mathbf{A})^{-1}\mathbf{A}^T\mathbf{B}^{-1}\mathbf{v},\; (\mathbf{A}^T\mathbf{B}^{-1}\mathbf{A})^{-1}\right]
> \end{align}
> $$
> provided $\mathbf{A}^T\mathbf{B}^{-1}\mathbf{A}$ is invertible.

Both follow by expanding the exponents, which are quadratic in $\mathbf{w}$, and completing the square: only the quadratic and linear terms in $\mathbf{w}$ determine the normal's covariance and mean.

# Properties
- In 1D: $\mathrm{Norm}_w[a, \sigma_a^2]\,\mathrm{Norm}_w[b, \sigma_b^2] \propto \mathrm{Norm}_w\left[\frac{\sigma_b^2 a + \sigma_a^2 b}{\sigma_a^2 + \sigma_b^2}, \frac{\sigma_a^2\sigma_b^2}{\sigma_a^2 + \sigma_b^2}\right]$.
- Underlies conjugate Gaussian [[Bayesian Inference|Bayesian updating]]: a Gaussian prior times a linear-Gaussian likelihood is a Gaussian posterior (the Kalman filter update).
- Used to derive the [[Conditional Diffusion Distribution]] $q(\mathbf{z}_{t-1}|\mathbf{z}_t, \mathbf{x})$ in closed form.[^1]
- Closely related to [[Multivariate Normal Distribution Conditional Distribution]], which gives the same result from the joint-Gaussian viewpoint.

[^1]: [Prince, p. 356](zotero://open-pdf/library/items/BWT7FYX5?page=370&annotation=XA24XYDT)
