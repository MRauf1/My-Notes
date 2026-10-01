---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Admissible Decision Rule
> A decision rule $\delta'$ dominates $\delta$ if $R(\theta, \delta') \leq R(\theta, \delta)$ for all $\theta \in \Omega$, with strict inequality for some $\theta$, where $R$ is the [[Risk Function (Statistics)|risk function]]. $\delta$ is inadmissible if some rule dominates it, and admissible otherwise.

> [!abstract] Complete Class Theorems (Wald)
> Under mild regularity conditions (e.g. a compact parameter space or a finite one, and a continuous risk), essentially every admissible rule is a [[Bayes Estimator|Bayes rule]] or a limit of Bayes rules. The Bayes rules, together with their limits, form a complete class: every rule outside the class is dominated by one inside it.

Admissibility rules out estimators whose risk curve can be beaten everywhere by another. It is a minimal requirement, not an optimality criterion. Admissible rules are usually many, and they include silly ones: the constant $\delta \equiv \theta_0$ is admissible because nothing else has zero risk at $\theta_0$. A frequentist looking for a procedure that cannot be uniformly beaten will find it among Bayes rules.

# Properties
- A unique Bayes rule under a proper prior is admissible.
- Unbiased or maximum-likelihood estimators can be inadmissible. The sample mean of $p \geq 3$ normal means is dominated by the [[James-Stein Estimator]].
- Admissibility, [[Minimax Decision Rule|minimaxity]], and unbiasedness ([[Minimum Variance Unbiased Estimator]]) are the three frequentist ways to deal with risk curves that cross ([[Frequentist vs Bayesian Inference]]).
