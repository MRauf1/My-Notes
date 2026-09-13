---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Finally Clause (Python)[^1]
> An optional clause on a [[Try Statement (Python)|try statement]] that always runs its block "on the way out" of the statement, whether or not an exception occurred in the try block — termination logic related to exceptions only incidentally, since it works around them rather than catching them.

# Properties
- Guarantees cleanup code runs even if an exception is raised partway through the code it wraps, unlike code placed immediately after a risky call, which is simply skipped if that call raises[^2].
- Can be combined with `except`/`else` clauses in the same try statement; it still runs regardless of whether an exception was raised, and regardless of whether an `except` clause caught it[^3].
- During [[Exception Propagation (Python)|exception propagation]], every enclosing try statement's `finally` block runs in turn as the exception unwinds outward, even though none of them catches or stops it — only a matching `except` does that[^4].
- The [[Context Manager (Python)|with statement]] offers an alternative to a `try`/`finally` pair for objects that support its protocol, running startup as well as termination actions with less code, though `try`/`finally` remains the more general tool[^5].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1331&annotation=8ECVHXC6)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1331&annotation=U3XKZ6J8)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1332&annotation=PVSSHCYP)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1404&annotation=KTFPGLIF)
[^5]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1367&annotation=A2A2EW4G)
