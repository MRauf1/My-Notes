---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Hölder's Inequality — Conjugate Exponents)[^1]
> Let $p, q \in [1, \infty]$ be conjugate exponents, i.e.
> $$
> \frac{1}{p} + \frac{1}{q} = 1
> $$
> (with the convention $\frac{1}{\infty} = 0$, so $p = 1 \Leftrightarrow q = \infty$). Then for any $x, y \in \mathbb{F}^n$,
> $$
> \begin{align}
> \left| \sum_{i=1}^n x_i y_i \right| \leq \sum_{i=1}^n |x_i y_i| \leq \lVert x \rVert_p \lVert y \rVert_q
> \end{align}
> $$
> where $\lVert \cdot \rVert_p$ is the [[p-Norm]]. More generally, on any measure space, for $f \in L^p$ and $g \in L^q$,
> $$
> \begin{align}
> \lVert fg \rVert_1 = \int |fg| \, d\mu \leq \lVert f \rVert_p \lVert g \rVert_q
> \end{align}
> $$

> [!info] Definition 2 (Hölder's Inequality — Dual Norms)[^2]
> Let $\lVert \cdot \rVert$ be an arbitrary norm on $\mathbb{R}^n$ and $\lVert \cdot \rVert_*$ its [[Dual Norm]]. Then for any $x, y \in \mathbb{R}^n$,
> $$
> \begin{align}
> |\langle x, y \rangle| \leq \lVert x \rVert \, \lVert y \rVert_*
> \end{align}
> $$
> More generally, for a [[Normed Space]] $V$ with dual space $V^*$, $|f(x)| \leq \lVert f \rVert_* \lVert x \rVert$ for all $x \in V$, $f \in V^*$.

Definition 2 follows immediately from the definition of the [[Dual Norm]] (apply the supremum to $x / \lVert x \rVert$). Definition 1 is the special case $\lVert \cdot \rVert = \lVert \cdot \rVert_p$, since the dual norm of the $p$-norm is the $q$-norm. Definition 2 is sometimes called the *generalized [[Cauchy-Schwarz Inequality]]*: it is the replacement for Cauchy-Schwarz when the norm does not come from an [[Inner Product]] — the price is that the two vectors are measured in *different* norms.

# Properties
- $p = q = 2$ recovers the [[Cauchy-Schwarz Inequality]] for the standard [[Dot Product]]; the $2$-norm is self-dual.
- $p = 1$, $q = \infty$: $\left| \sum_i x_i y_i \right| \leq \lVert x \rVert_1 \lVert y \rVert_\infty$ ([[1-Norm]] and [[Infinity Norm]] are dual to each other).
- Tightness: for every $y$ there is an $x \neq 0$ attaining equality, which is exactly why $\lVert y \rVert_q = \sup_{\lVert x \rVert_p \leq 1} \langle x, y \rangle$, i.e. the $q$-norm is the [[Dual Norm]] of the $p$-norm.
- Equality condition ($1 < p < \infty$): equality holds iff $|x_i|^p$ and $|y_i|^q$ are proportional (as vectors in $\mathbb{R}^n$) and the terms $x_i y_i$ all have the same phase/sign.
- Standard proof: normalize to $\lVert x \rVert_p = \lVert y \rVert_q = 1$ and apply Young's inequality $ab \leq \frac{a^p}{p} + \frac{b^q}{q}$ for $a, b \geq 0$ termwise, then sum.
- Generalized Hölder: if $\frac{1}{r} = \frac{1}{p} + \frac{1}{q}$ with $p, q, r \in (0, \infty]$, then $\lVert fg \rVert_r \leq \lVert f \rVert_p \lVert g \rVert_q$; by induction, $\lVert f_1 \cdots f_k \rVert_r \leq \prod_j \lVert f_j \rVert_{p_j}$ when $\sum_j \frac{1}{p_j} = \frac{1}{r}$.
- Hölder's inequality is the key step in proving Minkowski's inequality $\lVert x + y \rVert_p \leq \lVert x \rVert_p + \lVert y \rVert_p$, i.e. the [[Triangle Inequality]] for the [[p-Norm]].
- On a finite measure space, Hölder gives the $L^p$ inclusion $\lVert f \rVert_p \leq \mu(\Omega)^{1/p - 1/r} \lVert f \rVert_r$ for $p \leq r$ (take $g = 1$); in $\mathbb{R}^n$ this yields $\lVert x \rVert_1 \leq \sqrt{n} \lVert x \rVert_2$ from [[Norm Equivalence Inequalities (Finite-Dimensional)]].

[^1]: [Hölder's inequality — Wikipedia](https://en.wikipedia.org/wiki/H%C3%B6lder%27s_inequality)
[^2]: [Dual norm — Wikipedia](https://en.wikipedia.org/wiki/Dual_norm)
