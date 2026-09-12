---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Arbitrary Argument List (Python)[^1]
> In a [[Function (Python)|function]] definition, a `*name` parameter collects any extra unmatched positional arguments into a [[Python Tuple|tuple]], and a `**name` parameter collects any extra unmatched keyword arguments into a [[Python Dictionary|dictionary]].

# Properties
- In a function call, the same star syntax means the reverse: `*iterable` unpacks an iterable into separate positional arguments, and `**mapping` unpacks a mapping into separate keyword arguments, letting a caller assemble an argument list at runtime instead of hardcoding individual values[^2].
- Since Python 3.6, the dictionary built by a `**name` collector preserves the order the corresponding keyword arguments were passed in, following ordinary dictionary insertion order.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=674&annotation=Y4H2Y7KD)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=676&annotation=3U9WMUAF)
