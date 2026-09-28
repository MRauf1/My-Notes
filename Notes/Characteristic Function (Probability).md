---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Characteristic Function[^1]
> For a [[Random Variable]] $X$, $t \in \mathbb{R}$, and imaginary unit $i$, the characteristic function of $X$ is
> $$
> \begin{align}
> \varphi_X(t) = E\left(e^{itX}\right) = E[\cos(tX)] + i\,E[\sin(tX)]
> \end{align}
> $$

Since $|e^{itX}| = 1$, this expectation exists for every distribution, which removes the main limitation of the [[Moment Generating Function]]. For a continuous $X$ with pdf $f$, $\varphi_X(t) = \int e^{itx} f(x)\,dx$ is the Fourier transform of the density (up to the sign convention of the exponent).

# Properties
- Uniqueness: every distribution has a unique characteristic function, and each characteristic function corresponds to a unique distribution (inversion theorem).[^2]
- $\varphi_X(0) = 1$, $|\varphi_X(t)| \leq 1$, $\varphi_X(-t) = \overline{\varphi_X(t)}$, and $\varphi_X$ is uniformly continuous.
- If the mgf exists near $0$, then $\varphi_X(t) = M_X(it)$.
- If $E|X|^m < \infty$, then $\varphi_X^{(m)}(0) = i^m E(X^m)$.
- $\varphi_{aX+b}(t) = e^{ibt}\varphi_X(at)$; for [[Independent Random Variable|independent]] $X, Y$, $\varphi_{X+Y} = \varphi_X \varphi_Y$ (convolution of densities becomes multiplication).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=90)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=91)
