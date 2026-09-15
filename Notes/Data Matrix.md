---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Data Matrix)[^1]
> An array $\Phi$ whose columns are the features of each datapoint and whose rows correspond to datapoints, generalizing the raw data matrix $\mathbf{X}$ of a [[Linear Regression|linear regression]] problem to an arbitrary [[Featurization|feature representation]] of each datapoint.

# Properties
- For [[Polynomial Regression]] of degree $K$, the data matrix is $\Phi = [\phi(x^{(i)})]_{i=1}^N$ with rows $[1, x^{(i)}, (x^{(i)})^2, \dots, (x^{(i)})^K]$, so that the learning problem and closed-form optimizer look identical to those of $L_2$ linear regression in this feature space.
- A [[Machine Learning|neural network]] can be viewed as a sequence of transformations of an input data matrix into increasingly more powerful feature representations, i.e., a sequence of better and better data matrices.

[^1]: [MIT Vision Book - The Problem of Generalization](https://visionbook.mit.edu/problem_of_generalization.html)
