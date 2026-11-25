---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Neural Heterogeneous Reconstruction (cryoDRGN)[^1]
> Modelling continuous [[Conformational Heterogeneity]] with a [[Variational Autoencoder]]:
> - an encoder maps each particle's images to a latent $z_i \in \mathbb{R}^m$;
> - a decoder is a coordinate-based neural network $\hat V_\phi(k, z)$ that represents the Fourier transform of the 3D structure in state $z$;
> - the decoder is evaluated on the central slice rotated by the [[Particle Pose]] $R_i$ ([[Fourier Slice Theorem]]), so the image formation model is built into the likelihood.
>
> Training maximizes the evidence lower bound, with poses typically taken from a homogeneous consensus refinement.

# Properties
- The learned latent space is the estimated conformational landscape. Decoding points along a path through it produces a "movie" of the motion.
- **cryoDRGN-ET** extends it to cryo-ET. The encoder aggregates all tilt images of one particle, so each particle's tilt series is used directly instead of the wedge-corrupted subtomogram[^2].
- It is a nonlinear generalization of [[Cryo-EM Covariance Estimation]], whose linear decoder is $\mu + \sum_j z_j u_j$ in terms of the principal modes $u_j$.

[^1]: [Zhong, Bepler, Berger & Davis (2021), CryoDRGN: reconstruction of heterogeneous cryo-EM structures using neural networks](https://www.nature.com/articles/s41592-020-01049-4)
[^2]: [Rangan, Feathers et al. (2024), CryoDRGN-ET: deep reconstructing generative networks for visualizing dynamic biomolecules inside cells](https://www.nature.com/articles/s41592-024-02340-4)
