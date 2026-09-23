---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Recursion[^1]
> A kind of [[Reduction]] of a problem to itself:
> - If the given instance of the problem can be solved directly, solve it directly (**base case**).
> - Otherwise, reduce it to one or more simpler instances of the *same* problem.

The recursive calls are treated as a black box (the "Recursion Fairy") that correctly solves the simpler instances; formally, this black box is exactly the inductive hypothesis of a [[Proof by Induction]].[^2]

# Types
- [[Divide and Conquer]]

# Properties
- **Termination**: there must be no infinite sequence of reductions to simpler and simpler instances; the reductions must eventually reach an elementary base case solved by some other method, otherwise the algorithm loops forever. The most common way to guarantee this is to reduce to strictly *smaller* instances.[^3]
- Correctness of a recursive algorithm is proven by [[Proof by Induction|induction]] (often [[Proof by Strong Induction|strong induction]]) on the instance size.[^2]
- Running time is governed by a recurrence, often solved with a [[Recursion Tree]].

[^1]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=40&annotation=33ZU2I3E)
[^2]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=41&annotation=78YES3Y5)
[^3]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=41&annotation=GZTQZ6EL)
