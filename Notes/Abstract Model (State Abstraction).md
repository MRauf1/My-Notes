---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Abstract Model (State Abstraction)[^1]
> Given an MDP $M$, a [[State Abstraction|state abstraction]] $\phi$, and distributions $\{p_x : x \in \mathcal{S}_\phi\}$ with each $p_x$ supported on $\phi^{-1}(x)$, the abstract model is $M_\phi = (\mathcal{S}_\phi, \mathcal{A}, P_\phi, R_\phi, \gamma)$ with
> $$
> \begin{align}
> R_\phi(x, a) = \mathbb{E}_{s\sim p_x}[R(s, a)], \qquad P_\phi(x' \mid x, a) = \mathbb{E}_{s\sim p_x}[P(x' \mid s, a)],
> \end{align}
> $$
> where $P(x' \mid s, a) = [\Phi P(s,a)]_{x'}$ is the probability of landing in abstract state $x'$.

# Properties
- **Lemma.** If $\phi$ is an $(\epsilon_R, \epsilon_P)$-approximate [[Model-Irrelevant Abstraction|model-irrelevant abstraction]], then for any $\{p_x\}$ and all $s, a$:
$$
\begin{align}
|R_\phi(\phi(s), a) - R(s, a)| \leq \epsilon_R, \qquad \|P_\phi(\phi(s), a) - \Phi P(s, a)\|_1 \leq \epsilon_P.
\end{align}
$$
  Proof for transitions: with $q_s := \Phi P(s, a)$ and $x = \phi(s)$, $\|P_\phi(x,a) - q_s\|_1 = \|\sum_{\tilde{s}\in\phi^{-1}(x)} p_x(\tilde{s})(q_{\tilde{s}} - q_s)\|_1 \leq \sum_{\tilde{s}} p_x(\tilde{s})\epsilon_P = \epsilon_P$, by convexity of the norm.
- For an exact bisimulation, $M_\phi$ does not depend on $\{p_x\}$ and is a perfect compression of $M$.
- Certainty-equivalence on $\phi$-converted data estimates $M_\phi$ with weights $p_x(s) \propto |D_{s,a}|$ ([[State Abstraction Finite Sample Bound]]).
- Planning in $M_\phi$ and lifting the result: [[Approximate Bisimulation Abstract Model Loss Bound]] and [[Q-Star-Irrelevant Abstract Model Bound]].

[^1]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 5–6](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=5)
