---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Definition 1 (Rectifiable [[Curve (Real Analysis)|Curve]])[^1]
> To each [[Partition]] $P = \{x_0, \dots, x_n\}$ of $[a, b]$ and each curve $\gamma$ on $[a, b]$, associate
> $$
> \begin{align}
> \Lambda(P, \gamma) = \sum_{i=1}^n |\gamma(x_i) - \gamma(x_{i-1})|
> \end{align}
> $$
> the length of the polygonal path with vertices $\gamma(x_0), \gamma(x_1), \dots, \gamma(x_n)$, in this order. The length of $\gamma$ is
> $$
> \begin{align}
> \Lambda(\gamma) = \sup_P \Lambda(P, \gamma)
> \end{align}
> $$
> with the supremum taken over all partitions of $[a, b]$. If $\Lambda(\gamma) < \infty$, $\gamma$ is rectifiable.

As the partition becomes finer, the inscribed polygon approaches the range of $\gamma$ more closely; by the [[Triangle Inequality]], refining never decreases $\Lambda(P, \gamma)$, which motivates taking the supremum.

# Properties
- For $\gamma \in C^1$, $\Lambda(\gamma) = \int_a^b |\gamma'|$: [[Length of Continuously Differentiable Curve Theorem]], which justifies the [[Curve Arc Length]] formula of differential geometry.
- Reparameterization invariance: let $\varphi$ be a continuous one-to-one map of $[c, d]$ onto $[a, b]$ with $\varphi(c) = a$, and $\gamma_2 = \gamma_1 \circ \varphi$. Then $\gamma_2$ is an [[Arc]], a [[Closed Curve]], or rectifiable if and only if $\gamma_1$ is, and $\Lambda(\gamma_2) = \Lambda(\gamma_1)$.[^2] Length is a property of the traced path, not of the parameterization ([[Curve Reparameterization]]).
- Length is defined without derivatives, so it applies to merely continuous curves; some continuous curves (e.g. space-filling curves) are not rectifiable.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=145&annotation=2TIYTLNS)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=151&annotation=2RF8SY9Y)
