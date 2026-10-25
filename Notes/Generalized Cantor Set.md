---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Generalized Cantor Set[^1]
> For a bounded interval $I$ and $\alpha \in (0, 1)$, the **open middle $\alpha$th** of $I$ is the open interval with the same midpoint as $I$ and length $\alpha$ times that of $I$. Given a sequence $\{\alpha_j\}_1^\infty \subseteq (0, 1)$, let $K_0 = [0, 1]$ and obtain $K_j$ by removing the open middle $\alpha_j$th from each interval making up $K_{j-1}$. The limiting set
> $$
> \begin{align}
> K = \bigcap_{j=1}^\infty K_j
> \end{align}
> $$
> is a generalized Cantor set.

The ordinary [[Cantor Set]] is the case $\alpha_j = \tfrac{1}{3}$ for all $j$.

# Properties
- Shares the topological and cardinality properties of the Cantor set: compact, [[Nowhere Dense Subset|nowhere dense]], totally disconnected, without [[Isolated Point|isolated points]], and of [[Cardinality of the Continuum|cardinality]] $\mathfrak{c}$.[^1]
- Its [[Lebesgue Measure]] is an infinite product:[^1]
$$
\begin{align}
m(K_j) = (1 - \alpha_j)\, m(K_{j-1}) \implies m(K) = \prod_{j=1}^\infty (1 - \alpha_j) = \lim_{n \to \infty} \prod_{j=1}^n (1 - \alpha_j).
\end{align}
$$
- If all $\alpha_j = \alpha$ are equal, $m(K) = 0$. If $\alpha_j \to 0$ fast enough ($\sum \alpha_j < \infty$), $m(K) > 0$, and for any $\beta \in (0, 1)$ the $\alpha_j$ can be chosen so that $m(K) = \beta$ ("fat Cantor set").
- Gives nowhere dense ("topologically small") sets of positive measure ("measure-theoretically large").

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=52&annotation=34XWJBJ3)
