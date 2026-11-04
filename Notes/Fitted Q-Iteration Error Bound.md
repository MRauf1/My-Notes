---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Fitted Q-Iteration Error Bound[^1]
> Run [[Fitted Q-Iteration]] with a finite class $\mathcal{F} \subset [0, V_{max}]^{\mathcal{S}\times\mathcal{A}}$ ($V_{max} = R_{max}/(1-\gamma)$, $0 \in \mathcal{F}$) such that
> 1. $\mathcal{F}$ is [[Bellman Completeness|Bellman complete]]: $\mathcal{T}f \in \mathcal{F}$ for all $f \in \mathcal{F}$;
> 2. the data distribution $\mu$ has [[Concentrability Coefficient|concentrability coefficient]] $C$;
> 3. a [[Uniform Deviation Bound]] holds: $|\mathcal{L}_D(f; f') - \mathcal{L}_\mu(f; f')| \leq \epsilon$ for all $f, f' \in \mathcal{F}$.
>
> Then for every admissible $\nu$ and the greedy policy $\pi_{f_k}$,
> $$
> \begin{align}
> \|f_k - Q^\star\|_\nu &\leq \frac{1-\gamma^k}{1-\gamma}\sqrt{2C\epsilon} + \gamma^k V_{max}, \\
> J(\pi^\star) - J(\pi_{f_k}) &\leq \frac{2}{1-\gamma}\left(\frac{1-\gamma^k}{1-\gamma}\sqrt{2C\epsilon} + \gamma^k V_{max}\right).
> \end{align}
> $$

# Properties
- **Step 1 (decision loss to estimation error).** By the [[Performance Difference Lemma]] and greediness of $\hat{\pi} = \pi_{f_k}$ ($f_k(s, \hat{\pi}) \geq f_k(s, \pi^\star)$),
$$
\begin{align}
J(\pi^\star) - J(\hat{\pi}) = \sum_{h=1}^\infty\gamma^{h-1}\mathbb{E}_{s\sim d^{\hat{\pi}}_h}[V^\star(s) - Q^\star(s, \hat{\pi})] \leq \sum_{h=1}^\infty\gamma^{h-1}\Big(\|Q^\star - f_k\|_{d^{\hat{\pi}}_h\times\pi^\star} + \|Q^\star - f_k\|_{d^{\hat{\pi}}_h\times\hat{\pi}}\Big),
\end{align}
$$
  using $\|\cdot\|_{1,\nu} \leq \|\cdot\|_{2,\nu}$ ([[Jensen's Inequality]]). Both distributions are admissible.
- **Helper lemma.** With $\pi_{f,f'}(s) := \arg\max_a \max\{f(s,a), f'(s,a)\}$, for every $\tilde{\nu} \in \Delta(\mathcal{S})$: $\|V_f - V_{f'}\|_{\tilde{\nu}} \leq \|f - f'\|_{\tilde{\nu}\times\pi_{f,f'}}$, since $|\max_a f(s,a) - \max_a f'(s,a)| \leq |f(s, \pi_{f,f'}(s)) - f'(s, \pi_{f,f'}(s))|$ pointwise. This is the distribution-weighted version of the 1-Lipschitzness of $\max$ used for the [[Bellman Optimality Operator]] contraction.
- **Step 2 (error propagation).** With $P(\nu)$ the law of $s'$ for $(s,a)\sim\nu$, $s' \sim P(s,a)$,
$$
\begin{align}
\|f_k - Q^\star\|_\nu \leq \|f_k - \mathcal{T}f_{k-1}\|_\nu + \|\mathcal{T}f_{k-1} - \mathcal{T}Q^\star\|_\nu \leq \sqrt{C}\|f_k - \mathcal{T}f_{k-1}\|_\mu + \gamma\|f_{k-1} - Q^\star\|_{P(\nu)\times\pi_{f_{k-1},Q^\star}},
\end{align}
$$
  where $\|\mathcal{T}f - \mathcal{T}Q^\star\|_\nu \leq \gamma\|V_f - V^\star\|_{P(\nu)}$ by Jensen, then the helper lemma. $P(\nu)\times\pi_{f_{k-1},Q^\star}$ is again admissible, so the recursion unrolls $k$ times down to $\|f_0 - Q^\star\| \leq V_{max}$.
- **Step 3 (one regression step).** Since $\mathcal{T}f_{k-1}$ is the Bayes-optimal regressor and lies in $\mathcal{F}$, and $f_k$ minimizes $\mathcal{L}_D(\cdot; f_{k-1})$,
$$
\begin{align}
\|f_k - \mathcal{T}f_{k-1}\|_\mu^2 = \mathcal{L}_\mu(f_k; f_{k-1}) - \mathcal{L}_\mu(\mathcal{T}f_{k-1}; f_{k-1}) \leq \mathcal{L}_D(f_k; f_{k-1}) - \mathcal{L}_D(\mathcal{T}f_{k-1}; f_{k-1}) + 2\epsilon \leq 2\epsilon.
\end{align}
$$
- **Rate.** [[Hoeffding's Inequality]] with a union bound over $\mathcal{F}\times\mathcal{F}$ gives $\epsilon = O\big(V_{max}^2\sqrt{\log(|\mathcal{F}|/\delta)/n}\big)$, so the bound decays only as $O(n^{-1/4})$. The [[Fitted Q-Iteration Fast Rate]] improves this to $O(n^{-1/2})$.
- **Horizon dependence.** The bound is $O(\sqrt{C\epsilon}/(1-\gamma)^2)$: one $\frac{1}{1-\gamma}$ from error propagation, one from turning value error into decision loss. [[Non-Stationary Fitted Q-Iteration]] saves one of them, and also gives an alternative proof of this bound via the [[Non-Stationary Bellman Error Performance Difference Bound]].
- Error propagation here runs along the "ugly" policies $\pi_{f_k, Q^\star}$, which take the action witnessing the max-difference inequality. Classical ADP analyses (Munos & Szepesvári 2008) only need "simple" greedy policies $\pi_f$ and their concatenations.

# Questions
> [!question]- What is the proof idea?
> (i) Performance difference + greediness of $\pi_{f_k}$ bound the loss by $\frac{2}{1-\gamma}\sup_\nu\|f_k - Q^\star\|_\nu$ over admissible $\nu$. (ii) Split $f_k - Q^\star = (f_k - \mathcal{T}f_{k-1}) + (\mathcal{T}f_{k-1} - \mathcal{T}Q^\star)$; change measure on the first via $C$, and contract the second by $\gamma$ under the pushed-forward admissible distribution, using $|\max f - \max f'| \leq |f - f'|$ at a suitable action. (iii) Each regression step has $\|f_k - \mathcal{T}f_{k-1}\|_\mu^2 \leq 2\epsilon$ by completeness + uniform deviation. Unroll the recursion: a geometric sum plus $\gamma^k V_{max}$.

> [!question]- Where exactly is Bellman completeness used, and why would realizability ($Q^\star \in \mathcal{F}$) not suffice?
> In step (iii), twice: the identity $\mathcal{L}_\mu(f; f') - \mathcal{L}_\mu(\mathcal{T}f'; f') = \|f - \mathcal{T}f'\|_\mu^2$ compares with $\mathcal{T}f_{k-1}$, and the ERM inequality $\mathcal{L}_D(f_k; f_{k-1}) \leq \mathcal{L}_D(\mathcal{T}f_{k-1}; f_{k-1})$ needs $\mathcal{T}f_{k-1} \in \mathcal{F}$. Since $f_{k-1} \neq Q^\star$ in general, realizability only gives this at the fixed point. Without it, $f_k$ is the projection of $\mathcal{T}f_{k-1}$ onto $\mathcal{F}$, whose error does not vanish with data.

> [!question]- Why does the bound decay only as $n^{-1/4}$ with Hoeffding, and what makes the fast rate possible?
> Hoeffding gives $\epsilon \asymp n^{-1/2}$ for the loss deviation, but the bound uses $\sqrt{\epsilon}$, because $\epsilon$ controls the *squared* norm $\|f_k - \mathcal{T}f_{k-1}\|_\mu^2$. Hoeffding uses only the range of the loss. The excess loss $Y$ has $\mathrm{Var}(Y) \leq 4V_{max}^2\,\mathbb{E}[Y]$, so near the minimizer its variance vanishes. Bernstein's inequality exploits this to give $\|f_k - \mathcal{T}f_{k-1}\|_\mu^2 = O(1/n)$.

[^1]: [Jiang, Notes on Fitted Q-iteration (CS 542 notes), pp. 1–3](https://nanjiang.cs.illinois.edu/files/cs542f22/note5.pdf#page=1)
