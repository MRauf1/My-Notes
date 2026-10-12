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

**On $(-l, l)$ (PDE convention).**[^3][^4] The full Fourier series of $\phi$ on $-l < x < l$ is
$$
\begin{align}
\phi(x) = \tfrac12 A_0 + \sum_{n=1}^{\infty} \left(A_n \cos\frac{n\pi x}{l} + B_n \sin\frac{n\pi x}{l}\right), \qquad A_n = \frac1l \int_{-l}^{l} \phi(x) \cos\frac{n\pi x}{l}\, dx, \quad B_n = \frac1l \int_{-l}^{l} \phi(x) \sin\frac{n\pi x}{l}\, dx,
\end{align}
$$
for $n = 0, 1, 2, \dots$ and $n = 1, 2, \dots$ respectively. The interval is twice as long as for the sine and cosine series, so the normalization is $1/l$ rather than $2/l$. The eigenfunctions $\{1, \cos(n\pi x/l), \sin(n\pi x/l)\}$ of the [[Periodic Boundary Condition|periodic problem]] are pairwise orthogonal on $(-l, l)$. In complex form,[^5][^6]
$$
\begin{align}
\phi(x) = \sum_{n=-\infty}^{\infty} c_n e^{in\pi x/l}, \qquad c_n = \frac{1}{2l} \int_{-l}^{l} \phi(x)\, e^{-in\pi x/l}\, dx,
\end{align}
$$
a sum of two series, over $n \geq 0$ and over $n \leq -1$.

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
- Each term has period $2l$, so the sum (if it converges) does too: the full series expands either a function on $(-l, l)$ or its $2l$-periodic [[Periodic Extension]] on $\mathbb{R}$.[^7]
- Almost any function on $(-l, l)$ is the sum of its full Fourier series; each of the three classical series converges inside its interval, but not necessarily at the endpoints.[^8] Precise statements: [[Fourier Series Uniform Convergence Theorem]], [[Fourier Series L2 Convergence Theorem]], [[Fourier Series Pointwise Convergence Theorem]].
- The partial sums are convolutions with the [[Dirichlet Kernel]]; at jumps they overshoot by about $9\%$ ([[Gibbs Phenomenon]]).
- Term-by-term differentiation of a Fourier series is not always valid.[^9]
- Special case of the [[Eigenfunction Expansion]] for a [[Symmetric Boundary Condition]]; the orthogonality behind the coefficient formulas is the [[Symmetric Boundary Condition Orthogonality Theorem]].

[^1]: [MIT Vision Book - Fourier Analysis](https://visionbook.mit.edu/image_processing_fourier.html)
[^2]: Added from general knowledge.
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=119&annotation=6N9BMZWS)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=119&annotation=ZG356KUT)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=128&annotation=EYG4QPQA)
[^6]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=128&annotation=RGNH9294)
[^7]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=125&annotation=FBU7VNRG); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=126&annotation=PVFXJPIN)
[^8]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=125&annotation=2A6XSSFJ)
[^9]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=156&annotation=PJ6CUDY7)
