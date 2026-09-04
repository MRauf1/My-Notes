---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Stable Algorithm)[^1]
> An algorithm is stable if the result it produces is relatively insensitive to perturbations due to approximations made during the computation. Equivalently, from the viewpoint of backward error analysis, an algorithm is stable if the result it produces is the exact solution to a nearby problem, i.e. the effect of perturbations during the computation is no worse than the effect of a small amount of data error in the input.

Stability is concerned with [[Computational Error]], in contrast to [[Sensitivity]] (conditioning), which is concerned with [[Propagated Data Error]].

A weaker notion of stability, useful in some contexts, only requires that the algorithm produce nearly the correct result for nearly the correct problem, rather than exactly the correct result for a nearby problem.

# Properties
- A stable algorithm applied to a well-conditioned problem yields an [[Accuracy|accurate]] solution.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=37)
