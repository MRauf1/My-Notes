---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (Stone-Weierstrass Theorem, Real Version)[^1]
> Let $\mathscr{A}$ be an [[Algebra of Functions|algebra]] of real [[Continuous Function|continuous functions]] on a [[Compact Set]] $K$. If $\mathscr{A}$ [[Point-Separating Family of Functions|separates points]] on $K$ and if $\mathscr{A}$ [[Point-Separating Family of Functions|vanishes at no point]] of $K$, then the uniform closure $\mathscr{B}$ of $\mathscr{A}$ consists of all real continuous functions on $K$.

> [!abstract] Theorem 2 (Stone-Weierstrass Theorem, Complex Version)[^2]
> Suppose $\mathscr{A}$ is a [[Self-Adjoint Algebra of Functions|self-adjoint]] algebra of complex continuous functions on a compact set $K$, $\mathscr{A}$ separates points on $K$, and $\mathscr{A}$ vanishes at no point of $K$. Then the uniform closure $\mathscr{B}$ of $\mathscr{A}$ consists of all complex continuous functions on $K$. In other words, $\mathscr{A}$ is [[Dense Subset|dense]] in $\mathscr{C}(K)$ ([[Space of Bounded Continuous Functions]]).

Theorem 1 does not hold for complex algebras without the self-adjointness condition (e.g., polynomials in $z$ on the unit circle are not dense, since their uniform limits extend holomorphically to the disk).[^3]

# Properties
- Generalizes the [[Weierstrass Approximation Theorem]] (polynomials on $[a, b]$).
- Implies trigonometric polynomials are uniformly dense in continuous $2\pi$-periodic functions ([[Fourier Series]]).
- Proof relies on the $|x|$ approximation corollary of the [[Weierstrass Approximation Theorem]] and on two-point interpolation ([[Point-Separating Family of Functions]]).

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=171&annotation=QB2G2FQP)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=174&annotation=CYAAU98N)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=174&annotation=H93A4LG9)
