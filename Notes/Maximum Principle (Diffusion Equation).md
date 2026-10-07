---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Maximum Principle (Diffusion Equation)[^1][^2]
> **Weak form.** If $u$ satisfies the [[Diffusion Equation]] $u_t = k u_{xx}$ in the rectangle $0 \le x \le l$, $0 \le t \le T$, then the maximum of $u$ over the rectangle is attained on the bottom ($t = 0$) or on the lateral sides ($x = 0$ or $x = l$).
>
> **Strong form.** The maximum cannot be attained anywhere else (corners allowed) unless $u$ is constant.
>
> **Minimum principle.** The same holds for the minimum, by applying the maximum principle to $-u$.
>
> **$n$-D form.** If $u_t = k\Delta u$ in $D \times (0, T]$ for a bounded domain $D \subset \mathbb{R}^n$, then
> $$
> \begin{align}
> \max_{\bar{D} \times [0, T]} u = \max_{\Gamma} u, \qquad \Gamma = (\bar{D} \times \{0\}) \cup (\partial D \times [0, T]),
> \end{align}
> $$
> where $\Gamma$ is the parabolic boundary. If $D$ is connected and the maximum is attained at an interior point $(\mathbf{x}_0, t_0)$, $t_0 > 0$, then $u$ is constant on $\bar{D} \times [0, t_0]$.

![[Diffusion Maximum Principle Parabolic Boundary.png]]

**Interpretation.**[^3] In a rod with no internal heat source, the hottest and coldest spots can occur only initially or at an end. A hot spot at $t = 0$ cools off unless heat is fed in at an end; if you burn one end, the maximum temperature stays at that end and it is cooler away from it. The same holds for the concentration of a substance diffusing along a tube. In a "movie" of the solution, the maximum drops and the minimum rises: diffusion smooths the solution out. The top edge $t = T$ is excluded from $\Gamma$ because the future cannot feed back into the past.

# Properties
- Proof idea: an interior maximum has $u_t = 0$ (or $u_t \ge 0$ on the top edge) and $u_{xx} \le 0$, which does not contradict $u_t = k u_{xx}$ when $u_{xx} = 0$; perturbing to $v = u + \epsilon x^2$ gives the strict "diffusion inequality" $v_t - k v_{xx} = -2k\epsilon < 0$, which rules out an interior maximum.[^4]
- Gives uniqueness and stability in the uniform sense for the Dirichlet problem ([[Diffusion Equation Well-Posedness]]).
- Fails for the [[Wave Equation]]: waves carry their amplitude around without damping ([[Wave and Diffusion Equation Comparison]]).
- Also holds for subsolutions $u_t \le k \Delta u$ (max) and supersolutions (min), and on the whole line for bounded solutions: $\inf \phi \le u(x, t) \le \sup \phi$.
- The time-independent case is the maximum principle for [[Harmonic Function|harmonic functions]] ([[Laplace Equation]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=54&annotation=N5GCRVV8)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=54&annotation=HM2L2QR9); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=54&annotation=VE6A6KY5)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=55&annotation=7MC24ZCG)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=55&annotation=LKFPFSP6)
