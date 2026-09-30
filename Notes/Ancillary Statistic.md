---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Ancillary Statistic[^1]
> A [[Statistic]] $Z = u(X_1, \dots, X_n)$ is ancillary for $\theta$ if its distribution does not depend on $\theta$.

> [!info] Invariant Statistics[^2][^3]
> - Location-invariant: $u(x_1 + d, \dots, x_n + d) = u(x_1, \dots, x_n)$ for all real $d$.
> - Scale-invariant: $u(cx_1, \dots, cx_n) = u(x_1, \dots, x_n)$ for all $c > 0$.
> - Location- and scale-invariant: $u(cx_1 + d, \dots, cx_n + d) = u(x_1, \dots, x_n)$ for all $c > 0$ and real $d$.

Ancillary statistics are almost opposites of [[Sufficient Statistic|sufficient statistics]]. A sufficient statistic contains all the information about $\theta$, while an ancillary statistic has a distribution free of $\theta$ and, by itself, seemingly contains none.

Invariant statistics are ancillary for the matching model.[^4] Write $X_i = \theta + W_i$ for a location model, $X_i = \theta W_i$ for a scale model, or $X_i = \theta_1 + \theta_2 W_i$ for a location-scale model, with $W_i$ iid from a fixed distribution ([[Location Parameter]], [[Scale Parameter]]). The invariance removes $\theta$, so $Z = u(W_1, \dots, W_n)$, whose distribution is parameter-free. Examples:
- $S^2$ is ancillary for the $N(\theta, 1)$ location family.
- $X_1/(X_1 + X_2)$ is ancillary for the $\Gamma(\alpha, \theta)$ scale family, since it has a [[Beta Distribution]].
- $(X_i - \bar{X})/S$ is ancillary for a location-scale family.

# Properties
- By [[Basu's Theorem]], an ancillary statistic is independent of any complete sufficient statistic. So in that case it provides no information about $\theta$.
- If the sufficient statistic is not complete, an ancillary statistic can still be informative in combination with it, even though its marginal distribution is free of $\theta$.[^5] Conditioning inference on it (the conditionality principle) can then improve precision. The sample range in a uniform location model is a classic case.
- A nonconstant function of a complete statistic cannot be ancillary ([[Complete Family (Statistics)]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=473&annotation=8QGLKPLE)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=474&annotation=QEMSIC84)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=475&annotation=KDFUTFKW)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=475&annotation=RYVABG5V)
[^5]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=479&annotation=A6EXWH9A)
