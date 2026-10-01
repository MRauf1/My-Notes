---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Birnbaum's Theorem
> The sufficiency principle and the conditionality principle together imply the [[Likelihood Principle]]:
> - Sufficiency principle: if $T$ is a [[Sufficient Statistic]] for $\theta$ and $T(x) = T(y)$, then $x$ and $y$ carry the same evidence about $\theta$.
> - Conditionality principle: if one of several experiments is chosen by a random mechanism that does not depend on $\theta$, then the evidence about $\theta$ depends only on the experiment actually performed.

Both frameworks accept sufficiency, and most statisticians find conditionality reasonable, since it amounts to conditioning on an [[Ancillary Statistic|ancillary]] coin flip. Yet frequentist methods still break the likelihood principle, e.g. through stopping rules. This makes the theorem a central point of tension in the foundations of statistics ([[Frequentist vs Bayesian Inference]]).

# Properties
- The converse also holds: the likelihood principle implies both principles.
- The theorem's validity has been contested. For example, Mayo (2014) argues that the frequentist versions of the premises do not jointly force the conclusion.
