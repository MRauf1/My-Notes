---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Theorem 1 (Nested Interval Theorem)[^1]
> Let $\{I_n\}_{n=1}^{\infty}$ be a [[Sequence]] of [[Interval|intervals]] in $\mathbb{R}$ such that $I_n \supseteq I_{n+1}$ for every $n$. Then $\bigcap_{n=1}^{\infty} I_n$ is nonempty.

> [!abstract] Theorem 2 (General Case: Nested $k$-Cells)[^2]
> Let $k$ be a positive integer, and let $\{I_n\}_{n=1}^{\infty}$ be a [[Sequence]] of [[k-Cell|$k$-cells]] in $\mathbb{R}^k$ such that $I_n \supseteq I_{n+1}$ for every $n$. Then $\bigcap_{n=1}^{\infty} I_n$ is nonempty.

The $n=1$ case (intervals in $\mathbb{R}$) is the special case $k=1$ of the general [[k-Cell|$k$-cell]] statement, since a $1$-cell is exactly an interval.

> [!abstract] Theorem 3[^3]
> Every [[k-Cell|$k$-cell]] is [[Compact Set|compact]].

# Properties
- Follows from, and is a special case of, the [[Finite Intersection Property]] for [[Compact Set|compact sets]], since every $k$-cell is compact (Theorem 3).
- Used to prove the [[Heine-Borel Theorem]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=47)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=48)
[^3]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=48)
