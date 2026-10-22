---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplace Equation in a Wedge[^1][^2][^3]
> On the wedge $\{0 < \theta < \beta,\ 0 < r < a\}$, the Laplace equation with homogeneous Dirichlet conditions on the straight sides and an inhomogeneous [[Neumann Boundary Condition|Neumann]] condition on the arc,
> $$
> \begin{align}
> u(r, 0) = 0 = u(r, \beta), \qquad \frac{\partial u}{\partial r}(a, \theta) = h(\theta),
> \end{align}
> $$
> has the solution
> $$
> \begin{align}
> u(r, \theta) = \sum_{n=1}^\infty A_n\, r^{n\pi/\beta}\sin\frac{n\pi\theta}{\beta}, \qquad A_n = a^{1 - n\pi/\beta}\,\frac{2}{n\pi}\int_0^\beta h(\theta)\sin\frac{n\pi\theta}{\beta}\, d\theta .
> \end{align}
> $$

[[Separation of Variables]] in the [[Laplacian in Polar Coordinates]]: the $\theta$-problem is the [[Dirichlet Eigenvalue Problem on an Interval]] $(0, \beta)$, so $\lambda_n = (n\pi/\beta)^2$; the Euler equation gives $r^{\pm n\pi/\beta}$, of which $r^{-n\pi/\beta}$ is rejected as unbounded at $r = 0$; the Neumann condition at $r = a$ is a [[Fourier Sine Series]] on $[0, \beta]$.

# Properties
- Belongs to the domains bounded by concentric circles and rays, where polar separation works; other boundary condition combinations follow the same steps.[^4]
- The leading term $r^{\pi/\beta}$ shows corner behavior: for a reentrant corner $\beta > \pi$ the exponent is $< 1$ and the gradient blows up at the vertex.[^5]
- Replacing the Dirichlet conditions on the rays by periodic ones in $\theta$ gives the [[Laplace Equation in a Disk]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=184&annotation=Z5JHEMUN)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=185&annotation=ADEXGTQ5)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=185&annotation=FFFW6AGI)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=184&annotation=ITJGNJP3)
[^5]: Added from general knowledge.
