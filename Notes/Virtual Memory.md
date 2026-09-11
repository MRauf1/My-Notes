---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Virtual Memory[^1]
> Virtual memory is a memory access scheme in which a process accesses memory as if it had an entire machine to itself, rather than by the memory's actual physical location.

# Properties
- Enabled by the [[Memory Management Unit]] (MMU), CPU hardware that intercepts a process's memory accesses.
- The MMU translates a process's memory accesses into physical memory locations using a [[Page Table|memory address map]].
- The [[Kernel (Operating System)|kernel]] initializes and continuously maintains and alters this address map.
- A specific application of the [[Memory Hierarchy]]: it uses main memory as a "cache" for secondary storage, with a virtual memory block called a page and a virtual memory miss called a page fault (an event triggered when an accessed page is not present in main memory).[^2]
- The processor produces a virtual address, an address in the program's own address space, which address translation (address mapping) converts into a physical address — an address in main memory — via the page table; a [[Translation-Lookaside Buffer|TLB]] caches recently used translations to avoid the extra memory access this otherwise costs.
- Historically motivated by two goals: letting multiple programs safely and efficiently share main memory (each compiled into its own protected address space), and letting a single program's address space exceed the size of physical main memory; the former is the dominant motivation today, especially for sharing memory among virtual machines in cloud computing.
- Provides protection: a set of mechanisms ensuring that processes sharing the processor, memory, or I/O devices cannot interfere with each other's data, and that isolate the [[Operating System]] from user processes; the hardware needs at least the ability to run in two modes (user versus [[Kernel (Operating System)|supervisor/kernel mode]]), to make part of the processor state (such as the page table pointer) readable but not writable in user mode, and to provide mechanisms for switching between modes, typically via a [[System Call]].
- Also provides relocation: since every virtual memory system relocates a program as a set of fixed-size pages rather than a single contiguous block, the operating system need only find enough free pages, not one large contiguous span, letting a program load anywhere in main memory. Two virtual addresses can alias the same physical page to let programs share data or code.
- Segmentation is an alternative, variable-size address mapping scheme in which an address consists of a segment number, mapped to a physical address, and a segment offset; extending an existing unsegmented address space by adding segmentation on top of it is a common pitfall.
- A TLB miss can mean either that a valid translation is simply missing from the TLB (resolved by reloading it from the page table) or that the page itself is not in memory at all (a genuine page fault, handled via an [[Exception (Computer Architecture)|exception]] into the operating system).
- Extends real memory with disk storage by paging out to [[Swap Space]] when memory runs low.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=451&annotation=J2ASJQXW)
