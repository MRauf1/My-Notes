---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Bayes Estimator
> Let $\theta$ have prior $\pi(\theta)$ and posterior $\pi(\theta | \mathbf{x}) \propto f(\mathbf{x} | \theta)\pi(\theta)$ ([[Bayes' Theorem]]). For a [[Loss Function|loss]] $L(\theta, a)$, the Bayes estimator $\delta^\pi(\mathbf{x})$ minimizes the posterior expected loss:
> $$
> \begin{align}
> \delta^\pi(\mathbf{x}) = \underset{a}{\arg\min}\; E[L(\theta, a) | \mathbf{x}] = \underset{a}{\arg\min} \int_\Omega L(\theta, a)\,\pi(\theta | \mathbf{x})\,d\theta
> \end{align}
> $$
> Equivalently, it minimizes the Bayes risk $\int_\Omega R(\theta, \delta)\pi(\theta)\,d\theta$, the prior-weighted average of the frequentist [[Risk Function (Statistics)|risk]].

This is the Bayesian analogue of the [[Minimum Variance Unbiased Estimator]]. There is no unbiasedness constraint; optimality is defined by the choice of loss, and the estimate is conditioned on the data actually observed rather than averaged over hypothetical repeated samples.

| Loss $L(\theta, a)$ | Bayes estimator | Frequentist counterpart |
| --- | --- | --- |
| Squared error $(\theta - a)^2$ | Posterior mean $E(\theta \mid \mathbf{x})$ ([[Conditional Expectation]]) | MVUE / minimum [[Mean Squared Error]] |
| Absolute error $\lvert\theta - a\rvert$ | Posterior [[Median]] | Minimum mean absolute deviation |
| 0-1 loss $\mathbb{1}[\lvert\theta - a\rvert > \epsilon]$, $\epsilon \to 0$ | Posterior [[Mode]] (MAP) | [[Maximum Likelihood Estimation\|MLE]] (under a flat prior) |

# Properties
- MAP is a Bayesian point estimator but not, strictly speaking, a full Bayes estimator. It combines prior and likelihood via Bayes' theorem and returns the posterior peak ([[Maximum Likelihood vs Maximum a Posteriori Estimation]]).
  - In continuous spaces, it is the Bayes rule only in the limit of the degenerate 0-1 loss, which rewards exact hits only. So it is not Bayes-optimal for standard continuous losses.
  - It is also not invariant to reparametrization.
- Full Bayesian inference keeps the whole posterior ([[Bayesian Inference]], [[Predictive Distribution]]). Every Bayes estimator is a summary of the posterior chosen by the loss, and choosing a single point discards the posterior's uncertainty.
- From a frequentist standpoint, Bayes estimators are almost always biased, because they shrink toward the prior. With a [[Conjugate Prior]], the posterior mean is often a weighted average of the prior mean and the MLE. The weight on the data tends to $1$ as $n \to \infty$, so Bayes estimators are typically consistent and asymptotically equivalent to the MLE (Bernstein-von Mises).
- Frequentist evaluation:
  - A unique Bayes estimator with a proper prior is admissible.
  - A Bayes estimator with constant risk is minimax ([[Minimax Decision Rule]]).
  - Complete-class theorems: every admissible rule is Bayes or a limit of Bayes rules.
- The [[James-Stein Estimator]] can be derived as an empirical Bayes estimator.
