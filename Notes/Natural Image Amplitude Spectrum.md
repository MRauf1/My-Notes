---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Natural Image Amplitude Spectrum[^1]
> The magnitude of the [[Discrete Fourier Transform|DFT]] of natural images is quite similar across images and can be approximated by
> $$
> \begin{align}
> \left| \mathscr{L}[u, v] \right| \approx A[u, v] = \frac{a}{(u^2 + v^2)^b}
> \end{align}
> $$
> with $a$ and $b$ two constants. It generally has its maximum at the origin and decays roughly inversely proportional to the radial frequency $\sqrt{u^2 + v^2}$, i.e. $b \approx 1/2$.

# Properties
- Equivalently, the power spectrum $|\mathscr{L}|^2$ of natural images falls off approximately as $1 / f^2$ with radial [[Spatial Frequency|spatial frequency]] $f$; this is consistent with the approximate scale invariance of natural image statistics (Field, 1987).[^2]
- This typical structure has been used as a prior for many tasks, such as image denoising.
- Provides a generic, non-informative amplitude for studying the information carried by the phase ([[Fourier Amplitude and Phase]]).

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
