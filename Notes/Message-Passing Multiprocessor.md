---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Message-Passing Multiprocessor[^1]
> A [[Multiprocessor]] organization built from nodes with private, separate memories rather than a single shared address space; processors communicate by explicitly sending and receiving messages, via send-message and receive-message routines, instead of reading and writing shared variables.

# Properties
- Contrasted with a [[Shared Memory Multiprocessor]], which instead communicates implicitly through a shared address space over a fast memory interconnect.
- A [[Cluster (Computing)|cluster]] is the most common form of message-passing parallel computer today.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=554&annotation=7YBV785H)
