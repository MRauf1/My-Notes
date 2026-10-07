---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Wave and Diffusion Equation Comparison[^1][^2]
> The basic property of waves is that information is **transported** in both directions at a finite speed. The basic property of diffusions is that the initial disturbance is **spread out** smoothly and gradually disappears.
>
> | Property | [[Wave Equation\|Waves]] $u_{tt} = c^2\Delta u$ | [[Diffusion Equation\|Diffusions]] $u_t = k\Delta u$ |
> | --- | --- | --- |
> | (i) Speed of propagation | Finite ($\le c$) | Infinite |
> | (ii) Singularities for $t > 0$ | Transported along characteristics (speed $c$) | Lost immediately |
> | (iii) Well-posed for $t > 0$ | Yes | Yes (at least for bounded solutions) |
> | (iv) Well-posed for $t < 0$ | Yes | No |
> | (v) Maximum principle | No | Yes |
> | (vi) Behavior as $t \to +\infty$ | Energy is constant, so does not decay | Decays to zero (if $\phi$ integrable) |
> | (vii) Information | Transported | Lost gradually |

**Explanation of each row.**[^3][^4]
- **(i)** Waves obey the [[Principle of Causality (Wave Equation)|principle of causality]]: $u(\mathbf{x}, t)$ depends only on data in the ball $|\mathbf{y} - \mathbf{x}| \le ct$ ([[Domain of Dependence]]). For diffusion, $u(x, t)$ depends on $\phi(y)$ for all $y$, and $\phi$ at $x_0$ immediately affects every point for $t > 0$, though most of its effect stays near $x_0$ for a short time, because the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]] (a Gaussian) is positive everywhere. Solutions of the diffusion equation can travel at any speed, in stark contrast to all [[Hyperbolic Partial Differential Equation|hyperbolic equations]].
- **(ii)** A kink or jump in wave data rides along the characteristics forever ([[D'Alembert's Formula]]). A diffusion solution is $C^\infty$ for every $t > 0$ even if $\phi$ is not, because it is $\phi$ convolved with a smooth Gaussian.
- **(iii), (iv)** The wave equation is time-reversible ($t \mapsto -t$ leaves it invariant). Diffusion run backward must un-blur, amplifying high frequencies like $e^{k\xi^2|t|}$: it is ill-posed. Heat flow and [[Brownian Motion]] are **irreversible** processes, and going backward leads to chaos ([[Diffusion Equation Well-Posedness]]).
- **(v)** Diffusion has the [[Maximum Principle (Diffusion Equation)|maximum principle]]: maxima drop and minima rise. Waves do not; they carry their amplitude around and can build new peaks by interference.
- **(vi)** Wave energy is conserved ([[Wave Equation Energy Conservation]]); diffusion decays like $t^{-n/2}$ as the Gaussian flattens.
- **(vii)** Waves move information along characteristics in 1D and on expanding circles/spheres in higher dimensions ([[Huygens's Principle]]); diffusion averages it away, as the flattening graph of $S(x, t)$ shows.

# Properties
- The table is the prototype of the contrast between [[Hyperbolic Partial Differential Equation|hyperbolic]] and [[Parabolic Partial Differential Equation|parabolic]] equations.
- The time-independent limit of both is the [[Laplace Equation]].
- Whole-line problems isolate these properties without boundary effects; for waves this is physically justified because the boundary's influence takes finite time to arrive.[^5]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=66&annotation=USPZ5SCZ)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=66&annotation=W8RR9LU5)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=67&annotation=A2CEKVHF); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=67&annotation=FIXAJVFR)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=67&annotation=MFI8VP92); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=67&annotation=NWLNLRCD)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=45&annotation=JGSNR9QP)
