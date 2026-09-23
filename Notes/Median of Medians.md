---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Median of Medians (Blum–Floyd–Pratt–Rivest–Tarjan Selection)[^1]
> A worst-case linear-time [[Quickselect]] variant that chooses a good pivot by [[Recursion|recursively]] computing the median of a carefully chosen subset of the input:[^2]
> 1. Divide the array into $\lceil n/5 \rceil$ blocks of $5$ elements (padding the last block with $\infty$s).
> 2. Compute the [[Median]] of each block by brute force and collect them into an array $M[1..\lceil n/5 \rceil]$.
> 3. Recursively compute the median of $M$ ("mom") and use it as the quickselect pivot.

# Properties
- **Good pivot**: mom is larger than $\lceil n/5 \rceil/2 - 1 \approx n/10$ block medians, each of which is larger than $2$ other elements in its block, so mom is larger than at least $3n/10$ elements; symmetrically, it is smaller than at least $3n/10$. Hence the second recursive call is on at most $7n/10$ elements.[^3]
- **Recurrence**: $T(n) \leq T(n/5) + T(7n/10) + O(n)$. In the [[Recursion Tree]], level $i$ has total size $(1/5 + 7/10)^i n = (9/10)^i n$, so the level sums decay geometrically. Bounding the non-recursive work by $8n/5$,[^4]
$$\begin{align}
T(n) \leq \frac{8n}{5}\sum_{i \geq 0}\left(\frac{9}{10}\right)^i = \frac{8n}{5}\cdot 10 = 16n.
\end{align}$$
- **Block size $5$** is the smallest odd block size that gives exponential decay in the recursion-tree analysis (block size $3$ gives $T(n/3) + T(2n/3) + O(n)$, whose level sums do not decay); even block sizes introduce additional complications.[^5]
- In practice it is faster than the worst-case bound suggests, but still slower than sorting for even moderately large arrays.[^4]

[^1]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=53&annotation=GEBADQW3)
[^2]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=55&annotation=5SWKDB93)
[^3]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=55&annotation=877I7A4D)
[^4]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=57&annotation=MYPGTLSX)
[^5]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=57&annotation=9FL27STJ)
