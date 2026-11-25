---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] 2D Classification[^1]
> In [[Single-Particle Analysis]], the clustering of particle images that show the same view of the molecule (the same projection direction $R_i^{\top} e_z$), up to in-plane rotation and shift. Images in a class are aligned in 2D and averaged into a **class average** with much higher SNR. It is typically fitted as a 2D [[Mixture Distribution|mixture model]] with latent in-plane poses, by the [[Expectation-Maximization Algorithm]].

# Properties
- Averaging $n$ aligned images of the same view reduces the noise standard deviation by $\sqrt{n}$.
- Uses: removing junk particles; checking view coverage ([[Preferred Orientation]]); input to [[Common Lines]] and other [[Ab Initio Reconstruction]] methods.
- Only in-plane rotations are symmetries of a 2D image. Different out-of-plane views are different projections, so they fall into different classes.
- **ML-EM formulation.** Each image is one of $K$ class images after in-plane rotation, translation, CTF and noise, with class, rotation and shift latent. Two issues: a finite $K$ is a misspecified model of a continuum of views, and a large $K$ is costly and leaves few images per class.
- **"Rich get richer".** Images correlate best with the high-SNR classes, so ML-EM tends to output a few low-resolution classes. The same happens in [[3D Classification]].
- Further uses: picking templates, symmetry detection, quick dataset assessment.
- **Three difficulties**: low SNR hampers clustering and alignment; finding the optimal clustering of $10^5$ images is costly; and the right similarity metric is unclear. An alternative to ML-EM averages each image with its nearest neighbours, found efficiently through [[Bispectrum|bispectra]] of [[Steerable PCA]] coefficients.[^2]

[^1]: [Singer & Sigworth (2020), Computational Methods for Single-Particle Cryo-EM](https://arxiv.org/abs/2003.13828)
[^2]: [Bendory et al., 2020, p. 18](zotero://open-pdf/library/items/N4ZIHINK?page=18&annotation=4RWYMIVG)
