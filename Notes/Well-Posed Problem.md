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
- For a [[Partial Differential Equation]], the problem is the PDE in a domain together with [[Initial Condition|initial]] and/or [[Boundary Condition|boundary conditions]]; existence and uniqueness pick out exactly one solution, and stability means small changes in these data change the solution only a little.[^2]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=24)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=37&annotation=XVI7BG7D)
