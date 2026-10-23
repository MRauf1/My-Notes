---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Absolutely Continuous Measure[^1]
> A [[Measure (Measure Theory)|measure]] $\nu$ is **absolutely continuous** with respect to a measure $\mu$ on $(\Omega, \mathcal{F})$, written $\nu \ll \mu$, if every $\mu$-null set is $\nu$-null:
> $$
> \begin{align}
> \mu(A) = 0 \implies \nu(A) = 0, \qquad A \in \mathcal{F}
> \end{align}
> $$
> $\mu$ is then said to **dominate** $\nu$. A distribution on $\mathbb{R}^D$ is called absolutely continuous (without qualification) when $\nu \ll \lambda$, the [[Lebesgue Measure]].

# Properties
- **Radon-Nikodym theorem**: for $\sigma$-finite $\mu, \nu$, $\nu \ll \mu$ if and only if there is a measurable $f \geq 0$ with $\nu(A) = \int_A f\,d\mu$ for all $A$. This $f = d\nu/d\mu$ is the Radon-Nikodym derivative, unique $\mu$-almost everywhere ([[Density with Respect to a Measure]]).
	- With $\mu = \lambda$, $d\nu/d\lambda$ is the [[Probability Density Function|pdf]]; with $\mu$ the counting measure, it is the [[Probability Mass Function|pmf]].
- The opposite extreme is [[Mutually Singular Measures|mutual singularity]]; the Lebesgue decomposition splits any $\sigma$-finite measure into an absolutely continuous part and a singular part.
- [[Kullback-Leibler Divergence]] $D_{\mathrm{KL}}(P \| Q) = \int \log \frac{dP}{dQ}\,dP$ is finite only if $P \ll Q$; [[Maximum Likelihood Estimation|maximum likelihood]] with model densities implicitly assumes the data distribution is absolutely continuous with respect to the same reference measure as the model.
- **Closed under convolution with a.c. noise**: if $\boldsymbol{\epsilon}$ has a density and is independent of $\mathbf{s}$, then $\mathbf{s} + \boldsymbol{\epsilon}$ has density $\int f_{\boldsymbol{\epsilon}}(\mathbf{x} - \mathbf{s})\,dP_{\mathbf{s}}(\mathbf{s})$, however singular $P_{\mathbf{s}}$ is; this is why noisy measurements (classical statistics) have densities while clean manifold data does not ([[Manifold Hypothesis]]).
- For distributions on $\mathbb{R}$, $P \ll \lambda$ is equivalent to the [[Cumulative Distribution Function|cdf]] being an absolutely continuous function, which is stronger than mere continuity (the Cantor distribution has a continuous cdf but no pdf).

[^1]: Supplementary notes provided by the creator.
