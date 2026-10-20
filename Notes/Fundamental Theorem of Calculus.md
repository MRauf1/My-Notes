---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Fundamental Theorem of Calculus Part 1)[^1]
> If $f$ is [[Continuous Function]] on $[a, b]$, then the [[Function]] $g$ defined by $g(x) = \int_a^x f(t) dt$ for $x \in [a, b]$ is [[Continuous Function]] on $[a, b]$ and [[Differentiable Function]] on $(a, b)$ and $g'(x) = f(x)$
> Alternatively, we can write it as $g'(x) = \frac{d}{dx} \int_a^x f(t) dt = f(x)$

FTC states that if a [[Function]] is [[Continuous Function]], then it is Riemann integrable on that [[Domain]].

Function $g$ is the [[Antiderivative]] of $f$.

> [!abstract] Theorem 2 (Fundamental Theorem of Calculus Part 2)
> If $f$ is [[Continuous Function]] on $[a, b]$ then $\int_a^b f(x) dx = F(b) - F(a)$ where $F$ is any [[Antiderivative]] of $f$

> [!abstract] Theorem 3 (Rudin's Version, Part 1)[^2]
> Let $f \in \mathscr{R}$ on $[a, b]$. For $a \leq x \leq b$, put $F(x) = \int_a^x f(t)\,dt$. Then $F$ is continuous on $[a, b]$; furthermore, if $f$ is continuous at a point $x_0$ of $[a, b]$, then $F$ is differentiable at $x_0$ and $F'(x_0) = f(x_0)$.

> [!abstract] Theorem 4 (Rudin's Version, Part 2)[^3]
> If $f \in \mathscr{R}$ on $[a, b]$ and there is a [[Differentiable Function]] $F$ on $[a, b]$ such that $F' = f$, then
> $$
> \begin{align}
> \int_a^b f(x)\,dx = F(b) - F(a)
> \end{align}
> $$

These versions only assume integrability, not continuity: in Theorem 3, $F$ is even uniformly continuous ($|F(y) - F(x)| \leq M|y - x|$ when $|f| \leq M$), and in Theorem 4, $f$ need not be continuous so long as it is integrable and has an antiderivative. Both extend to $\mathbb{R}^k$-valued functions ([[Riemann-Stieltjes Integral of Vector-Valued Function]]).

[[Derivative]] and [[Riemann Integral]] are [[Inverse Function|Inverse operators]].

# Types
- [[Fundamental Theorem for Line Riemann Integral]]
- [[Fundamental Theorem for Contour Riemann Integral]]
- $n$-fold iterated version over a box, $\int_{\mathbf{a}}^{\mathbf{b}} \frac{\partial^n G}{\partial x_1 \cdots \partial x_n} = \sum_{I} (-1)^{|I|} G(\mathbf{c}_I)$ over the $2^n$ corners (see [[Joint Cumulative Distribution Function]])

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=426)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=142&annotation=3MHXKA3J)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=143&annotation=WUXF4DA2)