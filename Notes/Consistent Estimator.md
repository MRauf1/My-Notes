---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Consistent Estimator[^1]
> Let $X$ have cdf $F(x; \theta)$, $\theta \in \Omega$, let $X_1, \dots, X_n$ be a sample from it, and let $T_n$ be a [[Statistic]]. $T_n$ is a consistent estimator of $\theta$ if
> $$
> \begin{align}
> T_n \xrightarrow{P} \theta
> \end{align}
> $$
> ([[Convergence in Probability]]) for every $\theta \in \Omega$.

**Interpretation.** Yes, as you read it: a consistent estimator converges to the true parameter as $n \to \infty$, in the precise sense that for every tolerance $\epsilon > 0$ the probability that $T_n$ misses $\theta$ by at least $\epsilon$ goes to $0$. The convergence is probabilistic: an individual large-$n$ estimate can still miss, but the chance of that becomes negligible. (Strong consistency, $T_n \to \theta$ almost surely, is the stronger pathwise version.)

**Consistency vs. unbiasedness.**
- Unbiasedness, $E_\theta(T_n) = \theta$, is a finite-sample property: the average of the estimator over repeated samples equals the true parameter for every sample size $n$ ([[Unbiased Estimator]]).
- Consistency is an asymptotic property: the estimator's distribution collapses onto $\theta$ as $n \to \infty$, with no requirement at any fixed $n$.
- They are independent properties, and all four combinations occur ([[Bias and Consistency of an Estimator]]). Biased but consistent: $V = n^{-1}\sum_i (X_i - \bar{X})^2$ has $E(V) = \frac{n-1}{n}\sigma^2$, bias $-\sigma^2/n \to 0$, and $V \xrightarrow{P} \sigma^2$ ([[Sample Variance]]). Unbiased but inconsistent: an estimator centered on $\theta$ whose variance does not shrink, e.g. using only the first observation $X_1$ to estimate $\mu$.
- Consistency is the more essential of the two: "it is a poor estimator that does not approach its target as the sample size gets large", whereas a vanishing bias is often acceptable.

**Role of variance.** Neither definition mentions variance, but variance links them through the [[Mean Squared Error]], $E_\theta[(T_n - \theta)^2] = \text{bias}^2 + \text{variance}$ ([[Bias-Variance-MSE Decomposition of an Estimator]]). By [[Markov's Inequality]], $P(|T_n - \theta| \geq \epsilon) \leq \text{MSE}/\epsilon^2$, so if both the bias and the variance tend to $0$ the estimator is consistent. Unbiasedness constrains only the center of the distribution and allows arbitrarily large variance; consistency needs the whole distribution to shrink onto $\theta$, and an estimator whose variance does not vanish keeps fluctuating and cannot be consistent (MSE $\to 0$ is sufficient, though not strictly necessary).

**Consistency vs. asymptotic unbiasedness.** An estimator is asymptotically unbiased if $\lim_{n\to\infty} E_\theta(T_n) = \theta$. Consistency does not imply asymptotic unbiasedness.
- $T_n \xrightarrow{P} \theta$ controls where most of the probability lies, while $E(T_n)$ can be dominated by rare, exploding values. For example, let $T_n = \theta$ with probability $1 - 1/n$ and $T_n = n^2$ with probability $1/n$. Then $T_n \xrightarrow{P} \theta$, but $E(T_n) \to \infty$.
- Convergence of expectations requires an extra condition, such as uniform integrability of $\{T_n\}$ (e.g. bounded support, or $\sup_n E|T_n|^{1+\epsilon} < \infty$).
- The converse also fails: asymptotic unbiasedness does not imply consistency (e.g. $T_n = X_1$).
- Consistency together with uniform integrability gives asymptotic unbiasedness. An asymptotically unbiased estimator whose variance tends to $0$ is consistent.

# Properties
- By the [[Weak Law of Large Numbers]], the [[Sample Mean]] is consistent for $\mu$ when the variance is finite; $S^2$ is consistent for $\sigma^2$.
- Preserved by continuous functions: if $T_n \xrightarrow{P} \theta$ and $g$ is continuous at $\theta$, then $g(T_n)$ is consistent for $g(\theta)$ ([[Convergence in Probability]]); unbiasedness is not preserved by nonlinear $g$.
- Vector parameters: $(\bar{X}_n, S_n^2)$ is consistent for $(\mu, \sigma^2)$, since convergence in probability of a vector is componentwise.[^2]
- Maximum likelihood estimators are consistent under regularity conditions ([[Maximum Likelihood Estimation Properties]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=340)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=366)
