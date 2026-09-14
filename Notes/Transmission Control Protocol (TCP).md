---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Transmission Control Protocol (TCP)[^1]
> A connection-based transport-layer protocol built on top of [[IPv4]] and [[IPv6]] (hence "TCP/IP"); it creates a pipe between two machines, abstracting away the network's underlying packet-based nature.

# Properties
- Used by most Internet services today, since it hides the complexity of the lower, packet-level nature of the Internet.[^1]
- Contrasts with [[User Datagram Protocol (UDP)|UDP]], the other major transport-layer protocol, which offers none of TCP's guarantees.[^2]
- Provides multiple applications on one machine with independent connections by means of [[Port (Networking)|ports]]; a connection is identified by the pair of IP addresses and port numbers at each end.[^3]
- Requires little from the application side beyond opening, reading from, writing to, and closing a connection, much like working with a file; behind the scenes it breaks an outgoing stream into packets, reconstructs an ordered input stream from arriving packets, and detects and corrects lost or mangled packets.[^4]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=251&annotation=7MLWU7WQ)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=251&annotation=YQJT3YEE)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=235&annotation=WWVN6DG2)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=237&annotation=6UYM934T)
