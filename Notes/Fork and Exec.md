---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] fork() and exec()[^1]
> fork() and exec() are the system calls by which nearly every Linux user process is created: fork() duplicates an existing process, and exec() then replaces that copy with a new program.

# Properties
- Both are [[System Call|system calls]].
- Every user process other than [[Init Process|init]] starts as a result of fork().
- exec() is usually run afterward to start a new program, rather than continuing to run a copy of the existing process; it replaces the calling process's image outright, so any of its code after the exec call is never reached.[^2]
- Produces a new [[Process (Computing)|process]].
- fork() returns twice: 0 in the new child process, and the child's PID in the parent; a child recovers its parent's PID with `getppid()` instead, since under [[POSIX]] every process has exactly one parent, while a parent must track the PIDs of its (possibly many) children explicitly.[^3]
- Repeatedly forking without bound produces a [[Fork Bomb]].
- A parent that never waits on a terminated child leaves it as a [[Zombie Process]]; a parent that terminates before waiting on a child instead leaves it as an [[Orphan Process]]. See [[Wait (System Call)]].
- Commonly composed with [[Wait (System Call)|wait()]] into the [[Fork-Exec-Wait Pattern]].
- fork() does not immediately copy the parent's memory; it relies on [[Copy-on-Write]], so the child's address space initially shares the parent's physical pages until either process writes to one.[^4]
- If the forking process has multiple [[Thread|threads]], only the thread that called fork() survives into the child, which is left single-threaded.[^5]
- Creating threads before forking is discouraged: since fork() clones only the calling thread, a [[Mutual Exclusion|mutex]] left locked by a different thread (for example, one held internally by `malloc`) is never unlocked in the child. `pthread_atfork`, from the [[POSIX Threads (pthread)|pthread library]], exists to help coordinate around this hazard for advanced use cases.[^6]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=106&annotation=7VICTQN3)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=95&annotation=3YCHW3G5)
[^4]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=131&annotation=U7Q4DELF)
[^5]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=139&annotation=EGPJ95GQ)
[^6]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=140&annotation=YNE8ED9V)
