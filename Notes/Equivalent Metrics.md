---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Equivalent Metrics[^1]
> Two [[Metric|metrics]] $\rho_1$ and $\rho_2$ on a [[Set]] $X$ are equivalent if there exist $C, C' > 0$ such that
> $$
> \begin{align}
> C \rho_1 \leq \rho_2 \leq C' \rho_1.
> \end{align}
> $$

Equivalent metrics define the same [[Open Set|open]], [[Closed Set|closed]], and [[Compact Set|compact]] sets, the same [[Convergent Sequence|convergent]] and [[Cauchy Sequence|Cauchy]] sequences, and the same [[Continuous Function|continuous]] and [[Uniformly Continuous Function|uniformly continuous]] mappings. Consequently most results about [[Metric Space|metric spaces]] depend only on the equivalence class of the metric.[^1]

# Properties
- This (strong, Lipschitz) equivalence is stronger than topological equivalence (same open sets only); e.g. $\rho$ and $\min(\rho, 1)$ are topologically but not necessarily Lipschitz equivalent, and they differ in which sets are [[Bounded Set|bounded]].
- All norms on a finite-dimensional vector space induce equivalent metrics: [[Norm Equivalence Inequalities (Finite-Dimensional)]].

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=29&annotation=8TB7JY8F)
