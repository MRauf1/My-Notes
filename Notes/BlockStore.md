---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] BlockStore[^1]
> An abstraction encapsulating an external storage device in the [[External Memory Model]]: a collection of memory blocks, each of size $B$, uniquely identified by an integer index.

# Operations
- **`read_block(i)`**: return the contents of the block at index $i$.
- **`write_block(i, b)`**: write the contents of $b$ to the block at index $i$.
- **`place_block(b)`**: store the contents of $b$ at a newly allocated index, and return that index.
- **`free_block(i)`**: mark the block at index $i$ as no longer used, so its space may be reused.[^1]

# Implementation
The simplest realization stores one file on disk, partitioned into fixed-size blocks of $B$ bytes, so that `read_block(i)`/`write_block(i, b)` simply read or write bytes $iB, \dots, (i+1)B - 1$ of that file. A free list tracks blocks released by `free_block(i)`; `place_block(b)` reuses a block from this list if one is available, or appends a new block to the end of the file otherwise.[^2]

# Properties
- [[External Memory Model]]
- Used by [[B-Tree]] to store its nodes, each sized to fit exactly one block.

[^1]: [Morin, p. 277](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 277](zotero://select/library/items/HYS8NDAB)
