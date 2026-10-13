---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 ([[Continuous Function]] Component Theorem)[^1]
> 1) Let $f_1, \dots, f_k$ be real functions on a [[Metric Space]] $X$, and let $\mathbf{f}: X \rightarrow \mathbb{R}^k$ be defined by
> $$
> \begin{align}
> \mathbf{f}(x) = (f_1(x), \dots, f_k(x)) \quad (x \in X)
> \end{align}
> $$
> Then $\mathbf{f}$ is continuous if and only if each of $f_1, \dots, f_k$ is continuous.
> 2) If $\mathbf{f}, \mathbf{g}$ are continuous mappings of $X$ into $\mathbb{R}^k$, then $\mathbf{f} + \mathbf{g}$ and $\mathbf{f} \cdot \mathbf{g}$ are continuous on $X$.

The functions $f_1, \dots, f_k$ are the components ([[Coordinate Function|coordinate functions]]) of $\mathbf{f}$. $\mathbf{f} + \mathbf{g}$ maps into $\mathbb{R}^k$, whereas $\mathbf{f} \cdot \mathbf{g}$ ([[Dot Product]]) is a real function on $X$.

# Properties
- Reduces continuity of [[Real Vector-Valued Function|vector-valued functions]] to continuity of real functions, e.g. [[Continuous Function Addition Rule]], [[Continuous Function Product Rule]].
- Follows from $|f_j(x) - f_j(y)| \leq |\mathbf{f}(x) - \mathbf{f}(y)| = \left(\sum_{i=1}^k |f_i(x) - f_i(y)|^2\right)^{1/2}$.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=96)
