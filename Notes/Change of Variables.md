---
tags: mathetatics, calculus
---

# Definition

> [!info] Definition 1 (Change of Variables)[^1]
> Given a [[Transformation]] $T: S \subseteq \mathbb{R}^n \rightarrow R \subseteq \mathbb{R}^n$ that is [[Bijective Function]] (except perhaps on the boundary of $S$) and [[Continuous Function]] $f$, the change of variables is
> $$
> \begin{align}
> T(u_1, \dots, u_n) &= (v_1, \dots, v_n) = (g_1(\mathbf{u}), \dots, g_n(\mathbf{u})) \\
> f(v_1, \dots, v_n) &= f(g_1(\mathbf{u}), \dots, g_n(\mathbf{u})) \\
> du_1 \dots du_n &= |\mathbf{J}| dv_1 \dots dv_n
> \end{align}
> $$
> where $|\mathbf{J}|$ is the [[Determinant]] of the [[Jacobian Matrix]] ([[Partial Derivative]] of $g_i$ with respect to $u_1$; first row is all $g_1$, second is $g_2$, and so on).
> In [[Riemann Integral]], this allows for
> $$
> \begin{align}
> \int \int_R f(v_1, v_2) dv_1 dv_2 = \int \int_S f(g_1(u_1, u_2), g_2(u_1, u_2)) |\mathbf{J}| du_1 du_2
> \end{align}
> $$

This allows to relate a product of one set of [[Differential]] with a set of other set of [[Differential]]. 

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=1088)