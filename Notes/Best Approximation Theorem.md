---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Best Approximation Theorem)[^1]
> Let $U$ be a finite-dimensional subspace of $V$.
> 1) For each $v \in V$, $\lVert P_U v \rVert \leq \lVert v \rVert$, with equality if and only if $v \in U$.
> 2) For each $v \in V$ and $u \in U$, $\lVert v - P_U v \rVert \leq \lVert v - u \rVert$, with equality if and only if $u = P_U v$.

![[Orthogonal Projection Norm Inequality.png]]
![[Orthogonal Projection Best Approximation.png]]

# Example
> [!example]- Best Quadratic Polynomial Approximation of $e^x$
> To approximate $f(x) = e^x$ by a quadratic polynomial $q(x)$ on $[0,1]$ so that $\int_0^1 |f(x) - q(x)|^2 \, dx$ is as small as possible, the best approximation is $q = P_{\mathcal{P}_2(\mathbb{R})} f$, using the inner product $\langle f, g \rangle = \int_0^1 f(x)g(x) \, dx$ on $C([0,1])$.

# Properties
- Part 2 says that, among all points $u \in U$, the [[Orthogonal Projection]] $P_U v$ is the unique closest point to $v$: finding the best approximation of $v$ by a point in $U$ reduces to computing $P_U v$.
- Underlies [[Simple Linear Regression|least-squares regression]]: the best-fitting line $y = mx+b$ minimizing $\sum_{i=1}^n (mx_i+b-y_i)^2$ is obtained by taking $u = P_U y$, for $U$ the subspace of vectors of the form $mx+b$.
- Underlies approximating a complicated function by a simpler one (e.g. a polynomial) with respect to a norm induced by an [[Inner Product]] over an interval, unlike a Taylor polynomial, which only approximates well near a single point.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=278)
