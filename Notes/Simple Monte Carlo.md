---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Simple Monte Carlo[^1]
> Simple (or crude) Monte Carlo estimates a population [[Expectation|expectation]] by the corresponding sample expectation. Express the quantity of interest as $\mu = E(Y)$, generate $Y_1, \dots, Y_n$ [[Independent and Identically Distributed|independently]] from the distribution of $Y$, and take
> $$
> \begin{align}
> \hat{\mu}_n = \frac{1}{n}\sum_{i=1}^n Y_i
> \end{align}
> $$
> Commonly $Y = f(X)$ with $X \in D \subseteq \mathbb{R}^d$ having density $p$ (or pmf $p$), so that
> $$
> \begin{align}
> \mu = \int_D f(x)\,p(x)\,dx
> \end{align}
> $$

It is a direct simulation of the problem of interest; the "crude" label only distinguishes it from more sophisticated methods, and simple Monte Carlo is often the appropriate method.[^1] The input $X$ need not be a point in Euclidean space at all: it can be the path of a wandering particle or an image. All that is required is that $Y = f(X)$ is something that can be averaged (a real number or a vector).[^2]

**Strengths.** The error $\sigma/\sqrt{n}$ contains neither the dimension $d$ nor any smoothness of $f$:[^3][^4]
- **Dimension-free:** $d$ can be $2$ or $1000$ and the RMSE is still $\sigma/\sqrt{n}$, whereas a product [[Simpson's Rule]] in $d$ dimensions degrades to $O(n^{-4/d})$ ([[Curse of Dimensionality]]).
- **Smoothness-free:** competing quadrature rules need bounded high-order derivatives of $f$ and do badly on non-smooth integrands; Monte Carlo needs only $\sigma^2 < \infty$.
- **No closed form needed:** it only requires the ability to sample $X$ and evaluate $f$.

Simple Monte Carlo is therefore most competitive in **high-dimensional, non-smooth problems without closed forms**. It is poorly suited to problems that must be answered to high precision ([[Monte Carlo Convergence Rate]]).

**When it is not enough.**[^5] Two difficulties remain even with variance reduction: (1) there may be no practical way to draw independent samples of the inputs (addressed by [[Markov Chain Monte Carlo]]), and (2) the samples can be drawn, but the estimate is still not accurate enough because of the slow $1/\sqrt{n}$ convergence.

# Properties
- **Consistency** (requires that $\mu$ exists, i.e. $E|Y| < \infty$):[^6] by the [[Weak Law of Large Numbers]], $\lim_{n\to\infty} P(|\hat{\mu}_n - \mu| \leq \epsilon) = 1$ for every $\epsilon > 0$; by the [[Strong Law of Large Numbers]], $P(\lim_{n\to\infty} |\hat{\mu}_n - \mu| = 0) = 1$, so the error eventually falls below $\epsilon$ and stays there. Neither law says how large $n$ must be, nor whether the error of a given sample is likely to be small.
- **Unbiased:**[^7] $E(\hat{\mu}_n) = \frac{1}{n}\sum_i E(Y_i) = \mu$ ([[Unbiased Estimator]]).
- **Variance:**[^7] if $\mathrm{Var}(Y) = \sigma^2 < \infty$, then $E((\hat{\mu}_n - \mu)^2) = \sigma^2/n$, so $\mathrm{RMSE} = \sigma/\sqrt{n} = O(n^{-1/2})$ ([[Monte Carlo Convergence Rate]], [[Mean Squared Error]]).
- **Error bars:** $\sigma^2$ is estimated by the [[Sample Variance]], and the [[Central Limit Theorem]] gives the [[Monte Carlo Confidence Interval]] $\hat{\mu}_n \pm 2.58\,s/\sqrt{n}$.
- Special cases: [[Monte Carlo Estimation of a Probability]] ($f$ an indicator), [[Monte Carlo Estimation of a Conditional Expectation]], and the [[Ratio Estimator]].
- Can fail when $E|Y| = \infty$ or $\sigma^2 = \infty$ ([[Infinite Moments in Monte Carlo]]).
- With importance-weighted $Y = g(X)/p(X)$ it becomes the general [[Monte Carlo Estimator]]; it is the base case of every [[Monte Carlo Method]].

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=15&annotation=FSL4YQEQ); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=15&annotation=MGZBXXE8); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=15&annotation=8ILJKEFG); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=16&annotation=3IWU39ID)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=16&annotation=DNBZBUBK)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=IA2TVW8I)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=LEXAWK3Q); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=18&annotation=X5WTL5AE)
[^5]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=9&annotation=HPTFBXUP); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=9&annotation=X322PYKX)
[^6]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=16&annotation=SEHKY7UX); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=16&annotation=IZIUCITV); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=16&annotation=PW56HQDR)
[^7]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=16&annotation=8JURKA5V); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=5DH5BFRV); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=17&annotation=5XNJZUY2)
