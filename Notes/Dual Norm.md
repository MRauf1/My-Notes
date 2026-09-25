---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Dual Norm)[^1]
> Let $(V, \lVert \cdot \rVert)$ be a [[Normed Space]] and $V^*$ its (continuous) [[Dual Space]]. The dual norm of $f \in V^*$ is
> $$
> \begin{align}
> \lVert f \rVert_* := \sup_{x \in V, \, \lVert x \rVert \leq 1} |f(x)| = \sup_{x \neq 0} \frac{|f(x)|}{\lVert x \rVert}
> \end{align}
> $$

> [!info] Definition 2 (Dual Norm on $\mathbb{R}^n$)[^1]
> Let $\lVert \cdot \rVert$ be any norm on $\mathbb{R}^n$. Identifying each $y \in \mathbb{R}^n$ with the functional $x \mapsto \langle x, y \rangle$, the dual norm of $y$ is
> $$
> \begin{align}
> \lVert y \rVert_* := \sup_{\lVert x \rVert \leq 1} \langle x, y \rangle = \sup_{\lVert x \rVert \leq 1} |\langle x, y \rangle|
> \end{align}
> $$

The dual norm measures $y$ by how large it can make the inner product against vectors in the unit ball of the original norm. In other words, it is the [[Operator Norm]] of the linear functional $x \mapsto \langle x, y \rangle$, viewed as a map from $(V, \lVert \cdot \rVert)$ to $(\mathbb{R}, |\cdot|)$.

# Properties
- $\lVert \cdot \rVert_*$ is always a [[Normed Space|norm]] (on $\mathbb{R}^n$ it is even well-defined for any norm, since the unit ball is compact).
- [[Hölder's Inequality]]: $|\langle x, y \rangle| \leq \lVert x \rVert \, \lVert y \rVert_*$ for all $x, y$, directly from the definition; this bound is tight for every $y$.
- Dual of the [[p-Norm]]: $(\lVert \cdot \rVert_p)_* = \lVert \cdot \rVert_q$ with $\frac{1}{p} + \frac{1}{q} = 1$. In particular:
	- the [[Vector Norm|2-norm]] is self-dual (the only self-dual $p$-norm), which is why the [[Cauchy-Schwarz Inequality]] uses the same norm on both sides;
	- the [[1-Norm]] and [[Infinity Norm]] are dual to each other.
- Bidual: in finite dimensions (and more generally in reflexive spaces), $\lVert \cdot \rVert_{**} = \lVert \cdot \rVert$.
- Unit balls: the unit ball of $\lVert \cdot \rVert_*$ is the polar set of the unit ball of $\lVert \cdot \rVert$, $B_* = \{ y : \langle x, y \rangle \leq 1 \ \forall x \in B \}$.
- Order reversal: if $\lVert x \rVert_a \leq \lVert x \rVert_b$ for all $x$, then $\lVert y \rVert_{b*} \leq \lVert y \rVert_{a*}$ for all $y$.
- Matrices under the [[Frobenius Inner Product Space|Frobenius inner product]] $\langle A, B \rangle = \operatorname{tr}(A^\top B)$: the dual of the spectral/[[Operator Norm]] is the nuclear (trace) norm $\sum_i \sigma_i$, and the [[Frobenius Norm]] is self-dual. More generally, the dual of the Schatten $p$-norm is the Schatten $q$-norm.
- The dual norm is the [[Supremum|supremum]] of linear functions, so it is the support function of the unit ball and appears as the conjugate of $\lVert \cdot \rVert$ in convex analysis: $\lVert \cdot \rVert^*(y) = 0$ if $\lVert y \rVert_* \leq 1$, else $+\infty$.

[^1]: [Dual norm — Wikipedia](https://en.wikipedia.org/wiki/Dual_norm)
