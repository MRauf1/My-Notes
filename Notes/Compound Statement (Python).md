---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Compound Statement (Python)[^1]
> A [[Statement (Python)|statement]] that has other statements nested inside it, following a general pattern of a header line terminated in a colon, followed by a nested block of code indented underneath the header.

# Properties
- Python determines where a nested block starts and stops from the statements' physical indentation alone, rather than from braces or keywords; the indentation style (spaces or tabs) and amount are unconstrained, except that every statement within one given nested block must be indented by the same distance, or a syntax error results[^2].
- Tabs and spaces should not be mixed within the same indented block; Python treats inconsistent use of the two as an error[^3].
- [[If Statement (Python)]], [[While Loop (Python)]], and [[For Loop (Python)]] are all compound statements built on this same header-and-indented-block pattern.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=393&annotation=DYFKAKSL)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=396&annotation=S2JYKHFF)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=399&annotation=CXVCV97H)
