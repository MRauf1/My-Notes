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

**Ways to represent a distribution.** Each of the following maps a distribution to a function or sequence. They differ in which distributions they are defined for, and in whether they are one-to-one there:

| Representation | Defined for | Determines the distribution |
| --- | --- | --- |
| [[Cumulative Distribution Function\|cdf]] $F$ | every distribution | yes |
| characteristic function $\varphi$ | every distribution | yes (inversion) |
| [[Moment Generating Function\|mgf]] $M$ | light tails only ($E\,e^{h\|X\|} < \infty$) | yes, among those |
| pmf / pdf | discrete / absolutely continuous only | yes (a pdf up to a.e.) |
| moments $(E X^n)$ | all moments finite | not always ([[Moment Problem]]) |

The cdf is the most literal representation: it *is* the distribution, as a [[Lebesgue-Stieltjes Measure]]. The characteristic function is the universal transform: always defined, always determining, and multiplicative over independent sums. Both are bijections onto known classes. Every nondecreasing right-continuous $F$ with limits $0$ and $1$ is a cdf. A function is a characteristic function if and only if it is continuous, positive-definite, and satisfies $\varphi(0) = 1$ (Bochner's theorem).

**Relation to the [[Characteristic Polynomial]] of a matrix.** In both names, "characteristic" means "determining", but the two uniqueness statements are not parallel:
- $\varphi_X$ determines the distribution of $X$ completely.
- $p_A$ does **not** determine $A$. Similar matrices share it ([[Similar Matrix Characteristic Polynomial]]), and so can non-similar ones: $\begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $0$ both have $p(x)=x^2$.

What $p_A$ determines is the eigenvalues with [[Algebraic Multiplicity of Eigenvalue|algebraic multiplicity]], i.e. the *spectral distribution* $\mu_A=\frac1n\sum_{i=1}^n\delta_{\lambda_i}$. That distribution is where the two concepts meet precisely. For a real symmetric $A$ with eigenvalues $\lambda_1,\dots,\lambda_n$,
$$
\begin{align}
\varphi_{\mu_A}(t)=\frac1n\sum_{i=1}^n e^{it\lambda_i}=\frac1n\operatorname{tr}e^{itA},\qquad \frac1n\,\frac{p_A'(z)}{p_A(z)}=\frac1n\sum_{i=1}^n\frac{1}{z-\lambda_i}=\int\frac{d\mu_A(\lambda)}{z-\lambda}.
\end{align}
$$
So $p_A$, $\mu_A$, and $\varphi_{\mu_A}$ carry the same information: $\mu_A$ gives $p_A=\prod_i(\lambda_i-x)$, and $\varphi_{\mu_A}$ gives $\mu_A$ by uniqueness. The log-derivative of $p_A$ is the Stieltjes transform of $\mu_A$, the transform used in random matrix theory. Here is the exact dictionary:

| Matrix side | Distribution side |
| --- | --- |
| symmetric matrix $A$ | random variable $X$ |
| characteristic polynomial $p_A$ | the distribution $\mu_A$ of a uniformly chosen eigenvalue |

The analogy breaks at the level of what is determined. The distribution is all there is to a law, but a matrix also has eigenvectors. By the [[Spectral Theorem]], $p_A$ determines a symmetric $A$ only up to orthogonal similarity $Q^\top AQ$. With $-\Delta$ in place of $A$, $\frac1n\operatorname{tr}e^{-tA}=M_{\mu_A}(-t)$ is the heat trace. The same loss appears there as isospectral drums: the spectrum does not determine the shape (Gordon–Webb–Wolpert 1992). The vault has no notes on the heat trace or isospectrality yet.

# Properties
- Uniqueness: every distribution has a unique characteristic function, and each characteristic function corresponds to a unique distribution (inversion theorem).[^2]
- $\varphi_X(0) = 1$, $|\varphi_X(t)| \leq 1$, $\varphi_X(-t) = \overline{\varphi_X(t)}$, and $\varphi_X$ is uniformly continuous.
- If the mgf exists near $0$, then $\varphi_X(t) = M_X(it)$.
- If $E|X|^m < \infty$, then $\varphi_X^{(m)}(0) = i^m E(X^m)$.
- $\varphi_{aX+b}(t) = e^{ibt}\varphi_X(at)$; for [[Independent Random Variable|independent]] $X, Y$, $\varphi_{X+Y} = \varphi_X \varphi_Y$ (convolution of densities becomes multiplication).
- Fourier inversion recovers the density, $f(x) = \frac{1}{2\pi}\int e^{-itx}\varphi(t)\,dt$, which allows numerical [[Inverse Transform Sampling|inversion]] when only $\varphi$ is known.[^3]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=90)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=91)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=13&annotation=36FFAK6R)
