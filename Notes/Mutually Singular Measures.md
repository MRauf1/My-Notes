---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Mutually Singular Measures[^1]
> Two [[Measure (Measure Theory)|measures]] $\mu$ and $\nu$ on a measurable space $(\Omega, \mathcal{F})$ are **mutually singular**, written $\mu \perp \nu$, if there is a measurable set $A \in \mathcal{F}$ such that
> $$
> \begin{align}
> \mu(A) = 0 \quad \text{and} \quad \nu(\Omega \setminus A) = 0
> \end{align}
> $$
> i.e. $\Omega$ splits into two disjoint pieces, one carrying all of $\nu$ and the other carrying all of $\mu$. For probability distributions $P \perp Q$: there is an event that has probability $1$ under $Q$ and probability $0$ under $P$, so the two distributions "live on" disjoint sets.

A distribution is called **singular** (without qualification) when it is singular with respect to [[Lebesgue Measure]] $\lambda$: it concentrates all of its mass on a set of zero volume, so it has no [[Probability Density Function|pdf]]. It is the opposite extreme of an [[Absolutely Continuous Measure|absolutely continuous]] distribution.

# Types
- **Discrete vs. continuous**: any distribution with countable support (a [[Probability Mass Function|pmf]]) is singular with respect to $\lambda$ on $\mathbb{R}^D$, since countable sets have volume zero.
- **Lower-dimensional support**: a distribution on a $k$-dimensional [[Manifold|manifold]] in $\mathbb{R}^D$ with $k < D$ (e.g. a curve in $\mathbb{R}^2$) is singular with respect to $\lambda$. More generally, the pushforward of any distribution under a locally [[Lipschitz Continuity|Lipschitz]] map $\mathbb{R}^k \to \mathbb{R}^D$, $k < D$, is singular, since Lipschitz maps do not increase Hausdorff dimension ([[Manifold Hypothesis]]).
- **Singular continuous**: a distribution can have no atoms and still be singular, e.g. the Cantor distribution supported on the [[Cantor Set]] (volume zero), whose cdf is continuous but has derivative $0$ almost everywhere.

# Properties
- Symmetric: $\mu \perp \nu \iff \nu \perp \mu$ (take $\Omega \setminus A$).
- If $\mu \perp \nu$ and $\mu \ll \nu$ ([[Absolutely Continuous Measure|absolute continuity]]), then $\mu = 0$; the two notions are opposite extremes.
- **Lebesgue decomposition**: for $\sigma$-finite $\mu, \nu$, there is a unique split $\nu = \nu_{\mathrm{ac}} + \nu_{\mathrm{s}}$ with $\nu_{\mathrm{ac}} \ll \mu$ and $\nu_{\mathrm{s}} \perp \mu$. With $\mu = \lambda$, any distribution on $\mathbb{R}$ is a mixture of a discrete part, an absolutely continuous part (with a pdf), and a singular continuous part.
- **Divergences** between $P \perp Q$:
	- [[Kullback-Leibler Divergence]]: $D_{\mathrm{KL}}(P \| Q) = \infty$ (it is already infinite whenever $P \not\ll Q$).
	- [[Jensen-Shannon Divergence]]: saturates at $\log 2$, giving no gradient.
	- Total variation: $\sup_A |P(A) - Q(A)| = 1$, its maximum.
	- [[Wasserstein Distance]]: stays finite and reflects how far apart the supports are, which is why it is used for such pairs ([[Wasserstein GAN]]).
- **Consequence for learning**: real data concentrated on a low-dimensional manifold ([[Manifold Hypothesis]], [[Intrinsic Dimension]]) is (nearly) singular with respect to $\lambda$, and so mutually singular with a full-dimensional model density. Density-based objectives such as [[Maximum Likelihood Estimation|maximum likelihood]] then become ill-posed ([[Manifold Overfitting]], [[Maximum Likelihood Loss Optimality and Failure Modes]], [[Normalizing Flow]]).

[^1]: Supplementary notes provided by the creator.
