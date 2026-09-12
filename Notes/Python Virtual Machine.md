---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Python Virtual Machine (PVM)[^1]
> The runtime engine of Python: a loop that iterates through a program's [[Python Bytecode]] instructions one by one and carries out their operations.

# Properties
- Not a separate program and need not be installed by itself — it is always present as part of the installed Python system, and is really just the final step of the "Python interpreter"[^1].
- Bytecode compilation and its execution by the PVM are deliberately hidden from Python programmers, who simply write and run files of statements while Python handles the runtime logistics behind the scenes[^2].
- Explains part of the speed gap with fully compiled languages: the PVM loop, not the CPU, must interpret each bytecode instruction, and a bytecode instruction requires more work than an equivalent native CPU instruction[^3].
- Net effect: because source is compiled to [[Python Bytecode]] only once rather than reparsed on every run, pure Python code runs at speeds somewhere between a fully compiled language and a traditional line-by-line interpreted language[^3].
- A process virtual machine — one that executes the instructions of a single program — distinct from a [[Virtual Machine|system virtual machine]], which virtualizes an entire computer, including its own operating system.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=42&annotation=6EDNMH6R)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=42&annotation=JICNC9YX)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=43&annotation=P82M397M)
