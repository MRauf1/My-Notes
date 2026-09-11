---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Cache Coherence[^1]
> The problem that arises when multiple processors each maintain their own private [[Cache Memory|cache]] of shared data: without coordination, two processors' caches can end up holding different values for what is supposed to be the same memory location.

# Properties
- Splits into two aspects: coherence, which defines what values a read may legitimately return, and consistency, which defines when a write becomes visible to reads by other processors.
- A coherent [[Multicore Microprocessor|multiprocessor's]] caches provide both migration (a block moves to whichever processor is using it) and replication (multiple processors hold read-only copies) of shared data.
- The most common coherence protocol is snooping: every cache tracks the sharing status of the blocks it holds, with no centralized directory, and every cache controller monitors ("snoops on") a shared broadcast medium (bus or network) to see whether a block it holds has been requested elsewhere.
- False sharing occurs when two unrelated variables happen to fall in the same cache block, causing that block to be exchanged between processors even though each processor is really only accessing its own, independent variable — an unnecessary coherence cost caused purely by data layout, related to but distinct from a genuine [[Data Race]].
- Pitfall: giving a cache shared by multiple cores or threads less set associativity than the number of cores or threads sharing it invites additional conflict misses purely from that contention; see [[Set-Associative Cache]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=489&annotation=ZZJHF3YB)
