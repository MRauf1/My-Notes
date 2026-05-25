---
tags: mathematics, differential_geometry
---

# Definition

> [!info] Definition 1 ([[Direction|Directional]] [[Derivative]])[^1]
> Let $f(\mathbf{x})$ be a [[Real-Valued Function]] [[Smooth Function]] on $\mathbb{R}^n$ and let $\mathbf{v}_{\mathbf{p}} \in T_{\mathbf{p}}(\mathbb{R}^n)$ be a [[Tangent Vector]] to $\mathbb{R}^n$. Then
> $$
> \begin{align}
> \nabla_{\mathbf{v}} f(\mathbf{p}) &:= \frac{d}{dt} [f(\mathbf{p} + t \mathbf{v})]|_{t = 0} \\
> &= \lim_{t \rightarrow 0} \frac{f(\mathbf{p} + t\mathbf{v}) - f(\mathbf{p})}{t} \\
> &= \sum_{i} v_i \frac{\partial f}{\partial x_i} (\mathbf{p}) \\
> &= \nabla f(\mathbf{p}) \cdot \mathbf{v} \\
> &= comp_{\mathbf{v}} \nabla f(\mathbf{p})
> \end{align}
> $$
> is the Directional Derivative of $f$ with respect to $\mathbf{v}_{\mathbf{p}}$.
> Note that some definitions restrict $\mathbf{v}_{\mathbf{p}}$ to be a [[Unit Vector]]. If it's not, that you can multiply the result by $\frac{1}{||\mathbf{v}_{\mathbf{p}}||}$.

It is the instantaneous rate of change of $f$ in the direction of $\mathbf{v}$ at the point $\mathbf{p}$.

It can also be thought of as the [[Scalar Projection]] of the [[Gradient Vector]] onto $\mathbf{v}$.

# Types
- [[Directional Derivative Vector Field]]

# Properties
- [[Directional Derivative Linearity]]
- [[Directional Derivative Product Rule]]
- [[Directional Derivative Chain Rule]]

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=27)