---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Integration by Parts for [[Indefinite Riemann Integral]])[^1]
> For integrable and [[Differentiable Function]] $f, g$
> $$
> \begin{align}
> \int f(x) g'(x) dx &= f(x) g(x) - \int g(x) f'(x) dx \\
> \int u dv &= u v - \int v du 
> \end{align}
> $$
> where $u = f(x), du = f'(x) dx, v = g(x), dv = g'(x) dx$

> [!info] Definition 1 (Integration by Parts for [[Definite Riemann Integral]])[^1]
> For integrable and [[Differentiable Function]] $f, g$
> $$
> \begin{align}
> \int_a^b f(x) g'(x) dx &= f(x) g(x)|_a^b - \int_a^b g(x) f'(x) dx \\
> \int_a^b u dv &= u v|_a^b - \int_a^b v du 
> \end{align}
> $$
> where $u = f(x), du = f'(x) dx, v = g(x), dv = g'(x) dx$

> [!abstract] Theorem 3 (Integration by Parts, Rudin's Version)[^2]
> Suppose $F$ and $G$ are [[Differentiable Function|differentiable functions]] on $[a, b]$, $F' = f \in \mathscr{R}$, and $G' = g \in \mathscr{R}$. Then
> $$
> \begin{align}
> \int_a^b F(x) g(x)\,dx = F(b)G(b) - F(a)G(a) - \int_a^b f(x) G(x)\,dx
> \end{align}
> $$

Follows from Rudin's [[Fundamental Theorem of Calculus]] applied to $H = FG$, using [[Functions that are Riemann-Stieltjes Integrable Theorem|integrability of products]]. Only integrability of the derivatives is required, not continuity.

# Properties
- Discrete analogue: [[Summation by Parts]].

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=504)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=143&annotation=BRLZ6Q38)