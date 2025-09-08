---
tags: statistics
---

# Definition

> [!info] Definition 1 (Mutually Independent Events for $n$ Cases)
> For [[Event|events]] $A_1, A_2, ..., A_n$, they are mutually independent $\iff$ every [[Combination|combination]] of the events satisfies the multiplication rule (i.e. given some combination (this must work all combinations) $\{A_{i1}, A_{i2}, \dots, A_{ik}\} \subseteq \{A_1, A_2, \dots, A_n\}$, $P(A_{i1} \cap A_{i2} \cap \dots \cap A_{ik}) = P(A_{i1}) P(A_{i2}) \dots P(A_{ik})$)

> [!info] Definition 2 (Mutually Independent Events for $3$ Cases)
> For [[Event|events]] $A, B, C$, they are mutually independent $\iff$ [^1]
> 1) $A, B, C$ are pairwise [[Independent Events|independent]]
> 2) $P(A \cap B \cap C) = P(A) P(B) P(C)$

# Properties

- $A, B, C$ are mutually independent events $\implies$
	1) $A, (B \cap C)$ are mutually independent
	2) $A, (B \cup C)$ are mutually independent
	3) $A^c, (B \cap C^c)$ are mutually independent
	4) $A^c, B^c, C^c$ are mutually independent

[^1]: [Probability and Statistical Inference](zotero://open-pdf/library/items/RM5FREYV?page=40)