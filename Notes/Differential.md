---
tags: mathematics, differential_geometry
---

# Definition

> [!info] Definition 1 (Differential)[^1]
> For a real-valued [[Smooth Function]] $f: \mathbb{R}^n \rightarrow \mathbb{R}$, the differential of $f$ is
> $$
> \begin{align}
> df = \sum_{i} \frac{\partial f}{\partial x_i} dx_{i}
> \end{align}
> $$

> [!info] Definition 2 (Differential as a [[1-Form]])
> If $f: \mathbb{R}^n \rightarrow \mathbb{R}$ is a [[Real-Valued Function]] [[Smooth Function]] on $\mathbb{R}^n$, the differential of $f$ is the [[1-Form]] such that
> $$
> \begin{align}
> df(\mathbf{v}_{\mathbf{p}}) = \nabla_{\mathbf{v}} f(\mathbf{p})
> \end{align}
> $$
> for all [[Tangent Vector]] $\mathbf{v}_{\mathbf{p}}$.

> [!info] Definition 3 (Differential as a [[1-Form]] Alternate Notation)
> If $\phi$ is a [[1-Form]] on $\mathbb{R}^n$, then $\phi(\mathbf{v}_\mathbf{p}) = \sum_{i} f_i dx_i (\mathbf{v}_\mathbf{p})$, where $f_i = \phi(U_i(\mathbf{p}))$. In particular, $f_i$ are the [[Euclidean Coordinate Function]] of $\phi$.

It represents an infinitesimal change in the function's value.

It can be also used to relate infinitesimal changes of variables to each other mathematically.

$d$ is an [[Operator]] that takes [[Function]] to its [[1-Form]].

# [[Operation]]
- [[Differential of Function Addition]]
- [[Differential of Function Multiplication]]
- [[Differential of Function Composition]]

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=38)