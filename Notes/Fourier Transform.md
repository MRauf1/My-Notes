---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Fourier Transform[^1]
> For infinite length signals on the continuous domain, the Fourier transform is
> $$
> \begin{align}
> \mathscr{L}(w) = \int_{-\infty}^{\infty} \ell(t) \exp(-jwt) \, dt
> \end{align}
> $$
> where $\mathscr{L}(w)$ is a continuous function of the frequency $w$ (in radians). Its inverse is
> $$
> \begin{align}
> \ell(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \mathscr{L}(w) \exp(jwt) \, dw
> \end{align}
> $$
> In 2D, the integrals become double integrals over the spatial variables $x$ and $y$.
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

The Fourier transform describes a signal as a sum (integral) of complex exponentials, each of a different [[Spatial Frequency|frequency]]. It is the basis of many computer vision approaches, a key tool for understanding images and how [[Shift-Invariant System|linear spatially invariant filters]] transform them, and for understanding modern representations such as [[Positional Encoding|positional encodings]].

# Types
| Time domain | Transform | Frequency domain |
| --- | --- | --- |
| Discrete, finite length $N$ | [[Discrete Fourier Transform]]: $\mathscr{L}[u] = \sum_{n=0}^{N-1} \ell[n] e^{-2\pi j \frac{un}{N}}$ | Discrete, finite length $N$ |
| Continuous, infinite length | Fourier transform (above) | Continuous, infinite length |
| Discrete, infinite length | [[Discrete-Time Fourier Transform]]: $\mathscr{L}(w) = \sum_{n=-\infty}^{\infty} \ell[n] e^{-jwn}$ | Continuous, finite length ($2\pi$) |
| Continuous, periodic | [[Fourier Series]][^2] | Discrete, infinite length |

All of them extend to 2D.

# Properties
- The continuous domain is convenient for operations not defined in the discrete domain (e.g. derivatives, which can only be approximated discretely, or the Gaussian, defined as a continuous function); images and filters are discrete in practice but often analyzed as continuous signals.
- Most properties of the DFT (linearity, separability, [[Parseval's Theorem]], [[Convolution Theorem]], [[Fourier Shift Theorem]], [[Fourier Modulation Theorem]]) carry over to the continuous domain by replacing sums with integrals; e.g. the continuous [[Convolution]] $\ell_1(t) \circ \ell_2(t) = \int_{-\infty}^{\infty} \ell_1(t - t') \ell_2(t') \, dt'$ transforms to $\mathscr{L}_1(w) \mathscr{L}_2(w)$.
- The [[Characteristic Function (Probability)|characteristic function]] of a random variable is the Fourier transform of its density (up to the sign of the exponent).[^2]
- The Fourier transform of the [[Dirac Delta Function]] is $1$.[^2]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
