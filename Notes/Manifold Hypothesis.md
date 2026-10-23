---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Manifold Hypothesis[^1]
> High-dimensional real-world data $\mathbf{x} \in \mathbb{R}^D$ (images, audio, shapes, ...) concentrates on or near a low-dimensional [[Manifold|manifold]] $\mathcal{M} \subset \mathbb{R}^D$ (more generally, a union of manifolds) of [[Intrinsic Dimension|intrinsic dimension]] $k \ll D$. Formally, $P_{\text{data}}$ is supported in a tube $T_\sigma(\mathcal{M}) = \{\mathbf{x} : \operatorname{dist}(\mathbf{x}, \mathcal{M}) \leq \sigma\}$ whose radius $\sigma$ is small compared with the spread of the data along $\mathcal{M}$; the exact version $\sigma = 0$ means $P_{\text{data}}$ lives on $\mathcal{M}$ itself.

Whether real data satisfies the hypothesis is an **empirical** claim (strongly supported, below). *Given* it, the consequences, that the data distribution is (nearly) [[Mutually Singular Measures|singular]] with respect to [[Lebesgue Measure]] and that density-based [[Maximum Likelihood Estimation|maximum likelihood]] degenerates, are **theorems**.

# Properties
## Theorems
> [!abstract] Smooth Low-Dimensional Generation Implies Singularity[^2]
> Let $\mathbf{x} = g(\mathbf{z})$ with $\mathbf{z} \in \mathbb{R}^k$ and $g: \mathbb{R}^k \to \mathbb{R}^D$ locally [[Lipschitz Continuity|Lipschitz]] (e.g. $C^1$), $k < D$. Then
> $$
> \begin{align}
> \lambda_D\left(g(\mathbb{R}^k)\right) = 0, \qquad \text{so} \qquad P_{\mathbf{x}} = g_\# P_{\mathbf{z}} \perp \lambda_D
> \end{align}
> $$
> and $\mathbf{x}$ has no [[Probability Density Function|pdf]], whatever the distribution of $\mathbf{z}$.
>
> *Proof sketch.* An $L$-Lipschitz map scales $s$-dimensional Hausdorff measure by at most $L^s$, $\mathcal{H}^s(g(A)) \leq L^s \mathcal{H}^s(A)$. Since $\mathcal{H}^D(\mathbb{R}^k) = 0$ for $k < D$ and $\lambda_D$ is a multiple of $\mathcal{H}^D$, the image is Lebesgue-null (cover $\mathbb{R}^k$ by countably many balls on which $g$ is Lipschitz). For $C^1$ maps this is also the easy case of Sard's theorem: when $k < D$ every point is critical, so the image has measure zero.

> [!abstract] Quantized Data Is Singular[^2]
> Data taking values in a finite set, e.g. 8-bit images in $\{0, \dots, 255\}^D$, has a purely atomic distribution, which is singular with respect to $\lambda_D$ in every dimension, including $D = 1$. This is exact and needs no manifold assumption ([[Dequantization]]).

> [!abstract] Additive Noise with a Density Restores Absolute Continuity[^2]
> If $\mathbf{x} = \mathbf{s} + \boldsymbol{\epsilon}$ with $\boldsymbol{\epsilon}$ independent of $\mathbf{s}$ and $\boldsymbol{\epsilon}$ having a density $f_{\boldsymbol{\epsilon}}$, then $\mathbf{x}$ has the density
> $$
> \begin{align}
> f_{\mathbf{x}}(\mathbf{x}) = \int f_{\boldsymbol{\epsilon}}(\mathbf{x} - \mathbf{s})\, dP_{\mathbf{s}}(\mathbf{s})
> \end{align}
> $$
> however singular $P_{\mathbf{s}}$ is ([[Absolutely Continuous Measure]], [[Convolution Formula]]).

This explains why classical statistics rarely meets the problem: $D$ is small, and data are measurements of a signal plus noise whose scale is comparable to the signal's variation, so the data are [[Absolutely Continuous Measure|absolutely continuous]] and fill their ambient space.

> [!abstract] Density Blow-Up Scales with Codimension (Weyl's Tube Formula)[^2]
> For a compact smooth $k$-dimensional submanifold $\mathcal{M} \subset \mathbb{R}^D$ and $\sigma$ below its reach,
> $$
> \begin{align}
> \operatorname{vol}_D\left(T_\sigma(\mathcal{M})\right) = \operatorname{vol}_k(\mathcal{M})\,\omega_{D-k}\,\sigma^{D-k}\left(1 + O(\sigma^2)\right)
> \end{align}
> $$
> where $\omega_m = \pi^{m/2}/\Gamma(m/2 + 1)$ is the volume of the unit $m$-ball. A distribution spread over the tube therefore has density of order $1/\operatorname{vol}_D(T_\sigma)$, i.e.
> $$
> \begin{align}
> \log p(\mathbf{x}) \approx (D - k)\log\frac{1}{\sigma} - \log \omega_{D-k} - \log \operatorname{vol}_k(\mathcal{M})
> \end{align}
> $$
> which diverges as $\sigma \to 0$, at a rate set by the **codimension** $D - k$.

- **Role of high dimensionality**: high dimensionality alone does not cause singularity. An isotropic Gaussian in $\mathbb{R}^D$ concentrates in a shell of radius $\approx \sigma\sqrt{D}$ ([[Curse of Dimensionality]]), but the shell has thickness $O(1)$ and positive volume, so it still has a density; concentration of measure is not singularity. Dimension enters through the codimension: the same $r^D$ volume scaling that makes the inscribed hypersphere's share of the hypercube vanish makes a thin tube's volume vanish like $\sigma^{D-k}$, and $\omega_{D-k} \to 0$ super-exponentially, so the density on the tube is enormous. For images, $D - k \sim 10^5$.
- **Manifold overfitting**: when the hypothesis holds, maximum likelihood with full-dimensional densities can reach infinite likelihood while converging to the *wrong* distribution on $\mathcal{M}$ ([[Manifold Overfitting]], [[Maximum Likelihood Loss Optimality and Failure Modes]]).

## Empirical evidence
- **Intrinsic dimension estimates**: nearest-neighbor estimators give intrinsic dimensions of roughly $26$ to $43$ for ImageNet, against $D \approx 1.5 \times 10^5$ pixels; datasets of lower intrinsic dimension are easier to learn, and the sample complexity of learning tracks the intrinsic rather than the ambient dimension ([[Intrinsic Dimension]]).[^3]
- **Union of manifolds**: the intrinsic dimension differs across classes of the same dataset, so data is better modeled as a union of manifolds of varying dimension; classes of higher intrinsic dimension are harder to classify.[^4]
- **Compressibility**: the best likelihood models reach about $3$ bits/dim on CIFAR-10, against $8$ bits/dim for raw pixels. By the asymptotic equipartition property ([[Entropy]]), the typical set then occupies a fraction of about $2^{-(8-3)D}$ of the pixel cube, $2^{-15360}$ for $D = 3072$: a measurable sense in which data fills a vanishing share of the volume.
- **Low-dimensional generators suffice**: generators with latent spaces of a few hundred dimensions ([[StyleGAN]], [[Variational Autoencoder|VAEs]], [[Latent Diffusion Model|latent diffusion]]) produce realistic images, and interpolating in latent space traces smooth paths of realistic images.
- **Random points are not data**: uniform samples from the pixel cube look like noise with overwhelming probability, never like natural images.
- **Testability**: whether samples lie near a manifold of given dimension, volume, and curvature can be tested statistically, with sample complexity independent of $D$.[^5]

## Intuition
- **Few causes, many measurements**: an image is the output of a physical process, a renderer mapping scene parameters (geometry, materials, lighting, camera pose) to pixels, so it is a smooth function of far fewer variables than pixels, and the first theorem applies.
- **Symmetry**: applying an $m$-dimensional transformation group (translation, rotation, scaling, illumination change) to an image traces out an $m$-dimensional orbit, a low-dimensional manifold through the data.
- **Local constraints**: neighboring pixels are strongly correlated (smoothness, edges, sparsity in wavelet bases), so most directions in pixel space violate these constraints and are not occupied.
- **Scale-dependent dimension**: below the noise scale $\sigma$, data looks $D$-dimensional; above it, $k$-dimensional. [[Diffusion Model|Diffusion]] and score-based models exploit this by training at many noise levels, where every perturbed distribution has a valid density.[^6]

## Consequences
- Motivates [[Dequantization]], noise perturbation in score-based and [[Diffusion Model|diffusion models]], latent-space models, and evaluation by [[Manifold Precision and Recall]].
- Explains why [[Normalizing Flow|normalizing flows]], which require latent and data dimensions to match, are poorly suited to manifold-supported data.
- Counters the [[Curse of Dimensionality]]: learning depends on $k$, not $D$.

[^1]: Supplementary notes provided by the creator; Bengio, Courville & Vincent (2013); Fefferman, Mitter & Narayanan (2016) in `REFERENCES.md`.
[^2]: Supplementary notes provided by the creator; Federer (1969); Sard (1942); Weyl (1939) in `REFERENCES.md`.
[^3]: Pope, Zhu, Abdelkader, Goldblum & Goldstein (2021) in `REFERENCES.md`.
[^4]: Brown, Caterini, Ross, Cresswell & Loaiza-Ganem (2023) in `REFERENCES.md`.
[^5]: Fefferman, Mitter & Narayanan (2016) in `REFERENCES.md`.
[^6]: Song & Ermon (2019) in `REFERENCES.md`.
