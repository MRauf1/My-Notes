---
tags: mathematics, real_analysis
---

# Definition

> [!info] Definition 1 (Cauchy [[Sequence]])[^1]
> Sequence $(s_n)$ is a Cauchy sequence if for all $\epsilon > 0$, there exists a number $N$ such that
> $$
> \begin{align}
> m, n > N \implies |s_n - s_m| < \epsilon
> \end{align}
> $$

> [!info] Definition 2 (Cauchy [[Sequence]] using [[Metric Space]])[^2]
> Given a [[Metric Space]] $(S, d)$, [[Sequence]] $(s_n) \in S$ is a Cauchy sequence if for each $\epsilon > 0$, there exists $N$ such that
> $$
> \begin{align}
> m, n > N \implies d(s_m, s_n) < \epsilon
> \end{align}
> $$

# Types
- [[High Dimensional Real Cauchy Sequence]]

# Properties
## [[Convergent Sequence]]
- [[Convergent Sequence is Cauchy Sequence]]

## [[Bounded Sequence]]
- [[Cauchy Sequence Boundedness]]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=74)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=97)