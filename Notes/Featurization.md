---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Featurization)[^1]
> Representing each raw datapoint $x$ with a feature vector $\phi(x)$, chosen so that a model that is nonlinear in $x$ becomes linear in the parameters when expressed in terms of $\phi(x)$.

# Properties
- For [[Polynomial Regression]], $f_\theta(x) = \sum_{k=0}^K \theta_k x^k = \theta^T\phi(x)$ with $\phi(x) = [1, x, x^2, \dots, x^K]^T$, turning the polynomial regression problem into a [[Linear Regression|linear regression]] problem in the feature space.
- Stacking the featurized datapoints as rows produces a [[Data Matrix]].

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
