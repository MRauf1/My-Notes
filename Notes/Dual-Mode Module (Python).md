---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Dual-Mode Module (Python)[^1]
> Every [[Module (Python)|module]] has a built-in `__name__` attribute: Python sets it to the string `'__main__'` when the file is run directly as the top-level script, and to the module's own name when the file is instead imported — so a file can test its own `__name__` to tell which case applies and behave differently in each.

# Properties
- The idiom `if __name__ == '__main__': ...` lets a single file define reusable tools and also run its own self-test or demo code only when launched directly, never when imported by another file; it is the simplest and most common self-testing convention in Python[^2].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=952&annotation=IVKVDTS4)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=953&annotation=4K9WB9IJ)
