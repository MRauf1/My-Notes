---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Standard Streams (Unix)[^1]
> Standard streams are the I/O streams that the [[Kernel (Operating System)|kernel]] provides to every [[Process (Computing)|process]] for reading and writing data: standard input (stdin), standard output (stdout), and standard error (stderr).

# Properties
- Standard input (stdin) is the stream a process reads its input data from.
- Standard output (stdout) is the stream a process writes its ordinary output to.
- Standard error (stderr) is an additional output stream reserved for diagnostics and debugging, separate from stdout, so redirecting stdout does not suppress it.
- The standard output of one program can be sent directly to another program's standard input.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=38&annotation=T3K7IISG)
