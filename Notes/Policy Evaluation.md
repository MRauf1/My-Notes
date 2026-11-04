---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Policy Evaluation[^1]
> The problem of computing the [[Value Function]] $V^\pi$ of a fixed [[Policy]] $\pi$ in a [[Markov Decision Process]] $M = (\mathcal{S}, \mathcal{A}, P, R, \gamma)$.

# Properties
- Since $\mathcal{S}$ is finite, fixing an order of states lets $V^\pi$ be treated as a vector in $\mathbb{R}^{|\mathcal{S}|}$, admitting a matrix-vector form of the [[Bellman Equation (Policy Evaluation)|Bellman equation]]:
$$
\begin{align}
V^\pi = R^\pi + \gamma P^\pi V^\pi
\end{align}
$$
using the policy's [[Transition Matrix (Markov Decision Process)|transition matrix]] $P^\pi$ and reward vector $R^\pi$.
- $(I_{|\mathcal{S}|} - \gamma P^\pi)$ is always invertible, giving $V^\pi$ a closed-form analytical solution:
$$
\begin{align}
V^\pi = (I_{|\mathcal{S}|} - \gamma P^\pi)^{-1} R^\pi
\end{align}
$$
- When the reward function depends only on the current state ($R(s,a) = R(s)$), $R^\pi$ is independent of $\pi$, and the value of a policy is linear in rewards, with the rows of $(I_{|\mathcal{S}|} - \gamma P^\pi)^{-1}$ giving the linear coefficients — the [[Discounted State Occupancy|discounted state occupancy]].
- The policy evaluation step of [[Policy Iteration]] computes $Q^\pi$ this way before taking the [[Greedy Policy]] for the next iteration.
- $V^\pi$ is the fixed point of the state-value [[Bellman Evaluation Operator]] $V \mapsto R^\pi + \gamma P^\pi V$, and $(I_{|\mathcal{S}|} - \gamma P^\pi)^{-1} = \sum_{t \geq 0} \gamma^t (P^\pi)^t$ is its Neumann series.

# Questions
> [!question]- Why is $I_{|\mathcal{S}|} - \gamma P^\pi$ invertible for $\gamma < 1$, and what goes wrong at $\gamma = 1$?
> For $x \neq 0$: $\|(I - \gamma P^\pi)x\|_\infty \geq \|x\|_\infty - \gamma\|P^\pi x\|_\infty \geq (1 - \gamma)\|x\|_\infty > 0$, since each entry of $P^\pi x$ is a convex combination of entries of $x$. So the kernel is trivial. Equivalently, the Neumann series $\sum_t \gamma^t (P^\pi)^t$ converges because $\|P^\pi\|_\infty = 1$. At $\gamma = 1$, row-stochasticity gives $P^\pi \mathbf{1} = \mathbf{1}$, so $(I - P^\pi)\mathbf{1} = 0$ and the matrix is singular.

> [!question]- Application: On a connected undirected graph with symmetric weights $W$ and degree matrix $D$, take the random-walk policy $P^\pi = D^{-1}W$ (CS 542 project: LSTD with Laplacian features). Write $V^\pi$ in the eigenbasis of $L_{\mathrm{sym}} = I - D^{-1/2}WD^{-1/2}$ with eigenpairs $(\lambda_k, \psi_k)$, $\lambda_1 = 0$. Which features dominate as $\gamma \to 1$?
> $P^\pi = D^{-1/2}(I - L_{\mathrm{sym}})D^{1/2}$, so $u_k = D^{-1/2}\psi_k$ satisfies $P^\pi u_k = (1 - \lambda_k)u_k$, and the $u_k$ are orthonormal in $\langle x, y\rangle_D = x^\top D y$. Expanding $R^\pi = \sum_k c_k u_k$ with $c_k = u_k^\top D R^\pi$ gives
> $$
> \begin{align}
> V^\pi = (I - \gamma P^\pi)^{-1}R^\pi = \sum_k \frac{c_k}{1 - \gamma + \gamma\lambda_k}\, u_k.
> \end{align}
> $$
> Each mode $k > 1$ is suppressed relative to the constant mode by $\frac{1 - \gamma}{1 - \gamma + \gamma\lambda_k} \to 0$, faster for larger $\lambda_k$. So low-frequency (small-$\lambda_k$) Laplacian eigenvectors carry $V^\pi$ as $\gamma \to 1$. The basis diagonalizes the propagator exactly because $P^\pi$ is a function of $L_{\mathrm{sym}}$ up to similarity, i.e. they commute: the commutation criterion in its simplest instance.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 3](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=3)
