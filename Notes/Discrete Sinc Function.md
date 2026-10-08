---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Discrete Sinc Function[^1]
> For a constant $a$,
> $$
> \begin{align}
> \text{sincd}(x; a) = \frac{\sin(\pi x)}{a \sin(\pi x / a)}
> \end{align}
> $$

# Properties
- A symmetric, periodic function with maximum value $1$ (at $x = 0$). For integer $a$, the period is $a$ when $a$ is odd and $2a$ when $a$ is even.[^2]
- The DFT of the [[Box Function (Signal Processing)|box function]] is a scaled discrete sinc:
$$
\begin{align}
\text{Box}_L[u] = \frac{\sin\left(\pi u (2L + 1)/N\right)}{\sin\left(\pi u / N\right)} = (2L + 1) \, \text{sincd}\left(\frac{u(2L+1)}{N}; 2L + 1\right)
\end{align}
$$
- As $a \to \infty$, $a \sin(\pi x / a) \to \pi x$, so $\text{sincd}(x; a) \to \frac{\sin(\pi x)}{\pi x} = \text{sinc}(x)$, the continuous sinc function (the Fourier transform of a continuous box).[^2]
- Up to scaling and change of variable, it is the Dirichlet kernel $D_L(\theta) = \frac{\sin((L + 1/2)\theta)}{\sin(\theta/2)}$ from [[Fourier Series]] theory: $\text{Box}_L[u] = D_L(2\pi u / N)$.[^2]

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
