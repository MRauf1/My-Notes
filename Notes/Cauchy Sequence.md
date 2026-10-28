---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Cauchy [[Sequence]])[^1]
> Sequence $(s_n)$ is a Cauchy sequence if for all $\epsilon > 0$, there exists a number $N$ such that
> $$
> \begin{align}
> m, n > N \implies |s_n - s_m| < \epsilon
> \end{align}
> $$

> [!info] Definition 2 (Cauchy [[Sequence]] using [[Metric Space]])[^2]
> Given a [[Metric Space]] $(S, d)$, [[Sequence]] $(s_n) \in S$ is a Cauchy sequence if for each $\epsilon > 0$, there exists $N$ such that
> $$
> \begin{align}
> m, n > N \implies d(s_m, s_n) < \epsilon
> \end{align}
> $$

# Types
- [[High Dimensional Real Cauchy Sequence]]

# Properties
## [[Convergent Sequence]]
- In any [[Metric Space]], every convergent sequence is Cauchy ([[Convergent Sequence is Cauchy Sequence]]).[^3]
- The converse holds only in a [[Complete Metric Space]]; in fact, a metric space is complete by definition exactly when every Cauchy sequence converges to a point of the space.[^3]
- In $\mathbb{R}$ (and $\mathbb{R}^k$), Cauchy $\iff$ convergent, by the [[Completeness Axiom]] ([[Convergent Sequence|Cauchy criterion]]).[^1]
- In an incomplete space such as $\mathbb{Q}$ or $(0, 1)$, a Cauchy sequence can fail to converge because its would-be limit is missing from the space.

## [[Bounded Sequence]]
- [[Cauchy Sequence Boundedness]] (holds in any [[Metric Space]]: all but finitely many terms lie within distance $1$ of $s_{N+1}$)

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=74)
[^2]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=97)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=62)
