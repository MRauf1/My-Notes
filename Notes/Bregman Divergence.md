---
tags:
  - mathematics
  - optimization
---

# Definition
> [!info] Bregman Divergence[^1]
> For a strictly [[Convex Function|convex]], continuously differentiable $\psi: \Omega \to \mathbb{R}$, the Bregman divergence between $\mathbf{y}, \hat{\mathbf{y}} \in \Omega$ is the gap between $\psi(\mathbf{y})$ and its first-order [[Taylor Series|Taylor expansion]] about $\hat{\mathbf{y}}$:
> $$
> \begin{align}
> D_\psi(\mathbf{y} \,\|\, \hat{\mathbf{y}}) = \psi(\mathbf{y}) - \psi(\hat{\mathbf{y}}) - \langle \nabla\psi(\hat{\mathbf{y}}), \mathbf{y} - \hat{\mathbf{y}} \rangle
> \end{align}
> $$

> [!abstract] Exponential Family-Bregman Correspondence (Banerjee et al., 2005)
> There is a bijection between regular [[Exponential Family|exponential families]] and regular Bregman divergences: the negative log-likelihood of such a family satisfies
> $$
> \begin{align}
> -\log p(\mathbf{y} | \boldsymbol{\theta}) = D_{\psi}(\mathbf{y} \,\|\, \boldsymbol{\mu}(\boldsymbol{\theta})) + \text{const.}
> \end{align}
> $$
> where $\psi$ is the convex conjugate (Legendre dual) of the log-partition function, $\boldsymbol{\mu}(\boldsymbol{\theta}) = \mathbb{E}[\mathbf{Y} | \boldsymbol{\theta}]$ is the mean parameter, and the constant does not depend on $\boldsymbol{\theta}$.

# Properties
- Geometrically, the vertical distance at $\mathbf{y}$ between the surface $\psi$ and its tangent hyperplane at $\hat{\mathbf{y}}$; nonnegative, zero iff $\mathbf{y} = \hat{\mathbf{y}}$, but generally not symmetric and not a metric.
- Examples:
	- $\psi(t) = \frac{1}{2}t^2 \Rightarrow D_\psi(y \| \hat{y}) = \frac{1}{2}(y - \hat{y})^2$, the squared error ([[Normal Distribution]] NLL).
	- $\psi(t) = t\log t + (1-t)\log(1-t) \Rightarrow D_\psi(y \| \hat{y}) = y\log\frac{y}{\hat{y}} + (1-y)\log\frac{1-y}{1-\hat{y}}$, which equals the [[Binary Cross-Entropy Loss]] for $y \in \{0, 1\}$ ([[Bernoulli Distribution]]).
	- $\psi(t) = t\log t - t \Rightarrow D_\psi(y \| \hat{y}) = y\log\frac{y}{\hat{y}} - (y - \hat{y})$, the generalized KL / [[Poisson Distribution]] NLL.
	- $\psi(\mathbf{p}) = \sum_k p_k \log p_k$ on the simplex gives the [[Kullback-Leibler Divergence]].
- Unifies the likelihood and geometric families of the [[Loss Function Taxonomy]].

[^1]: Supplementary notes provided by the creator.
