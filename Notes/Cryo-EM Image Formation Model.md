---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Cryo-EM Image Formation Model[^1]
> The electrostatic potential $\varphi$ of the molecule ([[Cryo-EM Density Map]]) is estimated from $n$ particle images, modelled as
> $$
> \begin{align}
> I_i = h_i \star S_{t_i} P(R_i \circ \varphi) + \varepsilon_i, \qquad (R \circ \varphi)(r) = \varphi(R^{-1} r), \qquad i = 1, \dots, n,
> \end{align}
> $$
> where:
> - $P$ is the projection along the beam, $Pf(x, y) = \int f(x, y, z)\, dz$ ([[Projection Approximation]]);
> - $h_i$ is the PSF of image $i$, the inverse Fourier transform of its [[Contrast Transfer Function|CTF]] $H_i$;
> - $R_i \in SO(3)$ is the unknown orientation;
> - $S_{t_i}$ is the unknown in-plane shift, $t_i \in \mathbb{R}^2$ ([[Particle Pose]]);
> - $\varepsilon_i$ is noise.

**Why the translations are often dropped.** Singer and Sigworth write the model with $R_i$ only, for simplicity of exposition: "non-perfect centering" can be added. In practice $t_i$ is a second nuisance parameter, searched alongside $R_i$. It is easy to add because a shift is diagonal in Fourier space, $\mathcal{F}(S_t g)(k) = e^{-2\pi i \langle k, t\rangle}\, \mathcal{F}g(k)$ (with $k$ in cycles per unit length), so it does not interact with the projection. Only 2 shift components exist: a shift along the beam is integrated away by $P$. Its only trace is a slightly different defocus, which is why per-particle defocus is refined.

# Properties
- **Nuisance parameters.** The structure $\varphi$ is the only parameter of interest. Rotations, shifts, per-image defocus, noise spectrum and image normalization are all nuisance parameters, best marginalized ([[Cryo-EM Maximum Likelihood Reconstruction]]).
- **Comparison with medical CT.** CT also reconstructs from projections, but there the poses are known, which makes it a linear inverse problem ([[Tomographic Reconstruction]]), and the noise is far lower. Unknown poses make cryo-EM a nonlinear inverse problem, and high noise demands huge datasets.
- Further effects that can be included: varying contrast, coloured noise, CTF uncertainty, ice-thickness variation.
- It is the end point of the approximation hierarchy A1–A9 applied to the full physical model; the hierarchy, all terms labelled, and the variants are in [[Cryo-EM Forward Model]].

[^1]: [Singer and Sigworth, 2020, p. 13](zotero://open-pdf/library/items/FKVQSKD6?page=13&annotation=NH8AJMCF)
