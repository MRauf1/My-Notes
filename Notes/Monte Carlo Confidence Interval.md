---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Monte Carlo Confidence Interval[^1]
> Let $\hat{\mu}_n$ be the [[Simple Monte Carlo]] estimate of $\mu = E(Y)$ with $0 < \sigma^2 < \infty$, and $s$ the sample standard deviation ([[Sample Variance]]). By the [[Central Limit Theorem]] and [[Slutsky's Theorem]] (since $s \xrightarrow{P} \sigma$),
> $$
> \begin{align}
> P\left(\sqrt{n}\,\frac{\hat{\mu}_n - \mu}{s} \leq z\right) \to \Phi(z), \qquad n \to \infty
> \end{align}
> $$
> which justifies the approximate $95\%$, $99\%$ and $100(1-\alpha)\%$ [[Confidence Interval|confidence intervals]]
> $$
> \begin{align}
> \hat{\mu}_n \pm 1.96\,\frac{s}{\sqrt{n}}, \qquad \hat{\mu}_n \pm 2.58\,\frac{s}{\sqrt{n}}, \qquad \hat{\mu}_n \pm \Phi^{-1}(1 - \alpha/2)\,\frac{s}{\sqrt{n}}
> \end{align}
> $$

More generally, most Monte Carlo $99\%$ intervals take the form[^2]
$$
\begin{align}
\hat{\mu}_n \pm 2.58\sqrt{\widehat{\mathrm{Var}}(\hat{\mu}_n)}
\end{align}
$$
where $\hat{\mu}_n$ is an unbiased (or nearly unbiased) estimate of $\mu$ satisfying a CLT, and $\widehat{\mathrm{Var}}(\hat{\mu}_n)$ is an unbiased (or nearly unbiased) estimate of its variance. In Monte Carlo the word "approximate" is usually omitted; exact intervals exist only in a few cases, such as [[Monte Carlo Estimation of a Probability|estimating a probability]].[^3]

**Coverage accuracy.**[^4] Two-sided CLT intervals typically satisfy
$$
\begin{align}
P\left(|\mu - \hat{\mu}| \leq \Phi^{-1}(1 - \alpha/2)\,\frac{s}{\sqrt{n}}\right) = 1 - \alpha + O(n^{-1})
\end{align}
$$
provided $E(Y^4) < \infty$ and $Y$ is not confined to a shifted lattice $\{a + bx \mid x \in \mathbb{Z}\}$ (Hall, 1992). The coverage error $O(n^{-1})$ is *better* than the $O(n^{-1/2})$ accuracy of $\hat{\mu}$ itself. One-sided intervals do not enjoy this: their coverage error is typically $O(n^{-1/2})$.

# Types
- **One-sided bounds:**[^5] $(-\infty,\ \hat{\mu} + \Phi^{-1}(1-\alpha)\,s/\sqrt{n}]$ (upper) or $[\hat{\mu} + \Phi^{-1}(\alpha)\,s/\sqrt{n},\ \infty)$ (lower).
- **$t$-intervals:**[^6] $\hat{\mu}_n \pm t^{(n-1)}_{1-\alpha/2}\,s/\sqrt{n}$, using the $1-\alpha/2$ quantile of the [[t-Distribution]] with $n-1$ degrees of freedom; exact when the $Y_i$ are normal ([[Student's Theorem]]). For $n \geq 1000$ the $99\%$ $t$-interval is only about $1 + 1.9/n$ times as wide as the normal one, so the distinction matters only for small $n$ (e.g. $n \leq 20$, which does occur in Monte Carlo when each sample is expensive).
- **Guaranteed (non-asymptotic) intervals** from prior knowledge: [[Chebyshev Confidence Interval]] (known variance bound) and [[Hoeffding's Inequality]] (known range).

# Properties
- Requires $\sigma^2 < \infty$; when the variance or mean is infinite the interval can have coverage $0$ ([[Infinite Moments in Monte Carlo]]).
- Numerically, $s$ should be computed with [[Welford's Algorithm]] or the [[Paired Difference Variance Estimator]] for very large $n$.
- Its half-width shrinks as $O(n^{-1/2})$ ([[Monte Carlo Convergence Rate]]).

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=18&annotation=ELDA5ZUM); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=19&annotation=L2BMXGBW); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=19&annotation=F2QVYP9K); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=19&annotation=P3ADCDQ8); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=19&annotation=BFXLQCPT); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=20&annotation=7ICNYRTN)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=20&annotation=W6EL7QQJ)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=20&annotation=AKA769NS)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=20&annotation=SD9PUUFK); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=21&annotation=P7BCDH6C); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=21&annotation=KH4ZEY9I)
[^5]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=20&annotation=RVU8I5X8)
[^6]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=20&annotation=TGIVEFY2); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=20&annotation=ERNAQ9IG)
