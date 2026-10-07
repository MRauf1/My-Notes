---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Infinite Moments in Monte Carlo[^1]
> [[Simple Monte Carlo]] is robust, but its guarantees depend on moments of $Y$:
> - $\mu = E(Y)$ exists and is finite only if $E|Y| < \infty$. If $E|Y| = \infty$, then $E(Y) = +\infty$, $E(Y) = -\infty$, or $E(Y)$ is undefined in $[-\infty, \infty]$ (when $E(\max(Y, 0)) = E(\max(-Y, 0)) = \infty$).
> - If $\mu$ is finite but $\sigma^2 = \infty$, the [[Strong Law of Large Numbers|law of large numbers]] still gives $\hat{\mu}_n \to \mu$, but the $O(n^{-1/2})$ rate and the CLT-based confidence intervals are lost.
> - If $\sigma^2 < \infty$ but $E|Y|^3$ or $E|Y|^4$ is infinite, the CLT still holds but sets in more slowly.

**Infinite mean.**[^2] If $\mu = \infty$, then $P(\hat{\mu}_n \to \infty) = 1$, yet $P(\hat{\mu}_n = \infty) = 0$ for every $n$ when all samples are finite, so one cannot wait for $\hat{\mu}_n = \infty$ to detect it. The [[Central Limit Theorem]] does not apply, and $\hat{\mu}_n \pm \Phi^{-1}(0.995)\,s/\sqrt{n}$ has probability $0$ of containing $\mu$ for every $n$.

**Ratios.**[^3] Infinite means commonly arise from $E(Y/X)$, which blows up for small $|X|$, not just large $Y$. Finiteness ordinarily needs a finite numerator mean and a denominator without positive density at $0$; small changes in the denominator's distribution can turn a finite expected ratio into an infinite one. (Contrast the [[Ratio Estimator]] of $E(Y)/E(X)$.)

**Infinite variance.**[^4] Monte Carlo allows reformulating the problem to keep the same finite expectation while obtaining finite variance; [[Optimal Importance Sampling Distribution|importance sampling]] is one such method. Conversely, poorly applied importance sampling is a common *source* of infinite variance ([[Monte Carlo Estimator Variance]]).

**Higher moments.**[^5] With $\sigma < \infty$, the speed of the CLT is governed by $E|Y - \mu|^3/\sigma^3$ (Berry–Esseen), and $s^2 \to \sigma^2$ by the law of large numbers, but $s^2$ has RMSE $O(n^{-1/2})$ only if $E(Y^4) < \infty$.

# Properties
- **Monte Carlo cannot diagnose moment existence; only mathematical analysis can be conclusive.**[^6] Running-mean plots can hint at $E|Y| = \infty$ or $\sigma^2 = \infty$, but they mislead both ways: a long tail that ends at a very large value can look like $\mu = \infty$, and a sample can look well behaved while $\mu$ fails to exist because of an unsampled region of probability, say, $10^{-23}$.
- Floating-point discreteness can produce $y_i = \infty$ even when $\mu$ is provably finite, e.g. $Y = |X - 1/2|^{-1/5}$, $X \sim U(0,1)$, if the generator can return exactly $1/2$ ([[Floating-Point Number System]]).
- The [[Cauchy Distribution]] is the canonical example of an undefined mean.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=32&annotation=UR9YMX7L); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=32&annotation=QETM4JYN); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=34&annotation=EPKBZCV7)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=32&annotation=N2P9ZCZ9)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=32&annotation=IL2M9J5K); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=33&annotation=GI5U8273)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=34&annotation=7VWHFA8U); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=46UYCZDZ)
[^5]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=TV4U9UKC)
[^6]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=34&annotation=U8LG5RJ6); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=46UYCZDZ); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=7BBXGMUP)
