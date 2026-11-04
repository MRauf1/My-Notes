---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Certainty-Equivalence Sample Complexity[^1]
> Under a [[Generative Model (Reinforcement Learning)|generative model]] with $n$ samples per $(s,a)$, let $\widehat{M} = (\mathcal{S}, \mathcal{A}, \widehat{P}, \widehat{R}, \gamma)$ be the [[Certainty-Equivalence (Reinforcement Learning)|certainty-equivalence]] model and $V_{max} = R_{max}/(1-\gamma)$. With high probability, for all $s \in \mathcal{S}$, the suboptimality $V^\star_M(s) - V^{\pi^\star_{\widehat{M}}}_M(s)$ satisfies each of the following ($\tilde{O}$ hides polylogarithmic factors in $|\mathcal{S}|, |\mathcal{A}|$, and the dependence on $R_{max}$ and $1/\delta$):
> $$
> \begin{align}
> \text{naive:} &\quad \tilde{O}\left(\frac{|\mathcal{S}|\,V_{max}}{\sqrt{n}\,(1-\gamma)}\right) \\
> \ell_1 \text{ concentration:} &\quad \tilde{O}\left(\frac{\sqrt{|\mathcal{S}|}\,V_{max}}{\sqrt{n}\,(1-\gamma)}\right) \\
> \text{via } Q^\star_M\text{:} &\quad \tilde{O}\left(\frac{V_{max}}{\sqrt{n}\,(1-\gamma)^2}\right) \\
> \text{large } n\text{:} &\quad \tilde{O}\left(\frac{V_{max}}{\sqrt{n}\,(1-\gamma)}\right) + O(1/n) \text{ burn-in}
> \end{align}
> $$

# Properties
- **Naive analysis.**
  1. Hoeffding plus a union bound give $\max_{s,a}|\widehat{R} - R| \leq R_{max}\sqrt{\frac{1}{2n}\ln\frac{4|\mathcal{S}\times\mathcal{A}|}{\delta}}$ and $\max_{s,a,s'}|\widehat{P}(s'|s,a) - P(s'|s,a)| \leq \sqrt{\frac{1}{2n}\ln\frac{4|\mathcal{S}\times\mathcal{A}\times\mathcal{S}|}{\delta}}$, splitting $\delta$ evenly between reward and transition events.
  2. Summing coordinates gives $\epsilon_P \leq |\mathcal{S}|\sqrt{\cdot}$.
  3. The [[Simulation Lemma]] and the [[Evaluation Error to Decision Loss Lemma]] finish the bound.
- **$\sqrt{|\mathcal{S}|}$.** Replace the coordinate sum by the [[Empirical Distribution L1 Concentration Bound]], $\epsilon_P = \tilde{O}(\sqrt{|\mathcal{S}|/n})$.
- **No $|\mathcal{S}|$.** Since $\mathcal{T}_{\widehat{M}}$ is a $\gamma$-contraction, $\|Q^\star_{\widehat{M}} - Q^\star_M\|_\infty \leq \frac{1}{1-\gamma}\|Q^\star_M - \mathcal{T}_{\widehat{M}}Q^\star_M\|_\infty$ (cf. [[Bellman Error]]). The right side needs only scalar concentration.
  - **Lemma.** For fixed $(s,a)$, with probability $1 - \delta$: $|Q^\star_M(s,a) - (\widehat{R}(s,a) + \gamma\langle \widehat{P}(s,a), V^\star_M\rangle)| \leq \frac{R_{max}}{1-\gamma}\sqrt{\frac{1}{2n}\log\frac{2}{\delta}}$. The bracket is the average of the i.i.d. variables $r + \gamma V^\star_M(s') \in [0, \frac{R_{max}}{1-\gamma}]$ with mean $Q^\star_M(s,a)$, so [[Hoeffding's Inequality]] applies.
  - A union bound over $(s,a)$ costs only logs. The [[Approximate Greedy Policy Suboptimality Bound]] then gives the $(1-\gamma)^{-2}$ rate. The total number of samples, $n|\mathcal{S}||\mathcal{A}|$, still scales with $|\mathcal{S}|$.
- **Why $Q^\star_M$ and not $Q^\star_{\widehat{M}}$.** Swapping the roles gives $\|Q^\star_{\widehat{M}} - Q^\star_M\|_\infty \leq \frac{1}{1-\gamma}\|Q^\star_{\widehat{M}} - \mathcal{T}_M Q^\star_{\widehat{M}}\|_\infty$, the standard Bellman residual. But $V^\star_{\widehat{M}}$ depends on the data in $D_{s,a}$, so $r + \gamma V^\star_{\widehat{M}}(s')$ are not i.i.d. with the right mean, and Hoeffding fails.
  - Workaround 1: a union bound over a deterministic function class containing $V^\star_{\widehat{M}}$ (e.g. all tabular functions in $[0, V_{max}]$), which reproduces the $\sqrt{|\mathcal{S}|}$ analysis.
  - Workaround 2: when $\mathcal{S}$ forms a DAG, $V^\star_{\widehat{M}}(s')$ depends only on data at later pairs. This needs care, e.g. under exploration, outcomes in $D_{s,a}$ can affect which later pairs get sampled.
- **Horizon accounting** for the $(1-\gamma)^{-3}$ total in the third bound (counting $V_{max}$): the value range, translating Bellman error into a $Q^\star$ gap, and error accumulation when acting greedily with respect to $\widehat{Q}$. The first two analyses avoid the third source.
- **Large-sample regime.** The [[Bellman Error Performance Difference Bound]] removes the greedy-step horizon factor: $\|V^\star_M - V^{\pi^\star_{\widehat{M}}}_M\|_\infty \leq \frac{2}{1-\gamma}\|Q^\star_{\widehat{M}} - \mathcal{T}_M Q^\star_{\widehat{M}}\|_\infty$. To handle data dependence, write $Q^\star_{\widehat{M}} = \mathcal{T}_{\widehat{M}}Q^\star_{\widehat{M}}$ and replace $Q^\star_{\widehat{M}}$ by $Q^\star_M$. The extra terms reduce to $\gamma|\langle P(s,a) - \widehat{P}(s,a), V^\star_{\widehat{M}} - V^\star_M\rangle| \leq \gamma\|P(s,a) - \widehat{P}(s,a)\|_1\|V^\star_{\widehat{M}} - V^\star_M\|_\infty$. That is a product of two $O(1/\sqrt{n})$ terms, i.e. $O(1/n)$, which is dominated once $n$ exceeds some function of $|\mathcal{S}|$ and $1/(1-\gamma)$.
- **Further improvement.** Bernstein-type inequalities exploit that $\mathrm{Var}(\langle P(s,a), V^\pi\rangle)$ is far below its worst case $O(V_{max}^2)$ when summed along an occupancy, which yields sharper sample complexities (Azar, Munos & Kappen 2013).
- The $|\mathcal{S}|$-free analysis is the core idea behind [[Sparse Sampling]].
- Extended to [[State Abstraction|state abstractions]], with $n$ replaced by the effective sample size $n_\phi(D)$, in [[State Abstraction Finite Sample Bound]].
- The total-variance identity behind the Bernstein improvement is the [[Bellman Equation for Variance]].

# Questions
> [!question]- Why does the $|\mathcal{S}|$-free analysis bound $\|Q^\star_M - \mathcal{T}_{\widehat{M}}Q^\star_M\|_\infty$ rather than the more natural Bellman residual $\|Q^\star_{\widehat{M}} - \mathcal{T}_M Q^\star_{\widehat{M}}\|_\infty$?
> The entry $(\mathcal{T}_{\widehat{M}}V)(s,a) = \frac{1}{n}\sum_{(r,s') \in D_{s,a}}(r + \gamma V(s'))$ is an average of i.i.d. bounded variables only if $V$ is fixed independently of $D_{s,a}$. $V^\star_M$ is a deterministic function of the true MDP, so Hoeffding's inequality applies. $V^\star_{\widehat{M}}$ is computed from all the data, including $D_{s,a}$, so the summands are dependent on the very samples being averaged.

> [!question]- What is the trade-off between the three non-asymptotic analyses?
> Concentrating the whole vector $\widehat{P}(s,a)$ (in $\ell_1$) costs a factor $|\mathcal{S}|$ (entrywise) or $\sqrt{|\mathcal{S}|}$ (via sign vectors), because it must hold against every possible value function. Concentrating only the scalar $\langle \widehat{P}(s,a), V^\star_M\rangle$ for the one fixed function $V^\star_M$ removes $|\mathcal{S}|$. But it controls $Q^\star_{\widehat{M}}$ only through a contraction argument, and the greedy step then costs an extra $1/(1-\gamma)$.

> [!question]- Why is the extra term in the large-sample analysis $O(1/n)$?
> After replacing $Q^\star_{\widehat{M}}$ by $Q^\star_M$, the leftover is $\gamma|\langle \widehat{P}(s,a) - P(s,a), V^\star_{\widehat{M}} - V^\star_M\rangle| \leq \gamma\|\widehat{P}(s,a) - P(s,a)\|_1\|V^\star_{\widehat{M}} - V^\star_M\|_\infty$. The first factor is $\tilde{O}(\sqrt{|\mathcal{S}|/n})$ by $\ell_1$ concentration and the second $\tilde{O}(1/\sqrt{n})$ by the $|\mathcal{S}|$-free analysis. Their product is $O(1/n)$ in $n$, so it is dominated by the leading $1/\sqrt{n}$ term for large $n$, even though its $|\mathcal{S}|$ and horizon factors are worse.

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), pp. 2–8](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=2)
