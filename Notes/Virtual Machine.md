---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Virtual Machine (System VM)[^1]
> Software that presents the illusion that each of several users has an entire computer to themselves, including a copy of the [[Operating System]], while a single physical computer's hardware resources are actually shared among multiple guest virtual machines and their (possibly different) guest operating systems.

# Properties
- Managed by a virtual machine monitor (VMM), or hypervisor, which is the software heart of the technology: it presents a software interface to guest software, isolates the state of each guest from the others, and protects itself from guest software, including guest operating systems.
- The underlying hardware platform is the host; the VMM maps virtual resources to physical ones, which it may time-share, partition, or emulate in software; a VMM is typically much smaller than a conventional operating system.
- To remain in control, the VMM must run at a higher privilege level than any guest, which normally runs in user mode, so that the VMM handles the execution of every privileged instruction.
- A key motivation for [[Virtual Memory]] today is enabling multiple virtual machines to safely and efficiently share a single main memory, particularly in cloud computing.
- Pitfall: implementing a VMM on an instruction set architecture that was not designed to be virtualizable — for example, one whose privileged instructions do not reliably trap when executed in user mode — greatly complicates or degrades virtualization.
- Contrasts with a process virtual machine such as the [[Python Virtual Machine|Python Virtual Machine (PVM)]], which executes the instructions of a single program rather than virtualizing an entire computer and its operating system.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=447&annotation=Z8NG8PK7)
