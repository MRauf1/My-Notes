---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Givens Rotation)[^1]
> A Givens rotation (plane rotation) is a matrix
> $$
> \begin{align}
> G = \begin{bmatrix} c & s \\ -s & c \end{bmatrix}, \qquad c^2 + s^2 = 1
> \end{align}
> $$
> where $c$ and $s$ are the cosine and sine of the angle of rotation. It is [[Orthogonal Matrix|orthogonal]], and is used to annihilate a single component of a vector.

> [!abstract] Theorem 2 (Choice of $c$ and $s$)[^2]
> For $a = [a_1, a_2]^T \neq 0$, taking
> $$
> \begin{align}
> c = \frac{a_1}{\sqrt{a_1^2 + a_2^2}}, \qquad s = \frac{a_2}{\sqrt{a_1^2 + a_2^2}}
> \end{align}
> $$
> gives $Ga = \begin{bmatrix} \alpha \\ 0 \end{bmatrix}$ with $\alpha = \sqrt{a_1^2 + a_2^2}$, i.e., $G$ rotates $a$ onto the first coordinate axis.

Derivation: rewrite $Ga = [\alpha, 0]^T$ as $\begin{bmatrix} a_1 & a_2 \\ a_2 & -a_1 \end{bmatrix} \begin{bmatrix} c \\ s \end{bmatrix} = \begin{bmatrix} \alpha \\ 0 \end{bmatrix}$, eliminate to get $s = \alpha a_2 / (a_1^2 + a_2^2)$, $c = \alpha a_1/(a_1^2 + a_2^2)$, and impose $c^2 + s^2 = 1$.[^2]

To avoid unnecessary [[Overflow Level|overflow]]/[[Underflow Level|underflow]]: if $|a_1| > |a_2|$, use $t = s/c = a_2/a_1$ and $c = 1/\sqrt{1 + t^2}$, $s = c \cdot t$; if $|a_2| > |a_1|$, use $\tau = c/s = a_1/a_2$ and $s = 1/\sqrt{1 + \tau^2}$, $c = s \cdot \tau$. Then no magnitude larger than 1 is squared. The angle itself is never needed.[^2]

> [!abstract] Theorem 3 (Annihilating Component $j$ of an $m$-Vector)[^3]
> To annihilate component $j$ of $a \in \mathbb{R}^m$ using component $i$, compute $c, s$ from $(a_i, a_j)$ as above and embed the $2 \times 2$ rotation in rows and columns $i, j$ of $I_m$: entries $(i,i) = (j,j) = c$, $(i,j) = s$, $(j,i) = -s$. This changes only components $i$ and $j$, setting $a_i \leftarrow \alpha$ and $a_j \leftarrow 0$.

A sequence of such rotations reduces $A$ to upper triangular form, giving a [[QR Decomposition]] whose $Q$ is the product of the rotations. The only constraint on the ordering is not to reintroduce nonzeros into previously annihilated entries. As with Householder, $Q$ need not be formed; if needed, accumulate the rotations into an initial identity matrix.[^3]

# Properties
- Introduces zeros one at a time, giving more selectivity than [[Householder Transformation|Householder transformations]].[^4]
- A straightforward Givens QR for general least squares takes about 50% more work than [[Householder QR Factorization|Householder]], and more storage (each rotation needs both $c$ and $s$, so the zeroed entry does not suffice). These can be overcome at the cost of a more complicated implementation.[^3]
- Hence reserved for cases where selectivity is paramount, e.g., [[Sparse Matrix|sparse]] matrices or when a pattern of existing zeros must be maintained.[^3]
- [[Rotation Matrix]] (with $\theta \to -\theta$)
- [[Orthogonal Matrix]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=147)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=148)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=149)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=147)
