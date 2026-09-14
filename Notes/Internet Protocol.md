---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Internet Protocol (IP)[^1]
> The protocol that describes how to send packets of information across a network from one machine to another.

# Types
- [[IPv4]]
- [[IPv6]]

# Properties
- Implements the network layer of the [[OSI Model]], equivalently the Internet layer of the [[Internet Protocol Suite]].
- Transport-layer protocols such as [[Transmission Control Protocol (TCP)|TCP]] and [[User Datagram Protocol (UDP)|UDP]] are built on top of it, hence names like "TCP/IP."
- Meant to be a software network placing no particular requirement on hardware or operating systems: Internet packets can be sent and received over any kind of hardware, using any operating system.[^2]
- Moves [[Packet|packets]] between hosts identified by an [[IP Address]], organized into [[Subnet|subnets]] and reachable beyond the local subnet through a [[Router|router]].

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=246&annotation=HYQU5WMM)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=217&annotation=ZMNQQL4F)
