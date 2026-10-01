---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Minimax Principle[^1]
> A decision function $\delta_0(y)$ is a minimax decision function if
> $$
> \begin{align}
> \max_{\theta \in \Omega} R[\theta, \delta_0(y)] \leq \max_{\theta \in \Omega} R[\theta, \delta(y)]
> \end{align}
> $$
> for every other decision function $\delta(y)$, where $R$ is the [[Risk Function (Statistics)|risk function]].

A uniformly smallest risk function rarely exists, so the minimax principle summarizes each risk function by its worst case and chooses the rule with the smallest worst case. It is a conservative, game-theoretic criterion: it guards against the least favorable $\theta$, as if nature picked $\theta$ adversarially.

# Properties
- The maximum can be replaced by a supremum when it is not attained.
- A [[Bayes Estimator]] whose risk is constant in $\theta$ is minimax. Often the minimax rule is the Bayes rule for a least favorable prior, the prior that maximizes the [[Bayes Risk]] by putting its weight where estimation is hardest. In this sense, worst-case analysis is average-case analysis with a pessimistic prior ([[Frequentist vs Bayesian Inference]]).
- Minimax rules can be overly pessimistic. They may accept poor performance over most of $\Omega$ in exchange for protection in a small region of it.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=431&annotation=G2SSQ82C)
