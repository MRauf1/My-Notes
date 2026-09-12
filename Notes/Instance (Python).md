---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Instance (Python)[^1]
> The tangible [[Object (Python)|object]] created each time its [[Class (Python)|class]] is called: a namespace of its own, starting out empty but inheriting the attributes that live in the class — and any superclasses — it was generated from.

# Properties
- Represents a concrete item in a program's domain, recording per-object data that varies from instance to instance, in contrast to the shared behavior and data defined on its class[^2].
- Comparable to the per-call state retained by a [[Closure (Python)|closure]], but explicit as instance attributes rather than implicit scope references, and a natural part of the class model rather than a workaround[^3].
- Assigning to an attribute of [[Self (Python)|self]] inside a method creates or changes that attribute on the instance being processed, not on the class; an instance's attributes can equally be set from entirely outside the class, by assigning directly to the instance object[^1].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1010&annotation=LC4KDYFK)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=993&annotation=XDUVPNZS)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1008&annotation=UCC6V2MH)
