---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Discrete Fourier Transform (DFT)[^1]
> The DFT transforms an image $\ell[n, m]$ of finite size $N \times M$ into the complex image $\mathscr{L}[u, v]$:
> $$
> \begin{align}
> \mathscr{L}[u, v] = \mathcal{F}\{\ell[n, m]\} = \sum_{n=0}^{N-1} \sum_{m=0}^{M-1} \ell[n, m] \exp\left(-2\pi j \left(\frac{un}{N} + \frac{vm}{M}\right)\right)
> \end{align}
> $$
> with **inverse DFT**
> $$
> \begin{align}
> \ell[n, m] = \mathcal{F}^{-1}\{\mathscr{L}[u, v]\} = \frac{1}{NM} \sum_{u=0}^{N-1} \sum_{v=0}^{M-1} \mathscr{L}[u, v] \exp\left(+2\pi j \left(\frac{un}{N} + \frac{vm}{M}\right)\right)
> \end{align}
> $$
> written $\ell[n, m] \xrightarrow{\mathcal{F}} \mathscr{L}[u, v]$, where $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$). In 1D: $\mathscr{L}[u] = \sum_{n=0}^{N-1} \ell[n] e^{-2\pi j \frac{un}{N}}$ and $\ell[n] = \frac{1}{N} \sum_{u=0}^{N-1} \mathscr{L}[u] e^{2\pi j \frac{un}{N}}$.

The inverse is derived by applying $\frac{1}{NM}\sum_u \sum_v$ to the forward transform and using the orthogonality of the [[Discrete Complex Exponential|complex exponentials]]. It rewrites the image, instead of as a sum of offset pixel values, as a sum of complex exponentials, each at a different [[Spatial Frequency|spatial frequency]], weighted by $\mathscr{L}[u, v]$.

More generally, the DFT is an invertible linear image transform $\mathbf{x} = \mathbf{H} \boldsymbol{\ell}_{\text{in}}$, $\boldsymbol{\ell}_{\text{in}} = \mathbf{H}^{-1} \mathbf{x}$ ([[DFT Matrix]]): a change of representation that reveals image properties not immediately available in the original pixels.

# Properties
- **Uniqueness**: the decomposition of a signal into a sum of complex exponentials is unique.
- **Periodicity**: since $\mathscr{L}$ is a sum of complex exponentials with common period $N, M$, $\mathscr{L}[u + aN, v + bM] = \mathscr{L}[u, v]$ for all $a, b \in \mathbb{Z}$; likewise the inverse DFT is a periodic image, $\ell[n + aN, m + bM] = \ell[n, m]$. The DFT implicitly treats a finite image as one period of a periodic signal.
- **Centered form**: since $e_{N-u, M-v} = e_{-u,-v}$, the sums can run over a centered frequency interval of length $N$ and $M$ (e.g. $u \in [-N/2, N/2 - 1]$), placing the zero frequency (DC) coefficient at the center:
$$
\begin{align}
\ell[n, m] = \frac{1}{NM} \sum_{u=-N/2}^{N/2-1} \sum_{v=-M/2}^{M/2-1} \mathscr{L}[u, v] \exp\left(2\pi j \left(\frac{un}{N} + \frac{vm}{M}\right)\right)
\end{align}
$$
  Frequencies near the origin represent slow, large variations; frequencies further away represent faster variation across space.
- **Conjugate symmetry**: for a real image, $\mathscr{L}[-u, -v] = \mathscr{L}^*[u, v]$.[^2] A conjugate pair with equal coefficients sums to a cosine wave; with opposite coefficients, to a sine wave.
- $\mathscr{L}[0, 0] = NM \mu$, where $\mu$ is the [[DC Value]] of the image.
- **Linearity**: $\alpha \ell_1 + \beta \ell_2 \xrightarrow{\mathcal{F}} \alpha \mathscr{L}_1 + \beta \mathscr{L}_2$ for $\alpha, \beta \in \mathbb{C}$; the same holds for the inverse.
- **Separability**: if $\ell[n, m] = \ell_1[n] \ell_2[m]$, then $\mathscr{L}[u, v] = \mathscr{L}_1[u] \mathscr{L}_2[v]$.
- [[Parseval's Theorem]]: inner products and energy are preserved up to the factor $\frac{1}{NM}$.
- [[Convolution Theorem]]: [[Circular Convolution|circular convolution]] becomes a product, and a product becomes a circular convolution.
- [[Fourier Shift Theorem]] and [[Fourier Modulation Theorem]]: a shift in one domain is a modulation in the other.
- Polar decomposition into [[Fourier Amplitude and Phase|amplitude and phase]].
- **Common transform pairs** (1D, length $N$; in 2D the factor $N$ becomes $NM$):

| $\ell[n]$ | $\mathscr{L}[u]$ |
| --- | --- |
| $\delta[n]$ | $1$ |
| $\exp\left(2\pi j \frac{u_0 n}{N}\right)$ | $N \delta[u - u_0]$ |
| $\cos\left(2\pi \frac{u_0 n}{N}\right)$ | $\frac{N}{2}\left(\delta[u - u_0] + \delta[u + u_0]\right)$ |
| $\sin\left(2\pi \frac{u_0 n}{N}\right)$ | $\frac{N}{2j}\left(\delta[u - u_0] - \delta[u + u_0]\right)$ |
| $\text{box}_L[n]$ | $\frac{\sin(\pi u (2L+1)/N)}{\sin(\pi u / N)}$ ([[Box Function (Signal Processing)]]) |

  The source omits the factor $N$ (resp. $NM$) for the exponential, cosine, and sine pairs; it follows from the orthogonality of the complex exponentials.[^2] The delta pair means that summing all complex exponentials with coefficient $1$ cancels everywhere but the origin: $\delta[n, m] = \frac{1}{NM} \sum_{u} \sum_{v} \exp\left(2\pi j \left(\frac{un}{N} + \frac{vm}{M}\right)\right)$.
- Computed efficiently by the [[Fast Fourier Transform]] in $O(N \log N)$.
- The discrete, finite length member of the [[Fourier Transform]] family; for infinite discrete signals see the [[Discrete-Time Fourier Transform]]. The DFT of a finite signal equals its DTFT sampled at $w = 2\pi u / N$.[^2]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge / corrected from the source.
