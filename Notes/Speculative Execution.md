---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Speculative Execution (Performance via Prediction)[^1]
> In some cases it is faster on average to guess and start working rather than to wait until an answer is known for sure, provided the mechanism to recover from a misprediction is not too expensive and the prediction is relatively accurate.

# Properties
- One of the [[Great Ideas in Computer Architecture]].
- Distinct from statistical [[Prediction]], which estimates an unknown output from data rather than guessing a hardware control decision to avoid stalling execution.
- Trades the cost of an occasional misprediction recovery against the average-case speedup gained by not waiting.
- May be performed by the compiler or by the hardware to expose more [[Instruction-Level Parallelism]] for [[Multiple Issue|multiple-issue]] execution. Software speculation has the compiler insert extra instructions that check the guess and run a fix-up routine if it was wrong; hardware speculation instead buffers speculative results and either commits them once the guess is confirmed or flushes them and re-executes the correct instructions if it was wrong.
- Speculating on an instruction can expose an exception that would not otherwise occur; compiler-based speculation suppresses such exceptions until it is clear they should really occur, while hardware-based speculation buffers them until the causing instruction is no longer speculative.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=35&annotation=WHW4MFU4)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=356&annotation=QAJ77Z7P)
