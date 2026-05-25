---
tags: [mathematics, real_analysis]
---

# Definition

> [!info] Definition 1 ([[Sequence of Function]] Pointwise [[Convergence]])[^1]
> Let $(f_n)$ be a [[Sequence]] of [[Real-Valued Function]] defined on the [[Set]] $S \subseteq R$. The sequence $(f_n)$ converges pointwise (i.e., at each point) to a function $f$ defined on $S$ if $\lim_{n \rightarrow \infty} f_n(x) = f(x)$ for all $x \in S$.
> Alternatively, it means that for each $\epsilon > 0$ and for each $x \in S$, there exists $N(x, \epsilon)$ such
> $$
> \begin{align}
> n > N \implies |f_n(x) - f(x)| < \epsilon
> \end{align}
> $$

Value of $N$ depends on both $\epsilon > 0$ and $x \in S$.

As such, points may converge at different rates to their limits, which can create [[Discontinuity]].

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=203)