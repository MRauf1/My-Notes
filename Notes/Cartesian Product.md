---
tags: mathematics, discrete_mathematics
---

# Definition

> [!info] Definition 1 (Cartesian Product)[^1]
> For two [[Set|sets]] $A, B$, their cartesian product is
> $$
> \begin{align}
> A \times B = \{(a, b) | a \in A \land b \in B\}
> \end{align}
> $$

The set of all [[Ordered Pair|ordered pairs]] where the first coordinate is the element of the first set and the second coordinate is the element of the second set.

# Properties

- $A \times (B \cap C) = (A \times B) \cap (A \times C)$ ([[Distributive Property|Distributes]] over [[Set Intersection|intersection]])
- $A \times (B \cup C) = (A \times B) \cup (A \times C)$ ([[Distributive Property|Distributes]] over [[Set Union|union]])
- $(A \times B) \cap (C \times D) = (A \cap C) \times (B \cap D)$
- $(A \times B) \cup (C \times D) \subseteq (A \cup C) \times (B \cup D)$
- $A \times \emptyset = \emptyset \times A = \emptyset$
- $A \times B = B \times A \iff A = \emptyset \lor B = \emptyset \lor A = B$

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=178)