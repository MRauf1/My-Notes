---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Saturating Arithmetic[^1]
> An overflow-handling convention, not generally found in general-purpose microprocessors, in which a calculation that overflows is clamped to the largest positive or most negative representable value, rather than wrapping around as in ordinary modulo [[Two's Complement]] arithmetic.

# Properties
- Preferred for media (audio/image/video) processing, where clamping to an extreme value is usually a better approximation of the intended result than the wraparound that ordinary [[Arithmetic Overflow]] handling would produce.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=204&annotation=9CI72RSP)
