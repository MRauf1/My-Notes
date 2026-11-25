---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Tomographic Reconstruction (Known Poses)[^1]
> When the poses $(R_i, t_i)$ and CTFs of all images are known, the map $\varphi \mapsto \big(A_i\varphi\big)_i$, with $A_i\varphi = h_i \star S_{t_i}P(R_i \circ \varphi)$, is **linear** ([[Cryo-EM Image Formation Model]]). Reconstruction is then a linear inverse problem, as in medical CT. Its least-squares solution is
> $$
> \begin{align}
> \hat\varphi = \Big(\sum_{i=1}^n A_i^{\top} A_i\Big)^{-1} \sum_{i=1}^n A_i^{\top} I_i:
> \end{align}
> $$
> back-project every image ($A_i^{\top}$ involves $P^{\top}$, the back-projection operator), then invert the normal operator.

So, ignoring noise: **yes**. If the poses can be estimated reliably, single-particle reconstruction becomes a linear inverse problem. All of its nonlinearity comes from the unknown poses (and, with [[Conformational Heterogeneity]], the unknown states).

# Properties
- **Fourier picture.** By the [[Fourier Slice Theorem]], $A_i^{\top}A_i$ multiplies $\hat\varphi$ by $|H_i|^2$ on the central plane $\Pi_i = R_i^{\top} e_z^{\perp}$. So $\sum_i A_i^{\top}A_i$ is diagonal in Fourier space (in the continuum), with weight $W(k) = \sum_i |H_i(k)|^2\, \delta_{\Pi_i}(k)$. In real space it is a convolution, which on a grid is a Toeplitz matrix: it is applied with FFTs, and the system is solved by conjugate gradient.
- **Solvers**: Fourier gridding, non-uniform FFT (NUFFT), algebraic reconstruction techniques (ART).
- **Ill-posed even with known poses**: poor slice coverage ([[Preferred Orientation]]), CTF zeros and the envelope make $W(k)$ small or zero. The unregularized estimate has large mean squared error and needs a prior ([[MAP Refinement (Cryo-EM)]]).
- With errors in the estimated poses, the problem stays linear but the operator is wrong, which blurs the map.
- **Classical CT solvers in cryo-EM.**
    - Filtered back-projection (FBP) is not optimal: viewing directions are not all represented, and Fourier sampling is non-uniform.
    - The algebraic reconstruction technique (ART, the Kaczmarz method) is slow, because it cannot use the Fourier slice theorem and FFTs.
    - Modern solvers use gridding (weights that resample non-uniform data onto a grid) or NUFFT.[^2]

# Questions
> [!question]- If the poses are known, what kind of problem is reconstruction, and why can it still be ill-posed?
> It is a linear least-squares problem: the forward map $\varphi \mapsto h_i \star S_{t_i}P(R_i\circ\varphi)$ is linear in $\varphi$. In Fourier space, the normal operator multiplies by $W(k) = \sum_i |H_i(k)|^2\delta_{\Pi_i}(k)$. Frequencies on no slice, or only on slices where $H_i \approx 0$, have $W \approx 0$, so the inverse is unstable there and noise is amplified.

> [!question]- Application: With known poses and a Gaussian prior independent across Fourier voxels (variance $\tau^2(k)$), why is the posterior diagonal in the Fourier basis, and how does this instance relate to Paper 1b's criterion?
> The normal operator $\sum_i A_i^{\top}A_i$ is diagonal in Fourier (multiplication by $W(k)$), and the prior covariance is diagonal in Fourier. Diagonal operators commute, so $A^{\top}A$ commutes with the prior covariance, which is exactly the condition under which Paper 1b's pivot is diagonal. The posterior is then independent across frequencies, with covariance $\big(W(k)/\sigma^2 + 1/\tau^2(k)\big)^{-1}$. Its mean is the Wiener-filtered back-projection.
>
> Where it breaks: on a finite grid, the normal operator is Toeplitz rather than circulant, so it is only approximately diagonal. With unknown poses or non-Gaussian priors, the posterior is not Gaussian at all.

[^1]: [Singer and Sigworth, 2020, p. 13](zotero://open-pdf/library/items/FKVQSKD6?page=13&annotation=3Z724FYN)
[^2]: [Bendory et al., 2020, p. 7](zotero://open-pdf/library/items/N4ZIHINK?page=7&annotation=E9L2TLY3)
