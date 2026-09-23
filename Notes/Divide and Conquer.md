---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Divide and Conquer[^1]
> A three-step [[Recursion|recursive]] algorithm design pattern:
> 1. **Divide** the given instance into several *independent* smaller instances of exactly the same problem.
> 2. **Delegate** each smaller instance to the recursion (the "Recursion Fairy").
> 3. **Combine** the solutions of the smaller instances into the solution of the given instance.
>
> If the size of an instance falls below some constant threshold, recursion is abandoned and the instance is solved directly by brute force in $O(1)$ time.[^2]

# Types
- [[Merge Sort]]
- [[Quicksort]]
- [[Quickselect]]
- [[Median of Medians]]

# Properties
- Proving a divide-and-conquer algorithm correct almost always requires [[Proof by Induction|induction]].[^3]
- Analyzing its running time requires setting up and solving a recurrence, which can usually (but not always) be done with a [[Recursion Tree]].[^3] An algorithm making $r$ recursive calls on instances of size $n/c$ and doing $O(f(n))$ non-recursive work satisfies
$$\begin{align}
T(n) = r\,T(n/c) + f(n).
\end{align}$$
- Floors, ceilings, and lower-order terms in such recurrences can be ignored, as justified by a [[Domain Transformation]].[^4]
- A special kind of [[Reduction]].

[^1]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=49&annotation=8M79YLSY)
[^2]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=49&annotation=M67TH2AB)
[^3]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=49&annotation=LQFW58X7)
[^4]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=53&annotation=SM5NN689)
