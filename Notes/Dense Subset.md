---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Dense [[Subset]])[^1]
> Let $S$ be a [[Metric Space]]. A [[Subset]] $D \subseteq S$ is dense in $S$ if every non-empty [[Open Set]] $U \subseteq S$ (open in $S$) intersects $D$, i.e., $D \cap U \neq \emptyset$.

> [!info] Definition 2 (Dense Subset via Limit Points)[^2]
> Let $(X, d)$ be a [[Metric Space]] and $E \subseteq X$. $E$ is dense in $X$ if every point of $X$ is a [[Limit Point]] of $E$, or a point of $E$ (or both), i.e., $X = E \cup E'$, where $E'$ is the set of limit points of $E$.

> [!info] Definition 3 (Dense Subset via Closure)[^3][^4]
> Let $X$ be a topological space. A [[Subset]] $A \subseteq X$ is dense in $X$ if its [[Closure Set|closure]] equals the entire space:
> $$\begin{align}
> \overline{A} = X
> \end{align}$$

# Properties
- Definitions 1, 2, and 3 are equivalent in a [[Metric Space]], since the [[Closure Set|closure]] satisfies $\overline{E} = E \cup E'$.
- Definition 3 is the general case. Definition 1 is equivalent to it in any topological space. Definition 2 is its specialization to [[Metric Space|metric spaces]].
- A [[Metric Space]] containing a [[Countable Set|countable]] dense subset is a [[Separable Metric Space]].
- Contrast with [[Nowhere Dense Subset]].

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=182)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=41)
[^3]: [Dense set - Wikipedia](https://en.wikipedia.org/wiki/Dense_set)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=26&annotation=LJPIER49)
