---
tags: computer_science, computer_vision
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

Gradient descent finds the [[Gradient|gradient]] of the cost function with respect to the parameters. The negative gradient then gives the direction of the steepest descent. We take that direction with the step being equal to the learning rate times the gradient magnitude.

With a random initialization of the parameter vector $\theta^0$ and a sufficiently small learning rate, the algorithm is guaranteed(?) to converge to a local minimum as $K \rightarrow \infty$.

Since gradient descent uses gradients, the cost function (and the preceding functions if using backpropagation) should ideally be [[Differentiable|differentiable]]. However, even non-differentiable functions can work as long as they have the property that one can get a meaningful signal of how to perturb the model's parameters in order to reduce the loss function. In particular, [[PyTorch|PyTorch]] uses the one-sided [[Derivative|derivative]] at the [[Discontinuity|discontinuities]].

# Potential Problems
- [[Vanishing Gradients|Vanishing Gradients]]
- [[Exploding Gradients|Exploding Gradients]]
- [[Suboptimal Local Minimum|Suboptimal Local Minimum]]

# Types
- [[Stochastic Gradient Descent|Stochastic Gradient Descent]]

#TODO 
- Is it guaranteed to converge?

[^1]: https://visionbook.mit.edu/gradient_descent.html