---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Signal Energy[^1]
> The sum of squared magnitudes of a [[Signal (Signal Processing)|signal]]. For a discrete signal:
> $$
> \begin{align}
> E = \sum_{n=-\infty}^{\infty} \left| \ell[n] \right|^2
> \end{align}
> $$
> For a continuous signal (assuming the integral is finite):
> $$
> \begin{align}
> E = \int_{-\infty}^{\infty} \left| \ell(t) \right|^2 dt
> \end{align}
> $$

# Types
- **Finite energy** signals: e.g. all finite length signals.
- **Infinite energy** signals: e.g. periodic signals (measured over the whole time axis); most natural signals have infinite energy.

# Properties
- Equal to the squared $\ell^2$ [[Norm]] of the signal, $E = \|\ell\|_2^2$; finite energy signals are exactly the elements of $\ell^2(\mathbb{Z})$ (resp. $L^2(\mathbb{R})$).[^2]
- Can equivalently be computed from the squared magnitudes of the signal's Fourier transform ([[Parseval's Theorem]]).

[^1]: [MIT Vision Book - Linear Image Filtering](https://visionbook.mit.edu/linear_image_filtering.html)
[^2]: Added from general knowledge.
