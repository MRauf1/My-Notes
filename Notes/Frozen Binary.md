---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Frozen Binary (Standalone Executable)[^1]
> A single executable or app that bundles a Python program's [[Python Bytecode]] together with the [[Python Virtual Machine|Python Virtual Machine (PVM)]] and any support files or libraries it needs, so the program can be shipped to users as one package (e.g., a `.exe` on Windows, a `.app` on macOS, or an `.apk`/`.aab` on Android).

# Properties
- Not the output of a true compiler: it still runs bytecode through the [[Python Virtual Machine|Python Virtual Machine (PVM)]], so apart from a possible startup improvement, it executes at the same speed as the original source files[^2].
- Because Python itself is embedded in the bundle, the receiving machine does not need Python installed to run the program[^2].
- Since the bytecode is embedded rather than left as loose source files, it is not as easily viewed as ordinary Python source[^2].
- Not unusually small, since it contains an entire [[Python Virtual Machine|Python Virtual Machine (PVM)]], but not unusually large by current standards either[^2].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=50&annotation=YGTW6VS3)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=50&annotation=X7BLQECZ)
