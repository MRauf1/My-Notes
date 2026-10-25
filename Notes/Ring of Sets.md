---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Ring and $\sigma$-Ring of Sets[^1]
> A family $\mathcal{R} \subseteq \mathcal{P}(X)$ is a **ring** if it is closed under finite [[Set Union|unions]] and set differences:
> $$
> \begin{align}
> E_1, \dots, E_n \in \mathcal{R} \implies \bigcup_{j=1}^n E_j \in \mathcal{R}, \qquad E, F \in \mathcal{R} \implies E \setminus F \in \mathcal{R}.
> \end{align}
> $$
> A ring closed under countable unions is a **$\sigma$-ring**.

A ring is an [[Algebra of Sets|algebra]] that need not contain the whole space $X$, so complements are replaced by relative differences. Not to be confused with the algebraic [[Ring]], although a ring of sets is a ring in that sense under $\triangle$ ([[Symmetric Difference]]) and $\cap$.

# Properties
- Rings (resp. $\sigma$-rings) are closed under finite (resp. countable) intersections.
- A ring (resp. $\sigma$-ring) is an [[Algebra of Sets|algebra]] (resp. [[Sigma-Field|$\sigma$-algebra]]) if and only if $X \in \mathcal{R}$.
- If $\mathcal{R}$ is a $\sigma$-ring, then $\{E \subseteq X : E \in \mathcal{R} \text{ or } E^c \in \mathcal{R}\}$ is a $\sigma$-algebra.
- If $\mathcal{R}$ is a $\sigma$-ring, then $\{E \subseteq X : E \cap F \in \mathcal{R} \text{ for all } F \in \mathcal{R}\}$ is a $\sigma$-algebra.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=37&annotation=YZT8X7BS)
