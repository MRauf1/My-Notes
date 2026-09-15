---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Lp Regularization)[^1]
> A [[Regularization|regularizer]] that penalizes the $L_p$ [[Norm]] of a model's parameters $\theta$:
> $$
> \begin{align}
> R(\theta) = \lVert \theta \rVert_p
> \end{align}
> $$

# Properties
- For any $p$, the effect is to encourage most parameters to be zero, or near zero; when most parameters are zero, the learned function takes on a simpler, degenerate form.
- $p=2$ gives [[L2 Regularization]] (also known as Tikhonov regression, ridge regression, or, in neural networks, weight decay); $p=1$ gives [[L1 Regularization]] (also known as Lasso, in regression settings).
- An embodiment of [[Occam's Razor]]: when multiple functions can explain the data, this regularizer prefers the simplest.

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
