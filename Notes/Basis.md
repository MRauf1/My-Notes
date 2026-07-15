---
tags:
  - mathematics
  - abstract_algebra
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Basis)
> Basis of [[Group]] $G$ is a [[Subset]] $B \subseteq G$ which is [[Linearly Independent]] and generates $G$
> $$
> \begin{align}
> G = <B> = \mathbb{Z}B = \{c_1 x_1 + \dots c_n x_n | c_i \in \mathbb{Z}, x_i \in B\}
> \end{align}
> $$

> [!info] Definition 2 (Basis of [[Finite-Dimensional Vector Space]])[^1]
> Let $V$ be [[Finite-Dimensional Vector Space]]. List $(v_1, \dots, v_n)$ in $V$ is a basis for $V$ if $(v_1, \dots, v_n)$ is [[Linearly Independent]] and $V \subseteq \langle v_1, \dots, v_n \rangle$.

Notice that it follows immediately that $\langle v_1, \dots, v_n \rangle \subseteq V$ and hence it follows that $V = \langle v_1, \dots, v_n \rangle$.

# Properties
- [[Basis Matrix RREF]]
- [[Basis Linear Combination]]
- [[Basis Sublist]]
- [[Basis Finite-Dimensional Vector Space]]
- [[Basis Algorithm]]
- [[Basis Unique Linear Map]]
- [[Basis Linear Map Isomorphism]]
- [[Two Bases Dimension]]
- [[Basis Dimension]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=170)