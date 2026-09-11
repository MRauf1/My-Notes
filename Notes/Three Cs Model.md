---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Three Cs Model[^1]
> A model that classifies every [[Cache Memory|cache]] miss into one of three categories.

# Types
- Compulsory miss (cold-start miss) — caused by the first-ever access to a block, which cannot already be in the cache regardless of cache design.
- Capacity miss — occurs because the cache, even with full associativity, is too small to hold all the blocks needed by the program at once.
- Conflict miss (collision miss) — occurs in a [[Direct-Mapped Cache|direct-mapped]] or [[Set-Associative Cache|set-associative]] cache when multiple blocks compete for the same set; a fully associative cache of the same size would eliminate it.

# Properties
- Used together with [[Average Memory Access Time]] to reason about why a cache design has a given miss rate and which design change would address it.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=482&annotation=LNEKKJVQ)
