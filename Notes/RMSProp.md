---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] RMSProp[^1]
> An adaptive optimizer (Hinton et al., 2012) that normalizes each parameter's step by an exponential moving average of its squared gradient:
> $$
> \begin{align}
> \mathbf{v}_{t+1} &\leftarrow \gamma \cdot \mathbf{v}_t + (1 - \gamma)\left(\frac{\partial L[\boldsymbol{\phi}_t]}{\partial \boldsymbol{\phi}}\right)^2 \\
> \boldsymbol{\phi}_{t+1} &\leftarrow \boldsymbol{\phi}_t - \alpha \cdot \frac{\partial L[\boldsymbol{\phi}_t] / \partial \boldsymbol{\phi}}{\sqrt{\mathbf{v}_{t+1}} + \epsilon}
> \end{align}
> $$

# Properties
- Modifies [[AdaGrad]] by recursively updating the squared-gradient term, so old gradients are forgotten and the learning rate does not decay to zero; AdaDelta (Zeiler, 2012) is a similar fix.
- [[Adam]] is RMSProp plus momentum on the gradient and bias correction.

[^1]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
