---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Importance Sampling[^1]
> To estimate $\mathbb{E}_{x\sim p}[f(x)]$ for $p \in \Delta(\mathcal{X})$ with samples from another distribution $q \in \Delta(\mathcal{X})$, assume $p$ is supported on $q$ ($p(x) > 0 \Rightarrow q(x) > 0$). The importance-weighted estimator
> $$
> \begin{align}
> \frac{p(x)}{q(x)}f(x), \qquad x \sim q,
> \end{align}
> $$
> is unbiased: $\mathbb{E}_{x\sim q}\big[\frac{p(x)}{q(x)}f(x)\big] = \sum_x p(x)f(x) = \mathbb{E}_{x\sim p}[f(x)]$. The ratio $p(x)/q(x)$ is the **importance weight** (importance ratio, inverse propensity score), and it always satisfies
> $$
> \begin{align}
> \mathbb{E}_{x\sim q}\Big[\frac{p(x)}{q(x)}\Big] = 1.
> \end{align}
> $$

# Properties
- The [[Monte Carlo Estimator]] $f(X)/p(X)$ for an integral is the special case where the target "distribution" is the base measure. Averaging $n$ i.i.d. weighted samples gives the usual $O(n^{-1/2})$ rate, with variance $\mathbb{E}_q[(p/q)^2 f^2] - (\mathbb{E}_p f)^2$.
- **Two uses of the term.** Traditionally, importance sampling means *designing* $q$ to get lower variance than sampling from $p$ (see [[Optimal Importance Sampling Distribution]]). In RL [[Off-Policy Evaluation]], $q$ is *given* (the behavior policy) and the weighted estimator usually has *higher* variance than on-policy Monte Carlo. There, "importance weighted" or "IPS estimator" is the more accurate name.
- If the support condition fails, the estimator is biased: it misses the mass of $p$ where $q = 0$ ([[Zero-Density Bias (Importance Sampling)]]).
- Normalizing the weights by their sum instead of by $n$ gives [[Self-Normalized Importance Sampling]].
- RL instances: [[Inverse Propensity Score Estimator]], [[Per-Trajectory Importance Sampling]], [[Per-Step Importance Sampling]].

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), p. 1](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=1)
