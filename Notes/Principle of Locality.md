---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Principle of Locality[^1]
> Programs access a relatively small portion of their address space at any instant of time.

# Types
- Temporal locality — if a data location is referenced, it will tend to be referenced again soon.
- Spatial locality — if a data location is referenced, locations with nearby addresses will tend to be referenced soon.

# Properties
- The foundational assumption behind the [[Memory Hierarchy]]: temporal locality justifies keeping recently accessed items closer to the processor, while spatial locality justifies moving whole blocks of contiguous words, rather than single words, up the hierarchy.
- Also underlies [[Virtual Memory]] (both for page access patterns and for reuse of [[Page Table]] translations) and motivates software techniques like [[Cache Blocking]] that reorganize computation to increase locality directly.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=397&annotation=8CRUIZ25)
