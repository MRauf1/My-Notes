---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Startup File[^1]
> A startup file is a [[Dot File|dot file]], accumulated in a user's home directory, that a program consults to configure itself when it starts; most are created automatically the first time the corresponding program runs and never need to be changed.

# Properties
- Should be kept simple when written for other users: keeping the number of startup files small, and each file as small and simple as possible, keeps them easy to modify but hard to break, since every item in a startup file is one more thing that can break.[^2]
- Should be kept readable when written for other users: extensive comments let users understand what each part of a file does.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=312&annotation=9BMIGZEU)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=313&annotation=LTD9A5AC)
