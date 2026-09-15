---
tags:
  - computer_science
  - deep_learning
---

# Definition

> [!info] Definition 1 (ERM)
> With [[Hypothesis Space|hypothesis space]] $\mathcal{F}$, [[Loss Function|loss function]] $L$, and training data $\{\mathbf{x}^{(i)}, \mathbf{y}^{(i)}\}^{N}_{i=1}$, ERM is
> $$
> \begin{align}
> \underset{f \in \mathcal{F}}{\mathrm{\arg \min}} [\frac{1}{N} \sum_{i=1}^{N} L(f(\mathbf{x}^{(i)}, \mathbf{y}^{(i)})]
> \end{align}
> $$

Minimizing the [[Mean|average]] error/risk over all the training data (empirical distribution).[^1]

# Properties
- Depending on the [[Loss Function|loss function]] $L$, ERM often has an interpretation as [[Maximum Likelihood Learning|maximum likelihood]] probabilistic inference: searching for the hypothesis $f$ that assigns the highest probability to the observed data.

[^1]: https://visionbook.mit.edu/intro_to_learning.html