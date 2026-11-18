---
tags:
  - mathematics
  - ordinary_differential_equations
---

# Definition

> [!info] Definition 1 (Bernoulli Differential Equation)[^1]
> A [[First Order Ordinary Differential Equation]] of the form
> $$
> \begin{align}
> \frac{dy}{dx} + P(x)\,y = Q(x)\,y^n
> \end{align}
> $$
> For $n = 0$ or $1$ it is linear. For other $n$, the substitution $u = y^{1 - n}$ turns it into the [[First Order Linear Ordinary Differential Equation|linear equation]]
> $$
> \begin{align}
> \frac{du}{dx} + (1 - n)P(x)\,u = (1 - n)Q(x)
> \end{align}
> $$

# Properties
- Derivation: divide by $y^n$ to get $y^{-n}y' + P y^{1-n} = Q$; since $u' = (1 - n)y^{-n}y'$ ([[Derivative Chain Rule]]), this is $\frac{u'}{1-n} + Pu = Q$.
- Dividing by $y^n$ loses the solution $y \equiv 0$ when $n > 0$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=657)
