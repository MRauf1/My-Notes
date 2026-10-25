---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!abstract] Theorem 1.8 (Basic Properties of Measures)[^1][^2]
> Let $(X, \mathcal{M}, \mu)$ be a [[Measure Space]].
> 1. **(Monotonicity)** If $E, F \in \mathcal{M}$ and $E \subseteq F$, then $\mu(E) \leq \mu(F)$.
> 2. **(Subadditivity)** If $\{E_j\}_1^\infty \subseteq \mathcal{M}$, then $\mu\left(\bigcup_1^\infty E_j\right) \leq \sum_1^\infty \mu(E_j)$.
> 3. **(Continuity from below)** If $\{E_j\}_1^\infty \subseteq \mathcal{M}$ and $E_1 \subseteq E_2 \subseteq \cdots$, then
> $$
> \begin{align}
> \mu\left(\bigcup_{j=1}^\infty E_j\right) = \lim_{j \to \infty} \mu(E_j).
> \end{align}
> $$
> 4. **(Continuity from above)** If $\{E_j\}_1^\infty \subseteq \mathcal{M}$, $E_1 \supseteq E_2 \supseteq \cdots$, and $\mu(E_1) < \infty$, then
> $$
> \begin{align}
> \mu\left(\bigcap_{j=1}^\infty E_j\right) = \lim_{j \to \infty} \mu(E_j).
> \end{align}
> $$

Subadditivity and continuity from below come from the disjointification trick of [[Algebra of Sets|algebras]]: rewrite the union as a disjoint union and apply countable additivity. The hypothesis $\mu(E_1) < \infty$ in continuity from above is needed, as $E_j = [j, \infty)$ under [[Lebesgue Measure]] shows.

# Properties
- **Inclusion–exclusion for two sets**: for $E, F \in \mathcal{M}$, $\mu(E) + \mu(F) = \mu(E \cup F) + \mu(E \cap F)$.[^3]
- **Fatou-type inequalities for sets**: for $\{E_j\} \subseteq \mathcal{M}$ ([[Limit Superior and Limit Inferior of Sets]]),[^4]
$$
\begin{align}
\mu\left(\liminf E_j\right) \leq \liminf \mu(E_j), \qquad \mu\left(\limsup E_j\right) \geq \limsup \mu(E_j) \ \text{ if } \mu\left(\textstyle\bigcup_1^\infty E_j\right) < \infty.
\end{align}
$$
- **Characterization of countable additivity**: a [[Finitely Additive Measure]] is a measure iff it is continuous from below; if $\mu(X) < \infty$, iff it is continuous from above.[^5]
- **Positive combinations**: if $\mu_1, \dots, \mu_n$ are measures on $(X, \mathcal{M})$ and $a_1, \dots, a_n \in [0, \infty)$, then $\sum_1^n a_j \mu_j$ is a measure.[^6]
- Countable unions of [[Null Set (Measure Theory)|null sets]] are null, by subadditivity.
- The probabilistic version is the [[Continuity Theorem of Probability]], and subadditivity there is [[Boole's Inequality]].

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=38&annotation=27ACGXNN)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=39&annotation=CFGHAAJD)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=40&annotation=8IMTCSXE)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=40&annotation=ZACX3X48)
[^5]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=40&annotation=XEGYUGLZ)
[^6]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=40&annotation=Z2QA7VZG)
