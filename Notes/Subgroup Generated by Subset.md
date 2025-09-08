---
tags: mathematics, abstract_algebra
---

# Properties

## Main Property
- $G$ is a group, $\{H_i\}_{i \in I}$ is a collection of subgroups of $G$, then $H := \cap_{i \in I} H_i$ is a subgroup of $G$
## Subset Generating Subgroup
- Denoted as $<S>$ where $S$ is the subset
- $G$ is a group, $S \subseteq G$, $H$ is a subgroup of $G$, then $<S> := \cap_{H_i \leq G, S \subseteq H_i} H_i$ is the smallest subgroup of $G$ containing $S$
- $<S> = \{e\} \cup \{g_1 \cdot \dots \cdot g_k | k \geq 1, k \in \mathbb{N}, g_i \in S \lor g_i^{-1} \in S\}$ (Set of "words in $S$")
## Single Element Subset Generating Subgroup
- $<\{a\}>$ (also denoted as $<a>$) $= \{a^k | k \in \mathbb{Z}\}$
- $<\{a\}>$ is an [[Abelian Group]]