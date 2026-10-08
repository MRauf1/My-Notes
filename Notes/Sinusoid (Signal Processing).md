---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Sinusoid (Signal Processing)[^1]
> The **continuous time sine wave** is
> $$
> \begin{align}
> s(t) = A \sin(w t - \theta)
> \end{align}
> $$
> where $A$ is the **amplitude**, $w$ the **frequency** (in radians), and $\theta$ the **phase**; it is periodic with period $T = 2\pi / w$. The **discrete time sine wave** is
> $$
> \begin{align}
> s[n] = A \sin(w n - \theta)
> \end{align}
> $$
> Taking $\theta = 0$ gives the sine wave, and $\theta = -\pi/2$ gives the cosine wave ($\theta = \pi/2$ gives the cosine up to sign).

# Properties
- **Periodicity of the discrete wave**: a discrete signal $\ell[n]$ is periodic if there exists $T \in \mathbb{N}$ with $\ell[n] = \ell[n + mT]$ for all $m \in \mathbb{Z}$. Unlike the continuous wave, $s[n]$ is not periodic for arbitrary $w$: it is periodic iff $w = 2\pi K / N$ for $K, N \in \mathbb{N}$ (i.e. $w / 2\pi$ is rational). If $K/N$ is irreducible, the period is $T = N$ samples.
- To make the period $N$ explicit, write
$$
\begin{align}
s_k[n] = \sin\left(\frac{2\pi}{N} kn\right), \qquad c_k[n] = \cos\left(\frac{2\pi}{N} kn\right)
\end{align}
$$
  For periodic signals with period $N$ (or finite signals of length $N$, $n \in [0, N-1]$), $k \in [1, N/2]$ is the frequency: the number of wave cycles within the region of support.
- If $k = 0$, then $s[n] = 0$ and $c[n] = 1$ for all $n$.
- $c_{N-k} = c_k$ and $s_{N-k} = -s_k$, so frequencies $k > N/2$ give the same set of waves as $k \in [1, N/2]$ (related to [[Aliasing]]).
- **2D waves**: on an $N \times M$ grid,
$$
\begin{align}
s_{u,v}[n, m] = A \sin\left(2\pi\left(\frac{un}{N} + \frac{vm}{M}\right)\right), \qquad c_{u,v}[n, m] = A \cos\left(2\pi\left(\frac{un}{N} + \frac{vm}{M}\right)\right)
\end{align}
$$
  where $u, v$ are the two [[Spatial Frequency|spatial frequencies]], defining how fast the wave changes along $n$ and $m$.
- Related to the [[Discrete Complex Exponential]] by [[Euler's Identity]]: $c_k = \frac{1}{2}(e_k + e_{-k})$ and $s_k = \frac{1}{2j}(e_k - e_{-k})$, where $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]].
- The continuous counterparts are the [[Sine Function]] and [[Cosine Function]]; physically, a sinusoid in time is [[Simple Harmonic Motion]].

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
