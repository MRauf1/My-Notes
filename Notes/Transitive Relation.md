---
tags:
  - mathematics
  - discrete_mathematics
---

# Definition

> [!info] Definition 1 (Transitive [[Relation]])[^1]
> Let $R: A \rightarrow A$ be a [[Relation]]. It is transitive if for all $x, y, z \in A$, $((x, y) \in R \land (y, z) \in R) \implies (x, z) \in R$.
> $R$ is transitive if and only if $R \circ R \subseteq R$.

# Types
- [[Transitive Closure]]

# Properties
- If $R$ is transitive, so is $R^{-1}$
- - If $R_1, R_2$ are transitive, then so is $R_1 \cap R_2$, $R_1 \circ R_2$ (if also $R_1 \circ R_2 \subseteq R_2 \circ R_1$)

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=198)