---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] wait / waitpid[^1]
> System calls that let a parent process wait for one of its child processes to change state (for example, by exiting), so the parent can be notified when an asynchronous child finishes.

# Properties
- `waitpid` waits for a specific child and can be set to be non-blocking, returning immediately with whether that child has exited.[^2]
- `wait` is a simpler form that accepts a pointer to an integer and waits on any child process, returning as soon as the first one changes state.[^3]
- Necessary to reclaim a terminated child before it lingers as a [[Zombie Process|zombie]].
- The [[Init Process]] automatically waits on all of its (possibly [[Orphan Process|orphaned]]) children.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=102&annotation=L2UJA5YL)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=102&annotation=YIV6HNJW)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=103&annotation=PM8NCC6D)
