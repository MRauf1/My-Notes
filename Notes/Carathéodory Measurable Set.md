---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] $\mu^*$-Measurable Set (Carathéodory Criterion)[^1]
> If $\mu^*$ is an [[Outer Measure]] on $X$, a set $A \subseteq X$ is $\mu^*$-measurable if it splits every set additively:
> $$
> \begin{align}
> \mu^*(E) = \mu^*(E \cap A) + \mu^*(E \cap A^c) \qquad \text{for all } E \subseteq X.
> \end{align}
> $$

Since $\mu^*(E) \leq \mu^*(E \cap A) + \mu^*(E \cap A^c)$ always holds by subadditivity, and the reverse is trivial when $\mu^*(E) = \infty$, $A$ is $\mu^*$-measurable iff[^1][^2]
$$
\begin{align}
\mu^*(E) \geq \mu^*(E \cap A) + \mu^*(E \cap A^c) \qquad \text{for all } E \subseteq X \text{ with } \mu^*(E) < \infty.
\end{align}
$$

**Motivation.**[^3] If $E$ is a "well-behaved" set containing $A$, the equation says that the outer measure $\mu^*(A)$ equals the "inner measure" $\mu^*(E) - \mu^*(E \cap A^c)$: approximating $A$ from outside and from inside agree. The definition demands this for *every* test set $E$, a large leap justified by [[Carathéodory's Theorem]].

# Properties
- The $\mu^*$-measurable sets form a [[Sigma-Field|$\sigma$-algebra]] on which $\mu^*$ is a [[Complete Measure|complete measure]] ([[Carathéodory's Theorem]]).
- If $\mu^*$ is induced by a [[Premeasure]] on an algebra $\mathcal{A}$, every set in $\mathcal{A}$ is $\mu^*$-measurable.
- For an outer measure induced by a finite premeasure, $\mu^*$-measurability is equivalent to equality of [[Inner Measure|inner]] and outer measure.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=42&annotation=PWM9EGIE)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=42&annotation=ZCAPMGW8)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=42&annotation=WRYRS6JC)
