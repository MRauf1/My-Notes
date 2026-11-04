---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!abstract] Simulation Lemma[^1]
> Let $M$ and $\widehat{M}$ be [[Markov Decision Process|MDPs]] with the same $\mathcal{S}, \mathcal{A}, \gamma$, rewards in $[0, R_{max}]$, and $V_{max} := R_{max}/(1-\gamma)$. If
> $$
> \begin{align}
> \max_{s,a}|\widehat{R}(s,a) - R(s,a)| \leq \epsilon_R \quad \text{and} \quad \max_{s,a}\|\widehat{P}(s,a) - P(s,a)\|_1 \leq \epsilon_P,
> \end{align}
> $$
> then for any [[Policy|policy]] $\pi : \mathcal{S} \to \mathcal{A}$,
> $$
> \begin{align}
> \|V^\pi_{\widehat{M}} - V^\pi_M\|_\infty \leq \frac{\epsilon_R}{1-\gamma} + \frac{\gamma\,\epsilon_P\,V_{max}}{2(1-\gamma)}.
> \end{align}
> $$

# Properties
- **Proof.** For any $s$, using the [[Bellman Equation (Policy Evaluation)]] in both models:
$$
\begin{align}
|V^\pi_{\widehat{M}}(s) - V^\pi_M(s)| &= |\widehat{R}(s,\pi) + \gamma\langle \widehat{P}(s,\pi), V^\pi_{\widehat{M}}\rangle - R(s,\pi) - \gamma\langle P(s,\pi), V^\pi_M\rangle| \\
&\leq \epsilon_R + \gamma|\langle \widehat{P}(s,\pi) - P(s,\pi), V^\pi_{\widehat{M}}\rangle| + \gamma\|V^\pi_{\widehat{M}} - V^\pi_M\|_\infty \\
&= \epsilon_R + \gamma\left|\left\langle \widehat{P}(s,\pi) - P(s,\pi), V^\pi_{\widehat{M}} - \tfrac{V_{max}}{2}\mathbf{1}\right\rangle\right| + \gamma\|V^\pi_{\widehat{M}} - V^\pi_M\|_\infty \\
&\leq \epsilon_R + \tfrac{\gamma\,\epsilon_P V_{max}}{2} + \gamma\|V^\pi_{\widehat{M}} - V^\pi_M\|_\infty.
\end{align}
$$
  Take the sup over $s$ and rearrange. The centering by $\frac{V_{max}}{2}\mathbf{1}$ is valid because both $\widehat{P}(s,\pi)$ and $P(s,\pi)$ sum to $1$. Hölder ($\ell_1$–[[Infinity Norm|$\ell_\infty$]]) then uses $\|V - \frac{V_{max}}{2}\mathbf{1}\|_\infty \leq \frac{V_{max}}{2}$.
- **Alternative proof** via the [[Bellman Residual Telescoping Identity]] with $f = Q^\pi_{\widehat{M}}$ and $d_0$ a point mass at $s_0$: $V^\pi_{\widehat{M}}(s_0) - V^\pi_M(s_0) = \frac{1}{1-\gamma}\mathbb{E}_{(s,a)\sim d^\pi}\big[\widehat{R}(s,a) + \gamma\langle \widehat{P}(s,a), V^\pi_{\widehat{M}}\rangle - R(s,a) - \gamma\langle P(s,a), V^\pi_{\widehat{M}}\rangle\big]$. Bound the integrand as above.
- The bound holds for *every* $\pi$ simultaneously, which is what the [[Evaluation Error to Decision Loss Lemma]] needs, since $\pi^\star_{\widehat{M}}$ depends on the data.
- Core step of the [[Certainty-Equivalence Sample Complexity]] analysis and of [[Model-Based Reinforcement Learning]] guarantees generally.
- Its abstraction analogue, which compares a lifted abstract model with the true MDP, gives claim (1) of the [[State Abstraction Hierarchy Theorem]] and the [[Approximate Bisimulation Abstract Model Loss Bound]].

# Questions
> [!question]- What is the proof idea of the simulation lemma?
> Subtract the two Bellman equations for $\pi$. The reward mismatch contributes $\epsilon_R$. The transition mismatch, after adding and subtracting $\gamma\langle P(s,\pi), V^\pi_{\widehat{M}}\rangle$, contributes $\gamma|\langle \widehat{P} - P, V^\pi_{\widehat{M}}\rangle| \leq \gamma\epsilon_P V_{max}/2$. The remaining term is $\gamma\|V^\pi_{\widehat{M}} - V^\pi_M\|_\infty$. So the error $e = \|V^\pi_{\widehat{M}} - V^\pi_M\|_\infty$ satisfies $e \leq \epsilon_R + \gamma\epsilon_P V_{max}/2 + \gamma e$. Solve for $e$.

> [!question]- Why may one subtract $\frac{V_{max}}{2}\mathbf{1}$ inside $\langle \widehat{P}(s,\pi) - P(s,\pi), V\rangle$, and what does it gain?
> $\widehat{P}(s,\pi)$ and $P(s,\pi)$ are both probability vectors, so $(\widehat{P} - P)^\top\mathbf{1} = 0$ and $\langle \widehat{P} - P, V\rangle = \langle \widehat{P} - P, V - c\mathbf{1}\rangle$ for any $c$. Since $V \in [0, V_{max}]$, centering at $c = V_{max}/2$ gives $\|V - c\mathbf{1}\|_\infty \leq V_{max}/2$ instead of $V_{max}$. Hölder then saves a factor of $2$.

> [!question]- Where does the $1/(1-\gamma)^2$ horizon dependence of the transition term come from?
> One factor is the range of values, $V_{max} = R_{max}/(1-\gamma)$: a one-step transition error $\epsilon_P$ can shift the next-state value by up to $\epsilon_P V_{max}/2$. The other comes from solving $e \leq (\dots) + \gamma e$, i.e. accumulating that per-step error over the effective horizon $1/(1-\gamma)$.

> [!question]- Application: In Paper 3, a learned propagator plays the role of $\widehat{P}$ in a discounted control problem with exact rewards. How small must the per-step model error $\epsilon_P = \max_{s,a}\|\widehat{P}(s,a) - P(s,a)\|_1$ be to guarantee value error at most $\epsilon$ for every policy?
> With $\epsilon_R = 0$, the lemma gives $\|V^\pi_{\widehat{M}} - V^\pi_M\|_\infty \leq \frac{\gamma\epsilon_P R_{max}}{2(1-\gamma)^2}$, so $\epsilon_P \leq \frac{2(1-\gamma)^2\epsilon}{\gamma R_{max}}$ suffices. The required one-step accuracy shrinks quadratically in the effective horizon. The relevant error is the $\ell_1$ (total-variation-type) error of each next-state distribution, uniformly over $(s,a)$, not an average or spectral-norm error.

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), pp. 2–4](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=2)
