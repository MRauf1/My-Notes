---
tags:
  - mathematics
  - miscellaneous
---

# Definition
> [!info] Structured Proof[^1]
> (Lamport) A hierarchically structured [[Proof|proof]] style, a refinement of natural deduction, in which every step is given a name by which it is referred to, and the logical structure of the proof is made manifest: each step is justified by a lower-level sub-proof, down to short, completely transparent paragraph-style proofs at the lowest level.

# Properties
- Motivation: proofs have been written as essays in stilted prose for 300 years (Newton's *Principia* differs from a modern textbook only in being in Latin). Just as formulas become readable when variables are named and structure is explicit, proofs become readable when steps are named and structure is manifest.[^1]
- Readers who want only the outline read the high level and descend into as much detail as they like; until one is used to them, structured proofs look intimidating.[^2]
- Rewriting correct theorems' conventional proofs in structured form revealed serious mistakes in almost all of them, and attempts to structure blackboard proof sketches repeatedly revealed that conjectures were false; incorrect proofs do lead to incorrect theorems.[^3]
- Because every use of a hypothesis or step is explicit, text search reveals exactly where each hypothesis is used, which helps when deriving variants of a theorem (e.g. with weaker hypotheses).[^4]
- Format alone does not eliminate errors: most errors come from not expanding the proof to enough levels. Rule of thumb: expand until the lowest-level statements are obvious, then one more level. Unlike prose, structure accommodates arbitrary detail without confusion.[^5]
- Longer than conventional proofs, mainly because of more detail; they make omissions obvious and sloppiness hard ("this case is similar to the previous one" is not allowed, forcing a general step covering both). Shorter is not better: "the shortest proof is always 'left as an exercise for the reader'."[^6]
- For publication, provide a fully detailed version (for oneself, referees, colleagues) and a compressed one obtained by collapsing lower levels into paragraphs, which is still better than unstructured proofs where details seem randomly chosen.[^7]
- Close in spirit to machine-checked proofs in a [[Formal Proof Assistant]], and a counterpoint to reliance on [[Smell (Mathematics)|smell]]; see also [[Mathematical Writing]].
- *Creator's note*: conventional proofs are shorter, and deciphering their skipped steps can itself train one's proof-writing and reasoning ([[How to Write a Proof (Lamport)]]).

[^1]: [Lamport, p. 1](zotero://open-pdf/library/items/P7KZECMR?page=7&annotation=J4DU4UVY); [Lamport, p. 1](zotero://open-pdf/library/items/P7KZECMR?page=7&annotation=7YVUP898); [Lamport, p. 1](zotero://open-pdf/library/items/P7KZECMR?page=7&annotation=YKLT2VP8); [Lamport, p. 1](zotero://open-pdf/library/items/P7KZECMR?page=7&annotation=M7XKZFZ7); [Lamport, p. 1](zotero://open-pdf/library/items/P7KZECMR?page=7&annotation=CNNNKBEN)
[^2]: [Lamport, p. 2](zotero://open-pdf/library/items/P7KZECMR?page=8&annotation=GWSQUP4P)
[^3]: [Lamport, p. 9](zotero://open-pdf/library/items/P7KZECMR?page=15&annotation=NBZVT69K)
[^4]: [Lamport, p. 9](zotero://open-pdf/library/items/P7KZECMR?page=15&annotation=T3J5IWW5)
[^5]: [Lamport, p. 10](zotero://open-pdf/library/items/P7KZECMR?page=16&annotation=XT23D5ZV)
[^6]: [Lamport, p. 10](zotero://open-pdf/library/items/P7KZECMR?page=16&annotation=KRLPWIE4)
[^7]: [Lamport, p. 10](zotero://open-pdf/library/items/P7KZECMR?page=16&annotation=TGDVSTBT)
