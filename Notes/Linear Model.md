---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Linear Model[^1]
> A model that is a linear function of its unknown parameters $\mathbf{w}$, though not necessarily of its input $\mathbf{x}$:
> $$
> \begin{align}
> y(\mathbf{x}, \mathbf{w}) = \sum_{j=0}^{M} w_j \phi_j(\mathbf{x}) = \mathbf{w}^T \boldsymbol{\phi}(\mathbf{x})
> \end{align}
> $$
> where the $\phi_j$ are fixed (possibly nonlinear) basis functions, with $\phi_0(\mathbf{x}) = 1$ giving the bias term $w_0$.

The polynomial $y(x, \mathbf{w}) = \sum_{j=0}^M w_j x^j$ is the special case $\phi_j(x) = x^j$: nonlinear in $x$ but linear in $\mathbf{w}$ ([[Polynomial Regression]]).

# Properties
- Because $y$ is linear in $\mathbf{w}$, a sum-of-squares error function $E(\mathbf{w}) = \frac{1}{2}\sum_{n=1}^N \{y(\mathbf{x}_n, \mathbf{w}) - t_n\}^2$ is quadratic in $\mathbf{w}$, so its minimizer is unique and available in closed form, including with [[L2 Regularization]].[^2]
- Choosing the basis functions is [[Featurization]]; the number of basis functions needed for a general polynomial grows like $D^M$ in the input dimension $D$, one face of the [[Curse of Dimensionality]].
- Generalizes to [[Linear Regression]] and, through a link function, to the [[Generalized Linear Model]].
- The Gaussian posterior and [[Predictive Distribution|predictive distribution]] of a Bayesian linear model are analytically tractable.

[^1]: [Bishop, 2006, p. 5](zotero://open-pdf/library/items/5G99AZ8U?page=25&annotation=FRW9ZQR9)
[^2]: [Bishop, 2006, p. 5](zotero://open-pdf/library/items/5G99AZ8U?page=25&annotation=NG95Y9BS)
