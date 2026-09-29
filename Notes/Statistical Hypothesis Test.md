---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Statistical Hypothesis Test[^1][^2]
> Let $X$ have pdf $f(x; \theta)$, $\theta \in \Omega$, and partition the [[Parameter Space]] into disjoint $\omega_0, \omega_1$ with $\omega_0 \cup \omega_1 = \Omega$. The hypotheses are
> $$
> \begin{align}
> H_0: \theta \in \omega_0 \quad \text{versus} \quad H_1: \theta \in \omega_1
> \end{align}
> $$
> A test based on a sample $X_1, \dots, X_n$ with sample space $\mathcal{D}$ is specified by a [[Critical Region]] $C \subseteq \mathcal{D}$:
> $$
> \begin{align}
> \text{Reject } H_0 \text{ (accept } H_1) &\text{ if } (X_1, \dots, X_n) \in C \\
> \text{Retain } H_0 \text{ (reject } H_1) &\text{ if } (X_1, \dots, X_n) \in C^c
> \end{align}
> $$

$H_0$ is the null hypothesis, usually representing no change or no difference from the past; $H_1$ is the alternative hypothesis, the research worker's hypothesis of a change or difference. Because the decision is based on a random sample, it can be wrong ([[Type I and Type II Errors]]).

# Types
- [[Simple Hypothesis]] vs. composite hypotheses.
- One-sided alternatives (e.g. $H_1: \theta > \theta_0$) and two-sided alternatives ($H_1: \theta \neq \theta_0$).[^3]
- [[Randomized Test]].

# Properties
- The standard (Neyman-Pearson) approach bounds the probability of a Type I error by the [[Size of a Test|size]] $\alpha$ and, among tests of size $\alpha$, maximizes the [[Power Function (Statistics)|power]].
- The decision is usually expressed through a [[Test Statistic]] $T$, with $C = \{T \geq c\}$, and reported through the [[P-Value]].
- Duality with confidence sets: $\{\theta_0 : H_0: \theta = \theta_0 \text{ is not rejected at level } \alpha\}$ is a $(1 - \alpha)$ [[Confidence Interval]].
- "Retain $H_0$" is not evidence that $H_0$ is true, only that the data were not inconsistent enough with it.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=283)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=284)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=291)
