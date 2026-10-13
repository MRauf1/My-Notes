---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Sequential Characterization of [[Limit of Function]])[^1]
> Let $(X, d_X), (Y, d_Y)$ be [[Metric Space|metric spaces]], $E \subseteq X$, $f: E \rightarrow Y$, and $p$ a [[Limit Point]] of $E$. Then
> $$
> \begin{align}
> \lim_{x \rightarrow p} f(x) = q \iff \lim_{n \rightarrow \infty} f(p_n) = q
> \end{align}
> $$
> for every [[Sequence in Metric Space|sequence]] $\{p_n\}$ in $E$ such that $p_n \neq p$ and $\lim_{n \rightarrow \infty} p_n = p$.

> [!abstract] Corollary 2 (Uniqueness of [[Limit of Function]])[^1]
> If $f$ has a limit at $p$, this limit is unique.

# Properties
- Reduces limits of functions to [[Limit of Sequence|limits of sequences]], so uniqueness and the arithmetic laws ([[Limit of Function Addition Law]], [[Limit of Function Product Law]], [[Limit of Function Quotient Law]]) are inherited from [[Limit of Sequence Arithmetic Theorems]].
- The one-sided analogue is used to define $f(x^+)$ and $f(x^-)$ in [[One-Sided Limit of Function]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=93)
