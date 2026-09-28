---
tags:
  - statistics
  - categorical_variable_prediction
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Random Variable|Random]] [[Vector]])
> Vector of Random Variables
> $$
> \begin{align}
> \mathbf{Z} = \begin{bmatrix}Z_1 \\ \vdots \\ Z_m\end{bmatrix}
> \end{align}
> $$

> [!info] Definition 2 (Random Vector)[^1]
> Given a [[Random Experiment]] with [[Sample Space]] $\mathcal{C}$, let $X_1, X_2$ be [[Random Variable|random variables]], assigning to each $c \in \mathcal{C}$ one and only one ordered pair $X_1(c) = x_1$, $X_2(c) = x_2$. Then $(X_1, X_2)$ is a random vector, and its space is the set of ordered pairs
> $$
> \begin{align}
> \mathcal{D} = \{(x_1, x_2) : x_1 = X_1(c), x_2 = X_2(c), c \in \mathcal{C}\}
> \end{align}
> $$

> [!info] Definition 3 ($n$-Dimensional Random Vector)[^2]
> Let random variables $X_1, \dots, X_n$ assign to each $c \in \mathcal{C}$ one and only one real number $X_i(c) = x_i$. Then $\mathbf{X} = (X_1, \dots, X_n)^T$ is an $n$-dimensional random vector with space $\mathcal{D} = \{(X_1(c), \dots, X_n(c)) : c \in \mathcal{C}\}$, and for $A \subseteq \mathcal{D}$,
> $$
> \begin{align}
> P[\mathbf{X} \in A] = P(\{c \in \mathcal{C} : (X_1(c), \dots, X_n(c)) \in A\})
> \end{align}
> $$
> Observed values are written $\mathbf{x} = (x_1, \dots, x_n)^T$.

A random vector is written $\mathbf{X} = (X_1, X_2)^T$, the transpose of the row vector $(X_1, X_2)$ (Hogg et al. write $'$ for the transpose), or as $(X, Y)$. It is a single function $\mathbf{X}: \mathcal{C} \to \mathbb{R}^2$ (or $\mathbb{R}^m$), and its distribution $P_{X_1, X_2}$ is determined by the [[Joint Cumulative Distribution Function]]. Subscripts are often dropped or abbreviated, e.g. $f_{12}$ for $f_{X_1, X_2}$.

# Types
- Discrete random vector, with a [[Multivariate Discrete Probability Distribution|joint pmf]]
- Continuous random vector, with a [[Multivariate Continuous Probability Distribution|joint pdf]]

# Properties
- [[Joint Cumulative Distribution Function]]
- [[Random Variable Support]] (support of a random vector)
- Each component is a random variable with a [[Marginal Distribution]], and a [[Conditional Distribution]] given the others.
- [[Mean Vector]] $E[\mathbf{X}]$, [[Covariance Matrix]], and more generally the [[Expectation of Random Matrix]]
- [[Mutually Independent Random Variables]] and [[Independent and Identically Distributed]] components
- [[Moment Generating Function of Random Vector]]
- [[Expectation]] of $g(\mathbf{X})$ is computed with the joint pmf or pdf.
- Distributions of functions of $\mathbf{X}$: [[Random Vector Transformation]], [[Cumulative Distribution Function Method]], [[Moment Generating Function Technique]], [[Convolution Formula]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=101)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=150)
