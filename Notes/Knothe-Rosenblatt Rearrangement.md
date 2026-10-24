---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!abstract] Knothe-Rosenblatt Rearrangement[^1]
> Let $\mu, \nu$ be [[Absolutely Continuous Measure|absolutely continuous]] probability measures on $\mathbb{R}^D$. Then there exists a [[Monotone Triangular Map|monotone triangular map]] $T$ with
> $$
> \begin{align}
> T_\# \mu = \nu
> \end{align}
> $$
> i.e. $\mathbf{x} \sim \mu \implies T(\mathbf{x}) \sim \nu$, and it is unique $\mu$-almost everywhere. It is built coordinate by coordinate from [[Conditional Distribution|conditional]] [[Cumulative Distribution Function|cdfs]]:
> $$
> \begin{align}
> T_1(x_1) &= F_{\nu, 1}^{-1}\left(F_{\mu, 1}(x_1)\right) \\
> T_i(x_1, \dots, x_i) &= F_{\nu, i \mid <i}^{-1}\Big(F_{\mu, i \mid <i}(x_i \mid x_{<i}) \;\Big|\; T_1(x_1), \dots, T_{i-1}(x_{<i})\Big), \quad i = 2, \dots, D
> \end{align}
> $$
> where $F_{\mu, i \mid <i}(\cdot \mid x_{<i})$ is the cdf of the $i$-th coordinate under $\mu$ given the first $i-1$, and $F^{-1}$ its [[Quantile Function|quantile function]].

Each step is the 1D map $G^{-1} \circ F$ (the [[Probability Integral Transform]] followed by [[Inverse Transform Sampling]]), applied to the conditional distributions given by the chain rule of probability $p(\mathbf{x}) = \prod_i p(x_i \mid x_{<i})$. Each $T_i$ is increasing in $x_i$ because cdfs and quantile functions are increasing.

# Properties
- **Rosenblatt transform**: taking $\nu$ to be uniform on $[0,1]^D$ gives $T_i = F_{\mu, i \mid <i}(x_i \mid x_{<i})$, the multivariate [[Probability Integral Transform]], which maps any absolutely continuous $\mu$ to independent uniforms.
- **Universality of triangular flows**: every density is the pushforward of a standard [[Multivariate Normal Distribution|normal]] under a single monotone triangular map, so triangular-Jacobian [[Normalizing Flow|normalizing flows]] ([[Autoregressive Flow]], [[Coupling Flow]]) lose no expressivity in the limit ([[Normalizing Flow Expressivity]]).
- **Existence, not regularity**: $T$ need not be continuous. If $\nu$ has disconnected support (separated modes), $T$ jumps between them, so a continuous neural flow can only approximate it.
- **Depends on the variable ordering**: permuting the coordinates gives a different map, with different smoothness; a good ordering makes the conditionals simpler.
- **Relation to optimal transport**: it is not the [[Wasserstein Distance|optimal-transport]] (Brenier) map, which is the gradient of a convex function with a symmetric Jacobian. It is the limit of optimal-transport maps for quadratic costs with increasingly unequal weights on the coordinates, $\sum_i \varepsilon^{i-1}(x_i - y_i)^2$ as $\varepsilon \to 0$.[^2]
- Requires $\nu$ to have a density; for a [[Mutually Singular Measures|singular]] target (data on a manifold), the conditional cdfs degenerate and the required map collapses volume ([[Manifold Hypothesis]]).

[^1]: Supplementary notes provided by the creator; Rosenblatt (1952); Knothe (1957); Bogachev, Kolesnikov & Medvedev (2005) in `REFERENCES.md`.
[^2]: Carlier, Galichon & Santambrogio (2010) in `REFERENCES.md`.
