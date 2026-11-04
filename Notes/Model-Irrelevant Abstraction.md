---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Model-Irrelevant Abstraction (Bisimulation)[^1]
> A [[State Abstraction|state abstraction]] $\phi$ of an MDP $M$ is model-irrelevant if for all $s^{(1)}, s^{(2)}$ with $\phi(s^{(1)}) = \phi(s^{(2)})$, all $a \in \mathcal{A}$, and all $x' \in \mathcal{S}_\phi$,
> $$
> \begin{align}
> R(s^{(1)}, a) = R(s^{(2)}, a), \qquad \sum_{s' \in \phi^{-1}(x')} P(s' \mid s^{(1)}, a) = \sum_{s' \in \phi^{-1}(x')} P(s' \mid s^{(2)}, a),
> \end{align}
> $$
> i.e. $\Phi P(s^{(1)}, a) = \Phi P(s^{(2)}, a)$: aggregated states have the same rewards and the same distributions over *abstract* next states. Also called a (stochastic) **bisimulation**.

> [!info] $(\epsilon_R, \epsilon_P)$-Approximate Model-Irrelevance[^2]
> $\phi$ is an $(\epsilon_R, \epsilon_P)$-approximate model-irrelevant abstraction (approximate bisimulation) if for all $s^{(1)}, s^{(2)}$ with $\phi(s^{(1)}) = \phi(s^{(2)})$ and all $a$,
> $$
> \begin{align}
> |R(s^{(1)}, a) - R(s^{(2)}, a)| \leq \epsilon_R, \qquad \|\Phi P(s^{(1)}, a) - \Phi P(s^{(2)}, a)\|_1 \leq \epsilon_P.
> \end{align}
> $$

# Properties
- **Why not compare raw next-state distributions?** The naive condition $P(s' \mid s^{(1)}, a) = P(s' \mid s^{(2)}, a)$ for all $s' \in \mathcal{S}$ is sufficient but too strict. If $M$ is augmented with an irrelevant Markov chain $z$ (state $(x, z)$, rewards and $x$-dynamics ignoring $z$), then $\phi : (x, z) \mapsto x$ is a perfect abstraction. Yet it fails the naive condition whenever $z$ has state-dependent transitions. Comparing distributions *after* integrating out the aggregated factor accommodates it.
- **Factorization view.** Model-irrelevance holds exactly when the raw state factors into a relevant part $\phi(s)$ and an irrelevant remainder, with the relevant part's evolution and the reward not depending on the remainder.
- **Strictest notion** in the [[State Abstraction Hierarchy Theorem|hierarchy]]: implies [[Q-Star-Irrelevant Abstraction|$Q^\star$-irrelevance]]. It secures almost any tabular algorithm. Data from $M$ converted by $\phi$ is indistinguishable from data drawn from the [[Abstract Model (State Abstraction)|abstract model]] $M_\phi$ (a perfect compression), so guarantees transfer automatically.
- Can be checked *without* planning, unlike the other two notions.
- The class of Q-functions piecewise constant on the blocks of a bisimulation is [[Bellman Completeness|Bellman complete]], and the [[Concentrability Coefficient|relaxed concentrability]] for it only compares distributions over abstract state-action pairs.
- There is a unique coarsest bisimulation ([[Coarsest Bisimulation Uniqueness Theorem]]), but finding it, or the minimal $\epsilon$-approximate one, is NP-hard.
- **RKHS view.** $\phi$ induces the space $\mathcal{F}^\phi$ of functions that are piecewise constant on its classes. Two states are equivalent iff, for each action, their next-state distributions have the same embedding in $\mathcal{F}^\phi$. In other words, a kernel two-sample test using $\mathcal{F}^\phi$ cannot tell them apart.
- Generalizes to MDP homomorphisms, which also aggregate or permute actions. A related but different view uses bisimulation metrics.
- Its approximation error can be *non-monotone* under refinement. In function-approximation terms, it is a *closedness* (completeness) condition of the lifted function class under the Bellman operator, and adding functions can break closedness.
- Loss of the abstract model under approximate bisimulation: [[Approximate Bisimulation Abstract Model Loss Bound]].

# Questions
> [!question]- Why does model-irrelevance compare $\Phi P(s^{(1)}, a)$ and $\Phi P(s^{(2)}, a)$ rather than $P(s^{(1)}, a)$ and $P(s^{(2)}, a)$?
> Aggregated states should only need to agree on what the abstraction can see: rewards and the probability of landing in each *abstract* state. Requiring equal raw next-state distributions also demands agreement on the irrelevant part of the next state. For example, with an irrelevant Markov chain component $z$, the states $(x, z_1)$ and $(x, z_2)$ lead to different distributions over $z'$, yet the same distribution over $x'$. The raw condition is sufficient for model-irrelevance but not necessary.

> [!question]- Application: For a model-irrelevant $\phi$ and an abstract policy $\pi$ with lifted version $[\pi]$, show that the column span of $\Phi^\top$ (indicator features of the classes) is invariant under $P^{[\pi]}$, and explain why LSTD with these features is exact (CS 542 project: the analogue for Laplacian features).
> $(P^{[\pi]}\Phi^\top)(s, x) = \sum_{s' \in \phi^{-1}(x)} P(s' \mid s, \pi(\phi(s))) = [\Phi P(s, \pi(\phi(s)))]_x$, which depends on $s$ only through $\phi(s)$. So $P^{[\pi]}\Phi^\top = \Phi^\top P^\pi_\phi$ for the $|\mathcal{S}_\phi| \times |\mathcal{S}_\phi|$ abstract transition matrix $P^\pi_\phi$: $\operatorname{span}(\Phi^\top)$ is $P^{[\pi]}$-invariant. Rewards are also piecewise constant, $R^{[\pi]} = \Phi^\top R^\pi_\phi$.
>
> Hence the evaluation operator $V \mapsto R^{[\pi]} + \gamma P^{[\pi]}V$ maps $\operatorname{span}(\Phi^\top)$ into itself. Its fixed point $V^{[\pi]}$ lies in the span, so the projected fixed point equals $V^{[\pi]}$ for any projection weighting, with zero approximation error. Bisimulation is the indicator-feature case of an invariant subspace. Laplacian eigenvectors give exactness in the same way when they span a $P^\pi$-invariant subspace containing $R^\pi$, e.g. when $P^\pi$ commutes with the Laplacian.

[^1]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 2–4](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=2)
[^2]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 5–6](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=5)
