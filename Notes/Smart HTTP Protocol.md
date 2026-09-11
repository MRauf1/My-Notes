---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Smart HTTP Protocol[^1]
> Smart HTTP is a [[Git Transfer Protocol]] that negotiates data transfer intelligently, similarly to the [[SSH Protocol (Git)|SSH]] and [[Git Protocol (Daemon)|Git protocols]], but runs over standard HTTP(S) ports and can use ordinary HTTP authentication mechanisms instead of requiring SSH keys.

# Properties
- A single URL can serve both anonymous, read-only access and authenticated read/write access to the same repository; the server prompts for credentials only when authentication is actually required.
- Because it can run over HTTPS, transferred data can be encrypted, and access can optionally be restricted to clients presenting a specific signed certificate.
- Since HTTP(S) ports are almost universally allowed through corporate firewalls, this protocol tends to face fewer network-access obstacles than protocols that use less common ports.
- A simpler, predecessor Dumb HTTP mode also exists, in which a [[Bare Repository]] is served as ordinary static files by a web server; a client falls back to this mode only when the server does not support the smart protocol.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=113&annotation=VY8C3VBU)
