---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Multiple Issue[^1]
> A technique for exploiting [[Instruction-Level Parallelism]] by replicating a processor's internal components so that several instructions are launched in a single clock cycle, potentially driving the CPI below 1 or, equivalently, letting the instruction execution rate exceed the clock rate. The set of instructions issued together in one clock cycle is called an issue packet, occupying that cycle's issue slots.

# Types
- Static multiple issue — the compiler makes most decisions about which instructions to co-issue before execution; a Very Long Instruction Word (VLIW) architecture takes this furthest by encoding an entire issue packet, with several independent operations and their own opcode fields, as a single wide instruction.
- Dynamic multiple issue (superscalar) — the processor decides during execution which instructions to issue together, allowing it to execute more than one instruction per clock cycle without relying solely on the compiler's schedule; see [[Dynamic Pipeline Scheduling]].

# Properties
- Every multiple-issue design must both decide how instructions are grouped into issue packets and handle the data and control hazards that arise between simultaneously issued instructions.
- Static and dynamic multiple issue are not perfectly pure alternatives in practice: real designs often borrow techniques from both.
- Doubling issue width can in principle double performance, but requires overlapping twice as many instructions, which raises the relative performance cost of any remaining data and control hazards.
- [[Loop Unrolling]] and [[Register Renaming]] are compiler and hardware techniques, respectively, for supplying multiple-issue hardware with enough independent work to keep its issue slots full.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=355&annotation=ZA4PYAL5)
