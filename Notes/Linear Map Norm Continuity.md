---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Lemma 1 (Linear Map Norm Continuity)[^1]
> Let $V$ and $W$ be finite-dimensional [[Inner Product Space]]s, and let $T \in \mathcal{L}(V, W)$. Then there is a constant $C \geq 0$ such that, for every $v_1, v_2 \in V$,
> $$
> \big| \lVert T v_1 \rVert - \lVert T v_2 \rVert \big| \leq \lVert T v_1 - T v_2 \rVert \leq C \lVert v_1 - v_2 \rVert
> $$
> In particular, the function $f : V \rightarrow \mathbb{R}$ given by $f(v) = \lVert Tv \rVert$ is [[Continuous Function|continuous]].

The first inequality is the [[Triangle Inequality|reverse triangle inequality]] applied to $Tv_1, Tv_2 \in W$. The second inequality shows $T$ is [[Continuous Function|Lipschitz continuous]], with the constant $C$ later identified as the [[Operator Norm]] of $T$.

# Properties
- [[Operator Norm]]
- [[Triangle Inequality]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=289)
