---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Lemma 1 ([[Darboux Integral]] Sum of 2 [[Partition]] Lemma)[^1]
> Let $f$ be a [[Bounded Function]] on $[a, b]$. If $P, Q$ are [[Partition]] of $[a, b]$ with $P \subseteq Q$, then
> $$
> \begin{align}
> L(f, P) \leq L(f, Q) \leq U(f, Q) \leq U(f, P)
> \end{align}
> $$

> [!abstract] Lemma 2 (Riemann-Stieltjes Version)[^2]
> If $P^*$ is a [[Refinement of Partition|refinement]] of $P$ and $\alpha$ is monotonically increasing, then
> $$
> \begin{align}
> L(P, f, \alpha) \leq L(P^*, f, \alpha), \qquad U(P^*, f, \alpha) \leq U(P, f, \alpha)
> \end{align}
> $$

> [!abstract] Corollary 3 (Lower Integral at Most Upper Integral)[^3]
> $$
> \begin{align}
> \underline{\int_a^b} f \, d\alpha \leq \overline{\int_a^b} f \, d\alpha
> \end{align}
> $$

Corollary 3 follows by applying Lemma 2 to the common refinement $P_1 \cup P_2$ of any two partitions ([[Riemann-Stieltjes Integral]]).

[^1]: [Elementary Analysis: The Theory of Calculus](zotero://open-pdf/library/items/GUY2WR3V?page=282)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=132&annotation=LLJPB4L6)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=133&annotation=BWKNSG9E)