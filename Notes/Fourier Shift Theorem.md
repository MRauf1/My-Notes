---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Fourier Shift Theorem[^1]
> Translating an image $\ell[n, m]$ (with period $N, M$) by $(n_0, m_0)$ pixels multiplies its [[Discrete Fourier Transform|DFT]] by a complex exponential:
> $$
> \begin{align}
> \ell[n - n_0, m - m_0] \xrightarrow{\mathcal{F}} \mathscr{L}[u, v] \exp\left(-2\pi j \left(\frac{un_0}{N} + \frac{vm_0}{M}\right)\right)
> \end{align}
> $$
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

**Proof**: substitute $n \to n + n_0$, $m \to m + m_0$ in the DFT sum; since $\ell$ and the complex exponentials have period $N, M$, the sum can be taken over any range of $N \times M$ samples:
$$
\begin{align}
\mathcal{F}\{\ell[n - n_0, m - m_0]\} = \sum_{n,m} \ell[n, m] \exp\left(-2\pi j \left(\frac{u(n + n_0)}{N} + \frac{v(m + m_0)}{M}\right)\right) = \mathscr{L}[u, v] \exp\left(-2\pi j \left(\frac{un_0}{N} + \frac{vm_0}{M}\right)\right)
\end{align}
$$

# Properties
- A shift in space is a modulation in the frequency domain; dually, a shift in frequency is a modulation in space ([[Fourier Modulation Theorem]]).
- Exact only for a **circular shift** (pixels leaving one boundary reappear on the other side), a consequence of the periodicity assumed by the DFT. When the translation is due to camera motion, the shift is not circular (new pixels appear at the boundary), so the property holds only approximately.
- A translation leaves the magnitude $|\mathscr{L}[u, v]|$ unchanged and adds a phase linear in frequency, $-2\pi(un_0/N + vm_0/M)$; this is why the [[Fourier Amplitude and Phase|amplitude]] is largely invariant to location.[^2]
- In 1D: $\ell[n - n_0] \xrightarrow{\mathcal{F}} \mathscr{L}[u] \exp\left(-2\pi j \frac{un_0}{N}\right)$.

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
