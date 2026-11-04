---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] State Abstraction Finite Sample Bound[^1]
> Let $D = \{D_{s,a}\}$ be formed by sampling rewards and transitions from each $(s,a)$ a number of times that may vary with $(s,a)$ and may be zero. Given a [[State Abstraction|state abstraction]] $\phi$, let $D_{x,a} := \bigcup_{s\in\phi^{-1}(x)} D_{s,a}$ and define the effective sample size
> $$
> \begin{align}
> n_\phi(D) := \min_{x\in\mathcal{S}_\phi,\, a\in\mathcal{A}} |D_{x,a}|.
> \end{align}
> $$
> Let $\widehat{M}_\phi$ be the [[Certainty-Equivalence (Reinforcement Learning)|certainty-equivalence]] model over $\mathcal{S}_\phi$ built from $\phi$-converted data. Let $M_\phi$ be the [[Abstract Model (State Abstraction)|abstract model]] with weights proportional to the counts:
> $$
> \begin{align}
> R_\phi(x,a) = \frac{\sum_{\tilde{s}\in\phi^{-1}(x)}|D_{\tilde{s},a}|R(\tilde{s},a)}{|D_{x,a}|}, \qquad P_\phi(x' \mid x,a) = \frac{\sum_{\tilde{s}\in\phi^{-1}(x)}|D_{\tilde{s},a}|P(x' \mid \tilde{s},a)}{|D_{x,a}|}.
> \end{align}
> $$
> Then
> $$
> \begin{align}
> \left\|Q^\star_M - [Q^\star_{\widehat{M}_\phi}]_M\right\|_\infty \leq \underbrace{\left\|Q^\star_M - [Q^\star_{M_\phi}]_M\right\|_\infty}_{\text{approximation error}} + \underbrace{\left\|Q^\star_{M_\phi} - Q^\star_{\widehat{M}_\phi}\right\|_\infty}_{\text{estimation error}},
> \end{align}
> $$
> and with probability at least $1 - \delta$ the estimation error is at most $\frac{R_{max}}{(1-\gamma)^2}\sqrt{\frac{1}{2n_\phi(D)}\ln\frac{2|\mathcal{S}_\phi\times\mathcal{A}|}{\delta}}$.

# Properties
- The approximation error is bounded by the [[State Abstraction Hierarchy Theorem]] for approximate bisimulations, or the [[Q-Star-Irrelevant Abstract Model Bound]] for approximate $Q^\star$-irrelevance. It reflects how faithful $\phi$ is to $M$ and does not vanish with more data. Finer $\phi$ gives lower approximation error.
- The estimation error reflects how fast $\widehat{M}_\phi$ converges to its "expectation" $M_\phi$, and vanishes as $n_\phi(D) \to \infty$. It does not care whether $\phi$ is a legitimate representation of $M$, and coarser $\phi$ gives lower estimation error. The best balance depends on the sample size.
- The bound depends on $n_\phi(D)$ and the representation error, but not on the per-state sample sizes, which implicitly scale with $|\mathcal{S}|$. Even if $|D_{s,a}| = 0$ for many $(s,a)$, $n_\phi(D)$ can be large when $\phi$ aggregates aggressively and data are spread evenly over abstract states.
- **Estimation proof.** By contraction, $\|Q^\star_{M_\phi} - Q^\star_{\widehat{M}_\phi}\|_\infty \leq \frac{1}{1-\gamma}\|\mathcal{T}_{\widehat{M}_\phi}Q^\star_{M_\phi} - \mathcal{T}_{M_\phi}Q^\star_{M_\phi}\|_\infty$, with $Q^\star_{M_\phi}$ fixed (not data-dependent). Each entry is
$$
\begin{align}
\frac{1}{|D_{x,a}|}\sum_{s\in\phi^{-1}(x)}\sum_{(r,s')\in D_{s,a}}\Big(r + \gamma V^\star_{M_\phi}(\phi(s')) - R(s,a) - \gamma\langle P(s,a), [V^\star_{M_\phi}]_M\rangle\Big),
\end{align}
$$
  a centered average of independent variables in $[0, \frac{R_{max}}{1-\gamma}]$. They are *not* identically distributed, since samples from different $s \in \phi^{-1}(x)$ follow different laws, so the data in $D_{x,a}$ are not samples from $P_\phi(x,a)$. [[Hoeffding's Inequality]] needs only independence, so it applies; a union bound over $\mathcal{S}_\phi \times \mathcal{A}$ finishes.
- Extends the $|\mathcal{S}|$-free analysis of [[Certainty-Equivalence Sample Complexity]] to abstractions. Extending the analysis via uniform policy-evaluation error requires approximate bisimulation instead.

# Questions
> [!question]- Why is $M_\phi$ defined with weights proportional to $|D_{s,a}|$?
> So that it is the expectation of $\widehat{M}_\phi$ with respect to the data. $\widehat{R}_\phi(x,a)$ averages all rewards in $D_{x,a}$, and each $s \in \phi^{-1}(x)$ contributes $|D_{s,a}|$ of them, with mean $R(s,a)$. So $\mathbb{E}[\widehat{R}_\phi(x,a)]$ is the count-weighted average $R_\phi(x,a)$, and similarly for $P_\phi$. With these weights, the estimation error is a pure concentration term, and if all counts are scaled up by the same constant, $\widehat{M}_\phi \to M_\phi$.

> [!question]- Hoeffding's inequality is applied to data in $D_{x,a}$ that do not come from a single distribution. Why is this valid?
> Hoeffding's inequality requires independent bounded variables, not identically distributed ones. Under the sampling assumption, the tuples in $D_{x,a}$ are independent, and each $r + \gamma V^\star_{M_\phi}(\phi(s'))$ lies in $[0, \frac{R_{max}}{1-\gamma}]$ with its own mean $R(s,a) + \gamma\langle P(s,a), [V^\star_{M_\phi}]_M\rangle$. The bound controls the deviation of their average from the average of those means, which is exactly $(\mathcal{T}_{M_\phi}Q^\star_{M_\phi})(x,a)$.

[^1]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 9–11](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=9)
