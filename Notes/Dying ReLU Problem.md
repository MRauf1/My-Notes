---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Dying ReLU Problem[^1]
> Since $\frac{d}{dz}\mathrm{ReLU}[z] = 0$ for $z < 0$, if every training example produces a negative pre-activation at a given [[ReLU Function|ReLU]] unit, the gradient with respect to its incoming weights is locally flat and those parameters cannot be improved by [[Gradient Descent]].

# Properties
- Motivates ReLU variants with nonzero gradient for negative inputs: [[Leaky ReLU]], [[Parametric ReLU]], [[Concatenated ReLU]], and smooth functions such as [[Softplus Function|softplus]], [[Gaussian Error Linear Unit|GELU]], [[Swish Function|SiLU]], and [[Exponential Linear Unit|ELU]], most of which also limit the gradient for negative values.[^2]
- A cause of dead neurons among the [[ReLU Function Downsides]].

[^1]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=QC3TLEG7)
[^2]: [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=35695IHL)
