---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Nesterov Accelerated Momentum[^1]
> A variant of [[Gradient Descent with Momentum|momentum]] that evaluates the gradient at the point predicted by the momentum step rather than at the current point:
> $$
> \begin{align}
> \mathbf{m}_{t+1} &\leftarrow \beta \cdot \mathbf{m}_t + (1 - \beta) \sum_{i \in \mathcal{B}_t} \frac{\partial \ell_i[\boldsymbol{\phi}_t - \alpha\beta \cdot \mathbf{m}_t]}{\partial \boldsymbol{\phi}} \\
> \boldsymbol{\phi}_{t+1} &\leftarrow \boldsymbol{\phi}_t - \alpha \cdot \mathbf{m}_{t+1}
> \end{align}
> $$

# Properties
- The momentum term is a coarse prediction of where the algorithm will move next; the gradient term then corrects the path provided by momentum alone.
- Incorporated into [[Adam]] as NAdam (Dozat, 2016).

[^1]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
