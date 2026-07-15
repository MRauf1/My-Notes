---
tags: [literature_review]
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

1) Information Hiding - design decisions are hidden within the implementation, but are not seen within the interface. Try to hide as much of the information as possible to make the interface as simple as possible, while making the module as deep as possible. Can often be improved by making the class a little larger. It makes sense only when the information is not needed outside the module. This should not be done if the information is needed outside the module.
2) Information Leakage - when a design decision is reflected in multiple modules, which creates a dependency between the modules. Any change to this design decision would require changes to all involved modules. Information is also leaked when it is reflected in the interface. Can be reduced by making each module as independent as possible.

Defaults should be as simple as possible and do the right thing without the user asking for it. Overexposure increases the cognitive load for the developer oftentimes for features that are rarely used.

Usually, general-purpose code tends to be less complex than specialized code. Not just code, but any design decision. The more general, the less complex. Not just for the long run, but even when starting, even when the piece of code would be used only once at a single place, making things general-purpose tends to result in simpler and deeper modules and less code. The interface should be general enough to be able to be used for other applications, but the implementation itself should be at least specific enough to solve the task at hand. General-purpose code also results in better information hiding.

To make things general purpose:
1) Make the simplest interface that still covers all your needs
2) If a module is designed for a single use, that may be a sign that it is too special-purpose
3) Make the API easy and simple to use (lessen the cognitive load on the developer)

While specialized code is inevitable, it should be separated from the general-purpose code by moving it either up or down the software stack.
1) Pushing upwards means that the low-level classes are general-purpose, and the way they are used by high-level classes is specialized.
2) Pushing downwards is the reverse, similar to how device drivers are specialized and are low-level compared to the general-purpose operating system that works on top of them. In this way, the general-purpose modules define an interface that the specialized modules must implement so that they can be properly called by the high-level modules.

Limit the number of special cases (and avoid long if statements) by designing the normal case in a way that automatically handles the edge cases without any extra code.

Systems are typically composed of multiple layers, where each layer has its own abstraction. When the layers all have the same/similar abstraction, that is typically a red flag of Class Decomposition.

In such a case, these methods are called pass-through methods since they do nothing other than passing through its arguments to some other method and calling it. In other words, there is little significance and value for such a method. They make classes shallower, increase interface complexity, but don't increase the total functionality of the system. They can also create dependencies between classes. They usually indicate a confusion of division of responsibility between classes.

Interface to a piece of functionality should typically be within the same class that implements the functionality.
calling

It's fine to have the same signature as long as the method actually adds some new functionality.

The implementation of a class should ideally be deeper than its interface and the abstraction be higher. This results in a deeper class.

A similar issue is the idea of pass-through variables, which are variables that are passed through a long chain of methods. They increase complexity and create dependence between modules. While there are multiple solutions, one of the simplest and most elegant ones is creating a context object that stores all of the pass-through variables and the application's global state. Every object holds the reference to this object and thus can use it. They should ideally be immutable. While it works, it is not an ideal solution.

Usually, it's better for a module to have a simpler interface than a simple implementation. Make the module as simple as possible for the users of the module rather than the developers. In this way, you're pulling the complexity downwards.

The act of subdivision of a larger component into a bunch of smaller components can create additional complexity, and thus, is not always the right move forward.
1) More components -> more complexity.
2) Additional code to manage the new components.
3) Separates components that may be related.
4) Can result in duplication.

Similarly, combining modules into one is best done when they are related.
1) When they are related.
2) They are used together; they are related bidirectionally.
3) They overlap conceptually.
4) It's hard to understand one component without the other.

Combining:
1) If the information is shared.
2) If it will simplify the interface.
3) If it will eliminate duplication.
4) Separate general-purpose and special-purpose code.

Repetition - if the same piece of code appears again and again, that's a red flag that you haven't found the right abstraction.

Each method should do one thing and do it completely. If it cannot be understood without understanding another method, that is a red flag. It should be deep, but have a simple interface. The two potential ways to split a method are
1) Create a helper method that implements the subtask of the parent method, and the parent method calls the child method. The parent and child method are relatively independent, and the child method should ideally be general-purpose for the subtask it solves.
2) Less than ideal is to divide a method into several methods that are then called. Ideally, the sum of the interfaces of these methods should be simpler than their combined method interface. This approach can end up adding complexity instead especially if the parent method ends up invoking all of these new methods.

Exceptions, any uncommon condition that alters the normal flow of control in a program, contributes to complexity. Exception handling code can also result in more exceptions. They make the interfaces more complex, and the module more shallow compared to a module with fewer exceptions.

Rather than writing an excessive number of exception handling code, try to figure out a clean way to handle the exceptions in your normal code without resorting to exception handling. Best way to reduce the complexity damage is by reducing the number of places where exceptions are handled. 

Ways to deal with exceptions:
1) Define errors out of existence.
2) Masking exceptions - exception is detected and handled at a low level of the system, so that the high levels don't even see the exception. It results in deeper modules, adds functionality, and pulls complexity downwards.
3) Exception aggregation - handle multiple exceptions in one place with a single piece of code.
4) Crash the application.

Don't take this too far by ignoring all exceptions. Exceptions may be needed in certain cases and have a place to stay.

It is better to design a system twice first before diving straight into implementing it as your first design try is unlikely to be the best design. Consider multiple different designs, their strengths and weaknesses, compare them to each other, and figure out which one is the best fit for your system. Sometimes you may be able to combine the pros of different designs into one new design. This will pay off in the long run.

Comments play a big role in abstraction by hiding complexity and improving the system's design. They also improve the maintainability of the system. They capture the information that was in the mind of the designer that could not be captured in code. It helps resolve the cognitive load and unknown unknowns.

Comments should describe things that aren't obvious from the code. Don't repeat the code.

One should always comment the interface declarations for modules and variables. Interface comments ought to be separated and different from implementation comments.

Implementation comments should describe the what the code is doing and why the code is doing it/implemented this way. They shouldn't describe how the code does it; that should be done through code.

For cross-module comments, one option is to have a central document listing the comments of all cross-modules, and in each one of the related modules, just write "See Document X for details".

Commenting conventions are good insofar as they make you write comments and makes sure that the comments are consistent.

Good names are a form of documentation, make code easier to understand, reduce complexity, make errors easier to detect, prevent bugs and ambiguities.

Names should create an image that is as close as possible to what it is and what it represents. Name should tell what the thing is about even before the developer sees the documentation or implementation.

Good names should be precise and consistent.

If the thing is used in a small scope and implementation can be easily seen, then it's okay if the name is not fully precise, like for for loops names can be i, j.

If it's hard to pick out a simple, but precise and consistent name for a thing, then that's a red flag that the thing does not have a clean design.

Keep names consistent so that things used in different places for the same purpose have the same name. This reduces cognitive load.

By writing comments first before the code, you make the documentation a part of the design process. This results in better documentation and design. It also makes the process of documentation more enjoyable.

Just like when first implementing, use a strategic approach when modifying/extending code as well. Always look for ways to improve the system design even if by a little. Don't take shortcuts.

To make sure comments don't go stale when the code is updated, keep the relevant comments as close to the code as possible so that the developer is more likely to update the comments as well.

In languages like C/C++ that have header files too, it's better to keep comments in whichever file you expect the user/developer to reference when using your code. Since modification includes changing the implementation code, it's usually better to keep the comments with the implementation declaration rather than in the header files, which are not always referenced by developers. But generally, place the comments where it is most convenient for the developers.

If the comment is too long, it may be worthwhile to break it down into parts which are then put into their respective positions where they are implemented in the module itself. And then on top of the module, you can write a summary that references these parts.

When writing comments, avoid duplications and write each design decision only once. So that if the code is modified, you only have to modify a single comment instead going through the project modifying a bunch of them. Alternatively, you can put the comment in the designNotes file or have a master comment in one place, and children comments that reference the comment in other relevant places (e.g. See comment X for information). If the information is documented externally, reference the external documentation instead of creating a duplicate internal documentation.

Comments are easier to maintain if they are higher-level and more abstract than the code.

Be consistent. Create a document that lists the conventions or list them as comments. Enforce these conventions with a tool or talk about them in code reviews.

Software should be designed for ease of reading, not ease of writing.

Incremental development is fine as long as the increments are abstractions, not features.

When you encounter a bug, write a (unit) test that simulates that bug so that you can properly verify that the bug is fixed with a code change.

Keep your priorities straight.

[^1]: [A Philosophy of Software Design](zotero://open-pdf/library/items/283RR677?page=1)