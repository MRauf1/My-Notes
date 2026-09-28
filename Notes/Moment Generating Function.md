---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Moment Generating [[Function]])[^1]
> Let $X$ be a [[Random Variable]] such that for some $h > 0$, the [[Expectation]] of $e^{tX}$ exists for $-h < t < h$. The moment generating function (mgf) of $X$ is
> $$
> \begin{align}
> M_X(t) = E\left(e^{tX}\right), \quad -h < t < h
> \end{align}
> $$
> All that is needed is existence on some open neighborhood of $0$; existence at $t = 0$ alone is not enough.

**Intuition.** Expanding the exponential,
$$
\begin{align}
M_X(t) = E\left[\sum_{m=0}^\infty \frac{t^m X^m}{m!}\right] = \sum_{m=0}^\infty \frac{E(X^m)}{m!} t^m
\end{align}
$$
so the mgf is a single function whose [[Maclaurin Series]] coefficients are the [[Moment (Statistics)|moments]] of $X$: it packages the infinite sequence $E(X), E(X^2), \dots$ into one function, and differentiating at $0$ reads them back out. It is a transform of the distribution, the (two-sided) Laplace transform of the density evaluated at $-t$, in the same way the [[Characteristic Function (Probability)|characteristic function]] is its Fourier transform. The parameter $t$ exponentially tilts the distribution: large positive $t$ weights the right tail, large negative $t$ the left, so $M_X$ existing near $0$ means the tails decay at least exponentially.

It is useful because
1. moments come from differentiation instead of repeated integration or summation;
2. it determines the distribution uniquely ([[Moment Generating Function Equal Distribution Theorem]]), so recognizing an mgf identifies a distribution;
3. it turns sums of [[Independent Random Variable|independent]] variables into products, $M_{X+Y}(t) = M_X(t) M_Y(t)$, avoiding convolutions; this is the standard route to the distribution of sums and to proofs of the central limit theorem;
4. it gives exponential tail bounds (Chernoff bounds) via [[Markov's Inequality]] applied to $e^{tX}$.

# Properties
- $M(0) = 1$.
- $M'(0) = E(X) = \mu$, and in general $M^{(m)}(0) = E(X^m)$ for positive integers $m$.
- $\text{Var}(X) = M''(0) - [M'(0)]^2$.
- $M_{aX+b}(t) = e^{bt} M_X(at)$.
- The subscript $M_X$ is used to indicate which random variable the mgf belongs to.
- Not all [[Probability Distribution|distributions]] have an mgf (e.g. the [[Cauchy Distribution]], or any distribution missing some moment); the [[Characteristic Function (Probability)|characteristic function]] $\varphi(t) = E(e^{itX})$ always exists and plays the same role.
- [[Moment Generating Function Equal Distribution Theorem]]
- [[mth Moment Existence Theorem]]
- Multivariate version: [[Moment Generating Function of Random Vector]] $E[e^{\mathbf{t}^T \mathbf{X}}]$.
- Related generating functions: [[Cumulant Generating Function]] $\psi(t) = \log M(t)$, [[Factorial Moment Generating Function]] $K(t) = M(\log t)$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=86)
