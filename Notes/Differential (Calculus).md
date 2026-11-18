---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Differential)[^1]
> Let $y = f(x)$ with $f$ a [[Differentiable Function]]. The differential $dx$ is an independent variable (any real number), and the differential $dy$ is defined by
> $$
> \begin{align}
> dy = f'(x)\, dx
> \end{align}
> $$
> So $dy$ depends on both $x$ and $dx$ ([[Derivative]]).

# Properties
- Geometrically, with $dx = \Delta x$, $dy$ is the change in height of the [[Tangent Line]], while $\Delta y = f(x + \Delta x) - f(x)$ is the change in height of the curve. Then $\Delta y \approx dy$ for small $dx$, which is the [[Linear Approximation]] $f(x + dx) \approx f(x) + dy$.
- For $dx \neq 0$, $\frac{dy}{dx} = f'(x)$ is a genuine ratio of differentials.
- Used to estimate propagated errors: absolute error $dy$, relative error $dy/y$.
- In several variables and on manifolds, $df$ becomes a linear map or 1-form: see [[Differential]] (differential geometry). That generalization is a separate concept and is not a prerequisite here.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=286)
