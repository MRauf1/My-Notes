---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Characteristic Curve[^1]
> For the [[First Order Partial Differential Equation]] $a(x, y) u_x + b(x, y) u_y = 0$, the characteristic curves are the [[Curve|curves]] in the $xy$-plane whose tangent vector at each point is $(a(x,y), b(x,y))$, i.e., the solutions of the [[Ordinary Differential Equation]]
> $$
> \begin{align}
> \frac{dy}{dx} = \frac{b(x, y)}{a(x, y)}.
> \end{align}
> $$
> When $a, b$ are constant, they are the straight characteristic lines $bx - ay = \text{const}$.

# Properties
- Every solution $u$ is constant along each characteristic curve, since along it $\frac{d}{dx} u(x, y(x)) = u_x + \frac{b}{a} u_y = 0$ (the PDE says the [[Directional Derivative]] along $(a, b)$ vanishes).
- If the characteristics are $\{\xi(x, y) = C\}$, the general solution is $u = f(\xi(x, y))$ with $f$ arbitrary.
- Under regularity of $a, b$, the characteristics fill the plane without intersecting.
- For the [[Transport Equation]], each transported particle moves exactly along a characteristic line in the $xt$-plane.
- The 1D [[Wave Equation]] has two families of characteristic lines $x \pm ct = \text{const}$; its solutions are carried along them ([[D'Alembert's Formula]]) and they bound the [[Domain of Dependence]] and [[Domain of Influence]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=20&annotation=6SX3PID3)
