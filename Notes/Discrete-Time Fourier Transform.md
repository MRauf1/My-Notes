---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Discrete-Time Fourier Transform (DTFT)[^1]
> The Fourier transform of a discrete signal of infinite length, obtained from the [[Discrete Fourier Transform|DFT]] by letting the sum become infinite and substituting $w = 2\pi u / N$:
> $$
> \begin{align}
> \mathscr{L}(w) = \sum_{n=-\infty}^{\infty} \ell[n] \exp(-jwn)
> \end{align}
> $$
> with inverse, integrated over a single period,
> $$
> \begin{align}
> \ell[n] = \frac{1}{2\pi} \int_{2\pi} \mathscr{L}(w) \exp(jwn) \, dw
> \end{align}
> $$
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

# Properties
- The frequency $w$ is a continuous variable, and $\mathscr{L}(w)$ is periodic with period $2\pi$.
- Maps discrete, infinite length signals to continuous, finite length ($2\pi$) spectra ([[Fourier Transform]]).
- For a signal supported on $[0, N-1]$, the DFT equals the DTFT sampled at $w = 2\pi u / N$, $u = 0, \dots, N-1$.[^2]
- The periodicity of the spectrum reflects that discrete frequencies $w$ and $w + 2\pi$ give identical samples, the source of [[Aliasing]] when a continuous signal is [[Sampling (Signal Processing)|sampled]].[^2]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
