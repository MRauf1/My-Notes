---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!info] Definition 1 (Cantor Set)[^1]
> Let $E_0 = [0, 1]$. Form $E_1$ by removing the open middle third $(\frac{1}{3}, \frac{2}{3})$ from $E_0$, so that $E_1 = [0, \frac{1}{3}] \cup [\frac{2}{3}, 1]$. Continuing, form $E_{n+1}$ from $E_n$ by removing the open middle third of each of the $2^n$ [[Interval|intervals]] making up $E_n$, so that $E_n$ is a union of $2^n$ intervals each of length $3^{-n}$, and $E_1 \supseteq E_2 \supseteq E_3 \supseteq \dots$. The Cantor set is
> $$
> \begin{align}
> P = \bigcap_{n=1}^{\infty} E_n
> \end{align}
> $$

Each $E_n$ is a finite union of [[Closed Set|closed]] [[Interval|intervals]], hence [[Compact Set|compact]]. Since the $E_n$ are nonempty and nested, the [[Finite Intersection Property|nested compact sets corollary]] guarantees that $P$ is nonempty; $P$ is itself compact, being an intersection of closed subsets of the compact set $E_1$.

# Properties
- $P$ is an example of a nonempty [[Perfect Subset|perfect set]] in $\mathbb{R}$ that contains no [[Interval|segment]].
- By the [[Perfect Subset|uncountability of nonempty perfect sets]], $P$ is [[Uncountable Set|uncountable]].
- $P$ has (Lebesgue) measure zero: $P$ is an example of an uncountable set of measure zero.[^2]

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=50)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=51)
