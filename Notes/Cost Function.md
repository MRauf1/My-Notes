---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Cost Function)[^1]
> A function $J$ mapping some arbitrary input to a scalar cost. In a learning problem, the domain of $J$ is the training data and the parameters $\theta$; treating the training data as fixed, $J$ is denoted as a function of the parameters alone, $J(\theta)$, and the learning goal is to solve
> $$
> \begin{align}
> \theta^* = \underset{\theta}{\arg\min}\ J(\theta)
> \end{align}
> $$

# Properties
- Also called the [[Loss Function|loss]] or [[Objective Function|objective function]] when it scores a model's predictions against training data.
- More properly, the cost is the overall quantity minimized (e.g. the sum of per-datapoint [[Loss Function|losses]]), and may include additional terms not associated with individual data points, such as [[Regularization]] terms.[^2]
- Nearly all optimizers solve for $\theta^*$ by an iterative process: at each [[Operating Point]], an update function views some information about the cost's landscape, such as its value or [[Gradient Vector|gradient]], and uses it to move to a better operating point.

[^1]: [MIT Vision Book - Gradient Descent](https://visionbook.mit.edu/gradient_descent.html)
[^2]: [Prince, p. 23](zotero://open-pdf/library/items/BWT7FYX5?page=37&annotation=HMJPP2DF)
