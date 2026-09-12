---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Operator Overloading (Python)[^1]
> Letting a [[Class (Python)|class]] intercept and implement the built-in operations normally reserved for built-in types — addition, slicing, printing, and so on — by providing specially named, double-underscore methods that Python automatically invokes when its instances appear in the corresponding operation; the method's return value becomes the result of that operation.

# Properties
- Every such method name and the operation it maps to is predefined and fixed by the language; a class may implement any number of them, but none are required, and most have no inherited default — if a class defines or inherits no `__add__`, for instance, a `+` expression on its instances simply raises an exception[^2].
- An implicit [[Object (Python)|object]] root superclass provides default implementations for a few of these methods, such as basic printing, but not for most, including arithmetic ones[^1].
- An instance can be made directly callable, like a function, by defining `__call__`, which Python invokes for a function-call expression applied to that instance, forwarding whatever arguments were passed[^3].
- Best reserved for classes that genuinely need to mimic a built-in type's interface; ordinary, explicitly named methods are usually clearer for behavior that doesn't need to act like a built-in operator[^1].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1019&annotation=E5I5ADYB)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1126&annotation=TXCYZ6D8)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=1168&annotation=HTWKQDVE)
