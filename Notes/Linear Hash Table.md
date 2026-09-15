---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Linear Hash Table
> A [[Hash Table]] using open addressing with linear probing: elements are stored directly in an array $t$, with each location holding at most one value, instead of in per-bucket lists as in a [[Chained Hash Table]].[^1]

To store $x$ with $i \leftarrow \text{hash}(x)$, the table first tries location $t[i]$; if that is occupied, it tries $t[(i+1) \bmod \text{length}(t)]$, then $t[(i+2) \bmod \text{length}(t)]$, and so on, until it finds a place for $x$.[^2] Each entry of $t$ is one of three types: a **data value** actually in the set; **nil**, at a location never yet written to; or **del**, at a location whose data has since been deleted.[^3] Besides $n$ (the number of elements in the set), a second counter $q$ tracks the number of entries of the data and del types combined, i.e. $q = n + \#\{\text{del entries}\}$. Two invariants are maintained: $\text{length}(t) \geq 2q$, so that $t$ always has plenty of nil entries, and $\text{length}(t) = 2^d$ for an integer $d$, since many hash functions (e.g. [[Multiplicative Hashing]]) only work for table sizes that are a power of $2$.[^4]

# Operations
- **`find(x)`**: starting at $i = \text{hash}(x)$, probe $t[i], t[(i+1) \bmod \text{length}(t)], \dots$ until an index $i'$ is found with $t[i'] = x$ (return $t[i']$) or $t[i'] = \text{nil}$ (conclude $x$ is absent and return nil).[^5]
- **`add(x)`**: after confirming via `find(x)` that $x$ is not already present, probe the same sequence of locations until a nil or del entry is found, store $x$ there, and increment $n$ (and $q$, if the slot was nil rather than del).[^6]
- **`remove(x)`**: probe the same sequence until an index $i'$ is found with $t[i'] = x$ or $t[i'] = \text{nil}$; in the former case set $t[i'] \leftarrow \text{del}$ and return true, in the latter return false.[^7]
- **`resize()`**: triggered by `add(x)` once the number of non-nil entries exceeds $\text{length}(t)/2$, or by `remove(x)` once the number of data entries drops below $\text{length}(t)/8$. The smallest $d$ with $2^d \geq 3n$ is found, $t$ is reallocated to size $2^d$, every element is reinserted, and $q$ is reset to $n$ since the new $t$ contains no del entries.[^8]

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find(x)` | $O(1)$ expected$^*$ | $O(1)$ |
| `add(x)` | $O(1)$ expected$^*$ | $O(1)$ |
| `remove(x)` | $O(1)$ expected$^*$ | $O(1)$ |
| `resize()` | $O(m)$ total$^\dagger$ | $O(n)$ |

$^*$Ignoring the cost of calls to `resize()`, and assuming hash values are independently and uniformly distributed.
$^\dagger$Beginning from an empty table, any sequence of $m$ `add(x)`/`remove(x)` operations spends a total of $O(m)$ time across all calls to `resize()`.

## Why `add(x)` probes past elements with a different hash value
The probe sequence for `add(x)` walks *physical* slots $t[i], t[i+1], \dots$ of the array, not slots restricted to those sharing $\text{hash}(x)$ — it never compares hash codes while probing. It stops only when it reaches a slot that is nil, del, or (during the preceding `find(x)` check) equal to $x$. So it will indeed pass over occupied slots holding elements whose hash value differs entirely from $\text{hash}(x)$; those elements sit there because *they* collided with something earlier in *their own* probe sequence, or landed there directly. This is precisely what makes linear probing work without ever consulting hash codes mid-probe: correctness depends only on comparing against nil/del/$x$, never on matching hash values along the way.

## Why deleted entries become `del` rather than `nil`
None of `find(x)`, `add(x)`, or `remove(x)` ever sets a non-nil entry back to nil — the correctness of `find(x)` relies on this: reaching a nil entry proves it has *always* been nil, so no prior `add(x)` could have needed to probe past it, and therefore $x$ cannot be stored further along.[^9] If `remove(x)` set its slot to nil instead of del, it would punch a hole in the middle of what was a contiguous run of occupied slots. A later `find(y)` for some other key $y$ that had originally probed past that slot (because it was occupied when $y$ was added) would then stop early at the new nil and wrongly report $y$ as absent, even though $y$ is still stored further along the run. Marking the slot del instead preserves the run for the purposes of probing — it still counts as occupied so searches continue past it — while still being reusable as an insertion point for future `add(x)` calls.

# Analysis
Assuming all hash values are independent and uniformly distributed over $\{0, \dots, \text{length}(t)-1\}$ (an unrealistic but analytically convenient assumption), and that array indices are always taken modulo $\text{length}(t)$:[^10] a **run of length $k$ starting at $i$** occurs when $t[i], \dots, t[i+k-1]$ are all non-nil and $t[i-1] = t[i+k] = \text{nil}$.[^11]

> [!abstract] Lemma 5.4[^12]
> Fix a value $i \in \{0, \dots, \text{length}(t) - 1\}$. Then the probability that a run of length $k$ starts at $i$ is $O(c^k)$ for some constant $0 < c < 1$.

From this, the expected running time of `find(x)` for a value $x$ *not* in the table is $O(1)$.[^13] The cost of `add(x)` for a value not yet present is governed by the same analysis; the cost of `find(x)` for a value that *is* present equals the cost of the `add(x)` that originally inserted it; and the cost of `remove(x)` equals the cost of the corresponding `find(x)`.[^14] So, ignoring the cost of `resize()`, every operation runs in $O(1)$ expected time.[^15]

> [!abstract] Theorem 5.2[^16]
> A LinearHashTable implements the same interface as a [[Hash Table]]. Ignoring the cost of calls to `resize()`, a LinearHashTable supports `add(x)`, `remove(x)`, and `find(x)` in $O(1)$ expected time per operation. Furthermore, beginning with an empty LinearHashTable, any sequence of $m$ `add(x)` and `remove(x)` operations results in a total of $O(m)$ time spent during all calls to `resize()`.

This same $O(1)$-expected bound continues to hold even when the unrealistic full-independence assumption above is relaxed to [[Tabulation Hashing]].[^17]

# Space Usage
$n + O(n)$ words: the invariants $\text{length}(t) \geq 2q \geq 2n$ and the resizing target $2^d \geq 3n$ keep $\text{length}(t) = \Theta(n)$, and each of the $\text{length}(t)$ slots stores a single word-sized value.

# Properties
- [[Multiplicative Hashing]]
- [[Tabulation Hashing]]

[^1]: [Morin, p. 108](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 108](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 109](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 109](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 109](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 110](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 110](zotero://select/library/items/HYS8NDAB)
[^8]: [Morin, p. 111](zotero://select/library/items/HYS8NDAB)
[^9]: [Morin, p. 111](zotero://select/library/items/HYS8NDAB)
[^10]: [Morin, p. 112](zotero://select/library/items/HYS8NDAB)
[^11]: [Morin, p. 112](zotero://select/library/items/HYS8NDAB)
[^12]: [Morin, p. 112](zotero://select/library/items/HYS8NDAB)
[^13]: [Morin, p. 114](zotero://select/library/items/HYS8NDAB)
[^14]: [Morin, p. 115](zotero://select/library/items/HYS8NDAB)
[^15]: [Morin, p. 115](zotero://select/library/items/HYS8NDAB)
[^16]: [Morin, p. 115](zotero://select/library/items/HYS8NDAB)
[^17]: [Morin, p. 116](zotero://select/library/items/HYS8NDAB)
