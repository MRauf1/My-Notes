---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Variable (Python)[^1]
> A named entry in a system table that holds a reference (an object's address in memory) to an [[Object (Python)|object]]; variables are created when first assigned and must be assigned before they can be referenced.

# Properties
- Variables always link to objects and never to other variables, though a larger object (e.g., a list) may itself link to other objects it contains[^2].
- Types live with objects, not with variables: a variable is only ever a reference to a particular object at a particular time, so reassigning it to a new type of object does not "change its type" — it simply points the reference elsewhere[^3].
- Conceptually, each expression's result is a new, distinct object; as an optimization, CPython caches and reuses certain unchangeable objects, such as small integers and short strings, rather than always allocating fresh memory for them — see [[Object Identity (Python)]] and [[Garbage Collection (Python)]].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=194&annotation=KZZWPYMP)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=193&annotation=ARP2NUYV)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=195&annotation=9IKFPHWM)
