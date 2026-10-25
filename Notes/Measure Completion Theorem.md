---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!abstract] Theorem 1.9 (Completion of a Measure)[^1]
> Let $(X, \mathcal{M}, \mu)$ be a [[Measure Space]]. Let $\mathcal{N} = \{N \in \mathcal{M} : \mu(N) = 0\}$ and
> $$
> \begin{align}
> \overline{\mathcal{M}} = \{E \cup F : E \in \mathcal{M} \text{ and } F \subseteq N \text{ for some } N \in \mathcal{N}\}.
> \end{align}
> $$
> Then $\overline{\mathcal{M}}$ is a [[Sigma-Field|$\sigma$-algebra]], and there is a unique extension $\overline{\mu}$ of $\mu$ to a [[Complete Measure|complete measure]] on $\overline{\mathcal{M}}$, given by[^2]
> $$
> \begin{align}
> \overline{\mu}(E \cup F) = \mu(E).
> \end{align}
> $$

$\overline{\mu}$ is the **completion** of $\mu$, and $\overline{\mathcal{M}}$ is the completion of $\mathcal{M}$ with respect to $\mu$.[^3] Completion adds exactly the subsets of null sets and nothing else: every new set is a measurable set up to a negligible piece.

# Properties
- The Lebesgue $\sigma$-algebra is the completion of $\mathcal{B}_\mathbb{R}$ with respect to [[Lebesgue Measure]]; each Lebesgue measurable set is a Borel set union a subset of a Borel null set. More generally, each complete [[Lebesgue-Stieltjes Measure]] is the completion of its restriction to the [[Borel Sigma-Algebra]].
- Equivalently $E \in \overline{\mathcal{M}}$ iff $E = B \triangle N'$ for some $B \in \mathcal{M}$ and $N'$ contained in a null set ([[Symmetric Difference]]).

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=39&annotation=6LPIGGF6)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=40&annotation=IXELKGB5)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=40&annotation=ZZP7ZUP8)
