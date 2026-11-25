---
tags:
  - computer_science
  - cryoEM
---

# Definition
> [!info] CTF Estimation[^1]
> Estimating the defocus parameters $(z_1, z_2, \alpha_z)$ of the [[Contrast Transfer Function]] of a micrograph from its power spectral density (PSD), using the model
> $$
> \begin{align}
> \mathrm{PSD}_I = H^2 \cdot \mathrm{PSD}_f + \mathrm{PSD}_b,
> \end{align}
> $$
> where $\mathrm{PSD}_f$ is the average PSD of the particles and other contents and $\mathrm{PSD}_b$ that of the background noise.

# Properties
- **Thon rings.** $|\mathcal{F} I|^2 = H^2\, |\mathcal{F} P f|^2$ vanishes on the rings of the CTF's zero crossings, giving the pattern of dark and bright rings in the power spectrum.
- **Why it is tractable.** Recovering $H$ is formally ill-posed, since $\mathrm{PSD}_f$ and $\mathrm{PSD}_b$ are unknown. It works because those are slowly varying (usually decreasing in $|k|$), while $H^2$ oscillates rapidly.
- **Procedure.**
  1. Circularly average the PSD.
  2. Subtract a smooth background (local averaging, low-degree polynomial, or linear programming).
  3. Read the defocus off the minima, or cross-correlate with model CTFs.
  4. Fit the astigmatism parameters by 2D cross-correlation.
- **Assumption.** The CTF is taken as constant across the micrograph. A tilt, or particles at different heights in the ice, vary it; per-particle defocus refinement handles this later.
- The Thon rings are the CTF squared, seen through the expected [[Power Spectrum (Signal Processing)|power spectrum]] of a filtered random signal, $\langle S\rangle = \mathbb{E}|G|^2\,|H|^2$.

[^1]: [Singer and Sigworth, 2020, p. 10](zotero://open-pdf/library/items/FKVQSKD6?page=10&annotation=RRN9EHGP)
