---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Authentication (Computer Security)[^1]
> Authentication is the part of user security that asks users to prove that they are who they claim to be, following [[Identification (Computer Security)|identification]].

# Properties
- Practically everything related to authentication happens in [[User Space|user space]]; the kernel itself knows nothing about usernames, passwords, or how to verify them.[^2]
- Traditionally implemented by encrypting whatever a user typed and comparing it against the encrypted password stored for that user, historically directly in [[Passwd File|/etc/passwd]] and today in the [[Shadow File|shadow file]].[^3]
- This traditional approach set no system-wide encryption standard, assumed the verifying program had access to the encrypted password, assumed a user should be re-prompted for a password every time authentication was needed, and assumed passwords — rather than tokens, smart cards, or biometrics — were the desired authentication method; these limitations were addressed by [[Pluggable Authentication Modules (PAM)|PAM]].[^4]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=189&annotation=SDG29UHL)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=189&annotation=64BC6D7P)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=190&annotation=23EBB737)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=190&annotation=BPZZ6F3Z)
