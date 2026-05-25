---
tags: [mathematics, real_analysis]
---

# Definition

> [!info] Definition 1 ([[Sequence of Function]] Uniform Convergence)[^1]
> Let $(f_n)$ be a [[Sequence]] of [[Real-Valued Function]] defined on the [[Set]] $S \subseteq R$. The sequence $(f_n)$ converges uniformly on $S$ to a function $f$ defined on $S$ if for each $\epsilon > 0$, there exists $N(\epsilon)$ such that
> $$
> \begin{align}
> (\forall x \in S \land n > N) \implies |f_n(x) - f(x)| < \epsilon
> \end{align}
> $$

Value of $N$ depends only on $\epsilon > 0$. Stronger condition than [[Sequence of Function Pointwise Convergence]].

Unlike pointwise convergence, the "gap" between $(f_n)$ and $f$ must shrink at the same rate across the entire [[Domain]].

> [!info] Definition 2 (Alternative Definition)[^2]
> [[Sequence of Function]] $(f_n)$ on [[Set]] $S \subseteq \mathbb{R}$ converges uniformly to [[Function]] $f$ on $S$ if and only if
> $$
> \begin{align}
> \lim_{n \rightarrow \infty} \sup\{|f_n(x) - f(x)| : x \in S\} = 0
> \end{align}
> $$

# Types
- [[Sequence of Function Locally Uniform Convergence]]

# Properties
## Convergence
- Uniform convergence implies [[Sequence of Function Pointwise Convergence]]

## [[Continuity]]
- [[Uniform Limit of Continuous Functions Theorem]]

## [[Riemann Integral]]
- [[Uniform Limit of Integrals Theorem]]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=204)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=207)