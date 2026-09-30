---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Basu's Theorem[^1]
> Let $X_1, \dots, X_n$ be a random sample from a distribution with pdf $f(x; \theta)$, $\theta \in \Omega$, where $\Omega$ is an interval set. Suppose $Y_1$ is a complete and [[Sufficient Statistic|sufficient statistic]] for $\theta$. Let $Z = u(X_1, \dots, X_n)$ be any other statistic, not a function of $Y_1$ alone. If the distribution of $Z$ does not depend on $\theta$ ([[Ancillary Statistic]]), then $Z$ is [[Independent Random Variable|independent]] of $Y_1$.

> [!abstract] Converse and Characterization[^2]
> If $Y_1$ is sufficient, then independence of $Y_1$ and $Z$ implies that the distribution of $Z$ does not depend on $\theta$, whether or not $\{g_1(y_1; \theta)\}$ is complete. So when the family of $Y_1$ is known to be complete (e.g. a [[Regular Exponential Class|regular exponential class]]), $Z$ is independent of $Y_1$ if and only if $Z$ is ancillary. This extends to $m$ parameters with $m$ joint complete sufficient statistics: $Z$ is independent of them if and only if its distribution is free of all $m$ parameters.

Proof idea: fix an event $A$ for $Z$, and let $h(Y_1) = P(Z \in A | Y_1) - P(Z \in A)$.
- By sufficiency, $h$ is a statistic, i.e. free of $\theta$.
- By ancillarity, $P(Z \in A)$ is a constant, and $E_\theta[h(Y_1)] = 0$ for all $\theta$.
- By completeness, $h \equiv 0$, which is independence.

A complete sufficient statistic and an ancillary statistic are opposites: one carries all the information about $\theta$, and the other carries none. Basu's theorem makes "no relationship" precise as statistical independence.

# Properties
- A standard tool for proving independence without computing joint distributions. For example, for $N(\theta, \sigma^2)$ with $\sigma^2$ known, $\bar{X}$ is complete sufficient and $S^2$ is location-invariant. So $\bar{X}$ and $S^2$ are independent, part of [[Student's Theorem]].
- Completeness is essential for the forward direction. With an incomplete sufficient statistic, an ancillary statistic can be dependent on it and informative about $\theta$.[^3]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=478&annotation=3U45IIG3)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=478&annotation=8ZYI42CM)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=479&annotation=A6EXWH9A)
