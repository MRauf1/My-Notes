---
tags:
  - mathematics
  - real_analysis
  - cryoEM
---

# Definition
> [!info] Sinc Function[^1]
> The **normalized** sinc function (signal processing) is
> $$
> \begin{align}
> \operatorname{sinc}(u) = \frac{\sin \pi u}{\pi u}, \qquad \operatorname{sinc}(0) = 1.
> \end{align}
> $$
> It is the [[Fourier Transform]] of the unit-area rectangular pulse $\operatorname{rect}(x) = 1$ for $|x| < 1/2$ and $0$ otherwise:
> $$
> \begin{align}
> \operatorname{rect}(x) \ \xrightarrow{\ \mathcal{F}\ }\ \operatorname{sinc}(u), \qquad \operatorname{sinc}(x) \ \xrightarrow{\ \mathcal{F}\ }\ \operatorname{rect}(u).
> \end{align}
> $$

# Properties
- **Conventions differ.** Mathematicians often define the unnormalized $\operatorname{sinc}(x) = \sin x / x$; check which one a source uses.
- Its zeros are at the nonzero integers, and $\int \operatorname{sinc} = \operatorname{rect}(0) = 1$.
- The continuous counterpart of the [[Discrete Sinc Function]] and the [[Box Function (Signal Processing)|box function]] pair.
- An ideal low-pass filter (a rect in frequency) is convolution with a sinc in space, whose slowly decaying ripples cause ringing.

# Questions
> [!question]- Compute the Fourier transform of $\operatorname{rect}$.
> $$
> \begin{align}
> \int_{-1/2}^{1/2} e^{-2\pi iux}\,dx = \frac{e^{-\pi iu} - e^{\pi iu}}{-2\pi iu} = \frac{\sin\pi u}{\pi u} = \operatorname{sinc}(u),
> \end{align}
> $$
> using $e^{i\theta} - e^{-i\theta} = 2i\sin\theta$. The reverse pair follows because rect is even, so the forward and inverse transforms coincide for it.

[^1]: [Sigworth, Fourier transform notes, p. 3](zotero://open-pdf/library/items/FEUF2XYA?page=3&annotation=WKEGKKR9)
