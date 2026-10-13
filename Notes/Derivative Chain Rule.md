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

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=230)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=114)
