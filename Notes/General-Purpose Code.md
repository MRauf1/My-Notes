---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] General-Purpose Code[^1]
> Code, or any design decision, whose interface is broad enough to be reused for other applications, in contrast to special-purpose code that solves only the immediate task at hand.

# Properties
- Tends to produce simpler and [[Deep Module|deeper]] modules and less code overall than an equivalent special-purpose design, even when the code will only ever be used in one place.
- Improves [[Information Hiding]], since a general interface naturally hides the specifics of any one use case.
- To design something general-purpose: build the simplest interface that still covers all current needs, treat single-use-only design as a warning sign, and keep the API easy to use so it does not raise [[Cognitive Load (Software Design)|cognitive load]].
- Because specialized code is unavoidable somewhere in a system, it should be pushed either up or down the software stack, away from the general-purpose core: pushing it upward keeps low-level classes general-purpose while high-level code specializes their use; pushing it downward, as with device drivers beneath a general-purpose operating system, makes the general-purpose modules define an interface that specialized modules must implement.
- Special cases and long conditional chains should be minimized by designing the normal-case logic to handle edge cases automatically, without extra special-case code.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
