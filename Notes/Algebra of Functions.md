---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Algebra of Functions)[^1]
> A family $\mathscr{A}$ of complex [[Function|functions]] defined on a [[Set]] $E$ is an algebra if
> (i) $f + g \in \mathscr{A}$,
> (ii) $fg \in \mathscr{A}$,
> (iii) $cf \in \mathscr{A}$
> for all $f \in \mathscr{A}$, $g \in \mathscr{A}$, and all complex constants $c$; that is, $\mathscr{A}$ is closed under addition, multiplication, and scalar multiplication. For an algebra of real functions, (iii) is only required for real $c$.

> [!info] Definition 2 (Uniformly Closed, Uniform Closure)[^1]
> $\mathscr{A}$ is **uniformly closed** if $f \in \mathscr{A}$ whenever $f_n \in \mathscr{A}$ ($n = 1, 2, 3, \dots$) and $f_n \rightarrow f$ [[Sequence of Function Uniform Convergence|uniformly]] on $E$.
> Let $\mathscr{B}$ be the set of all functions which are limits of uniformly convergent sequences of members of $\mathscr{A}$. Then $\mathscr{B}$ is called the **uniform closure** of $\mathscr{A}$.

This matches the closure in the [[Supremum Norm]] metric of [[Space of Bounded Continuous Functions]].

# Properties
- The set of all [[Polynomial|polynomials]] is an algebra; the [[Weierstrass Approximation Theorem]] says its uniform closure on $[a, b]$ is the set of all continuous functions on $[a, b]$.[^1]
- Let $\mathscr{B}$ be the uniform closure of an algebra $\mathscr{A}$ of [[Bounded Function|bounded functions]]. Then $\mathscr{B}$ is a uniformly closed algebra.[^2]
- [[Point-Separating Family of Functions]]
- [[Self-Adjoint Algebra of Functions]]
- [[Stone-Weierstrass Theorem]]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=170&annotation=HB5K9JEK)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=170&annotation=WCQMMGWQ)
