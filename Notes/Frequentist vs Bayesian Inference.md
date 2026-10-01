---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Frequentist vs Bayesian Inference
> Both frameworks share the model $p(x \mid \theta)$ and hence the [[Likelihood Function]], but they slice the joint $p(\theta, x) = p(x \mid \theta)\,p(\theta)$ in orthogonal directions:
> - Frequentist (vertical slice): hold $\theta$ fixed at its unknown true value and study a procedure $\delta(X)$ over all datasets that could have been observed, $X \sim p(x \mid \theta)$. Bias, variance, [[Mean Squared Error]], coverage, and the [[Rao-Cramér Lower Bound]] are all properties of this slice.
> - Bayesian (horizontal slice): hold the data fixed at the observed $x$ and ask what is plausible about $\theta$. The posterior $p(\theta \mid x) \propto p(x \mid \theta)\,p(\theta)$ is this slice, renormalized.

![[Frequentist and Bayesian Slices.png]]

The frameworks are not the same question asked in different coordinates. They ask different questions:
- Frequentist: how good is my method across hypothetical repetitions?
- Bayesian: what should I believe given this dataset?

A simulated coverage study combines them. It checks intervals built from horizontal slices by averaging over many vertical draws.

**Not a change of basis.** Spatial and spectral representations are an invertible transform of the same information: Parseval's theorem guarantees that nothing is gained or lost. Bayesian and frequentist inference are not like that. Each adds something that the likelihood alone does not contain:
- The Bayesian adds a prior $p(\theta)$.
- The frequentist adds a reference set: the collection of hypothetical datasets that procedures are evaluated over. It depends on the experimental design and the stopping rule.

The clearest evidence is the [[Likelihood Principle]]. Two designs with proportional likelihoods give identical posteriors but different p-values.

**Average-case vs worst-case.** Bayesian analysis is average-case analysis over $\theta$, weighted by the prior. Frequentist analysis is closer to worst-case analysis: a guarantee such as "this interval covers 95% of the time" must hold at every $\theta$, including an adversarially chosen one.

# Properties
- Exact bridge through the [[Bayes Risk]]. Integrating the loss over the joint in the two orders ([[Fubini's Theorem]]) gives the prior average of the frequentist [[Risk Function (Statistics)|risk]], and also the marginal average of the Bayesian posterior expected loss.
  - So the [[Bayes Estimator]] minimizes average frequentist risk.
  - The frameworks part ways at the outer integral over $\theta$. The Bayesian performs it; the frequentist refuses and is left with a risk curve $R(\theta, \delta)$.
  - Collapsing that curve needs an extra criterion:
    - unbiasedness plus minimum variance ([[Minimum Variance Unbiased Estimator]]);
    - worst-case risk ([[Minimax Decision Rule]]);
    - non-domination ([[Admissible Decision Rule]]).
- Bayes rules generate the good frequentist procedures, and frequentist criteria evaluate Bayesian procedures. Minimax rules are Bayes under a least favorable prior, and admissible rules are Bayes or limits of Bayes (complete class theorems). So the relationship is not one of subsets.
- Exact agreement: in location and scale families, [[Probability Matching Prior|probability matching priors]] give credible intervals with exact or approximate frequentist coverage. This is agreement due to the model's symmetry.
- Asymptotic agreement holds in regular models ([[Bernstein-von Mises Theorem]]). It fails under non-identifiability, misspecification, and in high-dimensional or nonparametric models.
- They agree when the shared likelihood dominates (large $n$, regular model). They diverge when it does not (small $n$, weak identifiability, misspecification).
- The frequentist answer depends on unobserved datasets that could have occurred; the Bayesian answer depends only on the observed data. See [[Birnbaum's Theorem]] for the foundational tension.
- Philosophical bases: [[Probability Frequentist Framework]] and [[Probability Bayesian Framework]]. Notation: $f(x; \theta)$ for the frequentist and $f(x \mid \theta)$ for the Bayesian ([[Parameter Space]]).
