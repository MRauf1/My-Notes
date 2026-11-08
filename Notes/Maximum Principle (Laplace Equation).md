---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Maximum Principle (Laplace Equation)[^1]
> Let $D \subset \mathbb{R}^n$ ($n = 2, 3$ in the source; the statement holds for every $n$) be a connected bounded open set, and let $u$ be a [[Harmonic Function]] in $D$ that is continuous on $\bar D = D \cup \partial D$. Then the maximum and the minimum values of $u$ are attained on $\partial D$ and nowhere inside, unless $u \equiv$ constant:
> $$
> \begin{align}
> \min_{\partial D} u \le u(\mathbf{x}) \le \max_{\partial D} u \qquad \text{for all } \mathbf{x} \in \bar D.
> \end{align}
> $$

A harmonic function is biggest somewhere on the boundary and smallest somewhere else on the boundary; no interior point has either property (unless $u$ is constant), while several boundary points may.[^2]

# Generalizations
> [!abstract] Generalization 1 (Linear Second-Order Elliptic Operators)[^4]
> Let $U \subset \mathbb{R}^n$ be bounded and open, and let
> $$
> \begin{align}
> Lu = -\sum_{i,j=1}^n a^{ij}(x)\,u_{x_ix_j} + \sum_{i=1}^n b^i(x)\,u_{x_i} + c(x)\,u
> \end{align}
> $$
> have bounded coefficients, $a^{ij} = a^{ji}$, and be **uniformly elliptic**: $\sum_{i,j} a^{ij}(x)\xi_i\xi_j \geq \theta|\xi|^2$ for some $\theta > 0$. Let $u \in C^2(U) \cap C(\bar U)$.
> 1. **Weak form, $c \equiv 0$.** If $Lu \leq 0$ (subsolution), then $\max_{\bar U} u = \max_{\partial U} u$. If $Lu \geq 0$, then $\min_{\bar U} u = \min_{\partial U} u$.
> 2. **Weak form, $c \geq 0$.** If $Lu \leq 0$, then $\max_{\bar U} u \leq \max_{\partial U} u^+$. If $Lu \geq 0$, then $\min_{\bar U} u \geq -\max_{\partial U} u^-$.
> 3. **Strong form** ($U$ connected). If $c \equiv 0$, $Lu \leq 0$, and $u$ attains $\max_{\bar U} u$ at an interior point, then $u$ is constant. If $c \geq 0$, the same holds when the interior maximum is nonnegative. The proof uses **Hopf's lemma**: at a boundary point $x^0$ with an interior touching ball where $u(x^0) > u(x)$ for all $x \in U$ (and $u(x^0) \geq 0$ if $c \geq 0$), the outer normal derivative satisfies $\partial u/\partial\nu(x^0) > 0$.
> 4. **Comparison.** If $c \geq 0$, $Lu \leq Lv$ in $U$, and $u \leq v$ on $\partial U$, then $u \leq v$ in $U$. This follows from 2 applied to $u - v$, so it also gives uniqueness for the Dirichlet problem $Lu = f$.
>
> The Laplace case is $L = -\Delta$ ($a^{ij} = \delta_{ij}$, $b = 0$, $c = 0$), where $Lu \leq 0$ means $u$ is subharmonic.

**The sign of $c$ is essential.** On $U = (0,1)$, $u = \sin(\pi x)$ solves $-u'' - \pi^2 u = 0$, i.e. $Lu = 0$ with $c = -\pi^2 < 0$. It vanishes on $\partial U$ yet has interior maximum $1$. In general a Dirichlet [[Eigenfunction]] with $-\Delta\phi = \lambda\phi$ solves $L\phi = 0$ for $L = -\Delta - \lambda$, so the maximum principle must fail above the bottom of the spectrum. The sharp statement is that the (refined) maximum principle for $L$ on $U$ holds **if and only if the principal eigenvalue of $L$ on $U$ is positive**.[^5] For $L = -\Delta - \mu$ with constant $\mu$, this means $\mu < \lambda_1^D(U)$, the first Dirichlet eigenvalue of $-\Delta$.

> [!abstract] Generalization 2 (Nonlinear and First-Order Equations: Comparison Principle)[^6]
> Consider $F(x, u, Du, D^2u) = 0$ in a bounded open $U$, where $F(x, r, p, X)$ is continuous, **degenerate elliptic** ($F(x,r,p,X) \leq F(x,r,p,Y)$ whenever $Y \leq X$ as symmetric matrices), and **proper** (also nondecreasing in $r$). Under structure conditions on $F$ (for example, $F$ strictly increasing in $r$ together with suitable continuity in $x$), if $u$ is a viscosity subsolution, $v$ a viscosity supersolution, and $u \leq v$ on $\partial U$, then $u \leq v$ in $U$. In particular the Dirichlet problem has at most one viscosity solution.
>
> This covers quasilinear equations (the minimal surface equation, the $p$-Laplacian), fully nonlinear ones (Bellman and Isaacs equations of stochastic control), and **first-order Hamilton–Jacobi equations** $H(x, u, Du) = 0$, since an $F$ independent of $X$ is trivially degenerate elliptic.

> [!abstract] Generalization 3 (Scalar Conservation Laws)[^7]
> For the first-order equation $u_t + \operatorname{div}_x f(u) = 0$ on $\mathbb{R}^n \times (0, \infty)$ with $u_0 \in L^\infty$, the entropy solution satisfies the maximum principle $\operatorname{ess\,inf} u_0 \leq u(\cdot, t) \leq \operatorname{ess\,sup} u_0$. Two entropy solutions also satisfy the $L^1$ contraction $\|u(\cdot,t) - v(\cdot,t)\|_{L^1} \leq \|u_0 - v_0\|_{L^1}$.

**Scope.** Maximum and comparison principles come from **dissipation**: second-order terms that average out extremes. They are not a property of all PDEs.

| Class | Example | Maximum / comparison principle |
|---|---|---|
| Linear elliptic, 2nd order | [[Laplace Equation]], Poisson, $-\Delta u + cu = f$ | Yes, if $c \geq 0$ (sharp: principal eigenvalue $> 0$) |
| Linear parabolic, 2nd order | [[Heat Equation]], diffusion with drift | Yes, for any bounded $c$ ([[Maximum Principle (Diffusion Equation)]]) |
| Nonlinear degenerate elliptic or parabolic | minimal surface, $p$-Laplacian, Bellman | Comparison for viscosity solutions |
| First-order Hamilton–Jacobi | eikonal $\lvert Du\rvert = f$ | Comparison for viscosity solutions |
| Scalar conservation laws | Burgers $u_t + (u^2/2)_x = 0$ | $L^\infty$ bound and $L^1$ contraction (entropy solutions) |
| 2nd-order **hyperbolic** | [[Wave Equation]] | **No** |
| Higher order or systems | biharmonic $\Delta^2 u = 0$ | **No** in general |

Counterexamples. $u = \sin x \sin t$ solves $u_{tt} = u_{xx}$ on $[0,\pi]^2$ and vanishes on $t = 0$, $x = 0$, and $x = \pi$, but equals $1$ at $(\pi/2, \pi/2)$. Hyperbolic equations are controlled by energy conservation and finite speed of propagation instead ([[Wave Equation Energy Conservation]]). The function $u = 1 - |x|^2$ is biharmonic ($\Delta^2 u = 0$) on the unit ball, vanishes on its boundary, and has interior maximum $1$.

# Properties
- **Weak form** (extremes attained on $\partial D$) vs **strong form** (never attained inside unless constant); the strong form follows from the [[Mean Value Property (Harmonic Function)]].[^3]
- Time-independent case of the [[Maximum Principle (Diffusion Equation)]].
- Implies uniqueness and uniform stability of the Dirichlet problem: [[Laplace Equation Dirichlet Problem Uniqueness]].
- Holds one-sidedly for subharmonic ($\Delta u \ge 0$: max on $\partial D$) and superharmonic ($\Delta u \le 0$: min on $\partial D$) functions.[^3]
- **Discrete analogue.** For a [[Graph Laplacian Matrix|graph Laplacian]] with nonnegative edge weights, a function equal to the weighted average of its neighbours at every interior vertex attains its max and min on boundary vertices. The cotangent Laplacian on a triangle mesh has weight $\tfrac12(\cot\alpha + \cot\beta) = \frac{\sin(\alpha+\beta)}{2\sin\alpha\sin\beta}$ on an interior edge, which is nonnegative iff $\alpha + \beta \leq \pi$ (the Delaunay condition), so its discrete maximum principle can fail on non-Delaunay meshes.[^8]
- Fails on unbounded domains without growth conditions, e.g. on the exterior of a circle one must impose boundedness at infinity ([[Laplace Equation in the Exterior of a Circle]]).[^3]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=166&annotation=CK4QKFJT)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=166&annotation=X3FA493S); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=167&annotation=LRNN54X5)
[^3]: Added from general knowledge.
[^4]: [Partial Differential Equations, 2nd ed. (Evans, AMS GSM 19)](https://bookstore.ams.org/gsm-19-r), §6.4.1–6.4.2.
[^5]: [The principal eigenvalue and maximum principle for second-order elliptic operators in general domains (Berestycki, Nirenberg, Varadhan, 1994)](https://doi.org/10.1002/cpa.3160470105)
[^6]: [User's guide to viscosity solutions of second order partial differential equations (Crandall, Ishii, Lions, 1992)](https://www.ams.org/journals/bull/1992-27-01/S0273-0979-1992-00266-5/)
[^7]: [First order quasilinear equations in several independent variables (Kružkov, 1970)](https://doi.org/10.1070/SM1970v010n02ABEH002156)
[^8]: [Discrete Laplace operators: No free lunch (Wardetzky, Mathur, Kälberer, Grinspun, 2007)](https://diglib.eg.org/items/43d99127-69ae-464d-aa71-497b72b41a0b)
