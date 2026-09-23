---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!abstract] Theorem 1 (Woodbury Formula)[^1]
> For $U, V \in \mathbb{R}^{n \times k}$,
> $$
> \begin{align}
> (A - UV^T)^{-1} = A^{-1} + A^{-1}U\,(I - V^T A^{-1} U)^{-1}\, V^T A^{-1}
> \end{align}
> $$
> This gives the inverse of a rank-$k$ modification of $A$.

The [[Sherman-Morrison Formula]] is the special case $k = 1$.

# Properties
- [[Sherman-Morrison Formula]]
- [[Matrix Inverse]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=102)
