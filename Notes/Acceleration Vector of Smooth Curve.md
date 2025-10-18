---
tags: mathematics, differential_geometry
---

# Definition

> [!info] Definition 1 ([[Acceleration]] [[Vector]] of [[Smooth Curve]])[^1]
> Let $\alpha: I \rightarrow \mathbb{R}^3$ be a [[Smooth Curve]] in $\mathbb{R}^3$ with $\alpha = (\alpha_1, \alpha_2, \alpha_3)$. For each number $t \in I$, the acceleration vector of $\alpha$ at $t$ is the [[Vector]] at the [[Point]] $\alpha(t) \in \mathbb{R}^3$ that is
> $$
> \begin{align}
> \alpha''(t) = [\frac{d^2 \alpha_1}{dt^2}(t), \frac{d^2 \alpha_2}{dt^2}(t), \frac{d^2 \alpha_3}{dt^2}(t)]_{\alpha(t)}
> \end{align}
> $$

> [!info] Definition 2 (Acceleration Vector from [[Frenet Frame Field]])[^2]
> For the [[Curve]] $\alpha$ with the [[Frenet Frame Field]] including $T, N, \kappa$ and with [[Curve Speed Function]] $v$, it is
> $$
> \begin{align}
> \alpha'' = \frac{dv}{dt}T + \kappa v^2 N
> \end{align}
> $$

In particular, the first part measures the rate of change of the length of $\alpha'$ (speed of $\alpha$), while the second part measures the rate of change of the direction of $\alpha'$.

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=71)
[^2]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=86)