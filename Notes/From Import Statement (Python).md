---
tags:
  - computer_science
  - python
---

# Definition
> [!info] From Import Statement (Python)[^1]
> `from module import name` copies specific names out of a [[Module (Python)|module]] directly into the importing scope, so they can be used without going through the module's own name — unlike plain [[Import Statement (Python)|import]], which binds only the module object itself.

# Properties
- Still runs a full ordinary import first, loading the entire file into memory regardless of how many names are copied out; only afterward does it copy the requested names — references to the same objects, not the objects themselves — into the importer's scope[^2].
- `from module import *` copies every top-level name from the module at once; it is restricted to a module file's top level (a syntax error inside a function) and, by convention, should be used sparingly, since it can silently overwrite existing names in the importer's scope and makes it hard to trace where a given name came from[^3].
- Accepted convention generally favors plain `import` for clarity, since `module.name` is easier to trace back to its source than a bare `name` copied out by `from`[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=885&annotation=SPXBA63D)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=890&annotation=5HURD3LD)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=891&annotation=IUTD29SJ)
