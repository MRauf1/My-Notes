---
tags:
  - computer_science
  - computer_vision
  - cryoEM
---

# Definition
> [!info] Rotation Synchronization[^1]
> Estimate absolute rotations $R_1, \dots, R_N \in SO(3)$, up to one global rotation, from noisy measurements of relative rotations $R_iR_j^{\top}$ for many pairs $(i,j)$, using all pairs simultaneously. In cryo-EM, the relative rotations come from [[Common Lines]]. The estimate is computed by a spectral method or semidefinite programming, with theoretical guarantees.

# Properties
- **More robust than angular reconstitution**, which assigns rotations sequentially from triples of images and accumulates errors.
- **Still needs high SNR inputs.** At low SNR every rotation estimator fails ([[Multi-Reference Alignment]]), so in cryo-EM it is applied to class averages ([[2D Classification]]). These blur fine detail, which limits the resolution of the result.
- The same problem appears in structure from motion and SLAM.

# Questions
> [!question]- Why does the spectral method work in the noiseless case?
> Stack the rotations into $\mathbf{R} = [R_1; \dots; R_N] \in \mathbb{R}^{3N\times3}$, and form the $3N\times3N$ block matrix $H$ with blocks $H_{ij} = R_iR_j^{\top}$. Then $H = \mathbf{R}\mathbf{R}^{\top}$, and since $\mathbf{R}^{\top}\mathbf{R} = \sum_i R_i^{\top}R_i = NI_3$, we get $H\mathbf{R} = N\mathbf{R}$. So $H$ has rank 3, and its top-3 eigenspace is the column span of $\mathbf{R}$. The top eigenvectors give $\mathbf{R}Q$ for some orthogonal $Q$, i.e. all rotations up to a global one (and a possible reflection, the [[Handedness Ambiguity]]). With noise, the top eigenvectors are a stable estimate when the noise is small relative to the spectral gap $N$.

[^1]: [Bendory et al., 2020, p. 13](zotero://open-pdf/library/items/N4ZIHINK?page=13&annotation=KZ2UWE5T)
