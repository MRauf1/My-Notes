---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Bilinear Form[^1]
> A bilinear form on a [[Vector Space]] $V$ is a map $B: V \times V \rightarrow \mathbb{R}$, $(u, v) \mapsto B(u, v)$, that is linear in each argument separately. Given a [[Basis]], it is represented by a [[Matrix]] $B$ with $B(u, v) = u^T B v$.

Contrast with a [[Linear Operator]] $A: V \rightarrow V$, $u \mapsto Au$, which maps a vector to a vector. Both are written as square grids of numbers, but they are different objects.[^1]

> [!abstract] Change of Basis[^2]
> Under a change of coordinates $\tilde{x} = Px$ with $P$ invertible,
> $$\begin{align}
> \text{linear operator: } A &\mapsto PAP^{-1}, \\
> \text{bilinear form: } B &\mapsto P^{-T} B P^{-1}.
> \end{align}$$

Derivation: $u^TBv = (P^{-1}\tilde u)^T B (P^{-1}\tilde v) = \tilde u^T (P^{-T}BP^{-1})\tilde v$.

**Matrices are not objects, only representations of objects.** Since matrices can represent many kinds of objects that transform differently, scrawling grids of numbers makes it easy to forget which rules apply; the coordinate-free description should be kept in mind.[^3]

# Types
- Symmetric bilinear forms: $B(u, v) = B(v, u)$, i.e. $B^T = B$.
- Positive-definite symmetric forms are [[Inner Product|inner products]] (matrix: [[Positive Definite Matrix]]).
- In geometry: [[Induced Metric]]/[[First Fundamental Form]], [[Second Fundamental Form]], [[Riemannian Metric]].

# Properties
- Products of different kinds must be interpreted by what they represent: $\mathrm{I}S$ (bilinear form $\times$ linear map) represents the [[Second Fundamental Form]] and so transforms as a bilinear form.
- Compare [[Change of Basis Matrix with Linear Map]] and [[Similar Matrix]] (operator transformation) with congruence $B \mapsto Q^TBQ$ (form transformation).

[^1]: [Crane, p. 43](zotero://open-pdf/library/items/9N6JDPI2?page=44&annotation=T5VUXCT8)
[^2]: [Crane, p. 43–44](zotero://open-pdf/library/items/9N6JDPI2?page=45&annotation=ZFL249YY)
[^3]: [Crane, p. 42–43](zotero://open-pdf/library/items/9N6JDPI2?page=44&annotation=ZA5IPQSD)
