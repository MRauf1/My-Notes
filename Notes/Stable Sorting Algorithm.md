---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Stable Sorting Algorithm[^1]
> A [[Sorting Algorithm]] that preserves the relative order of equal elements: if $a[i]$ and $a[j]$ have the same value with $i < j$, a stable sort always places $a[i]$ before $a[j]$ in the output.

# Properties
- Stable: [[Merge Sort]] (when merging, ties are broken by taking from the same side consistently) and [[Counting Sort]].[^1]
- [[Radix Sort]] is stable because it is built entirely out of stable [[Counting Sort]] passes — indeed, this is exactly what makes sorting digit-by-digit correct: each pass must preserve the order established by the previous (less significant) pass.[^2]
- Not (necessarily) stable: [[Quicksort]] and [[Heapsort]], both of which reorder elements via swaps that don't track which of two equal elements originally came first.

[^1]: [Morin, p. 233](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 234](zotero://select/library/items/HYS8NDAB)
