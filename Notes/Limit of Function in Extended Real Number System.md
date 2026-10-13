---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 ([[Limit of Function]] in [[Extended Real Number Set|Extended Real Number System]])[^1]
> Let $f$ be a real function defined on $E \subseteq \mathbb{R}$. We say that
> $$
> \begin{align}
> f(t) \rightarrow A \quad \text{as } t \rightarrow x
> \end{align}
> $$
> where $A$ and $x$ are in the [[Extended Real Number Set|extended real number system]], if for every neighborhood $U$ of $A$ there is a neighborhood $V$ of $x$ such that $V \cap E$ is not empty, and such that $f(t) \in U$ for all $t \in V \cap E$, $t \neq x$.

When $A$ and $x$ are real, this coincides with the metric-space definition of [[Limit of Function]]. Neighborhoods of $\pm\infty$ are the rays $(c, +\infty)$ and $(-\infty, c)$, so the definition unifies [[Limit of Function at Infinity]] and [[Infinite Limit of Function]].

> [!abstract] Theorem 2 (Arithmetic of Limits in Extended Reals)[^2]
> Let $f, g$ be defined on $E \subseteq \mathbb{R}$, and suppose $f(t) \rightarrow A$, $g(t) \rightarrow B$ as $t \rightarrow x$. Then
> 1) $f(t) \rightarrow A'$ implies $A' = A$;
> 2) $(f + g)(t) \rightarrow A + B$;
> 3) $(fg)(t) \rightarrow AB$;
> 4) $(f / g)(t) \rightarrow A / B$,
>
> provided the right-hand sides of 2), 3), and 4) are defined.

$\infty - \infty$, $0 \cdot \infty$, $\infty / \infty$, and $A / 0$ are not defined ([[Extended Real Number Set]]).

# Properties
- Analogue of [[Limit of Function Addition Law]], [[Limit of Function Product Law]], [[Limit of Function Quotient Law]], and uniqueness of limits ([[Limit of Function Sequential Characterization]]).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=106)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=107)
