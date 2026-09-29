---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Leaky ReLU[^1]
> A variant of the [[ReLU Function|ReLU]] (Maas et al., 2013) that is linear with a smaller slope for negative inputs:
> $$
> \begin{align}
> \mathrm{LReLU}[z] = \begin{cases} \alpha z & z < 0 \\ z & z \geq 0 \end{cases}
> \end{align}
> $$
> with a fixed small slope, e.g. $\alpha = 0.1$.

# Properties
- Its nonzero negative-side gradient avoids the [[Dying ReLU Problem]].
- Special case of the [[Parametric ReLU]] with $\alpha$ fixed rather than learned.
- Can give minor performance gains over ReLU in particular situations.

[^1]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=QC3TLEG7)
