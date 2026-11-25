---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Steerable PCA[^1]
> [[Principal Component Analysis]] of images that accounts for all their in-plane rotations without rotating them explicitly. Expand each image in a **steerable basis** $\psi_{k,q}(r,\theta) = R_{k,q}(r)\, e^{ik\theta}$: radial functions times angular Fourier modes. Examples are Fourier–Bessel functions, 2D prolate spheroidal wave functions and Zernike polynomials. Averaged over all in-plane rotations, the covariance of the coefficients is **block-diagonal in the angular frequency $k$**.

# Properties
- **Complexity.** An $L\times L$ image covariance has $L^4$ entries, but only $O(L^3)$ survive block-diagonalization. Cost drops from $O(NL^4 + L^6)$ to $O(NL^3 + L^4)$: sample covariance plus eigendecompositions of the blocks.
- **High dimensions.** The image dimension is comparable to the number of images, so the sample eigenvalues are biased. Eigenvalue shrinkage under the spiked covariance model gives better denoising.
- **Uses**: denoising images, and [[2D Classification]] (with [[Bispectrum]]-based nearest neighbours). Covariance estimation in cryo-EM goes back to Kam ([[Kam's Method]]).

# Questions
> [!question]- Why is the rotation-averaged covariance block-diagonal in the angular frequency $k$?
> Let $\rho(\alpha)$ rotate images by $\alpha$. On the steerable basis it acts diagonally: $\psi_{k,q} \mapsto e^{-ik\alpha}\psi_{k,q}$. The averaged covariance $C = \int \rho(\alpha)\, \Sigma\, \rho(\alpha)^{*}\, d\alpha/2\pi$ commutes with every $\rho(\alpha)$. In coefficients, its $(k,q),(k',q')$ entry picks up the factor $\int e^{-i(k-k')\alpha}d\alpha/2\pi = \delta_{kk'}$. So entries between different angular frequencies vanish, and $C$ preserves each $k$-subspace (Schur's lemma for $SO(2)$).

> [!question]- Application: How is steerable PCA an instance of the commutation criterion from the thesis question ($[L,A] = 0 \Rightarrow G$ block-diagonal)?
> The role of the basis operator $A$ is played by the generator of in-plane rotations, $\partial_\theta$, whose eigenfunctions are the steerable modes $e^{ik\theta}$ (eigenvalue $ik$). The role of $L$ is played by the averaged covariance $C$. Rotation-averaging makes $C$ commute with the rotation group, hence with $\partial_\theta$. So $C$ is block-diagonal in the eigenbasis of $\partial_\theta$, with one block per eigenvalue $k$, exactly as $[L,A] = 0$ makes the propagator block-diagonal.
>
> Where it breaks: the blocks are not $1\times1$, because the eigenvalue $ik$ is shared by all radial indices $q$. If the in-plane rotation distribution is non-uniform, the averaging no longer gives exact commutation, and off-diagonal blocks appear, which measure the non-uniformity.

[^1]: [Bendory et al., 2020, p. 19](zotero://open-pdf/library/items/N4ZIHINK?page=19&annotation=7Z3U246N)
