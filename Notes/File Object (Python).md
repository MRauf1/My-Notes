---
tags:
  - computer_science
  - python
---

# Definition
> [!info] File Object (Python)[^1]
> The object returned by the built-in `open` function, which serves as a script's link to an external file and provides methods for transferring string data to and from it.

# Properties
- A file's content is always read into a script as a string, regardless of the underlying data the file actually holds[^2].
- Output is buffered by default, so written text may not reach disk immediately; closing the file, or calling its `flush` method, forces any buffered output to be written[^3].
- Closing a file releases its system resources and flushes any remaining buffered output; Python's [[Garbage Collection (Python)|garbage collection]] also closes a file automatically once it is no longer referenced, though this auto-close is a CPython implementation detail, not a guarantee of the language itself[^4].
- The `with` statement acts as a context manager that guarantees a file is closed on exit from its block, whether or not an error occurs, as a more reliable alternative to relying on garbage collection or a manual `try`/`finally`[^5].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=340&annotation=AI5WZMV6)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=130&annotation=9CV4XCYS)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=344&annotation=QRMDIHTQ)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=345&annotation=L8TWSHP3)
[^5]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=356&annotation=87XMX6G8)
