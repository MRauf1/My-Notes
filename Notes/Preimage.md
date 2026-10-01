---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 (Preimage)[^1]
> Let $f: X \rightarrow Y$ be a [[Function]], and let $E \subseteq Y$. The preimage (or inverse image) of $E$ under $f$ is
> $$
> \begin{align}
> f^{-1}(E) := \{x \in X \mid f(x) \in E\} \subseteq X
> \end{align}
> $$
> For a single element $y \in Y$, $f^{-1}(y) := \{x \in X \mid f(x) = y\}$ is the preimage of $y$.

If $f^{-1}(y)$ has at most one element for every $y \in Y$, then $f$ is an [[Injective Function]] (one-to-one): equivalently, $f(x_1) \neq f(x_2)$ whenever $x_1 \neq x_2$.

Note that $f^{-1}(E)$ is defined for any $f$, regardless of whether $f$ has an [[Inverse Function]] (which requires $f$ to be bijective); $f^{-1}$ here denotes a set-valued map on subsets of $Y$, not the inverse of $f$ itself.

# Properties
- [[Image]] is the dual notion: the image maps subsets of $X$ forward into $Y$, the preimage maps subsets of $Y$ backward into $X$.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=33)
