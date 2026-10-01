---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] AdaGrad[^1]
> An adaptive optimizer (Duchi et al., 2011) that assigns each parameter its own learning rate, attenuated by the cumulative squared gradient of that parameter:
> $$
> \begin{align}
> \mathbf{v}_{t+1} &\leftarrow \mathbf{v}_t + \left(\frac{\partial L[\boldsymbol{\phi}_t]}{\partial \boldsymbol{\phi}}\right)^2 \\
> \boldsymbol{\phi}_{t+1} &\leftarrow \boldsymbol{\phi}_t - \alpha \cdot \frac{\partial L[\boldsymbol{\phi}_t] / \partial \boldsymbol{\phi}}{\sqrt{\mathbf{v}_{t+1}} + \epsilon}
> \end{align}
> $$
> with pointwise squares, roots, and division.

# Properties
- Addresses the possibility that some parameters must move further than others.
- Since $\mathbf{v}_t$ only grows, the effective learning rates decrease over time and learning can halt before the minimum is found; [[RMSProp]] and AdaDelta fix this by recursively (exponentially) averaging the squared gradient instead.

[^1]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
