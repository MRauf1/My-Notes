---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Decision Rule, Loss, and Risk[^1]
> Let $X_1, \dots, X_n$ be a random sample from $f(x; \theta)$, $\theta \in \Omega$, and let $Y = u(X_1, \dots, X_n)$ be a [[Statistic]].
> - A decision function (decision rule) $\delta$ maps the observed value $y$ to a point estimate $\delta(y)$ of $\theta$. The value $\delta(y)$ is called a decision.
> - A [[Loss Function|loss function]] assigns a nonnegative number $L[\theta, \delta(y)]$ to each pair $[\theta, \delta(y)]$, measuring how serious the difference between $\theta$ and $\delta(y)$ is.
> - The risk function is the expected loss,
> $$
> \begin{align}
> R(\theta, \delta) = E\{L[\theta, \delta(Y)]\} = \int_{-\infty}^\infty L[\theta, \delta(y)]\, f_Y(y; \theta)\,dy
> \end{align}
> $$
> with a sum for discrete $Y$.

The risk is a frequentist quantity. The parameter $\theta$ is held fixed, and the loss is averaged over the sampling distribution of the data. The result is a whole function of $\theta$, not a single number. Under squared-error loss $L = (\theta - \delta)^2$, the risk is the [[Mean Squared Error]] of $\delta(Y)$.

Ideally $\delta$ would minimize $R(\theta, \delta)$ for every $\theta \in \Omega$ simultaneously. This is usually impossible, because the rule that minimizes the risk at one $\theta$ need not do so at another. For example, the constant rule $\delta(y) \equiv \theta_0$ has zero risk at $\theta_0$ and large risk elsewhere. Without restrictions, it is hard to find a rule whose risk is uniformly below another's. The two ways out are:
- Restrict the class of rules, for example to unbiased estimators, which leads to the [[Minimum Variance Unbiased Estimator]].
- Order the risk functions by a scalar summary:
  - the worst case, $\max_\theta R(\theta, \delta)$ ([[Minimax Decision Rule]]);
  - a prior-weighted average, $\int R(\theta, \delta)\pi(\theta)\,d\theta$ ([[Bayes Estimator]]).

# Properties
- A rule $\delta$ is inadmissible if another rule $\delta'$ has $R(\theta, \delta') \leq R(\theta, \delta)$ for all $\theta$, with strict inequality for some $\theta$. Otherwise $\delta$ is admissible. The [[James-Stein Estimator]] shows that the sample mean of $p \geq 3$ normal means is inadmissible under squared-error loss.
- Complete-class theorems: under mild conditions, every admissible rule is a Bayes rule or a limit of Bayes rules.
- Part of statistical [[Decision Theory]]. The classification analogue, which averages the loss against a posterior, is the [[Minimum Expected Loss Decision Rule]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=430&annotation=HSYUFUCI)
