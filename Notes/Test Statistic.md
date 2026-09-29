---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Test Statistic[^1]
> A [[Statistic]] $T(\mathbf{X})$ on which a [[Statistical Hypothesis Test]] is based: the [[Critical Region]] is expressed through it, typically as $C = \{\mathbf{x} : T(\mathbf{x}) \geq c\}$, where larger values of $T$ indicate stronger evidence against $H_0$.

A good test statistic has a known (or approximable) distribution under $H_0$, so that the critical value $c$ and the [[P-Value]] can be computed, and it tends to take different values under $H_1$.

# Types
- [[t-Test Statistic]], [[F-Test Statistic]], [[Wald Test Statistic]], [[Score Test Statistic]], [[Likelihood Ratio Test Statistic]].

# Properties
- It is often a pivot: a function of the data and the parameter whose distribution is free of the parameter, e.g. $(\bar{X} - \mu_0)/(S/\sqrt{n})$ under $H_0: \mu = \mu_0$ ([[Student's Theorem]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=284)
