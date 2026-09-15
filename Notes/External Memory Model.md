---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] External Memory Model[^1]
> A computational model for datasets too large to fit in RAM: the computer has access to a large external memory, divided into blocks of $B$ words each, plus a small internal memory used for computation. Transferring one block between internal and external memory takes constant time; any computation performed within internal memory is free.

This departs from the word-RAM model used elsewhere in this vault (where every machine-word instruction counts as a unit-cost step), whose implicit assumption — that the entire data structure fits in randomly-accessible memory — breaks down for collections too large for any computer's RAM, forcing data onto slower external storage (a hard disk, solid-state disk, or network file server).[^2] Accessing external storage is extremely slow, but hardware always transfers a whole block at once — e.g. a $4{,}096$-byte block for a typical disk — so a data structure organized to make full use of every block it reads or writes can turn one slow external access into thousands of bytes of useful work, rather than just one.[^3] Treating internal computation as free is a deliberate simplification that emphasizes exactly this asymmetry: it is the *number of block transfers*, not the number of instructions, that dominates real running time.

For the structures in this model (see [[B-Tree]]), an internal memory of size $O(B + \log_B n)$ suffices: enough to hold a constant number of blocks plus a recursion stack of height $O(\log_B n)$, with the $O(B)$ term usually dominating.[^4]

# Properties
- [[BlockStore]]
- [[B-Tree]]
- The real-world analogue of this model's block-based transfer is a [[Cache Memory|CPU cache]] or a [[Page Cache|page cache]], both of which move fixed-size blocks between a fast and a slow memory tier to exploit locality.

[^1]: [Morin, p. 276](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 275](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 275](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 276](zotero://select/library/items/HYS8NDAB)
