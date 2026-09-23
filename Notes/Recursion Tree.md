---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Recursion Tree[^1]
> A rooted [[Tree]] with one node per recursive subproblem of a [[Recursion|recursive]] algorithm, where the value of each node is the time spent on that subproblem *excluding* recursive calls. The total running time of the algorithm is the sum of the values of all nodes.

For a [[Divide and Conquer]] recurrence $T(n) = r\,T(n/c) + f(n)$, the root has value $f(n)$ and $r$ children, each the root of a recursion tree for $T(n/c)$. Equivalently, it is a complete $r$-ary tree ([[Complete m-ary Tree]]) whose nodes at depth $d$ have value $f(n/c^d)$.[^2]

# Properties
- **Level-by-level sum**: level $i$ has exactly $r^i$ nodes, each of value $f(n/c^i)$, so[^3]
$$\begin{align}
T(n) = \sum_{i=0}^{L} r^i f\!\left(\frac{n}{c^i}\right), \qquad L = \log_c n,
\end{align}$$
where the depth $L$ follows from the base case $n/c^L = 1$.
- **Number of leaves**: $r^L = r^{\log_c n} = n^{\log_c r}$, so the last term of the sum is $n^{\log_c r} f(1) = O(n^{\log_c r})$ since $f(1) = O(1)$.[^4]
- **Three easy cases** of the level-by-level [[Geometric Series|series]]:[^5]
	- *Decreasing*: if every term is a constant factor smaller than the previous, $T(n) = O(f(n))$ — dominated by the root.
	- *Equal*: if all terms are equal, $T(n) = O(f(n)\,L) = O(f(n)\log n)$.
	- *Increasing*: if every term is a constant factor larger than the previous, $T(n) = O(n^{\log_c r})$ — dominated by the leaves.
- The method also applies to recurrences with unequal subproblem sizes, e.g. $T(n) = T(n/5) + T(7n/10) + O(n)$ for [[Median of Medians]].
- Floors and ceilings can be removed beforehand via a [[Domain Transformation]].

[^1]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=49&annotation=6HJXD8EE)
[^2]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=50&annotation=9JUWJQJ3)
[^3]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=50&annotation=ZTA9VBDL)
[^4]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=51&annotation=R8HCMRSN)
[^5]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=51&annotation=PV5SRQWD)
