---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Slicing (Python)[^1]
> A generalization of indexing on a [[Sequence (Python)|sequence]] that extracts an entire section in one step; `X[I:J]` returns a new object containing everything in `X` from offset `I` up to but not including offset `J`.

# Properties
- The left bound defaults to 0 and the right bound defaults to the sequence's length when omitted, so `X[:]` returns a full top-level copy of `X` in a new object[^2].
- Extended slicing, `X[I:J:K]`, adds a step (or stride) `K`, which defaults to `+1`; an explicit step can skip items, and a negative stride — as in `X[::-1]` — walks from right to left, effectively reversing the sequence[^3].
- Unlike indexing, where an out-of-bounds offset is always an error, an out-of-bounds slice bound is simply clamped to the sequence's actual bounds, which is useful for code that must accommodate sizes flexibly[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=104&annotation=GKLJY9UT)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=104&annotation=4XG8ZGJZ)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=232&annotation=63ZMSCXZ)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=231&annotation=LZD5Z4EB)
