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
- Every user process other than init starts as a result of fork().
- exec() is usually run afterward to start a new program, rather than continuing to run a copy of the existing process.
- Produces a new [[Process (Computing)|process]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
