---
tags: mathematics, discrete_mathematics
---

# Definition

[[Quantifier|Quantifier]] representing that the [[Proposition|statement]] $P(x)$ is true for only one unique value $x$ and is written $\exists ! P(x)$.[^1]

Statement $\exists ! P(x)$ is logically equivalent to the statements[^2]
- $\exists x (P(x) \land \neg \exists y (P(y) \land y \neq x))$
- $\exists x (P(x) \land \forall y (P(y) \implies y = x))$
- $\exists x \forall y (P(y) \iff y = x)$
- $\exists x P(x) \land \forall y \forall z ((P(y) \land P(z)) \implies y = z)$

[^1]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=82)
[^2]: [HOW TO PROVE IT: A Structured Approach, Second Edition](zotero://open-pdf/library/items/THI2Q4PN?page=161)