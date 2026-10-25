---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Separating Points and Vanishing at No Point)[^1]
> Let $\mathscr{A}$ be a family of [[Function|functions]] on a [[Set]] $E$.
> - $\mathscr{A}$ **separates points** on $E$ if to every pair of distinct points $x_1, x_2 \in E$ there corresponds a function $f \in \mathscr{A}$ such that $f(x_1) \neq f(x_2)$.
> - $\mathscr{A}$ **vanishes at no point** of $E$ if to each $x \in E$ there corresponds a function $g \in \mathscr{A}$ such that $g(x) \neq 0$.

The [[Algebra of Functions|algebra]] of all [[Polynomial|polynomials]] in one variable has both properties on $\mathbb{R}$. The algebra of even polynomials on $[-1, 1]$ does not separate points, since $f(-x) = f(x)$.[^1]

> [!abstract] Theorem 2 (Two-Point Interpolation)[^2]
> Suppose $\mathscr{A}$ is an [[Algebra of Functions|algebra of functions]] on a set $E$, $\mathscr{A}$ separates points on $E$, and $\mathscr{A}$ vanishes at no point of $E$. Suppose $x_1, x_2$ are distinct points of $E$, and $c_1, c_2$ are constants (real if $\mathscr{A}$ is a real algebra). Then $\mathscr{A}$ contains a function $f$ such that
> $$
> \begin{align}
> f(x_1) = c_1, \quad f(x_2) = c_2
> \end{align}
> $$

# Properties
- Hypotheses of the [[Stone-Weierstrass Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=171&annotation=GY8LEERW)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=171&annotation=45RNQVYP)
