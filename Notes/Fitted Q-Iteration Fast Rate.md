---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Fitted Q-Iteration Fast Rate[^1]
> Let $\mathcal{F} \subset [0, V_{max}]^{\mathcal{S}\times\mathcal{A}}$ be finite with $N = |\mathcal{F}|$, fix $f' \in \mathcal{F}$ with $\mathcal{T}f' \in \mathcal{F}$, and let $D$ contain $n$ i.i.d. tuples $(s,a)\sim\mu$, $r \sim R(s,a)$, $s' \sim P(s,a)$. Then with probability at least $1 - \delta$, the empirical update $\widehat{\mathcal{T}}_{\mathcal{F}}f' = \arg\min_{f\in\mathcal{F}}\mathcal{L}_D(f; f')$ of [[Fitted Q-Iteration]] satisfies
> $$
> \begin{align}
> \|\widehat{\mathcal{T}}_{\mathcal{F}}f' - \mathcal{T}f'\|_\mu^2 \leq \left(\sqrt{2} + \sqrt{\tfrac{10}{3}}\right)^2\frac{V_{max}^2\log(N/\delta)}{n}.
> \end{align}
> $$
> Plugged into the [[Fitted Q-Iteration Error Bound]] (in place of $2\epsilon$), the decision loss becomes $O\!\left(\frac{V_{max}}{(1-\gamma)^2}\sqrt{\frac{C\log(N/\delta)}{n}}\right)$, i.e. $O(n^{-1/2})$ instead of $O(n^{-1/4})$.

# Properties
- **Excess loss.** Define $Y(f; f') := (f(s,a) - r - \gamma V_{f'}(s'))^2 - ((\mathcal{T}f')(s,a) - r - \gamma V_{f'}(s'))^2$. Its sample average is $\mathcal{L}_D(f; f') - \mathcal{L}_D(\mathcal{T}f'; f')$, an $f$-independent shift of $\mathcal{L}_D$, so $\widehat{\mathcal{T}}_{\mathcal{F}}f'$ also minimizes $\frac{1}{n}\sum_i Y_i(\cdot; f')$. Since $\mathcal{T}f'$ is the [[Regression Function|conditional mean]] of the target, $\mathbb{E}[Y(f; f')] = \|f - \mathcal{T}f'\|_\mu^2$.
- **Variance controlled by the mean.** Factoring the difference of squares and using $|f + \mathcal{T}f' - 2r - 2\gamma V_{f'}(s')| \leq 2V_{max}$,
$$
\begin{align}
\mathrm{Var}[Y(f; f')] \leq \mathbb{E}[Y^2] = \mathbb{E}\Big[(f - \mathcal{T}f')^2\big(f + \mathcal{T}f' - 2r - 2\gamma V_{f'}(s')\big)^2\Big] \leq 4V_{max}^2\,\mathbb{E}[Y(f; f')].
\end{align}
$$
- **Proof.** Apply the one-sided [[Bernstein's Inequality]] to $Y_i \in [-V_{max}^2, V_{max}^2]$ with a union bound ([[Boole's Inequality]]) over $f \in \mathcal{F}$: with probability $1 - \delta$, for all $f$,
$$
\begin{align}
\mathbb{E}[Y(f; f')] - \frac{1}{n}\sum_{i=1}^n Y_i(f; f') \leq \sqrt{\frac{8V_{max}^2\,\mathbb{E}[Y(f; f')]\log\frac{N}{\delta}}{n}} + \frac{4V_{max}^2\log\frac{N}{\delta}}{3n}.
\end{align}
$$
  Because $\mathcal{T}f' \in \mathcal{F}$, ERM gives $\frac{1}{n}\sum_i Y_i(\widehat{\mathcal{T}}_{\mathcal{F}}f'; f') \leq \frac{1}{n}\sum_i Y_i(\mathcal{T}f'; f') = 0$. So $x = \mathbb{E}[Y(\widehat{\mathcal{T}}_{\mathcal{F}}f'; f')]$ satisfies $x \leq \sqrt{bx} + c$; solving the quadratic in $\sqrt{x}$ gives the bound.
- **Data-dependent $f'$.** The statement is for a fixed $f'$. In FQI, $f' = f_{k-1}$ is computed from the same $D$, so applying it there requires a union bound over $f' \in \mathcal{F}$ as well, replacing $\log(N/\delta)$ by $\log(N^2/\delta)$ (only a constant factor). Alternatively, use a fresh data split per iteration.
- Same mechanism as fast rates for realizable least squares in general: a Bernstein-type condition $\mathrm{Var}(Y) \lesssim \mathbb{E}[Y]$ makes the deviation self-bounding.

# Questions
> [!question]- What is the proof idea of the fast rate?
> Shift the loss by the $f$-independent $\mathcal{L}_D(\mathcal{T}f'; f')$ to get excess losses $Y$ with $\mathbb{E}[Y] = \|f - \mathcal{T}f'\|_\mu^2$ and $\mathrm{Var}(Y) \leq 4V_{max}^2\,\mathbb{E}[Y]$. Bernstein + union bound bound $\mathbb{E}[Y] - \bar{Y}$ by $\sqrt{\mathbb{E}[Y]\log(N/\delta)/n} + \log(N/\delta)/n$ (up to constants). ERM with $\mathcal{T}f' \in \mathcal{F}$ forces $\bar{Y} \leq 0$ for the minimizer. Then $x \leq \sqrt{bx} + c$ with $b, c = O(\log(N/\delta)/n)$ gives $x = O(\log(N/\delta)/n)$.

> [!question]- Which step needs $\mathcal{T}f' \in \mathcal{F}$, and which holds without it?
> $\mathbb{E}[Y(f; f')] = \|f - \mathcal{T}f'\|_\mu^2$ and the variance bound hold for any $f$ regardless, since $\mathcal{T}f'$ is the conditional mean of the target. Membership is needed for $\bar{Y}(\widehat{\mathcal{T}}_{\mathcal{F}}f') \leq \bar{Y}(\mathcal{T}f') = 0$: the comparator must be feasible for the ERM. Without it, $\min_f \mathbb{E}[Y]$ is a positive approximation error and $\bar{Y}$ of the minimizer need not be $\leq 0$.

[^1]: [Jiang, Notes on Fitted Q-iteration (CS 542 notes), pp. 3–4](https://nanjiang.cs.illinois.edu/files/cs542f22/note5.pdf#page=3)
