---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Harmonic Function Smoothness[^1]
> Let $u$ be a [[Harmonic Function]] in any open set $D$ of the plane. Then $u(x, y)$ possesses all partial derivatives of all orders in $D$.

**Proof idea.**[^2] Around any point of $D$, take a disk whose closure lies in $D$; inside it $u$ equals [[Poisson's Formula]] applied to its own boundary values. The [[Poisson Kernel]] is infinitely differentiable for $r < a$, so differentiating under the integral sign shows $u \in C^\infty$.

# Generalizations
> [!abstract] Generalization 1 (Elliptic Regularity)[^3]
> Let $Lu = -\sum_{i,j}(a^{ij}u_{x_i})_{x_j} + \sum_i b^i u_{x_i} + cu$ be uniformly elliptic on an open set $U$, and let $u \in H^1(U)$ be a weak solution of $Lu = f$.
> 1. If $a^{ij} \in C^{m+1}(U)$, $b^i, c \in C^m(U)$, and $f \in H^m(U)$, then $u \in H^{m+2}_{\mathrm{loc}}(U)$: the solution has **two more derivatives than the data**.
> 2. If all coefficients and $f$ are $C^\infty$, then $u \in C^\infty(U)$.
>
> Weyl's lemma is the case $L = -\Delta$, $f = 0$.

> [!abstract] Generalization 2 (Hypoellipticity: Parabolic and Degenerate Operators)[^4]
> A differential operator $P$ is **hypoelliptic** if $Pu \in C^\infty(V)$ implies $u \in C^\infty(V)$ for every open $V$ and every distribution $u$. Elliptic operators with smooth coefficients are hypoelliptic, and so is the heat operator $\partial_t - \Delta$, which is not elliptic ([[Diffusion Equation Smoothing Theorem]]). **Hörmander's theorem:** if $X_0, X_1, \dots, X_m$ are smooth vector fields whose iterated commutators span the tangent space at every point, then
> $$
> \begin{align}
> P = \sum_{j=1}^m X_j^2 + X_0 + c
> \end{align}
> $$
> is hypoelliptic. Example: the Kolmogorov (Langevin) operator $\partial_v^2 + v\,\partial_x - \partial_t$ diffuses only in $v$, but $[\partial_v, v\partial_x - \partial_t] = \partial_x$ supplies the missing direction, so its solutions are smooth in $(x, v, t)$.

> [!abstract] Generalization 3 (Rough Coefficients: De Giorgi–Nash–Moser)[^5]
> If $A(x)$ is merely bounded, measurable, and uniformly elliptic, every weak solution of $\operatorname{div}(A(x)\nabla u) = 0$ is locally Hölder continuous, $u \in C^{0,\alpha}_{\mathrm{loc}}$ for some $\alpha > 0$, but in general no smoother: the regularity of solutions is capped by the regularity of the coefficients. Applied to the derivatives of minimizers of convex variational integrals with smooth integrands, this bootstraps to full smoothness (Hilbert's 19th problem).

Smoothing is a dissipative property, just like the maximum principle. [[Hyperbolic Partial Differential Equation|Hyperbolic]] equations do not smooth: $u = F(x + ct) + G(x - ct)$ solves the [[Wave Equation]] for any $F, G$, so a singularity in the data travels along characteristics forever (propagation of singularities).

# Properties
- Holds in every dimension; harmonic functions are even [[Real Analytic Function|real analytic]].[^2]
- Weyl's lemma: a merely locally integrable weak solution of $\Delta u = 0$ is already smooth, so the Laplace equation admits no non-smooth solutions; contrast with the [[Wave Equation]], which propagates singularities.[^2]
- Parallels the [[Diffusion Equation Smoothing Theorem]]: both are consequences of a smooth integral kernel.
- A [[Smooth Function]] result, part of what makes the [[Laplace Equation]] [[Elliptic Partial Differential Equation|elliptic]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=182&annotation=ESKJUQF5)
[^2]: Added from general knowledge.
[^3]: [Partial Differential Equations, 2nd ed. (Evans, AMS GSM 19)](https://bookstore.ams.org/gsm-19-r), §6.3.
[^4]: [Hypoelliptic second order differential equations (Hörmander, 1967)](https://doi.org/10.1007/BF02392081)
[^5]: [Elliptic Partial Differential Equations of Second Order (Gilbarg, Trudinger)](https://doi.org/10.1007/978-3-642-61798-0), Ch. 8.
