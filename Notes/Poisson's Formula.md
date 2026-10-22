---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Poisson's Formula[^1][^2]
> The solution of the [[Laplace Equation in a Disk]] of radius $a$ with boundary data $h(\phi)$ is
> $$
> \begin{align}
> u(r, \theta) = (a^2 - r^2)\int_0^{2\pi} \frac{h(\phi)}{a^2 - 2ar\cos(\theta - \phi) + r^2}\,\frac{d\phi}{2\pi}, \qquad r < a,
> \end{align}
> $$
> or geometrically, with $\mathbf{x}$ at $(r, \theta)$, $\mathbf{x}'$ at $(a, \phi)$ on the circle, and arc length $ds' = a\, d\phi$,
> $$
> \begin{align}
> u(\mathbf{x}) = \frac{a^2 - |\mathbf{x}|^2}{2\pi a}\oint_{|\mathbf{x}'| = a} \frac{u(\mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|^2}\, ds' .
> \end{align}
> $$

> [!info] Theorem (Poisson's Formula Solves the Dirichlet Problem)[^3]
> If $h$ is continuous on the circle $C = \partial D$, then Poisson's formula gives the only harmonic function in $D$ with $\lim_{\mathbf{x}\to\mathbf{x}_0} u(\mathbf{x}) = h(\mathbf{x}_0)$ for all $\mathbf{x}_0 \in C$. Thus $u$ is continuous on $\bar D = D \cup C$ and differentiable to all orders inside $D$.

The single formula replaces the triple of series formulas; it expresses any harmonic function inside a circle in terms of its boundary values.[^1] The geometric form follows from the [[Law of Cosines]] $|\mathbf{x} - \mathbf{x}'|^2 = a^2 + r^2 - 2ar\cos(\theta - \phi)$.[^2]

**General case.**[^4] For the ball of radius $a$ in $\mathbb{R}^n$,
$$
\begin{align}
u(\mathbf{x}) = \frac{a^2 - |\mathbf{x}|^2}{a\,\omega_n}\int_{|\mathbf{x}'| = a}\frac{u(\mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|^n}\, dS',
\end{align}
$$
with $\omega_n$ the area of the unit sphere ($\omega_2 = 2\pi$, $\omega_3 = 4\pi$).

**Exterior.**[^5] For $r > a$, the bounded solution of the [[Laplace Equation in the Exterior of a Circle]] is the same formula with $a^2 - r^2$ replaced by $r^2 - a^2$.

# Properties
- Equivalent to $u(r, \theta) = \int_0^{2\pi} P(r, \theta - \phi)\, h(\phi)\, \frac{d\phi}{2\pi}$, a circular convolution with the [[Poisson Kernel]].
- Consequences: [[Mean Value Property (Harmonic Function)]] (set $r = 0$) and [[Harmonic Function Smoothness]].[^3]
- In electrostatics it gives the potential due to charges on a cylinder that are uniform along its length.[^2]
- Summing a series of eigenfunctions to a closed-form kernel works only in special geometries.[^6]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=180&annotation=A3ASUPDB)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=180&annotation=W7GQS249)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=181&annotation=TS9KA277)
[^4]: Added from general knowledge.
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=187&annotation=BMNU3H3W)
[^6]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=184&annotation=ITJGNJP3)
