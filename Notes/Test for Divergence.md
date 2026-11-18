---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Test for Divergence)[^1]
> If $\lim_{n \to \infty} a_n$ does not exist or $\lim_{n \to \infty} a_n \neq 0$, then the [[Infinite Series]] $\sum a_n$ is divergent.

# Properties
- Contrapositive of: if $\sum a_n$ converges, then $a_n \to 0$, since $a_n = s_n - s_{n-1} \to s - s = 0$ ([[Limit of Sequence]]).
- The converse fails: $a_n \to 0$ does not imply convergence, e.g. the harmonic series $\sum \frac{1}{n}$ diverges ([[p-Series]]).

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=745)
