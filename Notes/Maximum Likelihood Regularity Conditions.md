---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Regularity Conditions for Maximum Likelihood Theory[^1][^2][^3]
> For $X_1, \dots, X_n$ iid with pdf $f(x; \theta)$, $\theta \in \Omega$, and true parameter $\theta_0$:
> - (R0) The cdfs are distinct: $\theta \neq \theta' \implies F(x; \theta) \neq F(x; \theta')$.
> - (R1) The pdfs have common support for all $\theta$.
> - (R2) $\theta_0$ is an interior point of $\Omega$.
> - (R3) $f(x; \theta)$ is twice differentiable as a function of $\theta$.
> - (R4) $\int f(x; \theta)\,dx$ can be differentiated twice under the integral sign with respect to $\theta$.
> - (R5) $f(x; \theta)$ is three times differentiable in $\theta$, and there are a constant $c$ and a function $M(x)$ with $\left|\frac{\partial^3}{\partial\theta^3}\log f(x; \theta)\right| \leq M(x)$ and $E_{\theta_0}[M(X)] < \infty$ for all $\theta_0 - c < \theta < \theta_0 + c$ and all $x$ in the support.

Interpretation: (R0) says the parameter identifies the distribution (identifiability), so different parameters are distinguishable from data. (R1) says the support does not depend on $\theta$; together with (R2)-(R4), $\theta$ does not appear in the endpoints of the region where $f > 0$, and differentiation with respect to $\theta$ can be interchanged with integration over $x$ ([[Interchange of Differentiation and Expectation]]). (R2) lets the likelihood be maximized at a stationary point rather than on the boundary. (R5) bounds the third derivative so that the Taylor remainder in the asymptotic expansion of the likelihood equation is negligible.

# Properties
- (R0)-(R1) give the [[Likelihood Maximization at True Parameter Theorem]]; (R0)-(R2) plus differentiability give consistency of a root of the likelihood equation; (R0)-(R4) give the [[Rao-Cramér Lower Bound]] and the identities for [[Fisher Information]]; (R0)-(R5) give [[Maximum Likelihood Estimator Asymptotic Normality]].
- For vector parameters, Hogg et al. add conditions (R6)-(R9) (Appendix A.1.1) analogous to these.
- A standard violation is the [[Continuous Uniform Distribution|uniform]] $U(0, \theta)$, whose support depends on $\theta$: its MLE $\max X_i$ converges at rate $1/n$, not $1/\sqrt{n}$, and is not asymptotically normal.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=372)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=379)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=384)
