---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Fourier Series[^1]
> The representation of a periodic function as an infinite linear combination of harmonically related sinusoids. For a (sufficiently regular) function $\ell(t)$ with period $2\pi$:[^2]
> $$
> \begin{align}
> \ell(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos(nt) + b_n \sin(nt) \right)
> \end{align}
> $$
> with coefficients
> $$
> \begin{align}
> a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} \ell(t) \cos(nt) \, dt, \qquad b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} \ell(t) \sin(nt) \, dt
> \end{align}
> $$
> Equivalently, in complex form, $\ell(t) = \sum_{n=-\infty}^{\infty} c_n e^{jnt}$ with $c_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} \ell(t) e^{-jnt} \, dt$.
> Here $j = \sqrt{-1}$ is the [[Imaginary Unit|imaginary unit]] (the signal processing notation for $i$).

The Fourier series is a **change of representation**: instead of describing the function by its values $\ell(t)$, it is described by the infinite sequence of coefficients $a_n$ (and $b_n$), which give an alternative description of the same function.

# Types
- [[Fourier Sine Series]]: expansion of a function on $(0, \pi)$ in sines only.
- [[Fourier Cosine Series]]: expansion of a function on $(0, \pi)$ in cosines only.
- In signal and image processing, discrete versions using discrete [[Sinusoid (Signal Processing)|sinusoids]] and [[Discrete Complex Exponential|complex exponentials]], leading to the [[Discrete Fourier Transform]].

# Properties
- Introduced by Joseph Fourier (1822, *Théorie analytique de la chaleur*) in his study of heat propagation ([[Heat Equation]]); one of the most important mathematical tools in science and engineering.
- Adding higher frequency terms adds finer detail to the partial sums, making them closer to the function.
- Coefficients are computed by projecting $\ell$ onto each sinusoid, which works because the sinusoids $\{1, \cos(nt), \sin(nt)\}$ are mutually orthogonal on an interval of length $2\pi$ ([[Orthogonal Basis]]).[^2]
- Convergence (general knowledge): for piecewise smooth $\ell$, the series converges pointwise to $\ell(t)$ at continuity points and to the average of the one-sided limits at jumps; for $\ell \in L^2$ it converges in the $L^2$ norm.[^2]
- The result of the series is always $2\pi$-periodic, so a function defined only on an interval is implicitly replaced by a periodic extension ([[Periodic Function]]).
- The Fourier series representation is important for studying [[Linear System (Signal Processing)|linear systems]] and [[Convolution|convolutions]].
- One of the variants of the [[Fourier Transform]]: it maps a continuous periodic signal to a discrete, infinite sequence of coefficients.

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
