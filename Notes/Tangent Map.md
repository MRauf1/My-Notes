---
tags: mathematics, differential_geometry
---

# Definition

> [!info] Definition 1 ([[Tangent]] [[Mapping|Map]])[^1]
> Let $F: \mathbb{R}^n \rightarrow \mathbb{R}^m$ be a [[Mapping]] and $\alpha: I \rightarrow \mathbb{R}^n$ be a [[Curve]] in $\mathbb{R}^n$ with initial [[Velocity Vector]] $\alpha'(0) = \mathbf{v}_{\mathbf{p}} \in T_{\mathbf{p}}(\mathbb{R}^n)$. Then $F_*: T_{\mathbf{p}}(\mathbb{R}^n) \rightarrow T_{F(\mathbf{p})}(\mathbb{R}^m)$ with $F_*(\mathbf{v}_{\mathbf{p}}) = \beta'(0)$, where $\beta$ is the [[Curve Under Mapping]], is the tangent map.

$F_*$ sends [[Tangent Vector]] in $\mathbb{R}^n$ to [[Tangent Vector]] in $\mathbb{R}^m$. In particular, it sends the [[Velocity Vector]] of $\alpha$ at $\alpha(t) = \mathbf{p}$ to a [[Velocity Vector]] of $\beta$ at $F(\mathbf{p})$.

> [!info] Definition 2 (Calculating Tangent Map)
> Let $F = (f_1, \dots, f_m)$ be a [[Mapping]] $F: \mathbb{R}^n \rightarrow \mathbb{R}^m$. If $\mathbf{v}_{\mathbf{p}} \in T_{\mathbf{p}}(\mathbb{R}^n)$, then
> $$
> \begin{align}
> F_*(\mathbf{v}_{\mathbf{p}}) = (\nabla_{\mathbf{v}} f_1(\mathbf{p}), \dots, \nabla_{\mathbf{v}} f_m(\mathbf{p}))_{F(\mathbf{p})}
> \end{align}
> $$

# Properties
- [[Tangent Map as Linear Transformation]]
- [[Tangent Map Velocity Vector of Curve]]
- [[Tangent Map on Natural Frame Field]]
- 
[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=52)