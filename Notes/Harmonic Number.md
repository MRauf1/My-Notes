---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] $k$-th Harmonic Number[^1]
> For a non-negative integer $k$, $$H_k = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{k}.$$

$H_k$ has no simple closed form, but is closely related to the [[Logarithm|natural logarithm]] of $k$: $$\ln k < H_k \leq \ln k + 1.$$

# Properties
- These bounds follow from interpreting $\int_1^k \frac{1}{x}\, dx = \ln k$ as the area between the curve $1/x$ and the $x$-axis: this area lower-bounds $H_k$ and $1 + \int_1^k \frac{1}{x}\, dx$ upper-bounds it.[^2]
- Used to express the expected search-path length in a [[Random Binary Search Tree]] and in a [[Treap]].

[^1]: [Morin, p. 146](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 147](zotero://select/library/items/HYS8NDAB)
