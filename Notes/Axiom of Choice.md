---
tags:
  - mathematics
  - measure_theory
---

# Definition
> [!info] Axiom of Choice[^1]
> If $\{X_\alpha\}_{\alpha \in A}$ is a nonempty collection of nonempty [[Set|sets]], then the [[Cartesian Product]] $\prod_{\alpha \in A} X_\alpha$ is nonempty.

An element $f \in \prod_\alpha X_\alpha$ is a choice function: it picks one $f(\alpha) \in X_\alpha$ from every set simultaneously, even when no rule for doing so is available.

> [!abstract] Corollary (Choice Set for Disjoint Families)[^2]
> If $\{X_\alpha\}_{\alpha \in A}$ is a [[Disjoint Sets|disjoint]] collection of nonempty sets, there is a set $Y \subseteq \bigcup_{\alpha \in A} X_\alpha$ such that $Y \cap X_\alpha$ contains precisely one element for each $\alpha \in A$.

# Properties
- Equivalent to the [[Hausdorff Maximal Principle]], [[Zorn's Lemma]], and the [[Well Ordering Principle (Set Theory)|well ordering principle]].[^1]
- Gödel (1938) showed AC is consistent with ZF, and Cohen (1963) showed its negation is also consistent with ZF; hence AC is independent of ZF. See also [[Continuum Hypothesis]].
- The disjoint-family corollary is exactly what is used to build non-measurable sets (e.g. the Vitali set, choosing one representative from each coset of $\mathbb{Q}$ in $\mathbb{R}$), which is why AC matters in [[Measure (Measure Theory)|measure theory]].

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=19&annotation=UECP67I7)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=19&annotation=8PVA8EBJ)
