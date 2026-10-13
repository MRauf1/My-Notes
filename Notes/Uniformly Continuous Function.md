---
tags:
  - mathematics
  - real_analysis
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

Continuity can be defined at a single point, while uniform continuity is a property of a function on a set; asking whether a function is uniformly continuous at a point is meaningless. For a continuous $f$ on $X$, $\delta$ depends on $\epsilon$ and on $p$; for a uniformly continuous $f$, one $\delta$ works for all $p \in X$.[^3]

> [!info] Definition 3 (Diameter Formulation)[^4]
> $f: X \rightarrow Y$ is uniformly continuous if and only if for every $\epsilon > 0$ there exists $\delta > 0$ such that $\operatorname{diam} f(E) < \epsilon$ for all $E \subseteq X$ with $\operatorname{diam} E < \delta$ ([[Diameter (Metric Space)]]).

# Properties
- [[Continuous to Uniformly Continuous Theorem]]
- [[Uniformly Continuous Function Cauchy Sequence Theorem]]
- [[Uniformly Continuous Function Extension of Function Theorem]]
- [[Uniformly Continuous Function Interval Theorem]]
- [[Uniformly Continuous Function Composition]]
- On a non-compact bounded subset of $\mathbb{R}$, continuity does not imply uniform continuity: [[Noncompact Subset of Real Line Continuous Function Theorem]]

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=151)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=175)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=99)
[^4]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=108)
