---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] User Datagram Protocol (UDP)[^1]
> A connectionless transport-layer protocol built on top of [[IPv4]] and [[IPv6]]; a sender simply specifies a destination address and port and sends a data packet.

# Properties
- Provides no delivery guarantee: packets may be dropped under network congestion, duplicated, or arrive out of order.
- Simpler to use than [[Transmission Control Protocol (TCP)|TCP]], at the cost of TCP's delivery guarantees and its abstraction over the packet-based network.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=262&annotation=Z7DWDMI9)
