---
tags: [mathematics, complex_analysis]
---

# Definition

> [!info] Definition 1 (atan2)
> 2 variable [[Function]] that is
> $$
> \begin{align}
> atan2(y, x) = 2 arctan(\frac{y}{\sqrt{x^2 + y^2} + x}) = 2 arctan(\frac{\sqrt{x^2 + y^2} - x}{y})
> \end{align}
> $$
> The [[Domain]] is $[-\pi, \pi)$
> Alternatively, for complex number $z = x + iy$, it is
> $$
> \begin{align}
> atan2(y, x) = arg(x + iy) = Im(log(x + iy))
> \end{align}
> $$

It is the [[Angle]] between positive x-axis and the [[Ray]] from the [[Origin]] to the [[Point]] $(x, y)$.

It is the [[Argument (Complex Number)]] of a [[Complex Number]].

It is an alternative way of calculating $arctan(\frac{y}{x})$.

> [!info] Definition 2 (In Terms of [[Arctangent Function]])
> $$
> \begin{align}
> atan2(y, x) = \begin{cases}arctan(\frac{y}{x}) & x > 0 \\ arctan(\frac{y}{x}) + \pi & x < 0, y \geq 0 \\ arctan(\frac{y}{x}) - \pi & x < 0, y < 0 \\ \frac{\pi}{2} & x = 0, y > 0 \\ - \frac{\pi}{2} & x = 0, y < 0 \\ undefined & x = 0, y = 0 \end{cases}
> \end{align}
> $$