---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Weak Law of Large Numbers[^1]
> Let $\{X_n\}$ be a sequence of [[Independent and Identically Distributed|iid]] random variables with common mean $\mu$ and variance $\sigma^2 < \infty$, and let $\bar{X}_n = n^{-1}\sum_{i=1}^n X_i$. Then
> $$
> \begin{align}
> \bar{X}_n \xrightarrow{P} \mu
> \end{align}
> $$
> ([[Convergence in Probability]]).

All the mass of the distribution of $\bar{X}_n$ concentrates at $\mu$ as $n \to \infty$: for large $n$, the [[Sample Mean]] is close to $\mu$ with high probability. Proof: by [[Chebyshev's Inequality]], $P(|\bar{X}_n - \mu| \geq \epsilon) \leq \frac{\text{Var}(\bar{X}_n)}{\epsilon^2} = \frac{\sigma^2}{n\epsilon^2} \to 0$.

**Weak vs. strong law.** The [[Strong Law of Large Numbers]] states that if $X_1, X_2, \dots$ are iid with $E|X_1| < \infty$, then
$$
\begin{align}
P\left(\lim_{n\to\infty}\bar{X}_n = \mu\right) = 1
\end{align}
$$
(almost sure convergence). The differences:
- Mode of convergence. The weak law says that for each large fixed $n$, a deviation $|\bar{X}_n - \mu| \geq \epsilon$ is unlikely; it does not rule out such deviations recurring infinitely often along a single sequence of experiments. The strong law says that with probability one, the running average of a single infinite sequence of observations actually converges to $\mu$: only finitely many deviations of size $\epsilon$ ever occur. Almost sure convergence implies convergence in probability, so the strong law implies the weak law.
- Hypotheses. The strong law is a first-moment theorem (only a finite mean is needed), while the version of the weak law proved via Chebyshev needs a finite second moment. (The weak law also holds under a finite mean alone, by Khinchin's theorem, but the proof is harder.)
- Interpretation. The strong law is what justifies the [[Relative Frequency]] interpretation of [[Probability]] along one long run of trials, and the consistency of a single long [[Monte Carlo Estimator]] run.

# Properties
- Makes $\bar{X}_n$ a [[Consistent Estimator]] of $\mu$; applied to indicators, the [[Relative Frequency]] of an event is consistent for its probability.
- Says nothing about the size or shape of the fluctuations; the [[Central Limit Theorem]] adds that they are of order $\sigma/\sqrt{n}$ and approximately normal.
- Fails without a finite mean: the sample mean of the [[Cauchy Distribution]] does not converge.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=338)
