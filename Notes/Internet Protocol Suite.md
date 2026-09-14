---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Internet Protocol Suite[^1]
> The Internet protocol suite (network stack) is the four-layer model — application, transport, network/Internet, and physical — that networked data actually travels through on the Internet, as opposed to the seven-layer [[OSI Model]] used mainly for teaching and design.

# Types
- [[Application Layer]] — contains the "language" applications and servers use to communicate, usually a high-level protocol such as HTTP, SSL, or FTP.[^2]
- Transport layer — defines the data transmission characteristics of the application layer, including data integrity checking, source/destination ports, and breaking application data into packets; implemented chiefly by [[Transmission Control Protocol (TCP)|TCP]] and [[User Datagram Protocol (UDP)|UDP]].[^3]
- Network (Internet) layer — defines how to move [[Packet|packets]] from a source host to a destination host; implemented for the Internet by [[Internet Protocol|IP]].[^4]
- Physical layer — defines how to send raw data across a physical medium, such as Ethernet or a modem; also called the link layer.[^5]

# Properties
- Data must travel down through these layers on the sender, across the physical medium, and back up through them on the receiver before reaching a program at its destination — at least twice per exchange.[^6]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=216&annotation=UXIKHCUD)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=216&annotation=RJFE7Y28)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=216&annotation=MEV3EPAY)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=216&annotation=2XHPZS27)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=216&annotation=JK3YRBNG)
[^6]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=216&annotation=MD9R7XBD)
