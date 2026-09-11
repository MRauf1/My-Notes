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
- Created via the [[Clone (System Call)|clone system call]], which resembles [[Fork and Exec|fork()]] but performs no [[Copy-on-Write|copying]], letting the new thread share its process's address space, variables, heap, and file descriptors rather than receive its own copy.[^2]
- A program's first thread comes for free, running the code inside `main`; additional threads are created with `pthread_create` from the [[POSIX Threads (pthread)|pthread library]].[^2]
- Since threads of the same process share one virtual memory, they all see the same heap, global variables, and program code.[^3]
- Multiple threads of one process can run simultaneously on multiple CPUs; the operating system assigns threads to CPUs, time-slicing a CPU across threads whenever there are more active threads than CPUs.[^4]
- Concurrent threads can produce a [[Race Condition]] whenever the program's outcome depends on how the kernel happens to schedule them.[^5]
- If a process with multiple threads calls [[Fork and Exec|fork()]], the resulting child process has only a single thread: a clone of the thread that called fork().[^6]

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=539&annotation=DFPPV23G)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=131&annotation=U7Q4DELF)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=132&annotation=P5QEVEXY)
[^4]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=133&annotation=KZ3Y2MQV)
[^5]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=136&annotation=VF4D4KGS)
[^6]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=139&annotation=EGPJ95GQ)
