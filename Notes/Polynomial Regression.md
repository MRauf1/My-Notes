---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Polynomial Regression)[^1]
> [[Linear Regression|Linear regression]] in which the [[Hypothesis Space]] is polynomial functions rather than linear functions,
> $$
> \begin{align}
> y = f_\theta(x) = \sum_{k=0}^K \theta_k x^k
> \end{align}
> $$
> where $K$, the degree of the polynomial, is a hyperparameter of the hypothesis space.

# Properties
- Via [[Featurization]], $\phi(x) = [1, x, x^2, \dots, x^K]^T$, $f_\theta$ becomes linear in $\theta$, $f_\theta(x) = \theta^T\phi(x)$, so polynomial regression reduces to a linear regression problem in the feature space, with the same closed-form optimizer.
- As $K$ increases, the model fits the training data increasingly well, but eventually [[Overfitting|overfits]]: the curve becomes wiggly enough to fit not just the true underlying relationship but also the noise in the training data, a property of the training data that does not generalize to test data.
- For large $K$, many hypotheses may fit the training data equally well, so there is insufficient data for the objective alone to uniquely identify the best hypothesis; which one the optimizer returns instead depends on details like initialization.

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
