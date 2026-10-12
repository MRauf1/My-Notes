---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Fourier Transform of Moving Image[^1]
> Let $\ell(x, y, t) = \ell_0(x - v_x t, y - v_y t)$ be a static image translating with constant velocity $(v_x, v_y)$ ([[Brightness Constancy Assumption]]). By the [[Fourier Shift Theorem|shift property]], its continuous spatio-temporal [[Fourier Transform]] is
> $$
> \begin{align}
> \mathscr{L}(w_x, w_y, w_t) = \mathscr{L}_0(w_x, w_y) \, \delta(w_t + v_x w_x + v_y w_y)
> \end{align}
> $$
> the product of the 2D FT of the static image and a **delta wall**: all energy lies on the plane $w_t + v_x w_x + v_y w_y = 0$ through the origin, with normal $(v_x, v_y, 1)$.

**Derivation**:[^2] transforming in space first, frame $t$ is $\ell_0$ shifted by $(v_x t, v_y t)$, so its 2D FT is $\mathscr{L}_0(w_x, w_y) e^{-j(v_x w_x + v_y w_y)t}$. The remaining FT over $t$ of this complex exponential is a [[Dirac Delta Function|delta]]:
$$
\begin{align}
\int_{-\infty}^{\infty} \mathscr{L}_0(w_x, w_y) e^{-j(w_t + v_x w_x + v_y w_y)t} \, dt = 2\pi \, \mathscr{L}_0(w_x, w_y) \, \delta(w_t + v_x w_x + v_y w_y)
\end{align}
$$
where the factor $2\pi$ depends on the FT normalization convention and is dropped above.

# Properties
- **Static image** ($v = 0$): the signal is constant in time, so the FT is $\mathscr{L}_0(w_x, w_y)\delta(w_t)$, confined to the plane $w_t = 0$. E.g. for a 1D [[Box Function (Signal Processing)|rectangular pulse]], a sinc ([[Discrete Sinc Function]]) along $w_x$ inside the wall $w_t = 0$.
- **Motion skews, not rotates**, the spectrum: each spatial frequency $(w_x, w_y)$ is moved to temporal frequency $w_t = -(v_x w_x + v_y w_y)$, so the zeros of $\mathscr{L}_0$ stay at the same $(w_x, w_y)$ locations. Faster motion gives a larger skew.
- The plane's orientation encodes the velocity, so motion can be detected by filters tuned to spatio-temporal orientation ([[Spatio-Temporal Filter]]).
- Fine spatial detail moving fast produces high temporal frequencies ($|w_t| = |v_x w_x|$ in 1D), which is relevant to temporal [[Aliasing]].[^2]

[^1]: [MIT Vision Book - Temporal Filters](https://visionbook.mit.edu/temporal_filters_v2.html)
[^2]: Added from general knowledge.
