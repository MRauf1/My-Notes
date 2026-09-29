---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Parametric ReLU[^1]
> A generalization of the [[Leaky ReLU]] (He et al., 2015) that treats the negative-side slope $\alpha$ as a learned parameter:
> $$
> \begin{align}
> \mathrm{PReLU}[z] = \begin{cases} \alpha z & z < 0 \\ z & z \geq 0 \end{cases}
> \end{align}
> $$

# Properties
- Reduces to the [[ReLU Function|ReLU]] for $\alpha = 0$ and to the [[Leaky ReLU]] for a fixed small $\alpha$.
- Avoids the [[Dying ReLU Problem]] and can give minor performance gains over ReLU in particular situations.

[^1]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=QC3TLEG7)
