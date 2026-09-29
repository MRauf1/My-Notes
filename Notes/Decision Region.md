---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Decision Region[^1]
> A rule assigning each input $\mathbf{x}$ to one of $K$ classes divides the input space into decision regions $\mathcal{R}_1, \dots, \mathcal{R}_K$, one per class, such that all points in $\mathcal{R}_k$ are assigned to class $\mathcal{C}_k$. The boundaries between decision regions are the [[Decision Boundary|decision boundaries]] (decision surfaces).

# Properties
- A decision region need not be contiguous; it may consist of several disjoint regions.[^1]
- The regions are chosen to optimize a decision criterion, e.g. the [[Minimum Misclassification Rate Decision Rule]] or the [[Minimum Expected Loss Decision Rule]]; because each $\mathbf{x}$ can be assigned independently, the optimal regions are determined pointwise.
- With the [[Reject Option]], part of the input space is assigned to no class.

[^1]: [Bishop, 2006, p. 39](zotero://open-pdf/library/items/5G99AZ8U?page=59&annotation=KGXFVQI9)
