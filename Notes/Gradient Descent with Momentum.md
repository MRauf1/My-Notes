---
tags: computer_science, computer_vision
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

[^1]: https://visionbook.mit.edu/gradient_descent.html