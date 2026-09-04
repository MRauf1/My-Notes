---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Normalized Floating-Point System)[^1]
> A [[Floating-Point Number System]] is normalized if the leading digit $d_0$ is always nonzero unless the number represented is zero. Thus, in a normalized system, the mantissa $m$ of a nonzero floating-point number always satisfies $1 \le m < \beta$.

# Properties
- The representation of each number is unique.
- No digits are wasted on leading zeros, maximizing precision.
- In a binary ($\beta = 2$) system, the leading bit is always $1$ and need not be stored, gaining one extra bit of precision for a given field width.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=39)
