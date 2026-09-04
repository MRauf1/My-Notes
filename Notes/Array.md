---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Array
> A [[Data Structure]] that stores elements of the same type in contiguous blocks of memory, where each element is accessed directly by an integer index.

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access | $O(1)$ | $O(1)$ |
| [[Linear Search\|Search (Unsorted)]] | $O(n)$ | $O(1)$ |
| [[Binary Search\|Search (Sorted)]] | $O(\log n)$ | $O(1)$ |
| Add (End) | $O(1)^*$ | $O(1)$ |
| Add (Beginning / Middle) | $O(n)$ | $O(1)$ |
| Remove (End) | $O(1)$ | $O(1)$ |
| Remove (Beginning / Middle) | $O(n)$ | $O(1)$ |

$^*$Amortized, since a dynamic array must occasionally reallocate to a larger block once it is full.
