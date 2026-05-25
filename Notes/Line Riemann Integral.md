---
tags: mathetatics, calculus
---

# Definition

> [!info] Definition 1 ([[Curve]] [[Riemann Integral]])[^1]
> If $f$ is defined on [[Smooth Curve]] $C$ with $a \leq t \leq b$ defined by $\alpha(t)$, then the line integral of $f$ along $C$ is
> $$
> \begin{align}
> \int_C f(x, y) ds &= \sum_{n \rightarrow \infty} \sum_{i=1}^n f(x_i^*, y_i^*) \Delta s_i \\
> &= \int_a^b f(\alpha_1(t), \alpha_2(t)) ||\alpha'(t)|| dt 
> \end{align}
> $$
> where $\Delta s_i$ is the [[Curve Arc Length]] of the $i$th subarc of $C$ from $t=a$ to $t=b$.

If the function is non-negative, then just like a single integral, line integral represents the [[Area of Region Under Curve]].

![[Pasted image 20251022204721.png]]

# Types
- [[Line Integral of Vector Field]]

# Properties
- [[Fundamental Theorem for Line Riemann Integral]]

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=1107)