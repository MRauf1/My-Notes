---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Multivariate Normal Distribution Independence[^1]
> Let $\mathbf{X} \sim N_n(\boldsymbol{\mu}, \Sigma)$ be partitioned as $\mathbf{X} = (\mathbf{X}_1^T, \mathbf{X}_2^T)^T$ with $\Sigma = \begin{bmatrix}\Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22}\end{bmatrix}$. Then $\mathbf{X}_1$ and $\mathbf{X}_2$ are [[Independent Random Variable|independent]] if and only if $\Sigma_{12} = O$.

Proof: if $\Sigma_{12} = O$, the quadratic form in the mgf splits, $\mathbf{t}^T\Sigma\mathbf{t} = \mathbf{t}_1^T\Sigma_{11}\mathbf{t}_1 + \mathbf{t}_2^T\Sigma_{22}\mathbf{t}_2$, so the joint [[Moment Generating Function of Random Vector|mgf]] factors into the marginal mgfs ([[Independent Random Variable Equivalent Conditions]]). The converse holds for any distribution, since independence implies zero [[Covariance]].

# Properties
- For jointly normal variables, uncorrelated is equivalent to independent. In general only independence $\implies$ uncorrelated ([[Correlation]]); the equivalence needs joint normality, not just normal marginals.
- In particular, $N_n(\boldsymbol{\mu}, \Sigma)$ with diagonal $\Sigma$ has [[Mutually Independent Random Variables|mutually independent]] components.
- Combined with the [[Multivariate Normal Distribution Affine Transformation|affine transformation]] theorem: $A\mathbf{X}$ and $B\mathbf{X}$ are independent iff $A\Sigma B^T = O$. This is the mechanism behind the independence of $\bar{X}$ and $S^2$ in [[Student's Theorem]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=219)
