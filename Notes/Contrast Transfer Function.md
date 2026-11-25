---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Contrast Transfer Function (CTF)[^1]
> For a weak phase object imaged with defocus $z$ and electron wavelength $\lambda$, the micrograph is the projection filtered by the CTF $H$ ([[Projection Approximation]]):
> $$
> \begin{align}
> I = h \star P f, \qquad (\mathcal{F} I)(k) = H(k)\, (\mathcal{F} P f)(k), \qquad h = \mathcal{F}^{-1} H,
> \end{align}
> $$
> where $h$ is the [[Point Spread Function]]. To first order,
> $$
> \begin{align}
> H(k) = \sin\!\big(-\pi z \lambda |k|^2\big),
> \end{align}
> $$
> and the more accurate model is
> $$
> \begin{align}
> H(k) = \sin\!\Big(-\pi z \lambda |k|^2 + \tfrac{\pi}{2} C_s \lambda^3 |k|^4 - w\Big)\, E(|k|),
> \end{align}
> $$
> with spherical aberration $C_s$, amplitude contrast $w$ and envelope $E$ ([[CTF Envelope Function]]). With astigmatism, the defocus depends on the direction $\alpha_k$ of $k$:
> $$
> \begin{align}
> z(\alpha_k) = \tfrac12(z_1 + z_2) + \tfrac12(z_1 - z_2)\cos\!\big(2(\alpha_k - \alpha_z)\big).
> \end{align}
> $$

**Derivation.** The scattered wave at frequency $k$ has relative amplitude $\varepsilon(k) \ll 1$. It carries the weak-phase shift $\pi/2$ plus the defocus path difference $\pi z \lambda |k|^2$, so $\Delta\varphi = \pi/2 + \pi z\lambda|k|^2$. The detected intensity is
$$
\begin{align}
|\psi_u + \psi_s|^2 = |\psi_u|^2\,\big|1 + \varepsilon(k) e^{i\Delta\varphi}\big|^2 \approx |\psi_u|^2\big(1 + 2\varepsilon(k)\cos\Delta\varphi\big),
\end{align}
$$
and $\cos(\pi/2 + x) = \sin(-x)$ gives $H$.

# Properties
- **Zero crossings.** $H$ vanishes on rings in Fourier space, where the information in that image is completely lost. It oscillates faster at high $|k|$, because the phase grows like $|k|^2$.
- **Sign.** $H$ starts negative at low $|k|$, so particles look dark.
- **Defocus trade-off.** Larger defocus gives more low-frequency contrast (easier [[Particle Picking]]) but faster high-frequency oscillation.
- **Spherical aberration** matters only at $|k| \gtrsim 0.25$ Å$^{-1}$. Astigmatism is usually small, so $H$ is nearly circularly symmetric.
- **Phase plates.** A Volta phase plate shifts the phase of $H$ to boost low-frequency contrast, but it drifts and its value is debated.
- It is estimated per micrograph ([[CTF Estimation]]) and undone or accounted for downstream ([[CTF Correction]]).
- **Centring depends on the CTF.** The CTF suppresses the lowest frequencies, so the centre of mass of a particle image depends on the defocus. Two images of the same view at different defoci have different centres, which complicates picking.[^2]
- **Model it rather than invert it.** Instead of correcting images, the CTF can be included in the forward model of ML-EM, SGD or the method of moments. Since different micrographs have different CTFs, full correction is possible in principle. Standard estimation software (CTFFIND4, Gctf) fits model CTFs to the Thon rings.
- **Sign conventions.** Derived with the focal plane a distance $z$ *below* the specimen, $\mathrm{CTF} = \sin(\pi z\lambda f^2)$ ([[Weak Phase Approximation]]). In practice one focuses *above* the specimen (underfocus $\delta = -z > 0$, [[Defocus (Cryo-EM)]]), so the literature CTF has the opposite polarity: $\mathrm{CTF} = \sin(\chi - \alpha)\,e^{-Bf^2/4}$, with $\chi = -\pi\lambda\delta f^2 + \tfrac{\pi}{2}C_s\lambda^3 f^4$ ([[Wave Aberration Function]], [[Amplitude Contrast]], [[Spherical Aberration]]).[^sigworth]
- **Physical origin**: interference between the unscattered and diffracted waves, which the microscope records as an in-line hologram ([[Phase Contrast Imaging]]).

# Questions
> [!question]- Why does an in-focus microscope give (almost) no contrast for a weak phase object?
> The specimen only changes the phase: $\psi \approx \psi_u(1 + i\sigma Pf)$, so $|\psi|^2 = |\psi_u|^2(1 + O(\sigma^2))$, and the first-order term is purely imaginary and invisible in intensity. Defocus adds a $k$-dependent phase $\pi z\lambda|k|^2$ that rotates part of the scattered wave into phase with the unscattered wave. With $z = 0$ (and $C_s, w$ ignored), $H(k) = \sin(0) = 0$ for every $k$.

> [!question]- Why must data be collected at several defocus values?
> The zeros of $H = \sin(-\pi z\lambda|k|^2)$ lie at $|k| = \sqrt{n/(z\lambda)}$, $n = 1, 2, \dots$, which depend on $z$. With different defoci, the rings sit at different radii, so every nonzero frequency is measured with nonzero $H$ in some images. A single defocus loses those rings entirely.

[^1]: [Singer and Sigworth, 2020, p. 6](zotero://open-pdf/library/items/FKVQSKD6?page=6&annotation=NCCVU36S)
[^2]: [Bendory et al., 2020, p. 16](zotero://open-pdf/library/items/N4ZIHINK?page=16&annotation=UZRDV3YV)
[^sigworth]: [Sigworth, p. 5](zotero://open-pdf/library/items/PZX9RV5T?page=5&annotation=X35IUQIM)
