---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!info] Definition 1 (Derivative of Vector-Valued Function)[^1]
> Let $\mathbf{f}$ map $[a, b]$ into $\mathbb{R}^k$. Then $\mathbf{f}'(x)$ is the point of $\mathbb{R}^k$ (if there is one) for which
> $$
> \begin{align}
> \lim_{t \rightarrow x} \left| \frac{\mathbf{f}(t) - \mathbf{f}(x)}{t - x} - \mathbf{f}'(x) \right| = 0
> \end{align}
> $$
> i.e. [[Derivative|Definition 2 of the derivative]], with the limit taken with respect to the norm of $\mathbb{R}^k$. If $f_1, \dots, f_k$ are the components of $\mathbf{f}$, then
> $$
> \begin{align}
> \mathbf{f}' = (f_1', \dots, f_k')
> \end{align}
> $$
> and $\mathbf{f}$ is differentiable at $x$ if and only if each $f_i$ is differentiable at $x$.

> [!info] Definition 2 (Complex-Valued Case)[^2]
> If $f = f_1 + i f_2$ on $[a, b]$ with $f_1, f_2$ real ([[Complex-Valued Function]]), then
> $$
> \begin{align}
> f'(x) = f_1'(x) + i f_2'(x)
> \end{align}
> $$
> and $f$ is differentiable at $x$ if and only if both $f_1$ and $f_2$ are differentiable at $x$.

# Properties
- [[Differentiable Implies Continuous]] still holds.[^1]
- [[Derivative Sum Rule]] and [[Derivative Product Rule]] still hold, with the product $fg$ replaced by the [[Inner Product]] $\mathbf{f} \cdot \mathbf{g}$. For complex-valued functions, the quotient rule holds too.[^1][^2]
- The [[Mean Value Theorem]] and [[L'Hospital's Rule]] fail for complex-valued (hence vector-valued) functions.[^1] The [[Mean Value Inequality for Vector-Valued Function]] is the replacement.
- Component-wise analogue of [[Continuous Function Component Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=121&annotation=VQL6WS8D)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=120&annotation=5VD4QVLK)
