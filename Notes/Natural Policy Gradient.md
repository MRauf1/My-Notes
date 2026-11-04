---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Natural Policy Gradient[^1]
> Natural policy gradient (NPG) measures parameter changes by the change in the induced action distributions $\pi_\theta(\cdot|s)$ (e.g. their [[Kullback-Leibler Divergence|KL divergence]]) rather than the Euclidean distance in $\theta$, which makes the update invariant to reparameterization. For the tabular softmax class (see [[Softmax Function]]), starting from the uniformly random policy, its update is, for $k = 1, 2, \dots$,
> $$
> \begin{align}
> \pi^{(k+1)}(a|s) \propto \pi^{(k)}(a|s)\exp\big(\eta\,Q^{\pi^{(k)}}(s,a)\big) \qquad \forall (s,a),
> \end{align}
> $$
> with learning rate $\eta$.

# Properties
- **Why "natural".** Plain gradient ascent is not invariant to reparameterization. In the extreme, if nearby parameters all induce the same policy, $\nabla J = 0$ at a non-optimal point (the parameterization obstacle in the [[Policy Gradient Stationary Point Suboptimality Bound]]). Measuring steps in distribution space removes this dependence.
- **Soft policy iteration.** The update acts in each state independently, moving $\pi(\cdot|s)$ slightly toward $\arg\max_a Q^{\pi^{(k)}}(s,a)$. As $\eta \to \infty$ it becomes [[Policy Iteration]].
- **Mirror descent view.** Up to rescaling of $\eta$, it is an independent run of entropic [[Mirror Descent]] in each state, with $\mathcal{X} = \mathcal{A}$, $p_k = \pi^{(k)}(\cdot|s)$, and $f_k = Q^{\pi^{(k)}}(s,\cdot)/V_{max}$. This gives the [[Natural Policy Gradient Convergence Bound]], which does not depend on $|\mathcal{S}|$ even though the softmax class is tabular.
- There is no standalone policy class: $\pi^{(k)} \propto \exp(\eta\sum_{j<k}Q^{\pi^{(j)}})$, so representing it requires keeping all previous Q-functions. With function approximation, the complexity is that of the class used to approximate $Q^\pi$.
- Like policy iteration, it is a planning algorithm when the $Q^{\pi^{(k)}}$ are exact. In learning, they are estimated from data.

[^1]: [Jiang, Notes on Importance Sampling and Policy Gradient (CS 542 notes), p. 10](https://nanjiang.cs.illinois.edu/files/cs542f23/note6.pdf#page=10)
