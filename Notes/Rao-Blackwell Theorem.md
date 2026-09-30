---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Rao-Blackwell Theorem[^1]
> Let $X_1, \dots, X_n$, with $n$ a fixed positive integer, be a random sample from a distribution (continuous or discrete) with pdf or pmf $f(x; \theta)$, $\theta \in \Omega$. Let $Y_1 = u_1(X_1, \dots, X_n)$ be a [[Sufficient Statistic]] for $\theta$, and let $Y_2 = u_2(X_1, \dots, X_n)$, not a function of $Y_1$ alone, be an [[Unbiased Estimator]] of $\theta$. Then $E(Y_2 | y_1) = \varphi(y_1)$ defines a statistic $\varphi(Y_1)$, which:
> - is a function of the sufficient statistic $Y_1$;
> - is an unbiased estimator of $\theta$;
> - has variance less than or equal to that of $Y_2$.

Proof:[^2] this is Theorem 2.3.1 with $X_1 = Y_1$ and $X_2 = Y_2$. By the [[Law of Total Expectation]] and the [[Law of Total Variance]],
$$
\begin{align}
\theta = E(Y_2) = E[\varphi(Y_1)], \qquad \text{Var}(Y_2) \geq \text{Var}[\varphi(Y_1)]
\end{align}
$$
Sufficiency is what makes $\varphi(Y_1)$ a statistic. The conditional distribution of $Y_2$ given $Y_1$ is free of $\theta$, so $\varphi$ does not involve the unknown $\theta$.[^3]

Conditioning on a sufficient statistic averages out the part of $Y_2$'s variability that carries no information about $\theta$. That is the within-slice term $E[\text{Var}(Y_2 | Y_1)]$, and removing it leaves an estimator that is at least as good.

**Consequence.**[^4] When searching for a [[Minimum Variance Unbiased Estimator|MVUE]], if a sufficient statistic exists, the search can be restricted to functions of it. Any unbiased estimator can be improved, or at least not made worse, by "Rao-Blackwellizing" it. It is not necessary to first find some unbiased $Y_2$ and condition it. The theorem only shows that functions of $Y_1$ are the right place to look.[^5] In most cases there is only one unbiased function of $Y_1$, which makes that function the MVUE ([[Lehmann-Scheffé Theorem]]).[^6]

# Properties
- The inequality is strict unless $Y_2 = \varphi(Y_1)$ with probability one, since $E[\text{Var}(Y_2 | Y_1)] = 0$ only in that case.
- Remark 7.3.1 (conditioning on a non-sufficient statistic):[^7] let $Y_3$ be a statistic that is not sufficient and set $\Upsilon(y_3) = E[\varphi(Y_1) | Y_3 = y_3]$. Then $E[\Upsilon(Y_3)] = \theta$ and $\Upsilon(Y_3)$ has smaller variance than $\varphi(Y_1)$. However, the conditional distribution of $Y_1$ given $Y_3$ depends on $\theta$. So $\Upsilon(Y_3)$ involves the unknown $\theta$ and is not a statistic at all, and it cannot be used as an estimate.
- Generalizes to any convex [[Loss Function|loss]]. By [[Jensen's Inequality]], $E\{L[\theta, E(Y_2 | Y_1)]\} \leq E\{L[\theta, Y_2]\}$, so the risk never increases ([[Risk Function (Statistics)]]). Unbiasedness is not needed for this version.
- In Monte Carlo methods, Rao-Blackwellization means replacing a sampled quantity by its conditional expectation when that expectation is available in closed form. It reduces variance for the same reason.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=443&annotation=2UJZLNP3)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=442&annotation=2SDQQHCE)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=443&annotation=DX9KAPE2)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=443&annotation=D3GHXUHH)
[^5]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=443&annotation=CHCJR8NK)
[^6]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=444&annotation=59F9MZM3)
[^7]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=444&annotation=AW4KYML6)
