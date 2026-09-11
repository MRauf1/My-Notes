---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Fused Multiply-Add (FMA)[^1]
> A floating-point instruction that computes $a + (b \times c)$ on three registers but rounds only once, after the addition, instead of rounding once after the multiply and again after the add as two separate instructions would.

# Properties
- The single rounding step increases the precision of a multiply-accumulate compared with separate multiply and add instructions; see [[Rounding]].
- Part of the IEEE 754-2008 revision of the [[Floating-Point Number System|IEEE 754 standard]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=243&annotation=VXEX4XAU)
