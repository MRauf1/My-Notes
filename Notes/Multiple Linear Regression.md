---
tags: computer_science, computer_vision
---

# Definition

> [!info] Definition 1 (Multiple Linear Regression)[^1]
> Model of the form $\hat{\mathbf{y}} = \mathbf{X} \mathbf{\theta}$, where $\mathbf{\theta}$ are the parameters.
> 
> The [[Cost Function|cost function]] is
> $$
> \begin{align}
> J(\mathbf{\theta}) = \sum_{i=1}^{N} L(f(\mathbf{x}^{(i)}), \mathbf{y}^{(i)}) = \\
> = \sum_{i=1}^{N} (\hat{\mathbf{y}}^{(i)} - \mathbf{y}^{(i)})^2 = \\
> = (\mathbf{y} - \mathbf{X} \mathbf{\theta})^T (\mathbf{y} - \mathbf{X} \mathbf{\theta})
> \end{align}
> $$
> 
> Calculating the [[Derivative|derivative]] and setting it [[Equality|equal]] to $0$, the optimal parameters are
> $$
> \begin{align}
> \theta^{\star} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}
> \end{align}
> $$

# Properties
## Coefficient Properties
- [[Multiple Linear Regression Hypothesis Test]]

[^1]: https://visionbook.mit.edu/intro_to_learning.html