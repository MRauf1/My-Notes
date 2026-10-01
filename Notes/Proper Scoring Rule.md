---
tags:
  - statistics
  - decision_theory
---

# Definition
> [!info] Proper Scoring Rule[^1]
> A loss $S(q, y)$ scoring a predicted distribution $q$ against a realized outcome $y$ is **proper** if, for every true distribution $p$, the expected score is minimized by reporting $q = p$:
> $$
> \begin{align}
> \mathbb{E}_{y \sim p}[S(q, y)] \geq \mathbb{E}_{y \sim p}[S(p, y)]
> \end{align}
> $$
> and **strictly proper** if equality holds only when $q = p$.

# Types
- Logarithmic score $S(q, y) = -\log q(y)$, i.e. the negative log-likelihood ([[Maximum Likelihood Loss Function Recipe]]), strictly proper by [[Kullback-Leibler Divergence|Gibbs' inequality]].
- Brier score $\sum_k (q_k - y_k)^2$, with $\mathbf{y}$ one-hot.
- Continuous ranked probability score $\mathrm{CRPS}(F, y) = \int_{-\infty}^{\infty} (F(t) - \mathbb{1}[t \geq y])^2\, dt$ for a predictive [[Cumulative Distribution Function|CDF]] $F$, generalizing the absolute error.

# Properties
- Strict propriety means the loss uniquely incentivizes honest, calibrated probability forecasts rather than over- or under-confident ones.
- Unlike the logarithmic score, the Brier score and CRPS are bounded for events assigned near-zero probability, avoiding an infinite penalty in the tails ([[Loss Function Taxonomy]]).

[^1]: Supplementary notes provided by the creator.
