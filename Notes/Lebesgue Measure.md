---
tags:
  - computer_science
  - monte_carlo_methods
  - mathematics
  - measure_theory
---

# Definition
> [!info] Lebesgue Measure[^1]
> The measure $\lambda$ on $\mathbb{R}^d$ that assigns to a box its volume. Nested [[Riemann Integral|Riemann integrals]] are [[Lebesgue Integral (Measure Theory)|Lebesgue integrals]] taken with respect to $\lambda$, used on $\mathbb{R}^d$ and PDE domains.

> [!info] Lebesgue Measure on $\mathbb{R}$ (Rigorous Definition)[^2]
> Lebesgue measure $m$ is the complete [[Lebesgue-Stieltjes Measure]] $\mu_F$ associated to $F(x) = x$, so the measure of an interval is its length. Its domain $\mathcal{L}$ is the class of **Lebesgue measurable sets**. The restriction of $m$ to $\mathcal{B}_\mathbb{R}$ is also called Lebesgue measure.

Every Lebesgue measurable set is a Borel set together with a Lebesgue null set: $E \in \mathcal{L}$ iff $E = B \cup N_1$, or $E = B' \setminus N_2$, with $B, B'$ Borel and $N_i$ subsets of null sets ([[Measure Completion Theorem]], [[Lebesgue-Stieltjes Measure Regularity]]).[^4] Unlike Borel sets, Lebesgue sets have no transfinite construction from open sets alone; they are defined relative to null sets.

> [!abstract] Theorem 1.21 (Translation and Dilation)[^3]
> For $E \subseteq \mathbb{R}$ and $s, r \in \mathbb{R}$ let $E + s = \{x + s : x \in E\}$ and $rE = \{rx : x \in E\}$. If $E \in \mathcal{L}$, then $E + s \in \mathcal{L}$ and $rE \in \mathcal{L}$, and
> $$
> \begin{align}
> m(E + s) = m(E), \qquad m(rE) = |r|\, m(E).
> \end{align}
> $$

# Properties
- An instance of a [[Measure (Measure Theory)|measure]]; [[Complete Measure|complete]] and [[Sigma-Finite Measure|$\sigma$-finite]].
- Translation invariance is exactly what makes a measure on all of $\mathcal{P}(\mathbb{R})$ impossible ([[Vitali Set]], [[Banach-Tarski Paradox]]).
- **Countable sets are null**: every singleton has measure zero, so every countable set does; in particular $m(\mathbb{Q}) = 0$.[^5] A nonempty open set never has measure zero.[^6]
- **Topological vs. measure-theoretic size**:[^6] covering an enumeration $\{r_j\}$ of $\mathbb{Q} \cap [0,1]$ by intervals of length $\epsilon 2^{-j}$ gives $U$ open and [[Dense Subset|dense]] in $[0,1]$ with $m(U) < \epsilon$, whose complement $K = [0,1] \setminus U$ is closed and [[Nowhere Dense Subset|nowhere dense]] with $m(K) > 1 - \epsilon$. Topologically large sets can be measure-theoretically small and vice versa ([[Generalized Cantor Set]]).
- Null sets need not be countable: the [[Cantor Set]] is a null set of cardinality $\mathfrak{c}$.[^7]
- **Not every Lebesgue set is Borel**:[^8] every subset of the Cantor set is Lebesgue measurable (completeness), so $\operatorname{card}(\mathcal{L}) = \operatorname{card}(\mathcal{P}(\mathbb{R})) > \mathfrak{c}$, while $\operatorname{card}(\mathcal{B}_\mathbb{R}) = \mathfrak{c}$ ([[Borel Sigma-Algebra]]). Explicit examples use the [[Cantor Function]].
- Regular: $m(E) = \inf\{m(U) : U \supseteq E \text{ open}\} = \sup\{m(K) : K \subseteq E \text{ compact}\}$ ([[Lebesgue-Stieltjes Measure Regularity]]).
- On $\mathbb{R}^n$ it is built on the [[Product Sigma-Algebra]] $\mathcal{B}_{\mathbb{R}^n} = \bigotimes_1^n \mathcal{B}_\mathbb{R}$.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=50&annotation=J6I55YDL)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=50&annotation=YTE2DNXR)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=50&annotation=PVZK5VU9)
[^5]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=50&annotation=5N28XIY4)
[^6]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=51&annotation=V9KYJX37)
[^7]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=51&annotation=L4B4BZ3Q)
[^8]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=52&annotation=C2S7QY73)
