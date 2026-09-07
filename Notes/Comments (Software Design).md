---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Comments (Software Design)[^1]
> Text alongside code that captures information from the designer's mind that cannot be expressed in the code itself, aiding abstraction and maintainability and reducing [[Cognitive Load (Software Design)|cognitive load]] and [[Unknown Unknowns]].

# Properties
- Should describe things that are not obvious from the code itself, and should never simply restate what the code already says.
- Interface comments, describing a module's or variable's declaration, should be written and kept separate from implementation comments.
- Implementation comments should explain what the code is doing and why it is implemented that way, not how it works line by line, since the code itself should convey the how.
- Cross-module design decisions can be centralized in one document, with each affected module referencing it rather than repeating it.
- Writing comments before writing the code turns documentation into part of the design process, which tends to improve both the documentation and the design.
- Keeping a comment as physically close as possible to the code it describes makes it more likely to be updated when the code changes; in languages with separate header and implementation files, comments generally belong wherever the developer using the code is more likely to look, though placement should ultimately favor whatever location is most convenient for readers.
- A long comment can be broken into smaller pieces placed near the specific code each piece describes, summarized by a short comment at the top of the module.
- Each design decision should be documented exactly once; when the same information would otherwise be duplicated, a master comment or an external document should be referenced from every other location instead of being repeated.
- Comments that are more abstract and higher-level than the code they describe are easier to keep accurate as the code evolves.
- Consistency in commenting and other conventions is best maintained by writing them down in a shared document and enforcing them with tooling or code review.
- Software should be designed for ease of reading, not ease of writing.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)
