---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Theorem 1 (Reduction to [[Riemann Integral]])[^1]
> Assume $\alpha$ increases monotonically and $\alpha' \in \mathscr{R}$ on $[a, b]$. Let $f$ be a bounded real function on $[a, b]$. Then $f \in \mathscr{R}(\alpha)$ if and only if $f\alpha' \in \mathscr{R}$. In that case
> $$
> \begin{align}
> \int_a^b f \, d\alpha = \int_a^b f(x) \alpha'(x) \, dx
> \end{align}
> $$

This justifies the formal rule $d\alpha = \alpha'(x)\,dx$: $\alpha'$ acts as a density (weight) on $[a, b]$. Where $\alpha'$ is large, that region contributes more to the integral. E.g. with a mass density $\rho$ and cumulative mass $\alpha(x) = \int_a^x \rho$, the total mass is $\int_a^b 1 \, d\alpha = \int_a^b \rho(x)\,dx$.

# Properties
- Together with [[Riemann-Stieltjes Integral with Step Function Integrator Theorem]], it shows that the [[Riemann-Stieltjes Integral]] unifies series and integrals.[^2]
- Probabilistic analogue: for a [[Continuous Random Variable]] with [[Cumulative Distribution Function]] $F_X$ and density $f_X = F_X'$, $\int g\,dF_X = \int g(x) f_X(x)\,dx$ ([[Expectation]]).
- Applied to [[Riemann-Stieltjes Integral Change of Variable Theorem]], it gives the usual substitution rule.
- Extends coordinatewise to the [[Riemann-Stieltjes Integral of Vector-Valued Function]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=140&annotation=L7DVWPZX)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=141&annotation=PX55TL9S)
