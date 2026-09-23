---
tags:
  - mathematics
  - linear_algebra
---

# Definition

[[Solution|Solution]] for the [[Linear System of Equations|linear system]] is a [[Set|set]] of $c_1, c_2, ..., c_n \in \mathbb{F}$, such that when plugged in for the $x$ [[Variable|variables]], the [[Equation|equations]] hold true.

With each [[Linear Function|linear equation]]'s [[Solution|solutions]] being represented by a [[Line|line]], the solution(s) (if exists) of the system is the [[Intersection|intersection]] of all the lines.

More generally, in $n$ dimensions each linear equation determines a [[Hyperplane]], and the solution(s) of the system is the intersection of all the hyperplanes. In 2D, non-parallel lines meet at a unique point, while parallel lines either never meet (no solution) or coincide (infinitely many solutions).[^3]

A system of linear equations may have $1$ unique solution, infinitely many solutions, or no solutions.

> [!abstract] Theorem 1 (Solutions of a Square Linear System)[^4]
> For a square system $Ax = b$ with $A \in \mathbb{R}^{n \times n}$:
> - Unique solution: $A$ [[Nonsingular Matrix|nonsingular]], $b$ arbitrary.
> - Infinitely many solutions: $A$ singular, $b \in \operatorname{span}(A)$ (consistent).
> - No solution: $A$ singular, $b \notin \operatorname{span}(A)$ (inconsistent).
>
> Here $\operatorname{span}(A) = \{Ax : x \in \mathbb{R}^n\}$ is the [[Matrix Column Space|column space]] of $A$.

# Existence of Solution

Solution(s) exists $\iff$
1) The [[Vector|vector]] $\mathbf{b}$ lies in $\langle \mathbf{v_1}, \mathbf{v_2}, \dots, \mathbf{v_n} \rangle$ (the [[Span|span]] of the vectors $\mathbf{v_1}, \mathbf{v_2}, \dots, \mathbf{v_n}$)[^2]

# Uniqueness of Solution

Solution is unique if it is the only solution. In other words, if whenever $c'_1, c'_2, ..., c'_n$ are also solutions, then $c_1 = c'_1, c_2 = c'_2, ..., c_n = c'_n$.[^1]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=27)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=47)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=72)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=72)
