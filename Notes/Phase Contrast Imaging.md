---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] Phase Contrast Imaging[^1]
> The main imaging mode for biological specimens in cryo-EM. The specimen changes only the [[Phase (Waves)|phase]] of the electron wave, which is invisible to an intensity detector exactly in focus ([[Weak Phase Approximation]]). Contrast is created by making the scattered waves [[Interference (Waves)|interfere]] with the unscattered wave after an extra phase difference has been introduced. In the electron microscope this is done by **defocusing** the objective lens ([[Defocus (Cryo-EM)]]); in light microscopy, by phase-contrast or interference-contrast optics.

# Properties
- **An in-line hologram.** The unscattered beam acts as the reference wave and the diffracted beams as the object waves. The microscope records their interference pattern, not a direct image of the specimen.
- **Contrast oscillates with distance.** For a sinusoidal phase grating of period $d$, contrast $\propto \sin(\pi z\lambda/d^2)$ at distance $z$ from the specimen: zero at $z = 0$ and wherever $z\lambda/d^2$ is an integer, with alternating positive and negative maxima in between ([[Contrast Transfer Function]]).
- **The distances are large.** For $d = 10$ Å and $200$ keV electrons ($\lambda = 0.025$ Å), $\theta = \lambda/d = 2.5$ mrad, and the first maximum $\pi z\lambda/d^2 = \pi/2$ falls at $z = d^2/(2\lambda) = 2000$ Å, about $80{,}000$ wavelengths. The diffraction angle is tiny, so the path difference builds up slowly.
- An alternative derivation propagates the exit wave with the Fresnel propagator, whose Fourier transform gives the CTF directly.

# Questions
> [!question]- What determines the optimal defocus for a feature of size $d$, and why does it grow like $d^2$?
> The diffracted wave at angle $\theta \approx \lambda/d$ lags the unscattered wave by $kz(1 - \cos\theta) \approx \pi z\lambda/d^2$. Contrast is greatest when this lag adds $\pi/2$ to the weak-phase $\pi/2$, i.e. $\pi z\lambda/d^2 = \pi/2$, so $z = d^2/(2\lambda)$. It grows like $d^2$ because the lag depends on $\theta^2 \propto 1/d^2$: coarser features scatter at smaller angles and need more propagation to dephase.

[^1]: [Sigworth, p. 2](zotero://open-pdf/library/items/PZX9RV5T?page=2&annotation=8A477UGX)
