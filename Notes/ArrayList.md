---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] ArrayList
> A resizable [[Data Structure]] built on an underlying [[Array]] that automatically reallocates to a larger block once its capacity is full, allowing elements to be added or removed beyond a fixed size.

Because the underlying array is doubled once it fills (and halved once it becomes at most one-quarter full), an ArrayList can waste up to $O(n)$ space at any given moment — for instance, immediately after growing, roughly half of the newly allocated block is unused. See [[RootishArrayList]] for a variant that reduces this to $O(\sqrt{n})$.

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access | $O(1)$ | $O(1)$ |
| [[Linear Search\|Search (Unsorted)]] | $O(n)$ | $O(1)$ |
| [[Binary Search\|Search (Sorted)]] | $O(\log n)$ | $O(1)$ |
| Insert (Beginning) | $O(n)$ | $O(1)$ |
| Insert (Middle) | $O(n)$ | $O(1)$ |
| Insert (End) | $O(1)^*$ | $O(1)$ |
| Remove (Beginning) | $O(n)$ | $O(1)$ |
| Remove (Middle) | $O(n)$ | $O(1)$ |
| Remove (End) | $O(1)$ | $O(1)$ |
| [[Sorting Algorithm\|Sort]] | Varies$^\dagger$ | Varies$^\dagger$ |

$^*$Amortized, since the array must occasionally reallocate to a larger block once it is full.
$^\dagger$Depends on the sorting algorithm used; see [[Sorting Algorithm]].

# Space Usage
$n + O(n)$ words in the worst case: the underlying array's capacity stays within a constant factor of $n$, but up to roughly half of it can be unused at any given moment right after growing. See [[RootishArrayList]] for a variant using only $n + O(\sqrt{n})$ words.

# Types
- [[Stack]]
- [[Queue]]
- [[Deque]]

# Properties
- [[Linear Data Structure]]
- [[Contiguous Data Structure]]
