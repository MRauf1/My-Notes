---
tags:
  - mathematics
  - topology
---

# Definition
> [!info] Principle of Recursive Definition[^1]
> Let $A$ be a [[Set]] and $a_0 \in A$. Suppose $\rho$ is a function that assigns, to each [[Function]] $f$ mapping a nonempty section $\{1, \dots, n\}$ of $\mathbb{Z}^+$ into $A$, an element of $A$. Then there exists a unique function $h: \mathbb{Z}^+ \to A$ such that
> $$
> \begin{align}
> h(1) &= a_0, \\
> h(i) &= \rho\left(h|_{\{1, \dots, i - 1\}}\right) \quad \text{for } i > 1. \tag{$*$}
> \end{align}
> $$
> The formula $(*)$ is called a recursion formula for $h$.

A recursion formula specifies $h(1)$ and expresses $h(i)$ in terms of the [[Restriction of Function|restriction]] of $h$ to the integers less than $i$. The theorem justifies "defining" a function this way: [[Proof by Induction|induction]] alone only proves statements about a function that is already known to exist.

> [!abstract] Special Case (Enumerating an Infinite Subset of $\mathbb{Z}^+$)[^2][^3][^4]
> Let $C \subseteq \mathbb{Z}^+$ be infinite and consider
> $$
> \begin{align}
> h(1) &= \min C, \\
> h(i) &= \min\left[C - h(\{1, \dots, i - 1\})\right] \quad \text{for } i > 1. \tag{$*$}
> \end{align}
> $$
> - **Lemma 8.1 (Existence on sections).** For each $n \in \mathbb{Z}^+$ there is $f: \{1, \dots, n\} \to C$ satisfying $(*)$ on its domain.
> - **Lemma 8.2 (Agreement).** If $f: \{1, \dots, n\} \to C$ and $g: \{1, \dots, m\} \to C$ both satisfy $(*)$, then $f(i) = g(i)$ for all $i$ in both domains.
> - **Theorem 8.3.** There exists a unique $h: \mathbb{Z}^+ \to C$ satisfying $(*)$ for all $i \in \mathbb{Z}^+$.

# Properties
- Proof strategy (general case identical to the special case): build functions on finite sections by induction, show any two agree on their common domain, then take the union of their graphs to get $h$.
- Generalizes to [[Well-Ordered Set|well-ordered]] index sets (transfinite recursion), whose uniqueness argument is the [[Principle of Transfinite Induction]].
- In computer science, this is the mathematical basis of [[Recursion]].

[^1]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=56&annotation=A3KC86TZ)
[^2]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=54&annotation=LWZTHJ6C)
[^3]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=55&annotation=TEKQER57)
[^4]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=56&annotation=NT734Y7Y)
