---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Coarsest Bisimulation Uniqueness Theorem[^1]
> For a given MDP $M$, there is a unique coarsest [[Model-Irrelevant Abstraction|model-irrelevant abstraction]] (bisimulation): one of which every other bisimulation of $M$ is a refinement.

# Properties
- **Proof.** It suffices to show that for any two bisimulations $\phi_1, \phi_2$, their *common coarsening* $\phi_{12}$ is a bisimulation. The coarsest bisimulation is then the common coarsening of all of them; finitely many exist, since $\mathcal{S}$ is finite.
  - $s^{(1)} \sim_{\phi_{12}} s^{(2)}$ iff there is a chain $s^{(1)} \sim_{\phi_{i_1}} s_1 \sim_{\phi_{i_2}} \cdots \sim_{\phi_{i_{n+1}}} s^{(2)}$ with each $i_j \in \{1, 2\}$. This is the transitive closure, i.e. the join of the two [[Equivalence Relation|equivalence relations]].
  - The reward condition is immediate. For transitions, it suffices to show $P(y' \mid s_A, a) = P(y' \mid s_B, a)$ for adjacent states $s_A, s_B$ in the chain, say $s_A \sim_{\phi_1} s_B$, and every $\phi_{12}$-class $y'$. Equality then propagates along the chain.
  - Each $\phi_{12}$-class is a disjoint union of complete $\phi_1$-classes, so
  $$
  \begin{align}
  P(y' \mid s_A, a) = \sum_{x' \in \phi_1(\phi_{12}^{-1}(y'))}\ \sum_{s' \in \phi_1^{-1}(x')} P(s' \mid s_A, a) = \sum_{x'}\ \sum_{s' \in \phi_1^{-1}(x')} P(s' \mid s_B, a) = P(y' \mid s_B, a),
  \end{align}
  $$
  using that $\phi_1$ is a bisimulation and $\phi_1(s_A) = \phi_1(s_B)$.
- Existence and uniqueness do not make it easy to compute: finding the coarsest bisimulation is NP-hard, and so is finding the minimal $\epsilon$-approximate bisimulation.

# Questions
> [!question]- Why must the common coarsening be defined through chains, and not just "equivalent under $\phi_1$ or $\phi_2$"?
> "Equivalent under $\phi_1$ or under $\phi_2$" is reflexive and symmetric but not transitive. $s \sim_{\phi_1} t$ and $t \sim_{\phi_2} u$ need not give $s \sim_{\phi_1} u$ or $s \sim_{\phi_2} u$, so it is not an equivalence relation and does not define an abstraction. The transitive closure (chains of hops) is the smallest equivalence relation containing both, i.e. the finest common coarsening. The 2025 update to the source fixes a proof that had overlooked this.

> [!question]- In the proof, where is it used that each $\phi_{12}$-class is a union of *complete* $\phi_1$-classes?
> To rewrite $P(y' \mid s, a)$ as a sum over $\phi_1$-classes $x'$ of $P(x' \mid s, a)$. Each such term is equal for $s_A$ and $s_B$ because $\phi_1$ is a bisimulation. If a $\phi_1$-class were split across two $\phi_{12}$-classes, the inner sums would be partial sums of a $\phi_1$-class, about which the bisimulation condition says nothing.

[^1]: [Jiang, Notes on State Abstractions (CS 542 notes), pp. 3–5](https://nanjiang.cs.illinois.edu/files/cs542f22/note4.pdf#page=4)
