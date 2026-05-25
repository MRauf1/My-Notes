---
tags: [mathetatics, calculus]
---

# Definition

> [!info] Definition 1 (Linear Approximation)[^1]
> For a [[Differentiable Function]] $f$, we can use the [[Tangent Line]] as an approximation of $f$ near [[Point]] $a$. The approximation function is
> $$
> \begin{align}
> L(x) = f(a) + f'(a)(x - a)
> \end{align}
> $$
> It is also called tangent line approximation or linearization of $f$ at $a$.
> In higher dimensions, you get
> $$
> \begin{align}
> &L(\mathbf{x}) = \\
> &= f(\mathbf{a}) + \frac{\partial f}{\partial x_1}(\mathbf{a})(x_1 - a_1) + \dots + \frac{\partial f}{\partial x_n}(\mathbf{a})(x_n - a_n) \\
> &= f(\mathbf{a}) + \nabla f(\mathbf{a})(\mathbf{x} - \mathbf{a})
> \end{align}
> $$

> [!info] Definition 2 (Linear Approximation in Terms of [[Differential]])
> $$
> \begin{align}
> f(a + dx) \approx f(a) + dy
> \end{align}
> $$
> In higher dimensions, this is
> $$
> \begin{align}
> f(\mathbf{x}) \approx f(\mathbf{a}) + df
> \end{align}
> $$

This approximation's quality worsens as we get farther away from $a$.

This can be extended to higher dimensions resulting in [[Tangent Plane]] in 3D and [[Tangent Hyperplane]] in higher dimensions.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=284)