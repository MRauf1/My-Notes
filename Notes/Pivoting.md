---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Pivoting)[^1]
> In [[Gaussian Elimination]], pivoting means interchanging rows (and possibly columns) so that a suitable nonzero entry sits in the diagonal pivot position before computing the multipliers of stage $k$. Interchanging rows of both the matrix and the right-hand side does not change the solution.

Any nonzero pivot works in exact arithmetic. In finite precision the pivot should keep the multipliers small, so that earlier rounding errors are not amplified when each [[Elementary Elimination Matrix]] is applied. Larger pivots give smaller multipliers and hence smaller errors.[^2]

# Types
- [[Partial Pivoting]]
- [[Complete Pivoting]]

# Properties
- Pivot selection depends on entry magnitudes, so it depends on the [[Scaling of Linear System|scaling]] of the matrix. A diagonal scaling may produce a different pivot sequence, and any nonzero entry of a column can be made the largest by weighting its row heavily enough.[^3]
- [[Growth Factor]]
- [[Permutation Matrix]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=90)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=91)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=95)
