---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Algebra of Sets[^1]
> Let $X$ be a nonempty [[Set]]. An algebra of sets on $X$ is a nonempty collection $\mathcal{A} \subseteq \mathcal{P}(X)$ that is closed under finite [[Set Union|unions]] and [[Set Complement|complements]]:
> $$
> \begin{align}
> E_1, \dots, E_n \in \mathcal{A} &\implies \bigcup_{j=1}^{n} E_j \in \mathcal{A}, \\
> E \in \mathcal{A} &\implies E^c \in \mathcal{A}.
> \end{align}
> $$
> Some authors call it a *field* of sets.

The finite version of a [[Sigma-Field|$\sigma$-algebra]]: it only guarantees closure under finitely many set operations. It is the natural domain of a [[Premeasure]].

# Types
- [[Sigma-Field|$\sigma$-algebra]]: an algebra closed under countable unions.
- [[Ring of Sets]]: drops the requirement that $X$ belongs to the family.

# Properties
- Closed under finite [[Set Intersection|intersections]], since $\bigcap_j E_j = \left(\bigcup_j E_j^c\right)^c$ ([[DeMorgan's Laws]]).[^2]
- $\emptyset, X \in \mathcal{A}$: for any $E \in \mathcal{A}$, $\emptyset = E \cap E^c$ and $X = E \cup E^c$.[^2]
- An algebra is a $\sigma$-algebra as soon as it is closed under countable **disjoint** unions.[^3] Given $\{E_j\}_{1}^{\infty} \subseteq \mathcal{A}$, the **disjointification**
$$
\begin{align}
F_k = E_k \setminus \left[\bigcup_{j=1}^{k-1} E_j\right] = E_k \cap \left[\bigcup_{j=1}^{k-1} E_j\right]^c
\end{align}
$$
  gives [[Disjoint Sets|disjoint]] sets $F_k \in \mathcal{A}$ with $\bigcup_1^\infty F_k = \bigcup_1^\infty E_j$. This device of replacing a sequence of sets by a disjoint sequence recurs throughout measure theory.
- The finite disjoint unions of members of an [[Elementary Family]] form an algebra.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=34&annotation=TYRWDLKR)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=34&annotation=VYZZLXB8)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=34&annotation=2E938DT7)
