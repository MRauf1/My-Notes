---
tags:
  - mathematics
  - differential_geometry
---

# Definition

> [!info] Definition 1 ([[Frenet Frame Field]] [[Derivative]])[^1]
> For a Frenet Frame Field $T, N, B$ on [[Unit Speed Curve]] $\beta$, their derivatives are
> - $T' = \beta'' = \kappa N$
> - $N' = - \kappa T + \tau B$
> - $B' = - \tau N$
> If the [[Curve]] $\beta$ does not have unit speed, then the above becomes
> - $T' = \kappa v N$
> - $N' = - \kappa v T + \tau v B$
> - $B' = -\tau v N$
> where $v$ is the [[Curve Speed]] of $\beta$.

> [!abstract] Theorem 2 (Matrix Form and Cartan's Proof)[^2]
> With $T, N, B$ as rows of $Q \in \mathbb{R}^{3\times3}$ and primes denoting change at unit speed,
> $$\begin{align}
> \underbrace{\begin{bmatrix} T' \\ N' \\ B' \end{bmatrix}}_{Q'} = \underbrace{\begin{bmatrix} 0 & \kappa & 0 \\ -\kappa & 0 & \tau \\ 0 & -\tau & 0 \end{bmatrix}}_{A} \underbrace{\begin{bmatrix} T \\ N \\ B \end{bmatrix}}_{Q}.
> \end{align}$$
> *Proof (Cartan).* $T, N, B$ orthonormal $\Rightarrow$ $QQ^T = I$ ([[Orthogonal Matrix]]). Differentiating, $Q'Q^T + QQ'^T = 0$, so $A = Q'Q^T$ is skew-symmetric: zero diagonal, $A_{ij} = -A_{ji}$. The first row is fixed by $T' = \kappa N$; the one remaining free entry $A_{23} = -A_{32}$ is named the torsion $\tau$.

The proof is easy to verify but gives little geometric insight (e.g. why $N$ changes along both $T$ and $B$ while $B$ changes only along $N$).[^2]

**Sign convention.** These notes follow O'Neill ($T' = \kappa N$, $\kappa \ge 0$). Crane instead writes $dT(X) = -\kappa N$ with $N$ a quarter turn counter-clockwise from $T$, giving the matrix with all signs of $\kappa$ and $\tau$ flipped.[^3]

# Properties
- Unit-vector argument: if $|T| = 1$ then $T' \perp T$ (otherwise $T$ would stop being unit length). This holds for any unit vector field.[^3]
- For a curve lying in a surface, the component of $T' = \kappa N$ along the surface normal is the [[Normal Curvature]].

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=74)
[^2]: [Crane, p. 36](zotero://open-pdf/library/items/9N6JDPI2?page=37&annotation=HD75Q7Q5)
[^3]: [Crane, p. 36](zotero://open-pdf/library/items/9N6JDPI2?page=37&annotation=AI5NT94E)
