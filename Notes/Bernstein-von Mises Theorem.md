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

In Gelman's informal form, the [[Central Limit Theorem]] put in a Bayesian context gives[^1]
$$
\begin{align}
\left(\frac{\theta - E(\theta \mid y)}{\sqrt{\text{var}(\theta \mid y)}} \,\middle|\, y\right) \to N(0, 1)
\end{align}
$$
which justifies approximating the [[Posterior Distribution]] by a normal distribution.

# Properties
- The normal approximation is more accurate after transforming $\theta$ to an unbounded scale, e.g. the [[Logit Function|logit]] $\log(\theta/(1-\theta))$ for a probability, which maps $[0, 1]$ to $(-\infty, \infty)$.[^1]
- Regular settings only: a fixed number of identifiable parameters, a correctly specified model, and a true value not on the boundary of $\Omega$. Outside them, the frameworks can disagree even as $n \to \infty$:
  - Non-identifiability: along directions the data cannot inform, the posterior stays equal to the prior (or whatever is assumed), however much data arrives.
  - Misspecification: the posterior still concentrates, near the KL-closest parameter, but its width is $\frac{1}{n}I^{-1}$ rather than the true sampling variance. That variance is the sandwich $\frac{1}{n}I^{-1}JI^{-1}$, with $J$ the variance of the score. So credible intervals miscover even asymptotically. Frequentist sandwich variance estimates are designed for this case.
  - High-dimensional and nonparametric models: the theorem can fail, and posteriors can even be inconsistent (Diaconis and Freedman).
- The frequentist counterpart is the asymptotic normality and efficiency of the MLE ([[Rao-Cramér Lower Bound]]).
[^1]: [Gelman et al., p. 35](zotero://open-pdf/library/items/HDF44SF4?page=45&annotation=RML66RPP)
