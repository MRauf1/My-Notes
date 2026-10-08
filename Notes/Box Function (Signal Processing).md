---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Box Function (Signal Processing)[^1]
> The box function of half-width $L$ is
> $$
> \begin{align}
> \text{box}_L[n] =
> \begin{cases}
> 1 & \text{if } -L \le n \le L \\
> 0 & \text{otherwise}
> \end{cases}
> \end{align}
> $$
> It has duration $2L + 1$. Its [[Discrete Fourier Transform|DFT]] as a finite length signal of length $N$ (viewed with its periodic extension) is
> $$
> \begin{align}
> \text{box}_L[n] \xrightarrow{\mathcal{F}} \text{Box}_L[u] = \frac{\sin\left(\pi u (2L + 1)/N\right)}{\sin\left(\pi u / N\right)}
> \end{align}
> $$
> which is a [[Discrete Sinc Function|discrete sinc function]].
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

**Derivation**: using the periodicity of the summand to shift the summation range, $\text{Box}_L[u] = \sum_{n=-L}^{L} a^n$ with $a = \exp(-2\pi j u / N)$, and by the [[Geometric Series|geometric series]]
$$
\begin{align}
\sum_{n=-L}^{L} a^n = a^{-L} \frac{1 - a^{2L+1}}{1 - a} = \frac{a^{-(2L+1)/2} - a^{(2L+1)/2}}{a^{-1/2} - a^{1/2}} = \frac{\exp\left(\pi j \frac{u(2L+1)}{N}\right) - \exp\left(-\pi j \frac{u(2L+1)}{N}\right)}{\exp\left(\pi j \frac{u}{N}\right) - \exp\left(-\pi j \frac{u}{N}\right)}
\end{align}
$$
which reduces to the ratio of sines by [[Euler's Identity]].

# Properties
- $\text{Box}_L[u]$ is a real, symmetric function with its maximum $\text{Box}_L[0] = 2L + 1$ at $u = 0$.
- $\text{Box}_L[u]$ is periodic with period $N$; one period lies in $[-N/2, N/2 - 1]$.
- Its first zero is at $u = N / (2L + 1)$: the wider the box, the narrower the main lobe of its DFT.[^2]
- **2D box**: separable, $\text{box}_{L_n, L_m}[n, m] = \text{box}_{L_n}[n] \, \text{box}_{L_m}[m]$, so its DFT is $\text{Box}_{L_n, L_m}[u, v] = \text{Box}_{L_n}[u] \, \text{Box}_{L_m}[v]$.
- Normalized by $2L+1$, it is the averaging (box) filter, a simple [[Low-Pass Filter]] whose sidelobes let some high frequencies through ([[Box Filter Antialiasing]]).[^2]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
