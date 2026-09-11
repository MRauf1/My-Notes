---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Thread Safety[^1]
> A function or piece of code is thread-safe if it can be called concurrently by multiple threads without producing a [[Race Condition]] or incorrect results.

# Properties
- Some common library functions are not thread-safe — for example `asctime`, `getenv`, `strtok`, and `strerror` — typically because they rely on shared or static internal state across calls.
- A program can be exposed to race conditions through calls into non-thread-safe code it did not write itself, not only through bugs in its own code.
- Equivalent to [[Atomic Operation|atomicity]]: an operation is thread-safe exactly when it is atomic.[^2]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=139&annotation=3IN4TLJL)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=156&annotation=WX4LPRFS)
