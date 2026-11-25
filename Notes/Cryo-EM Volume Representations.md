---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Volume Representations[^1]
> The parameterization of the 3D potential $\varphi$ that reconstruction estimates. It fixes how projections are computed in the [[Cryo-EM Image Formation Model]] and what the cost scales with.

# Types
- **Voxel grids** (real or Fourier space), the standard. Projections are computed by the [[Fourier Slice Theorem]] with NUFFT or gridding. Storage is $O(L^3)$, and [[Iterative Refinement (Cryo-EM)|ML-EM]] costs $O(nL^4\log L)$.
- **Gaussian mixtures / pseudo-atoms** (grid-free):
  - $\varphi = \sum_j a_j\, \mathcal{N}(\mu_j, \Sigma_j)$;
  - examples: E2GMM (2021)[^2], DynaMight (2024)[^3], Gaussian splatting (CryoSplat, 2025)[^4];
  - cost scales with the number of Gaussians, not $L^3$;
  - deforming the centres models motion. A fixed set of Gaussians conserves mass, so it cannot model compositional change.
- **Implicit neural fields** (grid-free): a coordinate network $\hat\varphi_\theta(k)$, evaluated only on the slices needed, as in cryoDRGN ([[Neural Heterogeneous Reconstruction]]).
- **Atomic models**: $\varphi = \sum_a \varphi_{Z_a} * G_{B_a}(\cdot - r_a)$ ([[Atomic Model]]).

# Properties
- Grid-free representations remove the $O(L^3)$ volume and interpolation, but not the cost of the pose search. That needs pruning (branch and bound, adaptive grids), amortized pose prediction, or pose-free methods.

# Questions
> [!question]- Why does a Gaussian representation have closed-form projections?
> A Gaussian density integrated along $z$ is a marginal of a Gaussian, hence Gaussian. Rotating $\mathcal{N}(\mu, \Sigma)$ by $R$ gives $\mathcal{N}(R\mu, R\Sigma R^{\top})$. Projecting along $z$ gives the 2D Gaussian with mean the first two coordinates of $R\mu$ and covariance the top-left $2\times2$ block of $R\Sigma R^{\top}$. The same holds in Fourier space (the transform of a Gaussian is a Gaussian), so the CTF can also be applied analytically before sampling on the pixel grid.

[^1]: [Singer and Sigworth, 2020, p. 16](zotero://open-pdf/library/items/FKVQSKD6?page=16&annotation=33VSZF3R)
[^2]: [Chen & Ludtke (2021), Deep learning-based mixed-dimensional Gaussian mixture model for characterizing variability in cryo-EM, Nature Methods](https://www.nature.com/articles/s41592-021-01220-5)
[^3]: [Schwab, Kimanius, Burt, Dendooven & Scheres (2024), DynaMight: estimating molecular motions with improved reconstruction from cryo-EM images, Nature Methods](https://www.nature.com/articles/s41592-024-02377-5)
[^4]: [CryoSplat: Gaussian Splatting for Cryo-EM Homogeneous Reconstruction (arXiv:2508.04929)](https://arxiv.org/abs/2508.04929)
