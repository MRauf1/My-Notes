---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Random Sample[^1]
> If the random variables $X_1, \dots, X_n$ are [[Independent and Identically Distributed|independent and identically distributed]] (iid), each with the same distribution, they constitute a random sample of size $n$ from that common distribution.

A random sample models $n$ independent repetitions of the same [[Random Experiment]]; the common distribution is the population being sampled.

# Properties
- Joint pdf $\prod_{i=1}^n f(x_i)$ for a common pdf $f$.
- Functions of the sample, such as the [[Sample Mean]] and [[Sample Variance]], are statistics; their moments follow from the rules for a [[Linear Combination of Random Variables]].
- The likelihood used in [[Maximum Likelihood Estimation]] is the joint pdf of a random sample viewed as a function of the parameter.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=168)
