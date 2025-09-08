---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (Special Orthogonal Matrix)
> [[Matrix]] $A$ such that
> 1) $A$ is [[Orthogonal Matrix|orthogonal]]
> 2) $det(A) = 1$

# Properties
- $I \in SO(n)$
- $A \in SO(n) \implies A^{-1} = A^T \in SO(n)$
- $det(A) = det(A^T) = det(A^{-1}) = det(A)^{-1}$
- $A$ is special orthogonal $\iff$ $A$ is a [[Rotation Matrix|rotation matrix]]
- $A, B \in SO(n) \implies AB \in SO(n)$
	- $(AB)^TAB = B^T A^T AB = I$
	- $det(AB) = det(A)det(B) = 1$

# [[Algebraic Structures]]
- [[Set of Special Orthogonal Matrices]]
- [[Group of Special Orthogonal Matrices]]