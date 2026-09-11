---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Atomic Operation[^1]
> A hardware primitive that atomically reads and modifies a memory location, so that nothing can interpose itself between the read and the write. Two simultaneous atomic operations on the same location are ordered by the hardware, making the operation indivisible.

# Types
- Atomic exchange (atomic swap) — interchanges a value in a register for a value in memory in a single indivisible step.
- Load linked / store conditional — a pair of instructions used in sequence: the store conditional stores a register's value to the address given by a preceding load linked, and reports success (1) or failure (0), failing if the memory location changed since the load linked (or, on a single processor, if a context switch occurred between the two instructions).
- Atomic compare-and-swap and atomic fetch-and-increment — additional synchronization primitives that can be built from load linked / store conditional, used in some parallel programming models.

# Properties
- The essential building block for implementing [[Mutual Exclusion]] and avoiding [[Data Race|data races]] in a multiprocessor.
- Only register-register instructions should appear between a load linked and its store conditional, and as few instructions as possible, to avoid deadlock and to minimize the chance that an unrelated event or a competing processor causes the store conditional to fail.
- Equivalently, an instruction is atomic if no other processor or [[Thread]] is allowed to perform any intermediate step of it while it is in progress; on x86 this is realized by prefixing the instruction with the lock prefix.[^2]
- Not applied to every instruction, since enforcing atomicity makes an instruction slower; it is reserved for the specific operations that need to be indivisible.[^2]
- Equivalent to [[Thread Safety]]: an operation is atomic exactly when it is thread-safe.[^3]
- Generalizes to higher-order data-structure operations: such an operation is atomic if it happens all at once, either succeeding entirely or not at all.[^4]
- Some atomic instructions come in a strong and a weak variant: the strong variant reliably reports success or failure, while the weak variant may spuriously report failure even though the operation actually succeeded (see [[Spurious Wakeup]] for an analogous phenomenon).[^5]

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=144&annotation=3GYGV6P7)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=21&annotation=ND5EX3Z6)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=156&annotation=WX4LPRFS)
[^4]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=157&annotation=KXLJMH4X)
[^5]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=152&annotation=35E6PGPJ)
