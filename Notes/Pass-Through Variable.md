---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Pass-Through Variable[^1]
> A variable that is passed as an argument through a long chain of methods that do not use it themselves, purely so that a method further down the chain can access it.

# Properties
- Increases complexity and creates [[Dependency (Software Design)|dependency]] between all the modules in the chain, analogous to how [[Pass-Through Method|pass-through methods]] create dependency between classes.
- One common, if imperfect, solution is to bundle all pass-through variables, along with the application's global state, into a single context object that every object holds a reference to; such a context object should ideally be immutable.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
