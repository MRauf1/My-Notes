---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Simple and Composite Hypotheses[^1]
> A hypothesis is simple if it completely specifies the underlying distribution, e.g. $H_0: \theta = \theta_0$ (a single point of the [[Parameter Space]]). A hypothesis that does not completely specify the distribution, being composed of many simple hypotheses, is composite, e.g. $H_1: \theta < \theta_0$.

# Properties
- For a simple null, the [[Size of a Test|size]] and the [[P-Value]] are computed under one distribution; for a composite null, they are maximized (suprema) over all distributions in the null.
- With a simple null and a continuous [[Test Statistic]], the p-value is uniform under $H_0$.
- Testing a simple null against a simple alternative is the setting in which the most powerful test is given by the likelihood ratio (Neyman-Pearson lemma).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=286)
