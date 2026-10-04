---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Label Smoothing[^1]
> Minimizing the [[Cross-Entropy Loss|cross-entropy]] between the predicted distribution and a target distribution in which the true class has probability $1 - \rho$ and the other $K - 1$ classes share the remainder equally, $\rho / (K - 1)$ each. Equivalent in expectation to assuming that a proportion $\rho$ of training labels are wrong and belong uniformly to the other classes.

# Properties
- Counters the overconfidence of maximum likelihood for [[Multiclass Classification]], which aims to predict the correct class with absolute certainty and so pushes the pre-[[Softmax Function|softmax]] activations to extreme values.
- Achieves the same effect as randomly changing labels each iteration, but deterministically through the loss; improves generalization in diverse scenarios.
- A form of [[Noise Injection (Regularization)|noise injection]] on the outputs.
- Common implementations instead mix the one-hot target with the uniform distribution over all $K$ classes, giving the true class $1 - \rho + \rho/K$.[^2]

[^1]: [Prince, p. 149](zotero://open-pdf/library/items/BWT7FYX5?page=163&annotation=NUWYK4DY); [Prince, p. 150](zotero://open-pdf/library/items/BWT7FYX5?page=164&annotation=RAF5PXPE)
[^2]: Implementation convention added from general knowledge (Szegedy et al., 2016).
