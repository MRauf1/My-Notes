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
- Inverse relation:[^2] $\Phi^{-1}(u) = \sqrt{2}\,\operatorname{erf}^{-1}(2u - 1)$, so published algorithms for erf yield $\Phi$ and $\Phi^{-1}$; neither $\Phi$ nor $\Phi^{-1}$ has a closed form, which makes the normal the most important distribution for which [[Inverse Transform Sampling|inversion]] is hard, though accurate numerical approximations of $\Phi^{-1}$ are widely implemented (alternatively, the [[Box-Muller Transform]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=63&annotation=9PA3BU9Y)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=10&annotation=F7JA8ZHF); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=10&annotation=GJCTGA2Q); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=7&annotation=EFHT2V5D)
