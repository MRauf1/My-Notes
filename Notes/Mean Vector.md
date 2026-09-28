---
tags:
  - statistics
  - categorical_variable_prediction
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Mean]] [[Vector]])[^1]
> Let $\mathbf{Z} = (Z_1, \dots, Z_m)^T$ be a [[Random Vector]]. Its expected value exists if the [[Expectation|expectations]] of all components $Z_1, \dots, Z_m$ exist, in which case it is the vector of component expectations
> $$
> \begin{align}
> E[\mathbf{Z}] = \begin{bmatrix}E[Z_1] \\ \vdots \\ E[Z_m]\end{bmatrix}
> \end{align}
> $$

# Properties
- Each $E[Z_i]$ can be computed from the joint distribution or from the [[Marginal Distribution]] of $Z_i$; the results agree.
- Linear: $E[A\mathbf{Z} + \mathbf{b}] = A\,E[\mathbf{Z}] + \mathbf{b}$ for a constant matrix $A$ and vector $\mathbf{b}$.
- Equals the gradient at $\mathbf{0}$ of the [[Moment Generating Function of Random Vector|mgf of the random vector]].
- The second-order counterpart is the [[Covariance Matrix]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=113)
