---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Process (Computing)[^1]
> A process (or user process) is a running program managed by the kernel, regardless of whether a user directly interacts with it. All processes running on a system collectively make up user space.

# Properties
- Runs in [[User Mode]] and occupies [[User Space]].
- Is, in essence, a [[State (Computing)|state]] (or image) residing in memory.
- Created via [[Fork and Exec|fork() and exec()]].
- Has a user owner and is said to run as that owner (see [[User (Unix)]]).
- Managed by [[Process Management]], including [[Context Switch|context switching]] between processes sharing a CPU.
- Identified by a numeric process ID (PID), and also carries the PID of its parent process (PPID); under [[POSIX]] every process has exactly one parent.
- Isolated by default: no process can communicate with another process without an explicit mechanism for doing so; see [[Inter-Process Communication]] for how this isolation can be deliberately broken.[^3]
- Reads and writes data through its [[Standard Streams (Unix)|standard streams]].
- Includes one or more [[Thread|threads]], its address space, and its operating-system state; a process switch therefore usually invokes the operating system, unlike a plain thread switch within the same process.[^2]
- A set of processes contending for resources can enter [[Deadlock]] or [[Livelock]] rather than making forward progress.[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=539&annotation=NM2XKJA2)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=91&annotation=ZWYDK74I)
[^4]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=195&annotation=DB7TZ4UD)
