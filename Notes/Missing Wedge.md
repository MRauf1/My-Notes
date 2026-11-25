---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Missing Wedge[^1]
> For a single-axis [[Tilt Series]] about $e_y$ with tilts $|\theta| \le \alpha < 90^\circ$, the beam directions in the specimen frame are $d_\theta = (\pm\sin\theta, 0, \cos\theta)$. By the [[Fourier Slice Theorem]], the measured frequencies are the union of the central planes $d_\theta^{\perp}$, all of which contain the $k_y$ axis. The **missing wedge** is the set of frequencies that are never measured:
> $$
> \begin{align}
> W = \{k \in \mathbb{R}^3 : |k_z| > \tan\alpha\, |k_x|\},
> \end{align}
> $$
> a double wedge of half-angle $90^\circ - \alpha$ around the $k_z$ axis, extended along all of $k_y$. In the ideal case (continuous angles, no noise), the reconstruction is
> $$
> \begin{align}
> \hat f_{\text{rec}} = \mathbf{1}_{W^c}\, \hat f \quad\Longleftrightarrow\quad f_{\text{rec}} = f * \text{PSF}, \qquad \text{PSF} = \mathcal{F}^{-1}\big[\mathbf{1}_{W^c}\big].
> \end{align}
> $$

![[Cryo-ET Tilt Series.mp4]]
![[Missing Wedge in Fourier Space.png]]
![[Missing Wedge Artifacts.png]]

# Properties
- For $\alpha = 60^\circ$, the wedge takes up $1/3$ of the directions in the $k_x$–$k_z$ plane.
- **Anisotropic resolution.** The missing frequencies have large $|k_z|$ and small $|k_x|$: fine variation along the beam axis. The [[Point Spread Function]] is elongated along $z$, with X-shaped streaks at $\pm\alpha$. A commonly quoted elongation factor is $e = \sqrt{(\alpha + \sin\alpha\cos\alpha)/(\alpha - \sin\alpha\cos\alpha)} \approx 1.55$ at $\alpha = 60^\circ$ (usually attributed to Radermacher 1988; formula not checked against the paper).
- **Surfaces parallel to the slab vanish.** Such a surface varies only along $z$, so its Fourier content lies on the $k_z$ axis, inside $W$. Examples are flat membranes and the tops and bottoms of vesicles. Surfaces parallel to the beam survive.
- **The tilt axis is unaffected.** Every measured plane contains $k_y$, so the anisotropy lives in the $x$–$z$ plane only.
- **Dual-axis** tilting shrinks the missing region to a missing *pyramid*. **Conical** tilting gives a missing *cone*.
- Discrete tilt steps leave additional gaps between neighbouring planes, and these widen with $|k|$.
- [[Subtomogram Averaging]] fills it in, provided the copies' orientations are diverse.

# Questions
> [!question]- Why is the unmeasured set a wedge (extended along $k_y$) rather than a cone?
> The tilt axis $e_y$ is perpendicular to every beam direction $d_\theta$, so every measured plane $d_\theta^{\perp}$ contains the whole $k_y$ axis. Whether a frequency $k$ is measured therefore depends only on the angle of $(k_x, k_z)$, not on $k_y$, so the missing set is invariant under translation along $k_y$: a wedge. In conical tilting, the beam directions sweep a cone around $z$ instead, and the missing set is a cone around $k_z$.

> [!question]- Why does a flat membrane parallel to the slab disappear from the tomogram, while one parallel to the beam survives?
> A membrane with normal $e_z$ has density $f(x, y, z) \approx h(z)$ over its extent, so $\hat f$ is concentrated near the $k_z$ axis. That axis lies in $W$ for every $\alpha < 90^\circ$. A membrane with normal $e_x$ has its Fourier content near the $k_x$ axis, which is measured at every tilt.

> [!question]- Why is the resolution along the tilt axis $y$ unaffected?
> Every measured plane contains the $k_y$ axis, and $W$ is a union of full lines parallel to $k_y$ through the angles $|\phi| > \alpha$ in the $k_x$–$k_z$ plane. So the loss depends only on direction in the $k_x$–$k_z$ plane: the PSF factors as a narrow function of $y$ times an anisotropic function of $(x, z)$.

[^1]: [Cryogenic electron tomography (Wikipedia)](https://en.wikipedia.org/wiki/Cryogenic_electron_tomography)
