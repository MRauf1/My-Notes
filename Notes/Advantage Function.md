---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Advantage Function
> For a [[Markov Decision Process]] and [[Policy]] $\pi$, the advantage of action $a$ at state $s$ over $\pi$ is
> $$
> \begin{align}
> A^\pi(s,a) := Q^\pi(s,a) - V^\pi(s)
> \end{align}
> $$
> The advantage of a policy $\pi'$ over $\pi$ at state $s$ is $A^\pi(s, \pi') := A^\pi(s, \pi'(s))$.

# Properties
- $A^\pi(s, \pi(s)) = 0$, since $Q^\pi(s,\pi(s)) = V^\pi(s)$.
- Central to the [[Performance Difference Lemma]], which expresses the value difference between two policies as an expectation of an advantage.
- In [[Policy Iteration]], the advantage of the new (greedy) policy over the old one is nonnegative by construction, which underlies the [[Policy Improvement Theorem]].
