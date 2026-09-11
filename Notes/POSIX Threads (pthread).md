---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] POSIX Threads (pthread)[^1]
> The POSIX-standard library for creating and managing threads within a process. A program's first [[Thread]] comes for free, running the code inside `main`; `pthread_create` spawns additional threads, given a pointer to the function where each new thread should begin executing.

# Properties
- Implements thread creation using the [[Clone (System Call)|clone system call]]: it allocates stack space for the new thread and uses `clone` to start it executing there.
- Provides `pthread_atfork` as a hook for coordinating threads around a [[Fork and Exec|fork()]] call, though creating threads before forking is generally best avoided unless the limitations of doing so are fully understood.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=132&annotation=M5BG8GYT)
