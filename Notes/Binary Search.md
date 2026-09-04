---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Binary Search
> $$
> \begin{array}{ll}
> 1 & \textbf{BINARY-SEARCH}(A, n, x) \\
> 2 & low = 1,\ high = n \\
> 3 & \textbf{while } low \le high \\
> 4 & \quad mid = \lfloor (low + high) / 2 \rfloor \\
> 5 & \quad \textbf{if } A[mid] = x \\
> 6 & \quad\quad \textbf{return } mid \\
> 7 & \quad \textbf{elseif } A[mid] < x \\
> 8 & \quad\quad low = mid + 1 \\
> 9 & \quad \textbf{else} \\
> 10 & \quad\quad high = mid - 1 \\
> 11 & \textbf{return } \text{NIL}
> \end{array}
> $$

Binary search repeatedly halves the search interval of a sorted [[Array]] $A$ by comparing the target value $x$ to the middle element and discarding the half of the array that cannot contain $x$. This requires $A$ to be sorted beforehand; if it is not, [[Linear Search]] must be used instead.

# Properties
- Time complexity: $O(\log n)$ worst-case and average-case; $O(1)$ best-case.
- Space complexity: $O(1)$ iteratively; $O(\log n)$ if implemented recursively, due to the call stack.
- Requires the [[Array]] to be sorted.
