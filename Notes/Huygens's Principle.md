---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Huygens's Principle[^1]
> For the [[Wave Equation]] $u_{tt} = c^2 \Delta u$ in $\mathbb{R}^n$ with $n \ge 3$ odd, signals travel at speed exactly $c$, never slower: $u(\mathbf{x}, t)$ depends only on the initial data on the sphere $|\mathbf{y} - \mathbf{x}| = ct$, and initial data supported at $\mathbf{x}_0$ affects only the expanding sphere $|\mathbf{x} - \mathbf{x}_0| = ct$. It is the sharp form of the [[Principle of Causality (Wave Equation)]].

A sharp sound or flash in 3D passes an observer as a clean pulse and then is gone: the solution inside the cone, behind the wavefront, is zero.

**It fails in 2D ("Flatland").**[^2] In 2D the solution depends on the data in the whole disk $|\mathbf{y} - \mathbf{x}| \le ct$, so after the wavefront passes, a decaying tail lingers (drop a pebble in a pond: the ripples keep coming). A 2D creature would hear each sound mixed with echoes of its earlier sounds and see each view fuzzily mixed with previous views. 1D also lacks the sharp form for initial velocities, which spread at all speeds $\le c$ ([[D'Alembert's Formula]]). In this sense, three is the best of all possible dimensions.

# Properties
- Holds in odd $n \ge 3$ and fails in every even $n$ (and for velocity data in $n = 1$); a 2D solution is a 3D solution independent of $x_3$ (method of descent), and the infinite line source along $x_3$ produces the tail.
- [[Domain of Influence]] reduces to the surface of the [[Light Cone]] rather than its interior.
- Not to be confused with the older Huygens–Fresnel construction of wavefronts from secondary wavelets, which it makes precise.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=53&annotation=YDYFSSW9)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=53&annotation=TVRUABZY)
