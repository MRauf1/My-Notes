---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Bernstein-von Mises Theorem
> Let $X_1, \dots, X_n$ be iid from $f(x; \theta_0)$ in a regular parametric model, with $\theta_0$ an interior point of $\Omega \subseteq \mathbb{R}^p$, [[Fisher Information Matrix]] $I(\theta_0)$ nonsingular, and a prior density that is continuous and positive near $\theta_0$. Then the posterior is asymptotically normal, centered at an efficient estimator (e.g. the [[Maximum Likelihood Estimation|MLE]] $\hat{\theta}_n$):
> $$
> \begin{align}
> \left\lVert \pi(\theta \mid X_1, \dots, X_n) - N_p\left(\hat{\theta}_n, \tfrac{1}{n}I^{-1}(\theta_0)\right) \right\rVert_{TV} \xrightarrow{P_{\theta_0}} 0
> \end{align}
> $$

The prior washes out, and the posterior matches the sampling distribution of the MLE ([[Maximum Likelihood Estimator Asymptotic Normality]]). So Bayesian credible intervals are asymptotically frequentist confidence intervals, and posterior means are asymptotically efficient. This is the asymptotic agreement of the two frameworks ([[Frequentist vs Bayesian Inference]]).

# Properties
- Regular settings only: a fixed number of identifiable parameters, a correctly specified model, and a true value not on the boundary of $\Omega$. Outside them, the frameworks can disagree even as $n \to \infty$:
  - Non-identifiability: along directions the data cannot inform, the posterior stays equal to the prior (or whatever is assumed), however much data arrives.
  - Misspecification: the posterior still concentrates, near the KL-closest parameter, but its width is $\frac{1}{n}I^{-1}$ rather than the true sampling variance. That variance is the sandwich $\frac{1}{n}I^{-1}JI^{-1}$, with $J$ the variance of the score. So credible intervals miscover even asymptotically. Frequentist sandwich variance estimates are designed for this case.
  - High-dimensional and nonparametric models: the theorem can fail, and posteriors can even be inconsistent (Diaconis and Freedman).
- The frequentist counterpart is the asymptotic normality and efficiency of the MLE ([[Rao-Cramér Lower Bound]]).
