---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 ([[Derivative]] Chain Rule)[^1]
> If $f, g$ are both [[Differentiable Function]],
> $$
> \begin{align}
> \frac{d}{dx}(f(g(x))) &= f'(g(x)) \cdot g'(x) \\
> \frac{dy}{dx} &= \frac{dy}{du} \frac{du}{dx}
> \end{align}
> $$
> For [[Real-Valued Function]], it can be derived from the [[Function]] [[Differential]]. For example, for $f(x, y), x(t), y(t)$, the chain rule gives $\frac{df}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt}$

> [!abstract] Theorem 2 (Pointwise Chain Rule)[^2]
> Suppose $f$ is continuous on $[a, b]$, $f'(x)$ exists at some point $x \in [a, b]$, $g$ is defined on an interval $I$ which contains the [[Range]] of $f$, and $g$ is differentiable at the point $f(x)$. If
> $$
> \begin{align}
> h(t) = g(f(t)) \quad (a \leq t \leq b)
> \end{align}
> $$
> then $h$ is differentiable at $x$, and
> $$
> \begin{align}
> h'(x) = g'(f(x)) f'(x)
> \end{align}
> $$

> [!abstract] Theorem 3 (Multivariable Chain Rule)[^3]
> Let $\mathbf{u} = \mathbf{u}(\mathbf{x}) : \mathbb{R}^n \to \mathbb{R}^k$ be differentiable at $\mathbf{x}$ and $\mathbf{f} = \mathbf{f}(\mathbf{u}) : \mathbb{R}^k \to \mathbb{R}^m$ be differentiable at $\mathbf{u}(\mathbf{x})$. Then $\mathbf{f}(\mathbf{u}(\mathbf{x}))$ is differentiable at $\mathbf{x}$ and its [[Jacobian Matrix]] is the (ordinary matrix) product of the Jacobians
> $$
> \begin{align}
> \frac{\partial \mathbf{f}}{\partial \mathbf{x}} = \frac{\partial \mathbf{f}}{\partial \mathbf{u}} \frac{\partial \mathbf{u}}{\partial \mathbf{x}}
> \end{align}
> $$
> where $\frac{\partial \mathbf{f}}{\partial \mathbf{x}}$ is $m \times n$, $\frac{\partial \mathbf{f}}{\partial \mathbf{u}}$ (evaluated at $\mathbf{u}(\mathbf{x})$) is $m \times k$, and $\frac{\partial \mathbf{u}}{\partial \mathbf{x}}$ is $k \times n$. Componentwise, each entry sums over all intermediate variables $u_1, \dots, u_k$:
> $$
> \begin{align}
> \frac{\partial f_i}{\partial x_j} = \sum_{l=1}^{k} \frac{\partial f_i}{\partial u_l} \frac{\partial u_l}{\partial x_j}
> \end{align}
> $$
> In particular, for a scalar $f = f(u_1, \dots, u_k)$ (i.e. $m = 1$), each [[Partial Derivative]] is
> $$
> \begin{align}
> \frac{\partial f}{\partial x_j} = \frac{\partial f}{\partial u_1} \frac{\partial u_1}{\partial x_j} + \cdots + \frac{\partial f}{\partial u_k} \frac{\partial u_k}{\partial x_j} = \nabla_{\mathbf{u}} f \cdot \frac{\partial \mathbf{u}}{\partial x_j}
> \end{align}
> $$
> The single-variable rule in Definition 1 is the case $n = k = m = 1$, and its $\frac{df}{dt}$ formula is the case $n = 1, k = 2, m = 1$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=230)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=114)
[^3]: [Chain Rule (Multivariable Case)](https://en.wikipedia.org/wiki/Chain_rule#Multivariable_case)
