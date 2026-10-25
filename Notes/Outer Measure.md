---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Outer Measure[^1]
> An outer measure on a nonempty set $X$ is a function $\mu^* : \mathcal{P}(X) \to [0, \infty]$ such that
> 1. $\mu^*(\emptyset) = 0$,
> 2. $\mu^*(A) \leq \mu^*(B)$ if $A \subseteq B$,
> 3. $\mu^*\left(\bigcup_1^\infty A_j\right) \leq \sum_1^\infty \mu^*(A_j)$.

The abstraction of *outer area*: approximate an arbitrary set from the outside by covering it with simple sets. Inner area is then derived from outer area, since for a large rectangle $R \supseteq E$, the inner area of $E$ is the area of $R$ minus the outer area of $R \setminus E$.[^2]

Compared with a [[Measure (Measure Theory)|measure]], an outer measure is defined on **every** subset but is only countably **sub**additive. It is an upper-bound estimate that becomes an honest measure only after restriction to the [[Carathéodory Measurable Set|Carathéodory-measurable sets]] ([[Carathéodory's Theorem]]).

# Properties
> [!abstract] Proposition 1.10 (Outer Measure from Elementary Sets)[^3]
> Let $\mathcal{E} \subseteq \mathcal{P}(X)$ and $\rho : \mathcal{E} \to [0, \infty]$ with $\emptyset \in \mathcal{E}$, $X \in \mathcal{E}$, and $\rho(\emptyset) = 0$. For $A \subseteq X$ define
> $$
> \begin{align}
> \mu^*(A) = \inf\left\{\sum_{j=1}^\infty \rho(E_j) : E_j \in \mathcal{E} \text{ and } A \subseteq \bigcup_{j=1}^\infty E_j\right\}.
> \end{align}
> $$
> Then $\mu^*$ is an outer measure.

- The most common source: a [[Premeasure]] $\mu_0$ on an [[Algebra of Sets|algebra]] induces an outer measure by Proposition 1.10, which agrees with $\mu_0$ on the algebra.
- Paired with [[Inner Measure]], it characterizes measurability for finite premeasures.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=41&annotation=URB6DQ9R)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=41&annotation=Z4FULVGT)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=42&annotation=PMHJRVWB)
