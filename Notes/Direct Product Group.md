---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Direct Product [[Group]])
> For groups $G, H$, there is a group $(G \times H, \cdot)$ with
> $$
> \begin{align}
> G \times H := \{(g, h) | g \in G, h \in H\}
> \end{align}
> $$
> and the operation being
> $$
> \begin{align}
> (g_1, h_1) \cdot (g_2, h_2) := (g_1 g_2, h_1 h_2)
> \end{align}
> $$
> [[Identity Property|Identity]] is $(e_G, e_H)$
> For $(g, h) \in G \times H$, the [[Inverse]] is $(g, h)^{-1} = (g^{-1}, h^{-1})$

This can be generalized to a direct product of $n$ groups.

# Properties

## [[Group Order]]
- $|G \times H| = |G| |H|$

## [[Group Isomorphism]]
- If $G_1 \cong G_2$, $H_1 \cong H_2$, then $G_1 \times H_1 \cong G_2 \times H_2$
- Let $G$ be a group with $A, B \leq G$. Then, if
	1) $A, B \trianglelefteq G$
	2) $A \cap B = \{e\}$
	3) $AB = G$
	- Then there exists an isomorphism $\phi: A \times B \rightarrow G$ with $\phi(a, b) = ab$