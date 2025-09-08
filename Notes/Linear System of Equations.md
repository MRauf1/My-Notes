---
tags: mathematics, linear_algebra
---

# Definition

> [!info] Definition 1 (Linear System of Equations)
> [[Linear Function|Linear]] system of $m$ [[Equation|equations]] in $n$ [[Variable|variables]] over [[Field|field]] $\mathbb{F}$, is a [[Set|set]] of equations of the form
> $$
> \begin{align}
> a_{11} x_1 + a_{12} x_2 + ... + a_{1n} x_n &= b_1 \\
> &\vdots \\
> a_{m1} x_1 + a_{m2} x_2 + ... + a_{mn} x_n &= b_m
> \end{align}
> $$
> Where $a_{ij}, b_i \in \mathbb{F}$, for $1 \leq i \leq m$, $1 \leq j \leq n$.
> For [[Solution|solutions]], see [[Solution of Linear System|solution of linear system]].
> This is also called an $m \times n$ linear system.

A system of [[Linear Function|linear equations]].[^1] It is called linear because the variables can only be
1) [[Multiplication|Multiplied]] by [[Constant|constants]], or
2) [[Addition|Added]] to other variables multiplied by constants

> [!info] Definition 2 ([[Vector|Vector]] Form of a Linear System)
> $$
> \begin{align}
> x_1 \begin{bmatrix} a_{11} \\ a_{21} \\ \dots \\ a_{m1} \end{bmatrix} + x_2 \begin{bmatrix} a_{12} \\ a_{22} \\ \dots \\ a_{m2} \end{bmatrix} + \dots + x_n \begin{bmatrix} a_{1n} \\ a_{2n} \\ \dots \\ a_{mn} \end{bmatrix} = \begin{bmatrix} b_{1} \\ b_{2} \\ \dots \\ b_{m} \end{bmatrix}  
> \end{align}
> $$

# Types

## Consistency

Linear system is consistent if it has at least $1$ solution. Linear system is inconsistent if it has no solutions.[^2]

## Underdetermined vs. Overdetermined

An $m \times n$ linear system is underdetermined if $m < n$. It has fewer [[Equation|equations]] than [[Variable|variables]], thus, there is not enough information.
An $m \times n$ linear system is overdetermined if $m > n$.[^5] It has more equations than variables, which puts too many constraints.

# Theorems

## Existence and Uniqueness of [[Solution|Solutions]]

> [!abstract] Theorem 1
> Assuming the [[Augmented Matrix|augmented matrix]] $A$ is in [[Row Echelon Form|REF]], then the system is consistent $\iff$ there is no pivot in the last column of $A$.[^3]

> [!abstract] Theorem 2
> Assuming the augmented matrix $A$ of a linear system in $n$ variables is in REF and is consistent, then the system has a unique solution $\iff$ there is a pivot in each of the first $n$ columns of $A$.[^4]

> [!abstract] Corollary 3
> It is impossible for an underdetermined linear system to have a unique solution.[^5]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=22)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=27)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=38)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=39)
[^5]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=40)