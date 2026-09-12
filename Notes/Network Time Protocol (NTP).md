---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Network Time Protocol (NTP)[^1]
> The Network Time Protocol (NTP) is a protocol run by a daemon (`ntpd`) to maintain a machine's [[System Clock|system clock]] using a remote time server over the Internet.

# Properties
- Requires the machine to be permanently connected to the Internet.[^1]
- Many distributions bundle NTP daemon support, but it may not be enabled by default and can require installing an `ntpd` package.[^1]
- The preferred way to correct [[Time Drift]], since it updates the clock smoothly rather than by abrupt correction.[^2]
- Can also be used to set the [[Real-Time Clock (RTC)|hardware clock]] so that time coherency survives a reboot.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=183&annotation=DFKXMINB)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=183&annotation=VZS6222V)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=184&annotation=DDF59VKX)
