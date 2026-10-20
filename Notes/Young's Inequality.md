---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Theorem 1 (Young's Inequality for Products)[^1]
> Let $p, q > 0$ be real numbers with $\frac{1}{p} + \frac{1}{q} = 1$. If $u \geq 0$ and $v \geq 0$, then
> $$
> \begin{align}
> uv \leq \frac{u^p}{p} + \frac{v^q}{q}
> \end{align}
> $$
> with equality if and only if $u^p = v^q$.

# Properties
- Key lemma for [[Hölder's Inequality]]: normalize $\int |f|^p\,d\alpha = \int |g|^q\,d\alpha = 1$, apply Young pointwise, and integrate to get $\int |fg|\,d\alpha \leq 1$.
- Follows from concavity of $\log$: $\log\left(\frac{u^p}{p} + \frac{v^q}{q}\right) \geq \frac{1}{p}\log u^p + \frac{1}{q}\log v^q = \log(uv)$ ([[Convex Function]]); i.e. a weighted AM-GM inequality.
- $p = q = 2$: $uv \leq \frac{u^2 + v^2}{2}$.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=148&annotation=9F2ZFFMT)
