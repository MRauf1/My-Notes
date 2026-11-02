---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Principle of Transfinite Induction[^1]
> Let $X$ be a [[Well-Ordered Set|well ordered set]]. If $A \subseteq X$ is such that $x \in A$ whenever $I_x \subseteq A$ (where $I_x$ is the [[Initial Segment]] of $x$), then $A = X$.

The general case of [[Proof by Strong Induction]]: taking $X = \mathbb{N}$, "$I_n \subseteq A \implies n \in A$" is exactly the strong induction step, and no separate base case is needed since $I_{\min X} = \emptyset$.

> [!info] Transfinite Induction over Ordinals[^2]
> Let $P(\alpha)$ be a statement about ordinals $\alpha$. If
> 1) Zero Case: $P(0)$ holds,
> 2) Successor Case: $P(\alpha) \implies P(\alpha + 1)$ for every ordinal $\alpha$,
> 3) Limit Case: for every limit ordinal $\lambda$, $\left(\forall \beta < \lambda,\; P(\beta)\right) \implies P(\lambda)$,
>
> then $P(\alpha)$ holds for every ordinal $\alpha$.

Ordinary [[Proof by Induction]] consists of only the zero and successor cases, so it reaches every finite ordinal $n < \omega$ but never $\omega$, the first limit ordinal. The limit case is exactly the "finite stages $\to$ infinite stage" step that ordinary induction lacks. It must be proved separately for each property, and it is often false (e.g. countability of $A_1 \times \cdots \times A_n$ holds for all $n < \omega$ but fails for the product indexed by $\omega$; see [[Set of Binary Sequences Uncountability Theorem]]).

# Properties
- Proof: if $A \neq X$, the [[Well-Ordered Set|well ordering]] gives a minimal $x \in X \setminus A$; then $I_x \subseteq A$, so $x \in A$, a contradiction.
- The ordinal form is the well-ordered form applied to an ordinal: $I_\alpha \subseteq A$ covers both the successor case ($\alpha = \beta + 1$) and the limit case ($\alpha$ a limit ordinal).
- Combined with the [[Well Ordering Principle (Set Theory)|well ordering principle]], it allows inductive constructions over arbitrary sets.
- Transfinite constructions indexed by the [[Set of Countable Ordinals|countable ordinals]] are a standard way to close a family under countable operations.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=22&annotation=KMRMP3Z9)
[^2]: [Transfinite Induction (Wikipedia)](https://en.wikipedia.org/wiki/Transfinite_induction)
