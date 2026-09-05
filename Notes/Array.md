---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Array
> A fixed-size [[Data Structure]] that stores elements of the same type in contiguous blocks of memory, where each element is accessed directly by an integer index. Its size is set at allocation and cannot grow or shrink; see [[ArrayList]] for a resizable variant.

As a fixed-size structure, an Array allocates exactly the space it needs and never wastes space due to resizing, unlike its dynamic counterparts (see [[ArrayList]]).

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access | $O(1)$ | $O(1)$ |
| [[Linear Search\|Search (Unsorted)]] | $O(n)$ | $O(1)$ |
| [[Binary Search\|Search (Sorted)]] | $O(\log n)$ | $O(1)$ |
| [[Sorting Algorithm\|Sort]] | Varies$^*$ | Varies$^*$ |

$^*$Depends on the sorting algorithm used; see [[Sorting Algorithm]].

# Space Usage
$n + O(1)$ words: $n$ words for the elements themselves, plus a constant number of bookkeeping fields (e.g. its length).

# Types
- [[ArrayList]]

# Properties
- [[Linear Data Structure]]
- [[Contiguous Data Structure]]
