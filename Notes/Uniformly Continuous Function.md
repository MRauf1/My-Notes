---
tags: mathematics, real_analysis
---

# Definition

> [!info] Definition 1 (Uniformly Continuous [[Function]])[^1]
> Function $f$ is uniformly continuous on set $S$ if for each $\epsilon > 0$, there exists $\delta > 0$ such that
> $$
> \begin{align}
> x, y \in S \land |x - y| < \delta \implies |f(x) - f(y)| < \epsilon
> \end{align}
> $$

$\delta$ only depends on $\epsilon$, not $x_0$.

It is defined for a set (like the domain), not for a point.

All uniformly continuous functions are also [[Continuous Function]].

> [!info] Definition 2 (Uniformly Continuous [[Function]] on [[Metric Space]])[^2]
> Given [[Metric Space]] $(S_1, d_1), (S_2, d_2)$, a [[Function]] $f: S_1 \rightarrow S_2$ is uniformly continuous at $E \subseteq S_1$ if for each $\epsilon > 0$, there exists $\delta > 0$ such that
> $$
> \begin{align}
> s, t \in E \land d_1(s, t) < \delta \implies d_2(f(s), f(t)) < \epsilon
> \end{align}
> $$

# Properties
- [[Continuous to Uniformly Continuous Theorem]]
- [[Uniformly Continuous Function Cauchy Sequence Theorem]]
- [[Uniformly Continuous Function Extension of Function Theorem]]
- [[Uniformly Continuous Function Interval Theorem]]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=151)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=175)