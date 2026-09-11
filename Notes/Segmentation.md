---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Segmentation[^1]
> A variable-size address mapping scheme in which an address consists of a segment number, mapped to a physical address, and a segment offset within that segment.

# Properties
- An alternative to purely fixed-size paged [[Virtual Memory|virtual memory]]: segments can vary in size to match the natural units of a program (code, stack, heap), unlike uniform pages.
- Pitfall: extending an existing, unsegmented address space by adding segments on top of it tends to produce an awkward, hybrid design rather than the benefits of a clean segmented architecture.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=454&annotation=XDG6LFA6)
