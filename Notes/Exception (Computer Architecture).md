---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Exception (Interrupt)[^1]
> An unscheduled event that disrupts normal program execution, functioning essentially as an unscheduled procedure call: the address of the offending instruction is saved, and the processor jumps to a predefined address to run the appropriate handler routine. Some architectures reserve the term interrupt for exceptions that come from outside the processor, while others use it for all exceptions.

# Properties
- Used to detect [[Arithmetic Overflow]] and other unscheduled events requiring the processor's attention.
- MIPS saves the address of the interrupted instruction in a dedicated exception program counter (EPC) register; software copies EPC into a general-purpose register (`mfc0`) so it can resume the interrupted instruction via a register-indirect jump once corrective code has run.
- Since an exception acts as an unscheduled call to a handler, MIPS software reserves two registers exclusively for the [[Operating System|operating system]] exception handler, which are not otherwise saved or restored on an exception, avoiding the chicken-and-egg problem of needing registers to save registers.
- Under a vectored interrupt scheme, the handler address to which control transfers is determined directly by the cause of the exception, rather than every exception jumping to one shared handler that must then determine the cause itself.
- In a pipelined processor, an exception is handled as a form of [[Control Hazard]]: the offending instruction's control signals are deasserted and later pipeline stages are flushed, much as for a mispredicted branch. A precise interrupt (precise exception) is always associated with the correct instruction despite several instructions being in flight simultaneously; an imprecise interrupt (imprecise exception) is not, which simplifies the hardware but complicates the exception handler.
- Because the operating system is briefly vulnerable while it is still saving process state, the processor first sets an exception-enable (interrupt-enable) bit that suppresses further exceptions until enough state — at minimum the EPC and a cause register — has been saved to allow recovery even if a second exception arrives; the OS then re-enables exceptions once that minimal state is safe. A restartable instruction is one that can resume after its exception is resolved without the exception affecting the instruction's own result, which a [[Page Table|page fault]] handler relies on to transparently retry the faulting access once the needed page has been brought into memory.
- The software routine invoked to service an exception is called its handler; a portion of the address space can be marked unmapped, meaning it is guaranteed never to raise a page fault.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=203&annotation=EKJCS2B4)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=350&annotation=2ZQ3SJ4C)
[^3]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=470&annotation=9DZCDU6Q)
