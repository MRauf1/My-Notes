---
tags:
  - computer_science
  - computer_vision
---

# Definition

> [!info] Definition 1 (Gradient Descent)
> For $k=0, 1, ..., K$ steps, do
> $$
> \begin{align}
> \theta^{(k + 1)} \leftarrow \theta^k - \eta \nabla_{\theta} J(\theta^k)
> \end{align}
> $$
> where $\eta$ is the [[Learning Rate|learning rate]] and $J$ is the [[Cost Function|cost function]].[^1]

Gradient descent finds the [[Gradient Vector|gradient]] of the cost function with respect to the parameters. The negative gradient then gives the direction of the steepest descent. We take that direction with the step being equal to the learning rate times the gradient magnitude.

With a random initialization of the parameter vector $\theta^0$ and a sufficiently small learning rate, the algorithm is guaranteed to converge to the global minimum as $K \rightarrow \infty$ if $J$ is [[Convex Function|convex]]. For a non-convex $J$ (the typical case for neural networks), it is only guaranteed to converge to a stationary point, which may be a local minimum, [[Saddle Point|saddle point]], or local maximum.

Since gradient descent uses gradients, the cost function (and the preceding functions if using backpropagation) should ideally be [[Differentiable Function|differentiable]]. However, even non-differentiable functions can work as long as they have the property that one can get a meaningful signal of how to perturb the model's parameters in order to reduce the loss function. In particular, [[PyTorch|PyTorch]] uses the one-sided [[Derivative|derivative]] at the [[Discontinuity|discontinuities]].

# Properties
- A [[Gradient-Based Learning|gradient-based]], or [[First-Order Optimization|first-order optimization]] method: at each [[Operating Point]], it observes the gradient of the [[Cost Function]] and uses it to move to a new operating point with lower cost, in contrast to [[Zeroth-Order Optimization]], which observes only the cost's value, and [[Higher-Order Optimization]], which also uses curvature information such as the [[Hessian Matrix]].
- The learning rate is often varied during training according to a [[Learning Rate Schedule]] rather than held fixed.

# Potential Problems
- [[Vanishing Gradients|Vanishing Gradients]]
- [[Exploding Gradients|Exploding Gradients]]
- [[Suboptimal Local Minimum|Suboptimal Local Minimum]]

# Types
- [[Stochastic Gradient Descent|Stochastic Gradient Descent]]

[^1]: https://visionbook.mit.edu/gradient_descent.html