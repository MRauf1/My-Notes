---
tags: mathematics, differential_geometry
---

# Definition

> [!info] Definition 1 (Covariant [[Derivative]])[^1]
> Let $W$ be a [[Vector Field]] on $\mathbb{R}^n$ and $\mathbf{v} \in T_{\mathbf{p}}(\mathbb{R}^n)$. The covariant derivative of $W$ with respect to $\mathbf{v}$ is the [[Tangent Vector]]
> $$
> \begin{align}
> \nabla_{\mathbf{v}} W(\mathbf{p}) = \frac{d}{dt} W(\mathbf{p} + t \mathbf{v})|_{t=0}
> \end{align}
> $$
> at the [[Point]] $\mathbf{p}$.

It measures the initial rate of change of $W(\mathbf{p})$ as $\mathbf{p}$ moves in the $\mathbf{v}$ direction.

> [!abstract] Theorem 2 (Alternate Notation)
> If $W = \sum w_i U_i$ is a [[Vector Field]] on $\mathbb{R}^n$ and $\mathbf{v} \in T_{\mathbf{p}}(\mathbb{R}^n)$ then
> $$
> \begin{align}
> \nabla_{\mathbf{v}} W(\mathbf{p}) = \sum \nabla_{\mathbf{v}} w_i(\mathbf{p}) U_i(\mathbf{p})
> \end{align}
> $$

# Types
- [[Covariant Derivative with Respect to Vector Field]]

# Properties
- [[Covariant Derivative Linearity]]
- [[Covariant Derivative Product Rule]]

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=96)