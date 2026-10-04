---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Connected [[Metric Space]])[^1]
> [[Subset]] $E$ of [[Metric Space]] $(S, d)$ is connected if it is not [[Disconnected Metric Space]]

> [!info] Definition 2 (Connected [[Metric Space]])
> [[Subset]] $E \subseteq S$ is connected if for all $O_1, O_2$ [[Open Set]] in $S$,
> $$
> \begin{align}
> (S \subseteq O_1 \cup O_2 \land O_1 \cap O_2 \neq \emptyset) \implies (S \subseteq O_1 \lor S \subseteq O_2)
> \end{align}
> $$

# Types
- [[Path Connected Metric Space]]

> [!abstract] Theorem 3 (Connected Metric Spaces with $\geq 2$ Points are Uncountable)[^3]
> Let $(S, d)$ be a connected [[Metric Space]] with at least two points. Then $S$ is [[Uncountable Set|uncountable]].

# Properties
- [[Connected Metric Space Continuous Function Theorem]]
- Equivalently, $E$ is connected if and only if $E$ is not the union of two nonempty [[Separated Sets]].[^2]
- [[Connected Subset of Real Line Theorem]]
- Every [[Path Connected Metric Space|path connected]] set is connected, but not conversely — see [[Path Connected Metric Space]].

[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=51)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=53)

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=190)