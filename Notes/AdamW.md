---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] AdamW[^1]
> A variant of [[Adam]] (Loshchilov & Hutter, 2019) that decouples weight decay from the adaptive gradient update, applying it directly to the parameters:
> $$
> \begin{align}
> \boldsymbol{\phi}_{t+1} \leftarrow \boldsymbol{\phi}_t - \alpha\left(\frac{\tilde{\mathbf{m}}_{t+1}}{\sqrt{\tilde{\mathbf{v}}_{t+1}} + \epsilon} + \lambda \boldsymbol{\phi}_t\right)
> \end{align}
> $$
> where $\lambda$ is the weight-decay coefficient.

# Properties
- Substantially improves Adam's performance in the presence of [[L2 Regularization]]: adding the L2 penalty to the loss in Adam rescales its gradient by $1/\sqrt{\tilde{\mathbf{v}}}$, so parameters with large gradient histories are regularized less, whereas decoupled decay shrinks all weights at the same rate.[^2]
- For plain [[Stochastic Gradient Descent|SGD]], L2 regularization and weight decay coincide; they differ only for adaptive methods.

[^1]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
[^2]: Explanation of the mechanism added from general knowledge of Loshchilov & Hutter (2019).
