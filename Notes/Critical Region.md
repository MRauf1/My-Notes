---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Critical Region[^1]
> For a [[Statistical Hypothesis Test]] of $H_0: \theta \in \omega_0$ versus $H_1: \theta \in \omega_1$ based on a sample with space $\mathcal{D}$, the critical (rejection) region is the subset $C \subseteq \mathcal{D}$ of samples for which $H_0$ is rejected. Its complement $C^c$ is the acceptance region.

Choosing a test is choosing $C$. The goal is to make both [[Type I and Type II Errors|error probabilities]] small, but they trade off, so $C$ is chosen with [[Size of a Test|size]] at most $\alpha$ and, among those, with the largest [[Power Function (Statistics)|power]].

# Properties
- Usually $C = \{\mathbf{x} : T(\mathbf{x}) \geq c\}$ for a [[Test Statistic]] $T$ and critical value $c$; a family $C_\alpha$ indexed by the level is nested (larger $\alpha$ gives a larger region), which is what defines the [[P-Value]].
- Extreme cases: $C = \emptyset$ never rejects (Type I error probability $0$, Type II error probability $1$); $C = \mathcal{D}$ always rejects.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=284)
