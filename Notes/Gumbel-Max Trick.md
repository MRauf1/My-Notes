---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Exponential Race / Gumbel Trick[^1]
> Given unnormalized weights $q_1, \dots, q_N > 0$, to sample an index with probability $p_k = q_k / \sum_{j=1}^N q_j$, draw $E_j \overset{\text{iid}}{\sim} \mathrm{Exp}(1)$ and return
> $$
> \begin{align}
> k = \operatorname*{argmin}_j \frac{E_j}{q_j}
> \end{align}
> $$
> With log-weights $t_j = \log q_j$, this is equivalently
> $$
> \begin{align}
> k = \operatorname*{argmax}_j \,(t_j + G_j), \qquad G_j = -\log E_j
> \end{align}
> $$
> where the $G_j$ are iid standard [[Gumbel Distribution|Gumbel]].

It never forms the normalized $p_k$, and the log form is stable when the $q_k$ span many orders of magnitude. It suits settings where only one sample is drawn before the target distribution changes, where setting up a guide table (tabulated [[Inverse Transform Sampling|inversion]]) is not worth it.

# Properties
- Why it works: $E_j/q_j \sim \mathrm{Exp}$ with rate $q_j$, and among independent exponentials the minimum is attained at index $j$ with probability proportional to its rate ([[Exponential Distribution]]).
- Costs $N$ exponential draws per sample.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=21&annotation=SRMUKQYD)
