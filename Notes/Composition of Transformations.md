---
tags:
  - computer_science
  - computer_graphics
---

# Definition
> [!info] Definition (Composition of Transformations)[^1]
> Applying two [[Geometric Transformation|transformations]] to a vector in sequence — first $S$, then $R$ — is equivalent to applying a single matrix $M = RS$, obtained by multiplying the two matrices together; the rightmost matrix in the product is the one applied first.

# Properties
- For a chain of transformations $M = M_1 M_2 \cdots M_n$, the inverse reverses both the order and each factor: $M^{-1} = M_n^{-1} \cdots M_2^{-1} M_1^{-1}$.
- Elementary transforms invert geometrically without needing general matrix inversion: the inverse of $\text{scale}(s_x, s_y, s_z)$ is $\text{scale}(1/s_x, 1/s_y, 1/s_z)$, the inverse of a rotation negates its angle, and the inverse of a translation negates its offset.
- The [[Singular Value Decomposition Theorem|SVD]] gives a general route to invert any matrix: if $M = R_1 \, \text{scale}(\sigma_1, \dots) \, R_2$, then $M^{-1} = R_2^T \, \text{scale}(1/\sigma_1, \dots) \, R_1^T$.

[^1]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=130&annotation=A56KBDAC)
