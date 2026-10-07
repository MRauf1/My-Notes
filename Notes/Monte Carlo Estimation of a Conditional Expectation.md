---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Monte Carlo Estimation of a Conditional Expectation[^1]
> To estimate $\mu_A = E(f(X) \mid X \in A)$ from $n$ IID draws, let $A_i = 1_{X_i \in A}$ and $n_A = \sum_{i=1}^n A_i$. Treat the $n_A$ retained points as a sample from the conditional density $p_A(x) = p(x)1_{x\in A}/\int_A p(x)\,dx$:
> $$
> \begin{align}
> \hat{\mu}_A = \frac{1}{n_A}\sum_{i=1}^n A_i Y_i, \qquad s_A^2 = \frac{1}{n_A - 1}\sum_{i=1}^n A_i (Y_i - \hat{\mu}_A)^2
> \end{align}
> $$
> with $99\%$ [[Monte Carlo Confidence Interval|confidence interval]] $\hat{\mu}_A \pm 2.58\,s_A/\sqrt{n_A}$.

$n_A$ must be large enough for $\hat{\mu}_A$ and $s_A$ to be reasonable, but the randomness of $n_A$ need not be accounted for: the answer is almost identical to what the [[Ratio Estimator]] derivation gives, since $\hat{\mu}_A = \overline{AY}/\overline{A}$.

# Properties
- A ratio of two [[Simple Monte Carlo]] averages, hence slightly biased for finite $n$ ([[Ratio Estimator]]).
- Estimates the [[Conditional Expectation]] by [[Rejection Sampling|rejection]] of samples outside $A$; it becomes inefficient when $P(X \in A)$ is small.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=29&annotation=HIWD4375); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=29&annotation=H9T79ZRV)
