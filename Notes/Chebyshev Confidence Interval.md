---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Chebyshev Confidence Interval[^1]
> If $\mathrm{Var}(Y) \leq \sigma_0^2$ is known in advance, then $\mathrm{Var}(\hat{\mu}) \leq \sigma_0^2/n$ and [[Chebyshev's Inequality]] gives
> $$
> \begin{align}
> P\left(|\hat{\mu} - \mu| \geq \frac{k\sigma_0}{\sqrt{n}}\right) \leq \frac{1}{k^2}
> \end{align}
> $$
> so $\hat{\mu} \pm 10\,\sigma_0/\sqrt{n}$ is a conservative $99\%$ [[Confidence Interval|confidence interval]] for $\mu$, valid for every $n$. A $99\%$ interval of width $\varepsilon$ is guaranteed by sampling
> $$
> \begin{align}
> n = \left\lceil \frac{400\,\sigma_0^2}{\varepsilon^2} \right\rceil
> \end{align}
> $$

Prior knowledge thus lets one fix $n$ before sampling.[^1]

# Properties
- **Requires a known bound:**[^2] replacing $\sigma_0$ by the estimate $s$ voids the guarantee.
- **Expensive:**[^3] for $99\%$ the CLT needs a multiplier of $2.58$, not $10$. By the [[Central Limit Theorem]], the Chebyshev interval actually has coverage $\to 1 - 2\Phi(-10) \approx 1 - 1.52\times 10^{-23}$, and it costs $(10/2.58)^2 \approx 15$ times as much computation as the [[Monte Carlo Confidence Interval]].
- For bounded $Y$, [[Hoeffding's Inequality]] gives a sharper guaranteed sample size.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=4NNRE69A); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=MYEYCP76)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=X4RM6C4V)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=XLPJXUHX)
