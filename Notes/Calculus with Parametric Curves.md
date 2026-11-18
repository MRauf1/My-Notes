---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Tangents to Parametric Curves)[^1]
> For a curve $x = f(t)$, $y = g(t)$ with $f, g$ differentiable and $\frac{dx}{dt} \neq 0$,
> $$
> \begin{align}
> \frac{dy}{dx} = \frac{dy/dt}{dx/dt}, \qquad \frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{dx/dt}
> \end{align}
> $$

> [!abstract] Theorem 2 (Area Under a Parametric Curve)[^2]
> If the curve is traced once as $t$ goes from $\alpha$ to $\beta$, the area under it is $A = \int_\alpha^\beta g(t)\,f'(t)\,dt$ (or with $\alpha, \beta$ swapped, so that $x$ runs from left to right).

# Properties
- Tangent lines are horizontal where $\frac{dy}{dt} = 0$ and $\frac{dx}{dt} \neq 0$, and vertical where $\frac{dx}{dt} = 0$ and $\frac{dy}{dt} \neq 0$. A curve crossing itself has one tangent per parameter value.
- Follows from the [[Derivative Chain Rule]] $\frac{dy}{dt} = \frac{dy}{dx}\frac{dx}{dt}$ for [[Parametric Equations]].
- Polar curves $r = f(\theta)$ are the parametric curves $x = r\cos\theta$, $y = r\sin\theta$ ([[Cartesian and Polar Coordinate System Change]]).
- Arc length: $L = \int_\alpha^\beta \sqrt{(dx/dt)^2 + (dy/dt)^2}\,dt$ ([[Arc Length]]).

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=681)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=684)
