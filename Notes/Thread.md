---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Thread[^1]
> A lightweight unit of execution consisting of a program counter, register state, and a stack. Threads commonly share a single address space, unlike [[Process (Computing)|processes]], which generally do not.

# Properties
- A [[Process (Computing)|process]] contains one or more threads plus its own address space and operating-system state; switching between threads of the same process is cheaper than a full process switch, since it need not invoke the operating system.
- Exploited by [[Hardware Multithreading]] to keep a processor's execution units busy across stalls, and organized into SIMD threads on a [[Graphics Processing Unit|GPU]], where a single thread carries exclusively SIMD instructions.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=539&annotation=DFPPV23G)
