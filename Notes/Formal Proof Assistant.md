---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Formal Proof Assistant[^1]
> Software (such as Lean or Rocq) that automatically checks the validity of a mathematical argument written in a precise formal computer language, certifying that each step is a correct application of the underlying axioms and inference rules.

# Properties
- Realises in practice mathematics' in-principle ability to reach consensus on validity by checking every step, and so can greatly reduce reliance on [[Smell (Mathematics)|smell]] and on careful human review.[^1]
- Limitations:[^2]
	- Formal verification only certifies that a formalised argument establishes a *formal* statement; it does not rule out errors in translating between the formal statement and the intended one, so human review is reduced but not eliminated.
	- Mathematics could even be "hacked" by subtly manipulating the formalisation of key definitions in standard libraries such as Mathlib.
	- Only part of an argument is deductive and formalisable; around the deductive core lies a penumbra of [[Heuristic|heuristic]], empirical, and metamathematical reasoning explaining why the argument works, whether it extends, why the question matters, and how to reconstruct it from basic principles.
- Advances in auto-formalisation make it easier to study how an argument depends on choices of foundations, allowing the metamathematics of a result to be explored rigorously alongside the result itself.[^3]
- Pairs naturally with AI proof generation in [[AI-Assisted Mathematics]].

[^1]: [Klowden and Tao, 2026, p. 8](zotero://open-pdf/library/items/D49IZRQS?page=8&annotation=G2NPYJUG); [Klowden and Tao, 2026, p. 7](zotero://open-pdf/library/items/D49IZRQS?page=7&annotation=P2Z67UDY)
[^2]: [Klowden and Tao, 2026, p. 9](zotero://open-pdf/library/items/D49IZRQS?page=9&annotation=272796FP); [Klowden and Tao, 2026, p. 9](zotero://open-pdf/library/items/D49IZRQS?page=9&annotation=RPN55R7N); [Klowden and Tao, 2026, p. 9](zotero://open-pdf/library/items/D49IZRQS?page=9&annotation=YQZK2HF9); [Klowden and Tao, 2026, p. 9](zotero://open-pdf/library/items/D49IZRQS?page=9&annotation=3EPVFKYJ)
[^3]: [Klowden and Tao, 2026, p. 10](zotero://open-pdf/library/items/D49IZRQS?page=10&annotation=RD23DUSQ); [Klowden and Tao, 2026, p. 11](zotero://open-pdf/library/items/D49IZRQS?page=11&annotation=B44P9X8C)
