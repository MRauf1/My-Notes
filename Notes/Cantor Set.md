---
tags:
  - mathematics
  - real_analysis
  - measure_theory
---

# Definition

> [!info] Definition 1 (Cantor Set)[^1]
> Let $E_0 = [0, 1]$. Form $E_1$ by removing the open middle third $(\frac{1}{3}, \frac{2}{3})$ from $E_0$, so that $E_1 = [0, \frac{1}{3}] \cup [\frac{2}{3}, 1]$. Continuing, form $E_{n+1}$ from $E_n$ by removing the open middle third of each of the $2^n$ [[Interval|intervals]] making up $E_n$, so that $E_n$ is a union of $2^n$ intervals each of length $3^{-n}$, and $E_1 \supseteq E_2 \supseteq E_3 \supseteq \dots$. The Cantor set is
> $$
> \begin{align}
> P = \bigcap_{n=1}^{\infty} E_n
> \end{align}
> $$

Each $E_n$ is a finite union of [[Closed Set|closed]] [[Interval|intervals]], hence [[Compact Set|compact]]. Since the $E_n$ are nonempty and nested, the [[Finite Intersection Property|nested compact sets corollary]] guarantees that $P$ is nonempty; $P$ is itself compact, being an intersection of closed subsets of the compact set $E_1$.

# Properties
- $P$ is an example of a nonempty [[Perfect Subset|perfect set]] in $\mathbb{R}$ that contains no [[Interval|segment]].
- By the [[Perfect Subset|uncountability of nonempty perfect sets]], $P$ is [[Uncountable Set|uncountable]].
- $P$ has (Lebesgue) measure zero: $P$ is an example of an uncountable set of measure zero.[^2]

> [!abstract] Proposition 1.22[^3]
> Let $C$ be the Cantor set.
> 1. $C$ is compact, [[Nowhere Dense Subset|nowhere dense]], and totally disconnected (its only connected subsets are single points). Moreover, $C$ has no [[Isolated Point|isolated points]].
> 2. $m(C) = 0$ ([[Lebesgue Measure]]).
> 3. $\operatorname{card}(C) = \mathfrak{c}$ ([[Cardinality of the Continuum]]).

- The standard example showing [[Null Set (Measure Theory)|Lebesgue null sets]] can have the cardinality of the continuum, not just be countable.[^4]
- $C$ consists of the $x \in [0,1]$ with a base-3 expansion using only the digits $0$ and $2$; the [[Cantor Function]] maps it onto $[0,1]$.
- Since $m$ is complete, every subset of $C$ is Lebesgue measurable, which shows that there are more Lebesgue measurable sets than Borel sets.
- Removing middle $\alpha_j$ths instead of thirds gives a [[Generalized Cantor Set]], which can have positive measure.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=50)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=51)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=51&annotation=TF92G9N5)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=51&annotation=L4B4BZ3Q)
