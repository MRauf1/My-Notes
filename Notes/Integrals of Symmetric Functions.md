---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Integrals of Symmetric Functions)[^1]
> Suppose $f$ is continuous on $[-a, a]$.
> - If $f$ is an [[Even Function]], then $\int_{-a}^{a} f(x)\,dx = 2\int_0^a f(x)\,dx$.
> - If $f$ is an [[Odd Function]], then $\int_{-a}^{a} f(x)\,dx = 0$.

# Properties
- Proof: split at $0$ and substitute $u = -x$ in $\int_{-a}^0 f(x)\,dx = \int_0^a f(-u)\,du$ ([[u-Substitution]]), which equals $\pm\int_0^a f(u)\,du$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=449)
