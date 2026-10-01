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
- As a deep-learning loss, see the [[Maximum Likelihood Loss Function Recipe]]: the network predicts the parameters of a chosen output distribution and minimizes the negative log-likelihood; its optimality and pitfalls are covered in [[Maximum Likelihood Loss Optimality and Failure Modes]].[^3]
- Depending on the [[Loss Function|loss function]] used, [[Empirical Risk Minimization|ERM]] often has this maximum likelihood interpretation, since minimizing certain losses is equivalent to maximizing the corresponding likelihood.
- If the prediction errors $(\mathbf{y} - f(\mathbf{x}))$ are assumed [[Normal Distribution|Gaussian distributed]], maximum likelihood learning reduces to the least-squares objective.
- In the machine learning literature, the negative log likelihood is called an **error function**; since $-\ln$ is monotonically decreasing, maximizing the likelihood is equivalent to minimizing the error.[^2] See [[Probabilistic Formulation of Regression]] for the correspondence between noise models and losses.
- When a [[Bayes' Theorem|prior]] $p(f)$ is used together with the likelihood, the result is instead [[Maximum a Posteriori Learning|maximum a posteriori learning]].

- Compared with MAP in [[Maximum Likelihood vs Maximum a Posteriori Estimation]].

[^1]: https://visionbook.mit.edu/intro_to_learning.html
[^2]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=4KU9QTLZ)
[^3]: [Prince, Ch. 5](zotero://select/library/items/T3V9WVXD)
