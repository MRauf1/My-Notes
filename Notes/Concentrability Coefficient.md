---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Admissible Distribution[^1]
> A state-action distribution $\nu \in \Delta(\mathcal{S}\times\mathcal{A})$ is admissible if it can be generated at some time step from the initial distribution $d_0$, i.e. $\nu = d^\pi_h$ for some $h \geq 1$ and some (possibly non-stationary) [[Policy|policy]] $\pi$, where $d^\pi_h(s,a) := \Pr[s_h = s, a_h = a \mid s_1 \sim d_0, \pi]$.

> [!info] Concentrability Coefficient[^1]
> A data distribution $\mu \in \Delta(\mathcal{S}\times\mathcal{A})$ has concentrability coefficient $C$ if every admissible $\nu$ satisfies
> $$
> \begin{align}
> \forall (s,a) \in \mathcal{S}\times\mathcal{A}: \quad \frac{\nu(s,a)}{\mu(s,a)} \leq C, \qquad \text{i.e.} \quad \Big\|\frac{\nu}{\mu}\Big\|_\infty \leq C.
> \end{align}
> $$
> Consequently, $\|g\|_\nu \leq \sqrt{C}\,\|g\|_\mu$ for every $g$, where $\|g\|_{p,\nu} := (\mathbb{E}_{x\sim\nu}[|g(x)|^p])^{1/p}$ and $\|\cdot\|_\nu := \|\cdot\|_{2,\nu}$.

> [!info] Relaxed (Function-Class) Concentrability[^2]
> Given $\mathcal{F}$ and the [[Bellman Optimality Operator]] $\mathcal{T}$, $C$ can be redefined as any upper bound on
> $$
> \begin{align}
> \max_{\nu \text{ admissible}}\ \max_{f, f' \in \mathcal{F}}\ \frac{\|f - \mathcal{T}f'\|_\nu^2}{\|f - \mathcal{T}f'\|_\mu^2}.
> \end{align}
> $$

# Properties
- Formalizes "the batch data are exploratory": $\mu$ puts mass wherever any policy can go. It is the change-of-measure constant that moves the regression error controlled under $\mu$ to the distributions where the [[Fitted Q-Iteration Error Bound]] needs it. It is the per-step analogue of a bounded density ratio between $\mu$ and [[State-Action Occupancy|occupancies]].
- The relaxed definition suffices for [[Fitted Q-Iteration]], because the assumption is only ever used as $\|f - \mathcal{T}f'\|_\nu \leq \sqrt{C}\|f - \mathcal{T}f'\|_\mu$. It is never larger than the density-ratio $C$, and can be far smaller when $\mathcal{F}$ is structured:
  - For $\mathcal{F}$ induced by a [[Model-Irrelevant Abstraction|bisimulation]] (which is [[Bellman Completeness|Bellman complete]]), $f - \mathcal{T}f'$ is constant on abstract states, so the ratio only involves distributions over *abstract* state-action pairs.
  - For linear $\mathcal{F}$ with Bellman completeness, $f - \mathcal{T}f'$ is again linear, and the ratio measures coverage in feature space.

# Questions
> [!question]- Why does $\|\nu/\mu\|_\infty \leq C$ give $\|g\|_\nu \leq \sqrt{C}\|g\|_\mu$, and what goes wrong if $\mu(s,a) = 0$ at some $(s,a)$ an admissible $\nu$ charges?
> $\|g\|_\nu^2 = \sum_{s,a}\nu(s,a)g(s,a)^2 = \sum_{s,a}\mu(s,a)\frac{\nu(s,a)}{\mu(s,a)}g(s,a)^2 \leq C\|g\|_\mu^2$. If $\mu(s,a) = 0 < \nu(s,a)$, then $C = \infty$: the data say nothing about $g(s,a)$, so a regression fit can be arbitrarily wrong exactly where the policy goes.

> [!question]- Why must $C$ cover *all* admissible distributions, rather than only the occupancy of $\pi^\star$?
> The error analysis of FQI propagates $\|f_k - Q^\star\|_\nu$ back to $\|f_{k-1} - Q^\star\|_{P(\nu)\times\pi_{f_{k-1}, Q^\star}}$, shifting the distribution one step forward under policies that depend on the learned iterates (and the suboptimality decomposition already involves $d^{\hat{\pi}}_h$). These are not known in advance, so the data must cover every distribution reachable from $d_0$.

> [!question]- Application: for a linear, Bellman-complete class with features $\phi$ (e.g. Laplacian eigenvectors in the CS 542 LSTD project), what does the relaxed $C$ become?
> Completeness makes $f - \mathcal{T}f' = \phi^\top w$ for some $w$. With $\Sigma_\nu = \mathbb{E}_\nu[\phi\phi^\top]$ and $\Sigma_\mu \succ 0$, the ratio is the Rayleigh quotient $\frac{w^\top\Sigma_\nu w}{w^\top\Sigma_\mu w}$, so $C = \max_\nu \lambda_{\max}(\Sigma_\nu, \Sigma_\mu)$, the top eigenvalue of the symmetric pencil $(\Sigma_\nu, \Sigma_\mu)$. Since $\nu \leq C_{\text{raw}}\,\mu$ pointwise gives $\Sigma_\nu \preceq C_{\text{raw}}\Sigma_\mu$, it never exceeds the density-ratio coefficient, and depends only on $K$ feature directions rather than on $|\mathcal{S}\times\mathcal{A}|$ states.

[^1]: [Jiang, Notes on Fitted Q-iteration (CS 542 notes), pp. 1–2](https://nanjiang.cs.illinois.edu/files/cs542f22/note5.pdf#page=1)
[^2]: [Jiang, Notes on Fitted Q-iteration (CS 542 notes), pp. 4–5](https://nanjiang.cs.illinois.edu/files/cs542f22/note5.pdf#page=4)
