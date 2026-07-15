---
tags: [mathetatics, calculus]
---

# Definition

> [!info] Definition 1 ([[Curve]] [[Riemann Integral]])[^1]
> If $f$ is defined on [[Smooth Curve]] $C$ with $a \leq t \leq b$ defined by $\alpha(t)$, then the line integral of $f$ along $C$ (with respect to [[Arc Length]]) is
> $$
> \begin{align}
> \int_C f(x, y) ds &= \lim_{n \rightarrow \infty} \sum_{i=1}^n f(x_i^*, y_i^*) \Delta s_i \\
> &= \int_a^b f(\alpha_1(t), \alpha_2(t)) ||\alpha'(t)|| dt 
> \end{align}
> $$
> where $\Delta s_i$ is the [[Curve Arc Length]] of the $i$th subarc of $C$ from $t=a$ to $t=b$.
> With everything as above, but instead of with respect to [[Arc Length]], we have it with respect to $x$ or $y$ or both, then we have
> $$
> \begin{align}
> \int_C f(x, y) dx &= \int_a^b f(x(t), y(t)) x'(t) dt \\
> \int_C f(x, y) dy &= \int_a^b f(x(t), y(t)) y'(t) dt \\
> \int_C P(x, y) dx + \int_C Q(x, y) dy &= \int_C P(x, y) dx + Q(x, y) dy
> \end{align}
> $$
> The last one is a common abbreviation.

If the function is non-negative, then just like a single integral, line integral represents the [[Area of Region Under Curve]].

![[Pasted image 20251022204721.png]]

# Types
- [[Line Integral of Vector Field]]

# Properties
- [[Line Riemann Integral Basic Properties]]
- [[Fundamental Theorem for Line Riemann Integral]]
- [[Green's Theorem]]

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=1107)