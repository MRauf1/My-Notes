---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!abstract] Theorem 1.14 (Carathéodory / Hahn–Kolmogorov Extension Theorem)[^1]
> Let $\mathcal{A} \subseteq \mathcal{P}(X)$ be an [[Algebra of Sets|algebra]], $\mu_0$ a [[Premeasure]] on $\mathcal{A}$, and $\mathcal{M}$ the [[Generated Sigma-Algebra|$\sigma$-algebra generated]] by $\mathcal{A}$. There exists a [[Measure (Measure Theory)|measure]] $\mu$ on $\mathcal{M}$ whose restriction to $\mathcal{A}$ is $\mu_0$, namely $\mu = \mu^*|_\mathcal{M}$ where $\mu^*$ is the induced [[Outer Measure]]
> $$
> \begin{align}
> \mu^*(E) = \inf\left\{\sum_{j=1}^\infty \mu_0(A_j) : A_j \in \mathcal{A},\ E \subseteq \bigcup_{j=1}^\infty A_j\right\}.
> \end{align}
> $$
> If $\nu$ is another measure on $\mathcal{M}$ extending $\mu_0$, then $\nu(E) \leq \mu(E)$ for all $E \in \mathcal{M}$, with equality when $\mu(E) < \infty$. If $\mu_0$ is [[Sigma-Finite Measure|$\sigma$-finite]], then $\mu$ is the **unique** extension of $\mu_0$ to a measure on $\mathcal{M}$.

The construction pipeline of measure theory:
$$
\begin{align}
\text{premeasure } \mu_0 \text{ on } \mathcal{A} \xrightarrow{\text{inf over covers}} \text{outer measure } \mu^* \text{ on } \mathcal{P}(X) \xrightarrow{\text{Carathéodory restriction}} \text{measure } \mu.
\end{align}
$$

# Properties
- The proof yields more: $\mu_0$ extends to a measure on the larger $\sigma$-algebra $\mathcal{M}^*$ of all $\mu^*$-measurable sets ([[Carathéodory's Theorem]]), and this extension is complete.[^2] For $\sigma$-finite $\mu_0$, $\mathcal{M}^*$ is the [[Measure Completion Theorem|completion]] of $\mathcal{M}$.
- The outer measures induced by $\mu_0$ and by $\mu$ coincide.[^2]
- Constructs every [[Lebesgue-Stieltjes Measure]], in particular [[Lebesgue Measure]], from lengths of h-intervals.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=44&annotation=CBRMACQ5)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=45&annotation=I9LL639W)
