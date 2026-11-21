---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!abstract] Theorem 1 ([[Moment Generating Function]] [[Random Variables Equal in Distribution]] Theorem)[^1]
> Let $X, Y$ be [[Random Variable]] with [[Moment Generating Function]] $M_X, M_Y$, respectively, existing in open intervals about 0. Then $F_X(z) = F_Y(z)$ for all $z \in \mathbb{R}$ if and only if $M_X(t) = M_Y(t)$ for all $t \in (-h, h)$ for some $h > 0$.

**Uniqueness is not existence.** The theorem says $F \mapsto M$ is one-to-one *on the distributions that have an mgf*. It does not say every distribution has one. The integrand $e^{tx}$ is unbounded in one tail for each $t \neq 0$, so an mgf exists only when $E\,e^{h|X|} < \infty$ for some $h > 0$, i.e. when the tails decay at least exponentially. The [[Cauchy Distribution]] and the lognormal fall outside this domain. For uniqueness on every distribution, use the [[Characteristic Function (Probability)|characteristic function]], whose integrand $e^{itx}$ is bounded. Where both exist, $\varphi(t) = M(it)$.

The proof (beyond Hogg) goes through that relation: an mgf on $(-h, h)$ extends analytically to the strip $|\operatorname{Re} z| < h$. So $M$ on a real interval determines it on the imaginary axis, i.e. determines $\varphi$, and $\varphi$ determines $F$ by Fourier inversion.

# Properties
- Since the moments determine $M$ through its Taylor series, a distribution with an mgf is determined by its moments ([[Moment Problem]]).
- Used to identify distributions: if $M_X$ matches a known mgf near $0$, then $X$ has that distribution.

# Questions
> [!question]- If an mgf uniquely determines a distribution, why do some distributions (e.g. Cauchy) have no mgf?
> Uniqueness is injectivity on the domain of the map $F \mapsto M$, and that domain contains only light-tailed distributions: $E\,e^{tX}$ must be finite on an open interval about $0$, which fails whenever a tail decays slower than exponentially, because $e^{tx}$ is unbounded. The Cauchy has $E\,e^{tX} = \infty$ for all $t \neq 0$. The characteristic function $E\,e^{itX}$ has a bounded integrand, so it is defined, and injective, on every distribution.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=87)