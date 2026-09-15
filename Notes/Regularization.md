---
tags:
  - computer_science
  - computer_vision
---

# Definition

Mechanisms that penalize [[Function Complexity|function complexity]] in order to reduce/prevent [[Overfitting|overfitting]].[^1]

These are additional [[Term|terms]] added to the [[Objective Function|objective function]] that guides towards simpler [[Function|functions]]. Ideally, one wants a function that is complex enough to fit the data, while not too complex/flexible as to cause overfitting.

They embody the principle of [[Occam's Razor]]: when multiple functions can fit the data, choose the simplest one.

Regularizers can also be thought of as [[Bayes' Theorem|priors]] for the types of functions that are to be selected (hypothesis).

The general form of a regularized objective is
$$
\begin{align}
J(\theta) = \frac{1}{N}\sum_{i=1}^N \mathcal{L}(f_\theta(x)^{(i)}, y^{(i)}) + \lambda R(\theta)
\end{align}
$$
where the first term is the data-fit loss, $R(\theta)$ is the regularizer, and $\lambda$ is a hyperparameter controlling the strength of the regularization.

# Types

- [[Lp Regularization|$L_p$ Norms]]
	- These encourage most parameters to be $0$/near $0$.
	- $p=2$: [[L2 Regularization]] (Tikhonov/ridge regression, or weight decay in neural networks).
	- $p=1$: [[L1 Regularization]] (Lasso).

# Properties
- Used in [[Regularized Image Reconstruction]] to recover a well-behaved scene estimate $\ell_w$ from a camera's sensor measurements $\ell_s$ when the camera's [[Imaging Matrix]] is non-invertible or ill-conditioned.

[^1]: https://visionbook.mit.edu/problem_of_generalization.html