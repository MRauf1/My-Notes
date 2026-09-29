---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Rejection Sampling[^1]
> Used when the CDF $F$ cannot be inverted, or the density $p$ cannot even be normalized. Take an envelope density $\tilde{p}$ with $p(x) \leq M\tilde{p}(x)$, and repeat:
> 1. Draw $x \sim \tilde{p}$, then $y \sim \mathcal{U}[0, M\tilde{p}(x))$.
> 2. If $y \leq p(x)$, return $x$; otherwise, go to 1.
>
> Accepted pairs $(x,y)$ are uniform under the graph of $p$, so their $x$-marginal is $p$, and the acceptance rate is $1/M$.

> [!info] Accept-Reject Algorithm[^2]
> Let $f$ be the target pdf and $g$ an instrumental pdf that is easy to sample, with $f(x) \leq Mg(x)$ for all $x$. With $Y \sim g$ and $U \sim \text{Uniform}(0, 1)$ independent:
> 1. Generate $Y$ and $U$.
> 2. If $U \leq \frac{f(Y)}{Mg(Y)}$, take $X = Y$; otherwise return to step 1.
>
> Then $X$ has pdf $f$.

# Properties
- The probability of acceptance is $1/M$, so the number of trials per sample is geometric with mean $M$; choose $M$ as small as possible.[^3]
- Normalizing constants can be ignored:[^3] if $f = kh$ and $g = ct$, then $f \leq Mg$ iff $h \leq M_2 t$ with $M_2 = cM/k$, and the test becomes $U \leq h(Y)/[M_2 t(Y)]$.
- Pro: needs only pointwise evaluations of $p$, and only up to a normalizing constant.
- Con: wastes samples, and $M$ grows brutally with dimension; use it only when [[Inverse Transform Sampling]] is unavailable.
- Made fast for monotone densities by the [[Ziggurat Algorithm]]; in high dimensions, [[Markov Chain Monte Carlo]] replaces it.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=314)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=315)
