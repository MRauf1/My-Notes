---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Spatial Frequency[^1]
> The rate at which a [[Signal (Signal Processing)|signal]] varies over space, by analogy with temporal frequency, which describes how quickly a signal varies over time. For the 2D [[Discrete Complex Exponential|complex exponential]] on an $N \times M$ image,
> $$
> \begin{align}
> e_{u,v}[n, m] = \exp\left(2\pi j \left(\frac{un}{N} + \frac{vm}{M}\right)\right)
> \end{align}
> $$
> the pair $(u, v)$ are the spatial frequencies along the dimensions $n$ and $m$: the number of wave cycles occurring within the image support along each dimension.
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

Spatial frequency gives a more precise language than "sharp" and "blurry" for describing image components and the effect of linear filters: the [[Fourier Transform]] describes a signal as a sum of complex exponentials, each of a different spatial frequency.

# Properties
- Frequencies near the origin of the [[Discrete Fourier Transform|DFT]] correspond to slow, large-scale variations (coarse structure); frequencies further from the origin correspond to fast variations across space (fine detail).
- The $(u, v) = (0, 0)$ component is the [[DC Value|DC]] component.
- An LTI filter acts by reweighting each spatial frequency according to its [[Transfer Function (Signal Processing)|transfer function]], which leads to the classification into [[Low-Pass Filter|low-pass]], [[Band-Pass Filter|band-pass]], and [[High-Pass Filter|high-pass]] filters.
- The amplitude of natural images decays with spatial frequency ([[Natural Image Amplitude Spectrum]]).
- Fourier analysis is also important for understanding sinusoidal [[Positional Encoding]] in transformers, which encodes position with sinusoids of several frequencies.

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
