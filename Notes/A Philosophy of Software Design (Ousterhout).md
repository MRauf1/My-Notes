---
tags: literature_review
---

# Review[^1]

Agile development - initial design focuses on a subset of features, those are implemented, evaluated, and then the developers can start working on the next feature. Rinse and repeat. This approach means that software design is a continuous and never ending process.

The author defines complexity as anything related to the structure of a software system that makes it hard to understand and modify the system. It is determined by the complexity of each part weighted by the fraction of time developers spend working on it. Thus, isolating a complexity where it will never be seen is as good as eliminating the complexity of that part altogether.

3 manifestations of complexity:
1) Change amplification
	1) Seemingly simple change requires code modifications in many places. Good design reduces the amount of code that is affected by each design decisions, so good design doesn't require many code modifications.
2) Cognitive load
	1) How much a developer needs to know (and keep track) to complete a task. Higher cognitive load is more prone to bugs from developers.
	2) In regards to manifestation #1, sometimes more lines of code is simpler because it reduces cognitive load.
3) Unknown unknowns
	1) It's not obvious which pieces of code must be modified or what information a developer must use to complete a task.
	2) This is the worst as you don't even know what must be done, while the first two manifestations are more tedious.

Good design is for a system to be obvious and clear.

2 causes of Complexity
1) Dependencies
	1) When a given piece of code cannot be understood and modified in isolation. This code relates to some other code, and the other code must be understood or modified to change the first code.
	2) Can't be completely eliminated.
	3) Goal is to reduce the number of dependencies and to make them as simple and obvious as possible.
	4) Leads to manifestations 1 and 2.
2) Obscurity
	1) When important information is not obvious.
	2) Can be combined with dependency if it's not obvious that a dependency exists.
	3) Inconsistency can also result in obscurity.
	4) Most of the time, is a result of poor documentation, but it also results from complex and non-obvious the design is. Too much documentation is a red flag, and best way to reduce obscurity is by simplifying system design.
	5) Leads to manifestation 3.

Complexity is incremental; it doesn't come from a single mistake. Thus, to slow down the growth of complexity, you must adopt a "zero tolerance" philosophy where when you are presented with a decision to add even a bit of complexity, you choose not to.

You should value good design and ease of modication/future extension over the speed of code writing. In the short term, the latter will win, but in the long term, the patient one who thinks about the design and doesn't take shortcuts that increase complexity will win.

Even with this, you'll inevitably make mistakes in design. When you notice them, don't code/patch around them. Fix them first.

Since good design emerges in bits and pieces incrementally, rather than spending a bunch of time upfront, dedicate 10-20% of your development time to good design, be it thinking about it or implementing it or improving/fixing old design.

The best modules are the ones that provide powerful functionality (through implementation) while maintaining a simple interface.

Thus, make sure that the interface is enough for any coder to fully understand all of the module's functionality that they might need to use. Don't make it too complex, but don't obscure important details either. Function/Class/Module signature and comments should tell the coder everything they need to know about the module.

The author argues against shallow/short modules like functions in favor of deep modules that have a simple interface. Especially for classes, avoid creating a million short and small classes as that increases the complexity of the program.

Interfaces should be designed to make the common case as simple as possible. If an interface has many features, but most developers only need to be aware of a few of them, the effective complexity of that interface is just the complexity of the commonly used features.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)