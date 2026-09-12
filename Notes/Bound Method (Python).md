---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Bound Method (Python)[^1]
> Accessing a [[Method (Python)|method]] attribute of a class through an instance returns a bound method object, which automatically pairs that instance with the function; calling the bound method later automatically supplies the paired instance as the function's [[Self (Python)|self]] argument. Accessing the same attribute through the class itself instead returns a plain function, which requires an explicit instance argument to be passed in.

# Properties
- Both forms are full [[First-Class Function (Python)|first-class objects]] and can be assigned, passed around, and stored just like any other value[^1].
- Calling a [[Superclass and Subclass (Python)|superclass's]] version of a method from within a subclass typically goes through the plain-function form — reached via the superclass's name — passing `self` along explicitly, since qualifying a class name rather than an instance does not produce a bound method[^2].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1200&annotation=5VU7FYII)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1057&annotation=Z6EWXHX9)
