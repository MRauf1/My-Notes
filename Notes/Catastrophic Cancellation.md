---
tags:
  - computer_science
  - numerical_analysis
---

# Definition

> [!info] Definition 1 (Catastrophic Cancellation)[^1]
> Subtraction between two $p$-digit floating-point numbers of the same sign and similar magnitude (differing by no more than a factor of two) is always exactly representable, because the leading digits of the two numbers cancel — yet the result has fewer than $p$ significant digits.

Despite the exactness of the result, cancellation often causes a serious loss of information, because the operands are typically already uncertain due to [[Rounding Error]] or other prior errors. The digits lost to cancellation are the most significant, leading digits, whereas the digits lost to rounding are the least significant, trailing digits. Consequently, computing a small quantity as the difference of two large, uncertain quantities is generally a bad idea, since rounding error is likely to dominate the result.

# Properties
- Cancellation is not unique to computer arithmetic; it arises in any setting with limited precision, such as empirical measurements or laboratory experiments.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=45)
