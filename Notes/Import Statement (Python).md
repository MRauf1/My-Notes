---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Import Statement (Python)[^1]
> Unlike a textual include, `import` is a runtime operation: the first time a program imports a given [[Module (Python)|module]], Python (1) finds the module's file, (2) compiles it to [[Python Bytecode|bytecode]] if needed, and (3) runs its code to build the objects it defines.

# Properties
- These three steps run only once per file, per process: Python records every loaded module in the `sys.modules` dictionary and checks it first, so later imports of the same module simply fetch the already-built module object instead of repeating the search, compile, and run steps[^2].
- `import` is a true executable [[Statement (Python)|statement]], not a compile-time declaration, so it can be nested inside `if` tests, function bodies, or `try` blocks, and the imported module is unavailable until Python actually reaches and runs the statement[^3].
- Also an implicit [[Assignment Statement (Python)|assignment]]: `import` binds the whole module object to a single name in the importer's scope[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=866&annotation=BKLIIBGI)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=866&annotation=D2USF58A)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=888&annotation=PXH2ZI3T)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=889&annotation=E8P3PZ2H)
