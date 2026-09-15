---
tags:
  - computer_science
  - deep_learning
---

# Definition

> [!info] Definition
> $$
> \begin{align}
> \underset{f}{\mathrm{\arg \max}} [p(\{\mathbf{y}^{(i)}\}_{i=1}^N | \{\mathbf{x}^{(i)}\}_{i=1}^N, f)]
> \end{align}
> $$

Learning using [[Maximum Likelihood Estimation|MLE]].[^1] Trying to infer the hypothesis $f$ that assigns the highest [[Probability|probability]] to the data.

The term $p(\{\mathbf{y}^{(i)}\}_{i=1}^N | \{\mathbf{x}^{(i)}\}_{i=1}^N, f)$ being maximized is called the [[Likelihood Function|likelihood]] of the $\mathbf{y}$ values given the model $f$ and the observed $\mathbf{x}$ values.

# Properties
- Depending on the [[Loss Function|loss function]] used, [[Empirical Risk Minimization|ERM]] often has this maximum likelihood interpretation, since minimizing certain losses is equivalent to maximizing the corresponding likelihood.
- If the prediction errors $(\mathbf{y} - f(\mathbf{x}))$ are assumed [[Normal Distribution|Gaussian distributed]], maximum likelihood learning reduces to the least-squares objective.
- When a [[Bayes' Theorem|prior]] $p(f)$ is used together with the likelihood, the result is instead [[Maximum a Posteriori Learning|maximum a posteriori learning]].

[^1]: https://visionbook.mit.edu/intro_to_learning.html