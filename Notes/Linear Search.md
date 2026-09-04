---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Linear Search
> $$
> \begin{array}{ll}
> 1 & \textbf{LINEAR-SEARCH}(A, n, x) \\
> 2 & \textbf{for } i = 1 \textbf{ to } n \\
> 3 & \quad \textbf{if } A[i] = x \\
> 4 & \quad\quad \textbf{return } i \\
> 5 & \textbf{return } \text{NIL}
> \end{array}
> $$

Linear search checks each element of an [[Array]] $A$ sequentially, from index $1$ to $n$, comparing it to the target value $x$, until a match is found or the array is exhausted. It makes no assumption about the ordering of $A$, so it works on both sorted and unsorted [[Array|arrays]].

# Properties
- Time complexity: $O(n)$ worst-case and average-case; $O(1)$ best-case.
- Space complexity: $O(1)$.
- Does not require the [[Array]] to be sorted.
