---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Angle Between $b$ and $\operatorname{span}(A)$)[^1]
> For the [[Linear Least Squares Problem|least squares problem]] $Ax \cong b$ with solution $x$ and $y = Ax = Pb$, let $\theta$ be the angle between $b$ and $y$:
> $$
> \begin{align}
> \cos(\theta) = \frac{\lVert Ax \rVert_2}{\lVert b \rVert_2} = \frac{\lVert y \rVert_2}{\lVert b \rVert_2}, \qquad \tan(\theta) = \frac{\lVert r \rVert_2}{\lVert Ax \rVert_2}
> \end{align}
> $$
> It measures how close $b$ is to $\operatorname{span}(A)$.

Unlike a square system, whose conditioning depends only on $A$, the conditioning of $Ax \cong b$ depends on $b$ as well, so the rectangular [[Condition Number of a Matrix|condition number]] $\operatorname{cond}(A) = \lVert A \rVert_2 \lVert A^+ \rVert_2$ alone does not characterize the sensitivity. If $b$ is nearly orthogonal to $\operatorname{span}(A)$ ($\theta \approx \pi/2$), then $y = Pb$ is itself small, so a small change in $b$ causes a relatively large change in $y$ and hence in $x$. A poor fit (large residual) means more sensitivity than a good fit (small residual).[^1]

> [!abstract] Theorem 2 (Perturbations in $b$)[^2]
> If $A$ has full column rank and $x + \Delta x$ solves $Ax \cong b + \Delta b$, then
> $$
> \begin{align}
> \frac{\lVert \Delta x \rVert_2}{\lVert x \rVert_2} \leq \operatorname{cond}(A) \frac{1}{\cos(\theta)} \frac{\lVert \Delta b \rVert_2}{\lVert b \rVert_2}
> \end{align}
> $$

Proof sketch: $\Delta x = A^+ \Delta b$, so $\lVert \Delta x \rVert_2 \leq \lVert A^+ \rVert_2 \lVert \Delta b \rVert_2$; divide by $\lVert x \rVert_2$ and use $\lVert A \rVert_2 \lVert x \rVert_2 \geq \lVert Ax \rVert_2$. The condition number is about $\operatorname{cond}(A)$ when the residual is small ($\cos\theta \approx 1$) but arbitrarily worse when it is large ($\cos\theta \approx 0$).[^2]

> [!abstract] Theorem 3 (Perturbations in $A$)[^3]
> If $A$ has full column rank and $x + \Delta x$ solves $(A + E)x \cong b$, then to first order
> $$
> \begin{align}
> \frac{\lVert \Delta x \rVert_2}{\lVert x \rVert_2} \lesssim \left( [\operatorname{cond}(A)]^2 \tan(\theta) + \operatorname{cond}(A) \right) \frac{\lVert E \rVert_2}{\lVert A \rVert_2}
> \end{align}
> $$

This uses $\lVert A \rVert_2^2 \cdot \lVert (A^TA)^{-1} \rVert_2 = [\operatorname{cond}(A)]^2$. The condition number is about $\operatorname{cond}(A)$ when the residual is small ($\tan\theta \approx 0$), effectively squared for a moderate residual, and arbitrarily large for a larger residual.[^4]

These bounds are the benchmark for judging least squares algorithms: an algorithm whose error is proportional to $\operatorname{cond}(A) + \lVert r \rVert_2 [\operatorname{cond}(A)]^2$ (e.g., [[Householder QR Factorization]]) is as good as can be expected, while the [[Normal Equations]] incur $[\operatorname{cond}(A)]^2$ even when the residual is small.[^4]

# Properties
- [[Condition Number of a Matrix]]
- [[Relative Condition Number]]
- [[Pseudoinverse]]
- [[Linear Least Squares Problem]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=134)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=135)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=135)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=136)
