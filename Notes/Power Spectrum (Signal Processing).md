---
tags:
  - mathematics
  - real_analysis
  - cryoEM
---

# Definition
> [!info] Power Spectrum (Signal Processing)[^1]
> For a signal $f$ with [[Fourier Transform]] $F$, the power spectrum is $S(u) = |F(u)|^2$. For a random signal, the transform is random too, and the **expected** power spectrum $\langle S(u)\rangle = \mathbb{E}|F(u)|^2$ shows which frequency components are large on average, as the variance does for a random variable.

# Properties
- **Filtered signals.** If $F = G\cdot H$, with $G$ random and $H$ a fixed filter, then
$$
\begin{align}
\langle S(u)\rangle = \mathbb{E}|G(u)|^2\,|H(u)|^2.
\end{align}
$$
This needs no independence assumption, since $H$ is deterministic. (The source phrases it as independence of $F$ and $H$.)
- **In cryo-EM**, the filter is the CTF, so a micrograph's power spectrum shows $\mathrm{CTF}^2$: the Thon rings used for [[CTF Estimation]] ([[Contrast Transfer Function]]).
- It is the transform of the autocorrelation ([[Cross-Correlation]]); for stationary random signals this is the Wiener–Khinchin theorem.
- It discards all phases, so very different signals can share a power spectrum ([[Fourier Amplitude and Phase]]).
- Not to be confused with the spectral power distribution of light ([[Power Spectrum]]).

[^1]: [Sigworth, Fourier transform notes, p. 6](zotero://open-pdf/library/items/FEUF2XYA?page=6&annotation=KN638UAZ)
