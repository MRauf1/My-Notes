---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Moment Problem
> Given a sequence $(m_n)_{n \geq 0}$ with $m_0 = 1$, the moment problem asks whether there is a [[Probability Distribution|distribution]] $P$ with [[Moment (Statistics)|moments]] $\int x^n\,dP(x) = m_n$ for all $n$ (existence) and whether it is unique (determinacy). A distribution is *moment-determinate* if no other distribution has the same moment sequence, and *moment-indeterminate* otherwise.
> The problem on $\mathbb{R}$ is the Hamburger moment problem, on $[0, \infty)$ the Stieltjes problem, and on a bounded interval the Hausdorff problem.

> [!abstract] Theorem 1 (Sufficient Conditions for Determinacy)[^1]
> A distribution $P$ on $\mathbb{R}$ is moment-determinate if either
> 1. its [[Moment Generating Function]] exists on some interval $(-h, h)$, $h > 0$; or
> 2. (Carleman's condition) $\displaystyle\sum_{n \geq 1} m_{2n}^{-1/(2n)} = \infty$.
>
> In particular, every distribution with bounded support is determinate.

> [!abstract] Theorem 2 (Indeterminacy of the Lognormal)[^2]
> If $f$ is the lognormal density, $f(x) = \frac{1}{x\sqrt{2\pi}}e^{-(\log x)^2/2}$ for $x > 0$, then for every $a \in [-1, 1]$
> $$
> \begin{align}
> f_a(x) = f(x)\bigl[1 + a\sin(2\pi \log x)\bigr]
> \end{align}
> $$
> is a density with the same moments $E X^n = e^{n^2/2}$ as $f$. The lognormal is therefore not determined by its moments.

**Why the mgf condition suffices.** If $M$ exists on $(-h, h)$, it is analytic there with [[Taylor Series]] $M(t) = \sum_n m_n t^n / n!$. So the moments determine $M$ near $0$, and $M$ determines the distribution ([[Moment Generating Function Equal Distribution Theorem]]). The lognormal has every moment finite but $E e^{tX} = \infty$ for every $t > 0$: its moments grow like $e^{n^2/2}$, too fast for their Taylor series to converge. Without the analytic packaging, the moments are coordinates that no longer pin down the distribution.

Moments are the values of the distribution, viewed as the linear functional $g \mapsto E\,g(X)$, on the monomials $1, x, x^2, \dots$. The [[Characteristic Function (Probability)|characteristic function]] gives its values on the Fourier modes $e^{itx}$. The Fourier modes always determine the distribution, while the monomials do so only when the tails are light enough.

# Properties
- The proof of Theorem 2 reduces, by the substitution $x = e^{n + s}$, to $\int_{-\infty}^{\infty} e^{-s^2/2}\sin(2\pi s)\,ds = 0$, which holds because the integrand is odd.
- Existence on $\mathbb{R}$ (Hamburger): $(m_n)$ is a moment sequence if and only if every Hankel matrix $(m_{i+j})_{i,j=0}^{N}$ is positive semidefinite, which is the condition that $E[p(X)^2] \geq 0$ for every polynomial $p$.
- Moment matching is used in practice, for example in the [[Central Limit Theorem]] by the method of moments, which is valid because the limit [[Normal Distribution]] is determinate (its mgf exists everywhere).

# Questions
> [!question]- The lognormal has every moment finite. Why is that not enough for its moments to determine it, when an mgf would be?
> Finite moments only give the coefficients $m_n/n!$ of a formal power series. Determinacy via the mgf needs that series to converge near $0$, which requires the tails to decay exponentially. For the lognormal $m_n = e^{n^2/2}$, so $\sum m_n t^n/n!$ diverges for every $t \neq 0$, and $E e^{tX} = \infty$ for $t > 0$. The perturbation $1 + a\sin(2\pi\log x)$ is orthogonal to every monomial under $f$, so it changes the distribution without changing any moment.

[^1]: Akhiezer, *The Classical Moment Problem and Some Related Questions in Analysis*, Oliver & Boyd (1965) (unverified page)
[^2]: [Heyde, On a Property of the Lognormal Distribution, JRSS B 25(2):392–393 (1963)](https://doi.org/10.1111/j.2517-6161.1963.tb00521.x)
