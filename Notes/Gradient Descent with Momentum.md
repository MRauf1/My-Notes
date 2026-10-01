---
tags:
  - computer_science
  - computer_vision
---

# Definition

> [!info] Definition 1 (Gradient Descent with Momentum)
> For $k=0, 1, ..., K$ steps and $\mathbf{v}$ initialized to $0$, do
> $$
> \begin{align}
> \mathbf{v}^{(k + 1)} \leftarrow \mu \mathbf{v}^k - \eta \nabla_{\theta} J(\theta^k) \\
> \theta^{(k + 1)} \leftarrow \theta^k + \mathbf{v}^{(k + 1)}
> \end{align}
> $$
> where $\eta$ is the [[Learning Rate|learning rate]] and $J$ is the [[Cost Function|cost function]].[^1]

In addition to the regular [[Gradient Descent]], this method adds a momentum hyperparameter $\mu$. The direction now is the [[Weighted Sum|weighted sum]] of the negative gradient direction and the previous direction vector.

Think of this algorithm as a skier descending down a snowy slope and accumulating momentum as they ski down.

# Properties
- Prince's (exponential moving average) form: $\mathbf{m}_{t+1} \leftarrow \beta \mathbf{m}_t + (1 - \beta)\sum_{i \in \mathcal{B}_t} \partial \ell_i[\boldsymbol{\phi}_t] / \partial \boldsymbol{\phi}$, $\boldsymbol{\phi}_{t+1} \leftarrow \boldsymbol{\phi}_t - \alpha \mathbf{m}_{t+1}$, with $\beta \in [0, 1)$ controlling how much the gradient is smoothed over time.[^2]
- The recursion makes each step an infinite weighted sum of all previous gradients, with weights decaying back in time: the effective learning rate grows when gradients are aligned over many iterations and shrinks when their direction keeps changing, giving a smoother trajectory and less oscillation in valleys.
- Variant: [[Nesterov Accelerated Momentum]].

[^1]: https://visionbook.mit.edu/gradient_descent.html
[^2]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
