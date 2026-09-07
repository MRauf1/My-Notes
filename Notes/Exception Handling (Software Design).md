---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Exception Handling (Software Design)[^1]
> The handling of any uncommon condition that alters a program's normal flow of control. Exceptions and their handling code contribute significantly to [[Software Complexity]], since they make interfaces more complex and modules shallower; see [[Deep Module]].

# Properties
- Best reduced by minimizing the number of places where exceptions must be handled, rather than writing exception-handling code at every call site.
- Four ways to deal with an exceptional condition:
	1) Define the error out of existence, so the condition no longer needs to be treated as exceptional.
	2) Mask the exception at a low level of the system so that higher levels never see it, which deepens the module that performs the masking.
	3) Aggregate multiple exceptions so they are handled by a single piece of code in one place.
	4) Let the exception crash the application, when recovery is not worthwhile.
- Should not be eliminated entirely; some exceptions genuinely need to propagate and be handled explicitly.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
