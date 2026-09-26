---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Pipeline (Unix)[^1]
> A pipeline connects several small commands together so that data can flow directly from one command's [[Standard Streams (Unix)|standard output]] to the next command's standard input, without an intermediate file.

# Properties
- The [[Tee (Command)|tee command]] can copy part of a pipeline's flow to a file while still passing it on to the next command.[^1]

[^1]: [Linux Journey: Text-Fu](https://labex.io/linuxjourney/courses/text-fu)
