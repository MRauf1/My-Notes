---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Loopback Address[^1]
> A special IP address reserved to refer to the sending machine itself; a packet sent to it never leaves the machine.

# Properties
- [[IPv4]]'s loopback address is `127.0.0.1`; [[IPv6]]'s is `::1` (`0:0:0:0:0:0:0:1`).
- Commonly called localhost.
- Implemented on Linux via the virtual `lo` network interface: outgoing data to localhost reaches the kernel's `lo` interface, which simply repackages it as incoming data and sends it back through `lo`.[^2]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=246&annotation=Q9NQNCWN)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=234&annotation=EYHB7WFX)
