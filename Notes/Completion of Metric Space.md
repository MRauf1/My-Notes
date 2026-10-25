---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Completion of [[Metric Space]])[^1]
> Every [[Metric Space]] $X$ is [[Isometry|isometric]] to a [[Dense Subset]] of a [[Complete Metric Space]] $Y$.

That is, every metric space can be isometrically embedded in a complete metric space, and the closure of its image (its completion) is complete. Note that the embedded copy of $X$ itself is complete only if $X$ was already complete; it is $Y$, the closure, that is complete.

One construction uses the [[Space of Bounded Continuous Functions]]: fix $a \in X$ and map $p \mapsto f_p$, where $f_p(x) = d(x, p) - d(x, a)$. Then $|f_p(x)| \leq d(a, p)$, so $f_p \in \mathscr{C}(X)$, and $\lVert f_p - f_q \rVert = d(p, q)$. Since $\mathscr{C}(X)$ is complete, the closure $Y$ of the image is complete. Another construction uses equivalence classes of [[Cauchy Sequence|Cauchy sequences]].[^1]

# Properties
- The completion is unique up to isometry.
- $\mathbb{R}$ is the completion of $\mathbb{Q}$.
- $L^p$ is the completion of continuous functions under the $L^p$ norm (see [[Space of Bounded Continuous Functions]]).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=179&annotation=Y2RTD7RM)
