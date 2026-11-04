---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Doubly Robust Estimator (Contextual Bandit)[^1]
> Given a reward model $\hat{Q} : \mathcal{X}\times\mathcal{A} \to \mathbb{R}$, $\hat{Q}(x,a) \approx \mathbb{E}[r|x,a]$, that is fixed with respect to the evaluation data, the doubly robust (DR) estimate of $J(\pi)$ from one logged sample $(x,a,r)$ is
> $$
> \begin{align}
> \mathbb{E}_{a'\sim\pi}[\hat{Q}(x,a')] + \rho\big(r - \hat{Q}(x,a)\big), \qquad \rho = \frac{\pi(a|x)}{\pi_b(a|x)}.
> \end{align}
> $$

> [!info] Doubly Robust Estimator (Multi-Step)[^2]
> With $\rho_h = \pi(a_h|s_h)/\pi_b(a_h|s_h)$, an estimate $\hat{Q}^\pi$ of $Q^\pi$, and $v_0^{DR} := 0$, define recursively
> $$
> \begin{align}
> v^{DR}_{H-h+1} := \mathbb{E}_{a\sim\pi}[\hat{Q}^\pi(s_h, a)] + \rho_h\big(r_h + \gamma v^{DR}_{H-h} - \hat{Q}^\pi(s_h, a_h)\big).
> \end{align}
> $$
> Then $v^{DR}_H$ is an unbiased estimate of $J(\pi)$.

# Properties
- **Unbiasedness.** Since $\hat{Q}$ doesn't depend on the evaluation data, $\mathbb{E}[\rho\hat{Q}(x,a) \mid x] = \mathbb{E}_{a'\sim\pi}[\hat{Q}(x,a')]$, so the first term cancels in expectation and leaves the [[Inverse Propensity Score Estimator]] $\rho r$. IPS is DR with $\hat{Q} \equiv 0$. If $\hat{Q}$ is fitted from data, it must use a separate dataset.
- **"Doubly" robust.** It is unbiased if *either* $\rho$ is exact (with any $\hat{Q}$) *or* $\hat{Q}(x,a) = \mathbb{E}[r|x,a]$ (with any estimated ratio $\hat{\rho}(x,a)$, since then $\mathbb{E}[\hat{\rho}(r - \hat{Q}) \mid x,a] = 0$). This matters when $\pi_b$ is unknown and $\rho$ must be estimated.
- It is the [[Control Variates|control variate]] estimator with coefficient $1$: $\rho\hat{Q}(x,a)$ is the control, and its known mean $\mathbb{E}_{a'\sim\pi}[\hat{Q}(x,a')]$ is added back. The variance comes from $r - \hat{Q}$ rather than $r$.
- The multi-step version is bandit DR applied at each step of the recursive form of [[Per-Step Importance Sampling]], with the return-to-go estimate $r_h + \gamma v^{DR}_{H-h}$ as the "reward" (Jiang & Li 2016).

# Questions
> [!question]- Show that the bandit DR estimator is unbiased when $\rho$ is exact, for any fixed $\hat{Q}$.
> Condition on $x$: $\mathbb{E}_{a\sim\pi_b}[\rho\,\hat{Q}(x,a)] = \sum_a \pi_b(a|x)\frac{\pi(a|x)}{\pi_b(a|x)}\hat{Q}(x,a) = \mathbb{E}_{a'\sim\pi}[\hat{Q}(x,a')]$, which cancels the first term. What remains is $\mathbb{E}[\rho r] = J(\pi)$ by importance sampling. $\hat{Q}$ must not depend on the same sample. Otherwise $\rho\hat{Q}(x,a)$ correlates with $r$ and the cancellation fails.

> [!question]- Application: Paper 2's hybrid spectral control variate and the DR estimator share a template. What corresponds to what, and what condition does each need to stay unbiased?
> Both have the form "known mean of a surrogate + reweighted residual": $\alpha G + (f - \alpha g)/p$ with $\alpha = 1$. In DR, the surrogate is $\hat{Q}$, its exactly computable mean is $\mathbb{E}_{a\sim\pi}[\hat{Q}(x,a)]$, and the residual $r - \hat{Q}(x,a)$ is importance weighted by $\rho$. In the spectral hybrid, the truncated spectral solution plays $\hat{Q}$ (its contribution is computed exactly) and the random-walk estimator handles the residual. Either way, unbiasedness needs the surrogate to be fixed independently of the samples used for the residual. The variance then scales with the size of the residual, not of the original integrand.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), pp. 3–4](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=3)
[^2]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), p. 5](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=5)
