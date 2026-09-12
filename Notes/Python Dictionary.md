---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Python Dictionary[^1]
> A mutable mapping object that stores other objects by key rather than by relative position, distinguishing it from Python's [[Sequence (Python)|sequence]] types.

# Properties
- Like [[Python List|lists]], dictionaries are mutable and can grow or shrink in place, but their mnemonic keys make them better suited than lists to collections whose items are named or labeled, such as database-record-like fields[^1].
- Since Python 3.7, a dictionary retains its keys' insertion order — the order in which keys were added — rather than the arbitrary order used in earlier versions, adding a sequence-like flavor not shared by other non-sequence types[^2].
- Iterating a dictionary directly (`for key in D`) steps through its keys implicitly, while iterating `D.items()` yields `(key, value)` pairs; both rely on the same [[Iterable and Iterator (Python)|iteration protocol]] as other Python collections[^3].
- CPython implements the dictionary as a [[Hash Table]], mapping each key to a table slot via a hash function.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=119&annotation=ZCX9EWGM)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=121&annotation=3MY7HKUD)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=127&annotation=RP2XS2EV)
