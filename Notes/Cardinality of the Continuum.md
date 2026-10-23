---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Cardinality of the Continuum[^1]
> A [[Set]] $X$ has the cardinality of the continuum if $\operatorname{card}(X) = \operatorname{card}(\mathbb{R})$. One writes
> $$
> \begin{align}
> \mathfrak{c} = \operatorname{card}(\mathbb{R}), \qquad \operatorname{card}(X) = \mathfrak{c} \iff \operatorname{card}(X) = \operatorname{card}(\mathbb{R}).
> \end{align}
> $$

Here $\operatorname{card}(X) \leq \operatorname{card}(Y)$ means there is an [[Injective Function|injection]] $X \to Y$, and equality means there is a [[Bijective Function|bijection]] (see [[Set Cardinality]]).

# Properties
> [!abstract] Proposition (Power Set of $\mathbb{N}$)[^2]
> $\operatorname{card}(\mathcal{P}(\mathbb{N})) = \mathfrak{c}$, where $\mathcal{P}$ is the [[Power Set]]. Equivalently $\mathfrak{c} = 2^{\aleph_0}$.

> [!abstract] Corollary[^3]
> If $\operatorname{card}(X) \geq \mathfrak{c}$, then $X$ is uncountable (not [[Countable Set|countable]]).

> [!abstract] Proposition (Closure under Products and Unions)[^4]
> a. If $\operatorname{card}(X) \leq \mathfrak{c}$ and $\operatorname{card}(Y) \leq \mathfrak{c}$, then $\operatorname{card}(X \times Y) \leq \mathfrak{c}$.
> b. If $\operatorname{card}(A) \leq \mathfrak{c}$ and $\operatorname{card}(X_\alpha) \leq \mathfrak{c}$ for all $\alpha \in A$, then $\operatorname{card}\left(\bigcup_{\alpha \in A} X_\alpha\right) \leq \mathfrak{c}$.

- In particular $\operatorname{card}(\mathbb{R}^n) = \mathfrak{c}$ for every $n$.
- The converse of the corollary ("uncountable implies $\operatorname{card} \geq \mathfrak{c}$") is the [[Continuum Hypothesis]], which is independent of ZFC.
- The [[Set of Binary Sequences Uncountability Theorem]] is the diagonal argument behind $\mathfrak{c} > \aleph_0$.

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=21&annotation=9GPIN2NE)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=21&annotation=CKGQAPPU)
[^3]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=21&annotation=4BDNK8SB)
[^4]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=22&annotation=J276E8NQ)
