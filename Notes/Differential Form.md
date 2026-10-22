---
tags:
  - mathematics
  - differential_geometry
---

# Definition

[[Expression]] obtained by adding/multiplying real-valued [[Function]] and the [[Differential]] of the [[Natural Coordinate Function]] of $\mathbb{R}^n$.[^1]

Extension of [[1-Form]]. If each summand has $p$ $dx_i$'s, then it is a $p$-form and is said to have degree $p$. In particular, $0$-form is just the [[Smooth Function]] $f$.

The multiplication of differential forms is denoted by the wedge product $\land$. In general, the product of a $p$-form and a $q$-form is a $(p + q)$-form.

**Scalars or vectors?** An ordinary (real-valued) $k$-form eats $k$ tangent vectors and returns a *number*: a $0$-form is a function, a $1$-form $\alpha(X)$ measures a vector (e.g. $d\phi(X)$ is a directional derivative), a $2$-form measures oriented area spanned by two vectors. One can also allow *vector-valued* forms, which return vectors: the differential $df$ of an immersion $f: M \rightarrow \mathbb{R}^3$ ([[Tangent Map|pushforward]]) is an $\mathbb{R}^3$-valued 1-form, i.e. a triple of ordinary 1-forms $(df_1, df_2, df_3)$, and likewise the [[Weingarten Map]] $dN$. So forms output scalars by default and vectors when their coefficients are vector-valued; the definition is applied componentwise.

# Properties
- [[Associative Property]]
- [[Distributive Property]]
- [[Differential Form Alternation Rule]]

## [[Wedge Product]]
- [[Differential Form Wedge Product Alternation Rule]]

[^1]: [Elementary Differential Geometry](zotero://open-pdf/library/items/F6CCEWIU?page=43)