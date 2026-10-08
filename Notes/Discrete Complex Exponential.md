---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Discrete Complex Exponential[^1]
> The 1D discrete complex exponential wave of frequency $u$ and period $N$ is
> $$
> \begin{align}
> e_u[n] = \exp\left(2\pi j \frac{un}{N}\right)
> \end{align}
> $$
> and in 2D, on an $N \times M$ grid with [[Spatial Frequency|spatial frequencies]] $u, v$,
> $$
> \begin{align}
> e_{u,v}[n, m] = \exp\left(2\pi j \left(\frac{un}{N} + \frac{vm}{M}\right)\right)
> \end{align}
> $$
> where $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]].

The notation $j$ for the imaginary unit (instead of $i$) is the electrical engineering and signal processing convention, where $i$ is reserved for electric current.

# Properties
- Related to the cosine and sine waves ([[Sinusoid (Signal Processing)]]) by [[Euler's Identity]]: $\exp(ja) = \cos(a) + j \sin(a)$.
- As $n$ goes from $0$ to $N - 1$, $e_u[n]$ rotates along the unit circle in the complex plane.
- **Separable**: $e_{u,v}[n, m] = e_u[n] \, e_v[m]$.
- **Orthogonality**: for images of size $N \times M$,
$$
\begin{align}
\langle e_{u,v}, e_{u',v'} \rangle = \sum_{n=0}^{N-1} \sum_{m=0}^{M-1} e_{u,v}[n, m] \, e^*_{u',v'}[n, m] = NM \, \delta[u - u'] \, \delta[v - v']
\end{align}
$$
  so the complex exponentials form an [[Orthogonal Basis|orthogonal basis]] for discrete signals and images of finite length (orthonormal after scaling by $1/\sqrt{NM}$). Hence any finite discrete image decomposes uniquely as a linear combination of complex exponentials: this is the [[Discrete Fourier Transform]].
- **Periodicity / conjugate symmetry**: $e_{N-u, M-v} = e_{-u,-v} = e^*_{u,v}$.
- **Eigenfunctions of LTI systems**: complex exponentials are the eigenfunctions of every [[Shift-Invariant System|space invariant linear operator]]; applying such an operator to a complex exponential yields a complex exponential of the same frequency, generally with a different amplitude and phase, $h \circ e_{u,v} = H[u, v] \, e_{u,v}$ ([[Transfer Function (Signal Processing)]], [[Convolution Theorem]]).

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
