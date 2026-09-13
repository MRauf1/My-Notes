---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Python[^1]
> A [[High-Level Programming Language|general-purpose programming language]] that blends procedural, functional, and object-oriented paradigms and accelerates software development by reducing complexity.

# Properties
- Runs on an interpreter: the standard implementation, [[CPython]], compiles source code to [[Python Bytecode]] and executes it via the [[Python Virtual Machine|Python Virtual Machine (PVM)]], rather than compiling all the way down to native machine code.
- Trades execution speed for development speed: because it is not fully compiled to machine code, Python can run more slowly than fully compiled, lower-level languages such as C and C++[^2]; however, this speed-of-development gain is often far more important than the speed-of-execution loss, given modern computer speeds and deadlines[^3].
- Runs at native C speed for tasks immediately dispatched to compiled C code inside the interpreter, such as file processing or GUI construction, so the interpretive overhead mainly affects pure Python computation[^4].
- Acts as a glue language: Python programs can be combined with components written in other languages, both locally and across networks, letting functionality be added to the Python system as needed[^5].
- Every piece of data a script processes is an [[Object (Python)|object]], and Python is both [[Dynamic Typing (Python)|dynamically]] and [[Strong Typing (Python)|strongly]] typed.
- A program is built from [[Statement (Python)|statements]] — such as the [[Assignment Statement (Python)|assignment]], [[If Statement (Python)|if]], [[While Loop (Python)|while]], and [[For Loop (Python)|for]] statements — that act on these objects.
- Code is packaged for reuse chiefly as [[Function (Python)|functions]], which Python also treats as first-class objects.
- Programs are organized into [[Module (Python)|modules]] — normally one file each — which a script or another module accesses via [[Import Statement (Python)|import]].
- Supports object-oriented programming through [[Class (Python)|classes]], which act as factories for [[Instance (Python)|instances]] and support customization via inheritance.
- Signals errors and unusual conditions as [[Exception (Python)|exceptions]], caught and recovered from with a [[Try Statement (Python)|try statement]].

# Types
- [[Python String]]
- [[Python List]]
- [[Python Tuple]]
- [[Python Dictionary]]
- [[Python Set]]
- [[None (Python)|None]]

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=20&annotation=T7H2LAMX)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=22&annotation=WUTIKMK5)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=23&annotation=8A2SR8R8)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=22&annotation=65GGQHKL)
[^5]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=32&annotation=BUUCEZL5)
