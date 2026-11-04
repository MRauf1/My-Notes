---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Multinomial Distribution]] [[Maximum Likelihood Estimation]])
> For a $Multinomial(n, p_1, \dots, p_c)$ distribution, its MLE is
> $$
> \begin{align}
> L(\mathbf{p}) &= \sum_{j} n_j ln(p_j) \\
> \hat{p_j} &= \frac{n_j}{n}
> \end{align}
> $$

# Properties

## [[Hypothesis Test]]
- [[Multinomial Distribution Maximum Likelihood Estimation Likelihood Ratio Test]]
- [[Multinomial Distribution Maximum Likelihood Estimation Score Test]
- In tabular [[Certainty-Equivalence (Reinforcement Learning)|certainty-equivalence]], the estimated transition $\widehat{P}(\cdot \mid s,a)$ is this MLE. Its $\ell_1$ error is controlled by the [[Empirical Distribution L1 Concentration Bound]].
]