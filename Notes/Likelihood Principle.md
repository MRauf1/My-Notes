---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Likelihood Principle
> All the evidence about $\theta$ in an observed $x$ is contained in the [[Likelihood Function]] $L(\theta; x)$. If two experiments give observations $x$ and $y$ with $L_1(\theta; x) = c(x, y)\,L_2(\theta; y)$ for all $\theta$, i.e. proportional likelihoods, then they must lead to identical inferences about $\theta$.

Bayesian inference obeys the principle automatically. The posterior $\propto L(\theta; x)\,p(\theta)$ depends on the data only through the likelihood, up to a constant; it lives on the horizontal slice. Frequentist procedures generally violate it, because p-values, coverage, and bias average over datasets that were not observed, and those datasets depend on the design ([[Frequentist vs Bayesian Inference]]).

**Stopping-rule example.** A coin gives 9 heads and 3 tails.
- Design A fixes 12 flips, so the data are [[Binomial Distribution|binomial]].
- Design B flips until the 3rd tail, so the data are [[Negative Binomial Distribution|negative binomial]].
- Both likelihoods are $\propto \theta^9(1-\theta)^3$, so every Bayesian analysis with the same prior agrees.
- The one-sided [[P-Value|p-values]] for $H_0 : \theta = 0.5$ differ: $P(X \geq 9) = 299/4096 \approx 0.073$ for A, and $\approx 0.033$ for B. At level $0.05$, one researcher rejects and the other does not, from identical data.

# Properties
- Follows from the sufficiency and conditionality principles ([[Birnbaum's Theorem]]).
- Maximum likelihood point estimates obey the principle: both designs give $\hat{\theta} = 9/12$. Frequentist evaluations of them (standard errors, tests, coverage) need not.
- Frequentist methods break the principle whenever the stopping rule or reference set matters. Whether this is a flaw or a feature is one of the deepest debates in the foundations of statistics.
