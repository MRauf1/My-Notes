---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Well-Posed Problem)[^1]
> A mathematical problem is well-posed if a solution exists, is unique, and depends continuously on the problem data.

The continuity condition means a small change in the problem data does not cause an abrupt, disproportionate change in the solution. This is especially important for numerical computations, where such perturbations are usually inevitable.

# Properties
- A well-posed problem may still be highly [[Sensitivity|sensitive]] (ill-conditioned) to perturbations in the problem data, even though it responds continuously.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=24)
