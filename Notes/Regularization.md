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
- **Strict vs. broad sense** (Prince): strictly, regularization adds an explicit term to the loss favouring certain parameters,
$$
\begin{align}
\hat{\boldsymbol{\phi}} = \underset{\boldsymbol{\phi}}{\arg\min}\left[\sum_{i=1}^I \ell_i[\mathbf{x}_i, \mathbf{y}_i] + \lambda \cdot g[\boldsymbol{\phi}]\right]
\end{align}
$$
where $g[\boldsymbol{\phi}]$ is larger for less preferred parameters and $\lambda > 0$ weighs the two terms; the minima of the regularized loss usually differ from the original ones. In machine learning, the term commonly covers any strategy that reduces the **generalization gap** between training and test performance.[^3]
- The explicit term is a negative log prior, $\lambda \cdot g[\boldsymbol{\phi}] = -\log[Pr(\boldsymbol{\phi})]$, turning maximum likelihood into [[Maximum a Posteriori Learning|MAP]] estimation.
- **Methods by mechanism** (overlapping):[^4]
	- *Make the function smoother*: explicit [[L2 Regularization]], [[Early Stopping]], [[Ensemble Learning|ensembling]], the Bayesian approach ([[Predictive Distribution]]), [[Dropout]], and [[Noise Injection (Regularization)|noise on inputs]] and on outputs ([[Label Smoothing]]).
	- *Increase data*: input noise, [[Label Smoothing]], [[Data Augmentation]], [[Transfer Learning]], [[Multitask Learning]].
	- *Combine multiple models*: [[Ensemble Learning|ensembling]], the Bayesian approach, [[Dropout]].
	- *Find wider minima*: [[Dropout]], [[Implicit Regularization]], noise on weights.

![[Regularization Methods Overview.png]]
- More generally, a **regularizer** is any factor that biases a model toward a subset of the solutions with similar training loss. Explicit penalty terms are one kind; the initialization and fitting of neural networks are thought to act as **implicit regularizers**, favouring smooth solutions in the over-parameterized regime ([[Double Descent]]).[^2]
- Used in [[Regularized Image Reconstruction]] to recover a well-behaved scene estimate $\ell_w$ from a camera's sensor measurements $\ell_s$ when the camera's [[Imaging Matrix]] is non-invertible or ill-conditioned.

[^1]: https://visionbook.mit.edu/problem_of_generalization.html
[^2]: [Prince, p. 132](zotero://open-pdf/library/items/BWT7FYX5?page=146&annotation=9KNLV3D7); [Prince, p. 132](zotero://open-pdf/library/items/BWT7FYX5?page=146&annotation=SL9GTGVU)
[^3]: [Prince, p. 138](zotero://open-pdf/library/items/BWT7FYX5?page=152&annotation=8CWW6J6G); [Prince, p. 139](zotero://open-pdf/library/items/BWT7FYX5?page=153&annotation=PJ5QN5PT); [Prince, p. 139](zotero://open-pdf/library/items/BWT7FYX5?page=153&annotation=ZZLTDSU4); [Prince, p. 140](zotero://open-pdf/library/items/BWT7FYX5?page=154&annotation=I48FKEB2)
[^4]: [Prince, Ch. 9](zotero://select/library/items/T3V9WVXD)
