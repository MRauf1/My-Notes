---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Bounded in Probability[^1]
> A sequence of random variables $\{X_n\}$ is bounded in probability if for every $\epsilon > 0$ there exist a constant $B_\epsilon > 0$ and an integer $N_\epsilon$ such that
> $$
> \begin{align}
> n \geq N_\epsilon \implies P[|X_n| \leq B_\epsilon] \geq 1 - \epsilon
> \end{align}
> $$
> This is written $X_n = O_p(1)$.

No mass escapes to infinity: for any tolerance, a single bound contains all but $\epsilon$ of the probability for all large $n$ (also called uniform tightness). It is the stochastic analogue of a bounded sequence, i.e. of [[Big O]] $O(1)$.

# Properties
- If $X_n \xrightarrow{D} X$ for some random variable $X$, then $\{X_n\}$ is bounded in probability.[^1]
- If $\{X_n\}$ is bounded in probability and $Y_n \xrightarrow{P} 0$, then $X_n Y_n \xrightarrow{P} 0$: $O_p(1)\,o_p(1) = o_p(1)$.[^2]
- If $\{Y_n\}$ is bounded in probability and $X_n = o_p(Y_n)$, then $X_n \xrightarrow{P} 0$ ([[Little O]]).[^3]
- Used in the proof of the [[Delta Method]]: $\sqrt{n}(X_n - \theta)$ converges in distribution, hence is $O_p(1)$, so $X_n - \theta = O_p(n^{-1/2})$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=349)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=350)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=351)
