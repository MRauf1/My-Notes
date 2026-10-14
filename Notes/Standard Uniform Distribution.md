---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Standard Uniform Distribution[^1]
> The standard uniform distribution is the [[Continuous Uniform Distribution]] on the unit interval. The four choices of unit interval $[0,1]$, $(0,1)$, $[0,1)$, $(0,1]$ all give the **same** distribution: if $0 \leq a \leq b \leq 1$ and $U$ follows any of $U[0,1]$, $U(0,1)$, $U[0,1)$, $U(0,1]$, then
> $$
> \begin{align}
> P(a \leq U \leq b) = b - a.
> \end{align}
> $$

It is the distribution that a [[Pseudorandom Number Generator]] simulates.[^1]

# Properties
- **Indistinguishable endpoints:** $P(U = 0) = P(U = 1) = 0$, so even a countably infinite independent sample from $U[0,1]$ contains an exact $0$ or $1$ with probability $0$; the four versions cannot be distinguished by sampling.[^1] More generally, changing a continuous distribution's support on a set of measure zero does not change the distribution.
- **Half-open convenience:** $[0,1)$ splits into $k \geq 2$ congruent pieces $[(i-1)/k,\, i/k)$, $i = 1, \dots, k$, with no differently shaped piece containing $1$; open pieces $((i-1)/k,\, i/k)$ would omit the points $i/k$, and closed pieces would duplicate some. This is mainly a notational convenience for theory.[^2]
- **Simulated values should never be exactly $0$ or $1$:**[^3] transformations such as [[Inverse Transform Sampling]] (e.g. $-\log U$) or the [[Box-Muller Transform]] produce infinities at the endpoints.
- **Floating-point unit interval:** floating-point numbers are more finely spaced near $0$ than near $1$, because they are equally spaced only between successive powers of the base ([[Floating-Point Number System]], [[Machine Epsilon]]). Hence $1 - U$ cannot resolve values as close to $0$ as $U$ can.[^4]

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=8&annotation=YP7S9QZZ); [Owen](zotero://open-pdf/library/items/GBISVAQW?page=9&annotation=8IR3RKW3)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=9&annotation=5235PP8R)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=9&annotation=6FU4MHZR)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/GBISVAQW?page=9&annotation=DUSQFYK6)
