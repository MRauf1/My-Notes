---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Orthogonal Projection)[^1]
> Let $U$ be a subspace of $V$. The orthogonal projection onto $U$ is the function $P_U : V \to V$ defined by $P_U(v) = u$, where $v = u + w$ for $u \in U$ and $w \in U^\perp$ (per the [[Orthogonal Decomposition Theorem]]).

# Properties
Let $U$ be a finite-dimensional subspace of $V$.
- $P_U$ is a [[Linear Map]].
- If $(e_1, \dots, e_m)$ is any [[Orthonormal Basis]] of $U$, then $P_U v = \sum_{j=1}^m \langle v, e_j \rangle e_j$ for each $v \in V$.
- For each $v \in V$, $v - P_U v \in U^\perp$.
- For each $v, w \in V$, $\langle P_U v, w \rangle = \langle P_U v, P_U w \rangle = \langle v, P_U w \rangle$.
- Suppose $\mathcal{B} = (e_1, \dots, e_n)$ is an [[Orthonormal Basis]] of $V$ such that $(e_1, \dots, e_m)$ is an [[Orthonormal Basis]] of $U$. Then $[P_U]_{\mathcal{B}} = diag(1, \dots, 1, 0, \dots, 0)$, with the first $m$ diagonal entries $1$ and the remaining diagonal entries $0$.
- [[Image]] $P_U = U$, and $P_U u = u$ for each $u \in U$.
- [[Kernel]] $P_U = U^\perp$.
- If $V$ is finite-dimensional, then $P_{U^\perp} = I - P_U$.
- $P_U^2 = P_U$.
- If $U$ is the [[Orthogonal Direct Sum]] $U = U_1 \oplus \dots \oplus U_m$, then $P_U = P_{U_1} + \dots + P_{U_m}$.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=275)
