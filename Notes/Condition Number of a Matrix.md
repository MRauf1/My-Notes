---
tags:
  - mathematics
  - linear_algebra
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Condition Number of a Matrix)[^1]
> The condition number of an invertible matrix $A \in M_n(\mathbb{C})$ is
> $$
> \kappa(A) = \lVert A \rVert_{op} \lVert A^{-1} \rVert_{op}
> $$

This is a special case of the [[Relative Condition Number]], specialized to the problem of solving the linear system $Ax = b$ using the [[Operator Norm]] of $A$ and $A^{-1}$.

> [!abstract] Theorem 2 (Condition Number is at Least 1)[^1]
> $\kappa(A) \geq 1$ for every invertible $A \in M_n(\mathbb{C})$.

> [!abstract] Theorem 3 (Relative Error Bound)[^2]
> Suppose $A^{-1}$ is known and used to solve $Ax = b$, but there is some error $h \in \mathbb{C}^n$ in $b$, i.e. the system actually solved is $Ay = b + h$. Then
> $$
> \frac{\lVert A^{-1} h \rVert}{\lVert x \rVert} \leq \kappa(A) \frac{\lVert h \rVert}{\lVert b \rVert}
> $$
> That is, the condition number of $A$ bounds the relative error in the computed solution in terms of the relative error in the input $b$.

The error in the computed solution is $A^{-1}h$, and its size can be bounded directly using the [[Operator Norm]] of $A^{-1}$: $\lVert A^{-1} h \rVert \leq \lVert A^{-1} \rVert_{op} \lVert h \rVert$. The operator norm of $A^{-1}$ tells us how an error of a given size in $b$ propagates to an error in the solution of $Ax = b$.

> [!abstract] Theorem 4 (Exercise 4.5.18)[^3]
> If $\kappa(A) = 1$ for $A \in M_n(\mathbb{C})$, then $A$ is a scalar multiple of a [[Unitary Matrix]].

> [!abstract] Theorem 5 (Exercise 5.2.11 -- In Terms of [[Singular Value|Singular Values]])[^4]
> Let $A \in M_n(\mathbb{C})$ be invertible with singular values $\sigma_1 \geq \dots \geq \sigma_n > 0$. Then
> $$
> \kappa(A) = \frac{\sigma_1}{\sigma_n}
> $$

> [!info] Definition 6 (Condition Number w.r.t. Any Matrix Norm)[^5]
> The condition number of a nonsingular square matrix $A$ with respect to a given [[Induced Matrix Norm|matrix norm]] is
> $$
> \begin{align}
> \operatorname{cond}(A) = \lVert A \rVert \cdot \lVert A^{-1} \rVert
> \end{align}
> $$
> By convention, $\operatorname{cond}(A) = \infty$ if $A$ is singular.

Since
$$
\begin{align}
\lVert A \rVert \cdot \lVert A^{-1} \rVert = \left( \max_{x \neq 0} \frac{\lVert Ax \rVert}{\lVert x \rVert} \right) \cdot \left( \min_{x \neq 0} \frac{\lVert Ax \rVert}{\lVert x \rVert} \right)^{-1}
\end{align}
$$
the condition number is the ratio of the maximum relative stretching to the maximum relative shrinking that $A$ does to any nonzero vector, i.e., it measures how much $A$ distorts the unit sphere of the norm. The larger it is, the more long and thin the image of the unit sphere (in 2D, the 2-norm circle becomes a cigar-shaped ellipse; the 1-/$\infty$-norm square becomes a skewed parallelogram).[^5]

The condition number measures how close a matrix is to being singular: a large condition number means nearly singular, and a condition number near 1 means far from singular. The [[Determinant]] is not a good indicator of near singularity: $\det(A) = 0$ iff $A$ is singular, but the magnitude of a nonzero determinant says nothing about how close to singular $A$ is.[^6]

> [!abstract] Theorem 7 (Estimating $\lVert A^{-1} \rVert$)[^6]
> Computing $\operatorname{cond}(A)$ from its definition costs more than solving $Ax = b$, so in practice it is only estimated (to about an order of magnitude) as a byproduct of the solution process. $\lVert A \rVert$ is cheap (max absolute column/row sum), while for $\lVert A^{-1} \rVert$: if $Az = y$, then $\lVert z \rVert = \lVert A^{-1}y \rVert \leq \lVert A^{-1} \rVert \cdot \lVert y \rVert$, so
> $$
> \begin{align}
> \frac{\lVert z \rVert}{\lVert y \rVert} \leq \lVert A^{-1} \rVert
> \end{align}
> $$
> with equality for some optimally chosen $y$. Choosing $y$ to make $\lVert z \rVert / \lVert y \rVert$ as large as possible gives a reasonable estimate of $\lVert A^{-1} \rVert$.

> [!abstract] Theorem 8 (Sensitivity to Perturbations in the Matrix)[^8]
> If $Ax = b$ and $(A + E)\hat{x} = b$, with $\Delta x = \hat{x} - x$, then
> $$
> \begin{align}
> \frac{\lVert \Delta x \rVert}{\lVert \hat{x} \rVert} \leq \operatorname{cond}(A) \frac{\lVert E \rVert}{\lVert A \rVert}
> \end{align}
> $$
> Together with Theorem 3 (perturbations in $b$), $\operatorname{cond}(A)$ is an "amplification factor" bounding the maximum relative change in the solution due to a relative change in the input data.

Geometrically in 2D: if the two lines are nearly parallel (ill-conditioned), small uncertainty in the lines (rounding/measurement error) makes their intersection poorly defined; if they are nearly perpendicular (well-conditioned), the intersection is sharply defined. The intersection can lie anywhere in the shaded parallelogram below.[^9]

![[Well-Conditioned and Ill-Conditioned Linear Systems.png]]

> [!abstract] Theorem 9 (Loss of Accuracy)[^9]
> If the input data are accurate to [[Machine Epsilon|machine precision]], the relative error of an approximate solution $\hat{x}$ to $Ax = b$ is expected to satisfy
> $$
> \begin{align}
> \frac{\lVert \hat{x} - x \rVert}{\lVert x \rVert} \lesssim \operatorname{cond}(A)\, \epsilon_{mach}
> \end{align}
> $$
> i.e., the computed solution loses about $\log_{10}(\operatorname{cond}(A))$ decimal digits of accuracy relative to the accuracy of the input.

Caveats:[^10]
- Norm-based bounds bound the relative error in the *largest* components of the solution; the relative error in smaller components can be much larger, since a norm is dominated by the largest components. Componentwise bounds exist but are more complicated, and matter most for poorly scaled systems.
- $\operatorname{cond}(A)$ is affected by the scaling of $A$. A large condition number can come from poor scaling as well as from near singularity; rescaling helps the former but not the latter.
- A small [[Residual of Linear System|residual]] does not imply a small error when $\operatorname{cond}(A)$ is large.

# Properties
- The following hold for any norm:[^7]
	- $\operatorname{cond}(A) \geq 1$.
	- $\operatorname{cond}(I) = 1$.
	- $\operatorname{cond}(\gamma A) = \operatorname{cond}(A)$ for any nonzero scalar $\gamma$.
	- For a [[Diagonal Matrix]] $D = \operatorname{diag}(d_i)$, $\operatorname{cond}(D) = \dfrac{\max |d_i|}{\min |d_i|}$.
	- $\operatorname{cond}(A) = \operatorname{cond}(A^{-1})$ for nonsingular $A$.
- The value of $\operatorname{cond}(A)$ depends on the norm used, but by [[Norm Equivalence Inequalities (Finite-Dimensional)|norm equivalence]], values in different norms differ by at most a constant depending on $n$, so they are equally useful measures of conditioning.[^5]
- [[Nonsingular Matrix]]
- [[Residual of Linear System]]
- [[Relative Condition Number]]
- [[Operator Norm]]
- [[Unitary Matrix]]
- [[Singular Value]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=294)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=295)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=307)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=330)
[^5]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=76)
[^6]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=78)
[^7]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=78)
[^8]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=80)
[^9]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=81)
[^10]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=81)
