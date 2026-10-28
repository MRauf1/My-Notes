---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Sklar's Theorem[^1]
> Let $F$ be a $d$-dimensional joint CDF with marginal CDFs $F_1, \dots, F_d$. Then there exists a [[Copula]] $C$ such that
> $$
> \begin{align}
> F(x_1, \dots, x_d) = C\big(F_1(x_1), \dots, F_d(x_d)\big), \qquad \mathbf{x} \in \mathbb{R}^d
> \end{align}
> $$
> If all of the $F_j$ are continuous, $C$ is unique; otherwise it is not.

Equivalently, for any $F$ there is a copula $C$ such that drawing $\mathbf{U} \sim C$ and setting $X_j = F_j^{-1}(U_j)$ delivers $\mathbf{X} \sim F$. This is what makes [[Copula-Marginal Sampling]] a fully general sampling method.

# Properties
- Conversely, any copula $C$ combined with any marginals $F_1, \dots, F_d$ through the formula above defines a valid joint CDF ([[Joint Cumulative Distribution Function]]).
- When some $F_j$ has atoms, $C$ is only determined on $\mathrm{Range}(F_1) \times \dots \times \mathrm{Range}(F_d)$.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=20&annotation=PJL59BR4)
