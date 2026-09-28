---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Turing Machine[^1]
> An idealised model of a human computing with pencil and paper, consisting of:
> - a finite set of *m-configurations* (internal states) $q_1, q_2, \dots, q_R$;
> - an unbounded *tape* divided into *squares*, each bearing at most one symbol;
> - a *scanned square*, the $r$-th, whose symbol $\mathfrak{S}(r)$ is the only one the machine is "directly aware" of.
>
> The pair $(q_n, \mathfrak{S}(r))$ is the *configuration*, which determines the machine's possible behaviour: in each step it may write a symbol on a blank scanned square or erase the scanned symbol, shift the scanned square one place left or right, and change its m-configuration.

# Types
- *Automatic machine* (a-machine) - a machine whose motion at every stage is completely determined by its configuration (the modern deterministic Turing machine).[^2]
- *Computing machine* - an a-machine printing two kinds of symbols: *figures* ($0$ and $1$) and symbols of the second kind (scratch work). Started on a blank tape in the correct initial m-configuration, the subsequence of figures it prints is the *sequence computed by the machine*, and the real number whose binary expansion is that sequence after a binary point is the *number computed by the machine*.[^3]
	- *Circular* - prints only finitely many figures.
	- *Circle-free* - prints infinitely many figures.[^4]
- [[Universal Turing Machine]] - a single machine that can compute any computable sequence.

# Properties
- Memory beyond the scanned symbol is only possible by altering the m-configuration, so the machine can "remember" some previously scanned symbols.[^1]
- Defines [[Computable Number|computable numbers]] and hence gives a precise characterisation of [[Computability|computability]].
- The finitely many m-configurations mirror the finitely many states of mind of a human computer.
- Introduced in [[On Computable Numbers (Turing)]].

[^1]: [Turing, 1936, p. 231](zotero://open-pdf/library/items/JN7TDAA3?page=2&annotation=A9V753DM); [Turing, 1936, p. 231](zotero://open-pdf/library/items/JN7TDAA3?page=2&annotation=DTVWIQA7); [Turing, 1936, p. 232](zotero://open-pdf/library/items/JN7TDAA3?page=3&annotation=652Z6Z5B)
[^2]: [Turing, 1936, p. 232](zotero://open-pdf/library/items/JN7TDAA3?page=3&annotation=5GP425UW)
[^3]: [Turing, 1936, p. 232](zotero://open-pdf/library/items/JN7TDAA3?page=3&annotation=GCEHJ98K)
[^4]: [Turing, 1936, p. 233](zotero://open-pdf/library/items/JN7TDAA3?page=4&annotation=Y25QCBUF)
