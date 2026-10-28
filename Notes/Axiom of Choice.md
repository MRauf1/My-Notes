---
tags:
  - mathematics
  - measure_theory
  - topology
---

# Definition
> [!info] Axiom of Choice[^1]
> If $\{X_\alpha\}_{\alpha \in A}$ is a nonempty collection of nonempty [[Set|sets]], then the [[Cartesian Product]] $\prod_{\alpha \in A} X_\alpha$ is nonempty.

An element $f \in \prod_\alpha X_\alpha$ is a choice function: it picks one $f(\alpha) \in X_\alpha$ from every set simultaneously, even when no rule for doing so is available.

> [!abstract] Corollary (Choice Set for Disjoint Families)[^2]
> If $\{X_\alpha\}_{\alpha \in A}$ is a [[Disjoint Sets|disjoint]] collection of nonempty sets, there is a set $Y \subseteq \bigcup_{\alpha \in A} X_\alpha$ such that $Y \cap X_\alpha$ contains precisely one element for each $\alpha \in A$.

> [!info] Axiom of Choice (Munkres's Formulation)[^3]
> Given a collection $\mathcal{A}$ of disjoint nonempty sets, there exists a set $C \subseteq \bigcup_{A \in \mathcal{A}} A$ such that $C \cap A$ contains exactly one element for each $A \in \mathcal{A}$.

> [!abstract] Lemma (Existence of a Choice Function)[^4]
> Given a collection $\mathcal{B}$ of nonempty sets (not necessarily disjoint), there exists a [[Function]] $c: \mathcal{B} \to \bigcup_{B \in \mathcal{B}} B$ such that $c(B) \in B$ for each $B \in \mathcal{B}$. Such $c$ is called a choice function for $\mathcal{B}$.

The lemma removes the disjointness requirement; e.g. $\mathcal{B}$ may be the collection of all nonempty subsets of a given set.

> [!info] Finite Axiom of Choice[^5]
> Given a finite collection $\mathcal{A}$ of disjoint nonempty sets, there exists a set $C$ consisting of exactly one element from each element of $\mathcal{A}$.

The finite form is provable in ordinary set theory and uncontroversial: any proof making only finitely many arbitrary choices uses it. "The axiom of choice" always refers to the strong form for arbitrary collections.[^5]

# Properties
- Equivalent to the [[Hausdorff Maximal Principle]], [[Zorn's Lemma]], and the [[Well Ordering Principle (Set Theory)|well ordering principle]].[^1] The well-ordering theorem was historically the most controversial consequence.[^3]
- Gödel (1938) showed AC is consistent with ZF, and Cohen (1963) showed its negation is also consistent with ZF; hence AC is independent of ZF. See also [[Continuum Hypothesis]].
- The disjoint-family corollary is exactly what is used to build non-measurable sets (e.g. the Vitali set, choosing one representative from each coset of $\mathbb{Q}$ in $\mathbb{R}$), which is why AC matters in [[Measure (Measure Theory)|measure theory]].

[^1]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=19&annotation=UECP67I7)
[^2]: [Real Analysis: Modern Techniques and Their Applications](zotero://open-pdf/library/items/D7QVECG5?page=19&annotation=8PVA8EBJ)
[^3]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=61&annotation=S6ZUVR6W)
[^4]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=61&annotation=CMQSRAGP)
[^5]: [Topology (Munkres)](zotero://open-pdf/library/items/2AUACM23?page=63&annotation=QVAJ7IX8)
