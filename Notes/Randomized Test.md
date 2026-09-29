---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Randomized Test[^1]
> A test that, for some observed values of the [[Test Statistic]] (typically the boundary value of a discrete statistic), decides whether to reject $H_0$ by an auxiliary random experiment independent of the data, e.g. reject with probability $\phi \in (0, 1)$.

With a discrete test statistic only a few [[Size of a Test|sizes]] are attainable by ordinary critical regions; randomizing on the boundary value makes the size exactly any desired $\alpha$.

# Properties
- Rarely used in practice: two statisticians with the same assumptions, data, and test could reach different decisions.[^2] Instead, the significance level is adjusted to an attainable one, or an observed significance level ([[P-Value]]) is reported, possibly the [[Mid P-Value]].
- Theoretically important: randomized tests make the set of tests convex, which is needed for exact optimality results such as the Neyman-Pearson lemma in the discrete case.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=294)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=295)
