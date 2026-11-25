---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Weak Phase Approximation[^1]
> If the specimen's [[Phase Shift|phase shift]] $\varphi(x, y) = \sigma\int V\,dz$ is small ($|\varphi| \ll 1$), the exit wave is linearized by the first two terms of the Taylor series of the [[Complex Exponential Function|exponential]]:
> $$
> \begin{align}
> \Psi(x, y, 0^+) = e^{i\varphi(x,y)} \approx 1 + i\varphi(x, y).
> \end{align}
> $$
> The specimen leaves the incident wave ($1$) unchanged to first order and adds a weak scattered wave $i\varphi$. The factor $i = e^{i\pi/2}$ means this wave is advanced by $90°$ relative to the incident wave.

# Properties
- **One diffracted pair per spatial frequency.** For a sinusoidal phase grating $\varphi(x) = \varepsilon\cos(2\pi x/d)$, the term $i\varphi$ is two plane waves of amplitude $i\varepsilon/2$ travelling at angles $\pm\theta$ with $\sin\theta = \lambda/d$ ([[Plane Wave]], [[Diffraction]]). By Fourier decomposition this covers any specimen, one spatial frequency at a time ([[Spatial Frequency]]).
- **No contrast at the specimen**: $|1 + i\varphi|^2 = 1 + \varphi^2$, with no first-order term. Contrast appears only after propagation or defocus ([[Phase Contrast Imaging]]).
- **It makes image formation linear in the potential**, which is what makes the [[Contrast Transfer Function]] a filter and reconstruction a linear inverse problem given the poses ([[Tomographic Reconstruction]]).
- It fails for thick or heavy specimens, where $\varphi$ is not small or electrons scatter more than once ([[Projection Approximation]]).
- It is approximations A3–A4 of the [[Cryo-EM Forward Model]], which also discusses why the approximation is made and when its bias matters.

# Questions
> [!question]- Derive the CTF of a sinusoidal phase grating at distance $z$ below the specimen.
> Take $\varphi(x) = \varepsilon\cos(2\pi x/d)$ and incident wave $e^{ikz}$. The diffracted waves travel at $\pm\theta$, so their phase along $z$ grows as $kz\cos\theta$:
> $$
> \begin{align}
> \Psi(x, z) = e^{ikz}\big(1 + i\varphi(x)\,e^{ikz(\cos\theta - 1)}\big).
> \end{align}
> $$
> Drop the unit-modulus factor $e^{ikz}$. The imaginary part is $O(\varepsilon)$, so its square is negligible, and the real part is $1 - \varphi\sin[kz(\cos\theta - 1)]$. So
> $$
> \begin{align}
> |\Psi|^2 \approx 1 - 2\varphi(x)\sin[kz(\cos\theta - 1)].
> \end{align}
> $$
> With $\cos\theta - 1 \approx -\theta^2/2 \approx -\lambda^2/(2d^2)$ and $k = 2\pi/\lambda$, the argument is $-\pi z\lambda/d^2$, giving $|\Psi|^2 \approx 1 + 2\varphi(x)\sin(\pi z\lambda/d^2)$. The CTF is $\sin(\pi z\lambda/d^2)$.

> [!question]- Why may the $\varphi^2$ terms be dropped, and what does the approximation assume physically?
> They are $O(\varepsilon^2)$ while the signal is $O(\varepsilon)$, and $\varepsilon$ is of order milliradians per atom, so they are smaller by roughly a factor $10^{3}$. Physically, each electron scatters at most once and weakly (single, kinematic scattering), so the scattered wave is small next to the unscattered one. This fails for thick ice or dense, heavy-atom regions.

[^1]: [Sigworth, p. 4](zotero://open-pdf/library/items/PZX9RV5T?page=4&annotation=JLHI7RV6)
