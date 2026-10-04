---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Theorem 1 (Summation by Parts / Abel's Formula)[^1]
> Let $\{a_n\}, \{b_n\}$ be sequences of complex numbers, and put $A_n = \sum_{k=0}^n a_k$ for $n \geq 0$, with $A_{-1} := 0$. Then for any integers $0 \leq p \leq q$,
> $$
> \begin{align}
> \sum_{n=p}^q a_n b_n = \sum_{n=p}^{q-1} A_n (b_n - b_{n+1}) + A_q b_q - A_{p-1} b_p
> \end{align}
> $$

This is the discrete analogue of integration by parts, and is the key identity used to prove the [[Dirichlet Test]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=79)
