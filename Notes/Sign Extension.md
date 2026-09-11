---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Sign Extension[^1]
> The process of converting an $n$-bit binary number to an equivalent representation with more than $n$ bits, by replicating the most significant bit (the sign bit) to fill the new, higher-order bits, while copying the old bits unchanged into the low-order portion of the wider word.

# Properties
- Works because a positive [[Two's Complement]] number has an implicit infinity of leading 0s and a negative one has an implicit infinity of leading 1s; the hardware simply hides these leading bits to fit its width, and sign extension restores some of them.
- Used when converting a signed load's data to fill a register: a signed load sign-extends, while an unsigned load fills the extra bits with 0s regardless of the sign.
- Contrasted with logical AND/OR immediate instructions, which insert 0s into the upper bits of a constant instead of sign-extending it.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=101&annotation=XDA856L2)
