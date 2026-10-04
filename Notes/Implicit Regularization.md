---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Implicit Regularization[^1]
> The preference of an optimization algorithm, such as [[Gradient Descent]] or [[Stochastic Gradient Descent]], for some solutions over others: neither moves neutrally to a minimum of the loss. For gradient descent with step size $\alpha$, the discrete trajectory matches continuous gradient flow $\frac{d\boldsymbol{\phi}}{dt} = -\frac{\partial L}{\partial \boldsymbol{\phi}}$ on the modified loss
> $$
> \begin{align}
> \tilde{L}_{\mathrm{GD}}[\boldsymbol{\phi}] = L[\boldsymbol{\phi}] + \frac{\alpha}{4}\left\lVert \frac{\partial L}{\partial \boldsymbol{\phi}} \right\rVert^2
> \end{align}
> $$
> and, on average, SGD with $B$ batches per epoch matches it on
> $$
> \begin{align}
> \tilde{L}_{\mathrm{SGD}}[\boldsymbol{\phi}] = L[\boldsymbol{\phi}] + \frac{\alpha}{4}\left\lVert \frac{\partial L}{\partial \boldsymbol{\phi}} \right\rVert^2 + \frac{\alpha}{4B}\sum_{b=1}^B \left\lVert \frac{\partial L_b}{\partial \boldsymbol{\phi}} - \frac{\partial L}{\partial \boldsymbol{\phi}} \right\rVert^2
> \end{align}
> $$
> where $L = \frac{1}{I}\sum_{i=1}^I \ell_i[\mathbf{x}_i, \mathbf{y}_i]$ and $L_b = \frac{1}{|\mathcal{B}_b|}\sum_{i \in \mathcal{B}_b} \ell_i[\mathbf{x}_i, \mathbf{y}_i]$ are the mean losses over the dataset and over batch $b$.

# Properties
- **Gradient descent** is repelled from steep regions where the gradient norm is large. The minima, where the gradient is zero, do not move, but the effective loss elsewhere and hence the trajectory change, possibly converging to a different minimum. This may explain why full-batch gradient descent generalizes better with larger step sizes.[^2]
- **SGD** adds a term equal to the variance of the batch gradients, so it favours places where all batches agree on the slope. If the model is over-parameterized and fits all data exactly, every gradient term is zero at the global minimum, so again only the trajectory changes.[^3]
- SGD generalizes better than gradient descent, and smaller batches generally better than larger ones. Besides randomness letting the algorithm reach other parts of the loss, this may be due to implicit regularization favouring solutions where all data fit well (small batch variance) over solutions where some data fit extremely well and others poorly at the same overall loss.[^4]
- A candidate explanation of the smooth interpolation in the modern regime of [[Double Descent]], and a form of [[Regularization]] in its broad sense.

[^1]: [Prince, p. 141](zotero://open-pdf/library/items/BWT7FYX5?page=155&annotation=Z7VNXYD3); [Prince, p. 141](zotero://open-pdf/library/items/BWT7FYX5?page=155&annotation=CCYJSMLQ); [Prince, p. 142](zotero://open-pdf/library/items/BWT7FYX5?page=156&annotation=396SGW4M); [Prince, p. 142](zotero://open-pdf/library/items/BWT7FYX5?page=156&annotation=9F72K6S6); [Prince, p. 143](zotero://open-pdf/library/items/BWT7FYX5?page=157&annotation=Y4C4VFB6)
[^2]: [Prince, p. 142](zotero://open-pdf/library/items/BWT7FYX5?page=156&annotation=U2S3GZ2F)
[^3]: [Prince, p. 143](zotero://open-pdf/library/items/BWT7FYX5?page=157&annotation=G837DA6D)
[^4]: [Prince, p. 143](zotero://open-pdf/library/items/BWT7FYX5?page=157&annotation=R9KMSV35)
