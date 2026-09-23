---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Residual)[^1]
> The residual of an approximate solution $\hat{x}$ to a [[Linear System of Equations|linear system]] $Ax = b$ is
> $$
> \begin{align}
> r = b - A\hat{x}
> \end{align}
> $$

> [!info] Definition 2 (Relative Residual)[^1]
> The relative residual of $\hat{x}$ is
> $$
> \begin{align}
> \frac{\lVert r \rVert}{\lVert A \rVert \cdot \lVert \hat{x} \rVert}
> \end{align}
> $$

If $A$ is [[Nonsingular Matrix|nonsingular]], then in theory the error $\lVert \Delta x \rVert = \lVert \hat{x} - x \rVert = 0$ iff $\lVert r \rVert = 0$, but in practice the two are not necessarily small at the same time. Multiplying $Ax = b$ by a nonzero constant leaves the solution unchanged but scales the residual by the same factor, so the raw residual is meaningless unless taken relative to the size of the data and solution. Hence the relative residual.[^1]

> [!abstract] Theorem 3 (Small Residual vs. Small Error)[^1]
> $$
> \begin{align}
> \frac{\lVert \Delta x \rVert}{\lVert \hat{x} \rVert} \leq \operatorname{cond}(A) \frac{\lVert r \rVert}{\lVert A \rVert \cdot \lVert \hat{x} \rVert}
> \end{align}
> $$
> Thus a small relative residual implies a small relative error in the solution when, and only when, $A$ is well-conditioned (see [[Condition Number of a Matrix]]).

> [!abstract] Theorem 4 (Large Residual vs. Backward Error)[^1]
> If $\hat{x}$ exactly satisfies $(A + E)\hat{x} = b$, then $\lVert r \rVert = \lVert E\hat{x} \rVert \leq \lVert E \rVert \cdot \lVert \hat{x} \rVert$, so
> $$
> \begin{align}
> \frac{\lVert r \rVert}{\lVert A \rVert \cdot \lVert \hat{x} \rVert} \leq \frac{\lVert E \rVert}{\lVert A \rVert}
> \end{align}
> $$
> Thus a large relative residual implies a large [[Backward Error]] in the matrix, i.e., the algorithm used is unstable.

Equivalently, a [[Stable Algorithm]] always produces a small relative residual regardless of the conditioning of the problem, so a small residual by itself says little about the quality of the approximate solution.[^2]

# Properties
- [[Condition Number of a Matrix]]
- [[Backward Error]]
- [[Stable Algorithm]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=82)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=83)
