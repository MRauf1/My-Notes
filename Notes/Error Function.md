---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Error Function[^1]
> $$
> \begin{align}
> \operatorname{erf}(x) = \frac{2}{\sqrt{\pi}} \int_0^x e^{-p^2}\, dp.
> \end{align}
> $$

It is a rescaled [[Cumulative Distribution Function]] of the [[Normal Distribution]]: the standard normal CDF is $\Phi(x) = \tfrac12\left[1 + \operatorname{erf}(x/\sqrt{2})\right]$.

# Properties
- $\operatorname{erf}(0) = 0$, $\lim_{x \to +\infty} \operatorname{erf}(x) = 1$, odd, strictly increasing; not an elementary function.
- $\operatorname{erf}'(x) = \frac{2}{\sqrt{\pi}} e^{-x^2}$.
- The [[Diffusion Equation]] on the line with step initial data ($\phi = 0$ for $x < 0$, $1$ for $x > 0$) has solution $Q(x, t) = \tfrac12 + \tfrac12\operatorname{erf}\!\left(x/\sqrt{4kt}\right)$, whose $x$-derivative is the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]]; solutions for piecewise-constant data are combinations of erf terms.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=63&annotation=9PA3BU9Y)
