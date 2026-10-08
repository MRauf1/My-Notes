---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Fourier Modulation Theorem[^1]
> Multiplying an image by a [[Discrete Complex Exponential|complex exponential]] translates its [[Discrete Fourier Transform|DFT]]:
> $$
> \begin{align}
> \ell[n, m] \exp\left(+2\pi j \left(\frac{u_0 n}{N} + \frac{v_0 m}{M}\right)\right) \xrightarrow{\mathcal{F}} \mathscr{L}[u - u_0, v - v_0]
> \end{align}
> $$
> and multiplying by a cosine wave splits it into two translated copies:
> $$
> \begin{align}
> \ell[n, m] \cos\left(2\pi \left(\frac{u_0 n}{N} + \frac{v_0 m}{M}\right)\right) \xrightarrow{\mathcal{F}} \frac{1}{2}\left(\mathscr{L}[u - u_0, v - v_0] + \mathscr{L}[u + u_0, v + v_0]\right)
> \end{align}
> $$
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

The source writes the exponential with a minus sign and omits the factor $\frac{1}{2}$ in the cosine case; with $\exp(-2\pi j(\cdot))$ the spectrum shifts to $\mathscr{L}[u + u_0, v + v_0]$. The corrected forms follow directly from the DFT definition (or from the transform pairs $\exp \to NM\delta$ and $\cos \to \frac{NM}{2}(\delta + \delta)$ with the dual [[Convolution Theorem]]).[^2]

# Properties
- Multiplying a signal by a wave is called **signal modulation**, a basic operation in communications and also important in image analysis.
- Dual of the [[Fourier Shift Theorem]]: a shift and a modulation are equivalent operations in different domains — a shift in space is a modulation in frequency, and a shift in frequency is a modulation in space.
- Proven from the dual (product) form of the [[Convolution Theorem]], since convolving with a shifted delta shifts the spectrum.
- Modulation by a complex exponential produces a non-real signal, so its Fourier transform no longer has the conjugate symmetry about $u, v = 0$ of real signals.

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Corrected from the source.
