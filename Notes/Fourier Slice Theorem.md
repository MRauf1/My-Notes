---
tags:
  - mathematics
  - real_analysis
  - cryoEM
---

# Definition
> [!info] Fourier Slice Theorem (Projection-Slice Theorem)[^1]
> Let $f \in L^1(\mathbb{R}^n)$ and let $d$ be a unit vector. Define the projection of $f$ along $d$ as the function on the hyperplane $d^{\perp}$
> $$
> \begin{align}
> (P_d f)(x) = \int_{\mathbb{R}} f(x + s\,d)\, ds, \qquad x \in d^{\perp}.
> \end{align}
> $$
> Then the $(n-1)$-dimensional [[Fourier Transform]] of the projection equals the $n$-dimensional Fourier transform of $f$ restricted to the **central** hyperplane $d^{\perp}$:
> $$
> \begin{align}
> \widehat{P_d f}(\xi) = \hat f(\xi), \qquad \xi \in d^{\perp}.
> \end{align}
> $$

# Properties
- **General form.** Projecting along a $k$-dimensional subspace $U$ (integrating over $U$) gives the restriction of $\hat f$ to the central subspace $U^{\perp}$.
- **Reconstruction.** If the planes $d^{\perp}$ over the measured directions cover $\mathbb{R}^n$, then $\hat f$, and hence $f$, is determined. In [[Cryo-Electron Microscopy|cryo-EM]], each image measures one central plane of the 3D transform of the potential ([[Projection Approximation]]). This underlies the [[Tomogram]], the [[Missing Wedge]], and [[Single-Particle Analysis]].
- The relation is linear in $f$, and the forward map $f \mapsto P_d f$ is the X-ray transform (in 2D, the Radon transform).
- **Operator form.** $S\,R\,\mathcal{F}_3\varphi = \mathcal{F}_2 P R\varphi$, with $S$ restriction to the $k_z = 0$ plane and $P$ projection along $z$. It is a corollary of the fact that the Fourier transform commutes with rotations, $R\mathcal{F} = \mathcal{F}R$: rotating the volume rotates its transform, so a projection along any direction reduces to the $z$ case.[^2]

# Questions
> [!question]- What is the proof idea, and where is $f \in L^1$ used?
> For $\xi \in d^{\perp}$, write every $y \in \mathbb{R}^n$ uniquely as $y = x + s\,d$ with $x \in d^{\perp}$. Since $\xi \cdot d = 0$, we have $\xi \cdot y = \xi \cdot x$, so
> $$
> \begin{align}
> \widehat{P_d f}(\xi) = \int_{d^{\perp}} \int_{\mathbb{R}} f(x + s d)\, e^{-j\,\xi\cdot x}\, ds\, dx = \int_{\mathbb{R}^n} f(y)\, e^{-j\,\xi\cdot y}\, dy = \hat f(\xi).
> \end{align}
> $$
> Merging the iterated integral into one integral over $\mathbb{R}^n$ is Fubini's theorem, which needs $f \in L^1$. It is also used to know that $P_d f$ is defined almost everywhere and is integrable.

> [!question]- Why does a single-axis tilt series over the full range $\theta \in (-90^\circ, 90^\circ]$ determine $f$ on $\mathbb{R}^3$, while $|\theta| \le \alpha < 90^\circ$ does not?
> With tilt axis $e_y$, every beam direction $d_\theta$ is perpendicular to $e_y$, so every measured plane $d_\theta^{\perp}$ contains the $k_y$ axis. Its other spanning direction makes angle $\theta$ with the $k_x$ axis in the $k_x$–$k_z$ plane. Any $k = (k_x, k_y, k_z)$ lies in the plane whose angle is that of $(k_x, k_z)$, which some $\theta$ in the full range attains. So the planes cover $\mathbb{R}^3$, and $f$ is determined by Fourier inversion. With $|\theta| \le \alpha$, the frequencies with $|k_z| > \tan\alpha\, |k_x|$ are never measured: this is the [[Missing Wedge]].

> [!question]- Why must the measured slice pass through the origin?
> Integrating along $d$ removes all variation of $f$ along $d$, and that is exactly the content of $\hat f$ at frequencies with a component along $d$. What remains is $\hat f$ at frequencies with zero $d$-component, i.e. on $d^{\perp}$, which is a subspace and so contains $0$. In particular $\widehat{P_d f}(0) = \hat f(0) = \int f$: every projection has the same total mass.

[^1]: [Projection-slice theorem (Wikipedia)](https://en.wikipedia.org/wiki/Projection-slice_theorem)
[^2]: [Bendory et al., 2020, p. 7](zotero://open-pdf/library/items/N4ZIHINK?page=7&annotation=I8E5D67T)
