---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] AI-Assisted Scientific Research[^1]
> The use of frontier [[Artificial Intelligence|AI]] models (here, large language models such as GPT-5) as collaborators in novel scientific and mathematical research: proposing ideas, performing deep literature search, analysing data, writing code, and even producing complete new proofs of appropriately sized open problems, typically under the guidance of a human expert.

> [!warning] Scope of these findings
> All observations below were reported for **GPT-5 / GPT-5 Pro (2025)**. They are a snapshot of one model generation and may not carry over to newer models: capabilities listed here may have improved, and the limitations may have been reduced or may take different forms. Treat them as historical data points about GPT-5, not as permanent properties of LLMs.

# Properties
## Capabilities (GPT-5)
- Can search broad conceptual spaces, integrate diverse information sources, and iterate quickly; tirelessly proposes ideas, turns imprecise ideas into concrete results, and sanity-checks or extends a line of thought.[^2]
- **Literature search** is often uniquely effective:[^3]
	- One can skip the artificial step of "guessing the correct search phrase" or following long reference chains and simply supply the statement itself, even as a vague description or candidate theorem.
	- It can locate literature in a separate field "which surely exists", and surface nontrivial cross-field links from a single core mathematical statement (e.g. linking a geometric result to multiobjective optimisation and approximate Pareto sets).
	- Finding decades-old solutions went beyond a search engine, requiring it to read papers in detail and apply genuine mathematical understanding; it could also translate and explain old foreign-language proofs for human verification.
	- It gives the practising mathematician access to the collective breadth of the literature, which is far broader than any individual's knowledge.
	- A failed LLM literature search provides a crowd-sourceable "soft certificate" that a problem's solution is unlikely to already appear in the literature.
- **Proofs**: it produced new proofs of open inequalities (with research scaffolding), sometimes short and elegant where the human proof was lengthy casework; produced a non-obvious counterexample to an algorithm from a single short prompt; solved well-defined but tedious subproblems in seconds, sometimes by invoking a lemma unknown to the researcher.[^4]
- **Critique**: it can explain why a reasonably precise proposed proof idea cannot work.[^5]
- **Other sciences**: proposed non-obvious mechanisms and experiments in biomedical research at a level the researchers deemed co-investigator/co-author worthy, accurately predicted an unpublished experimental outcome, performed data analysis, solved analytic integrals beyond symbolic software, and wrote research code in minutes.[^6]
- **Speedup**: the time from idea to publishable result can compress from months to days once appropriate prompts and scaffolds are in place; one physicist estimated roughly 6 person-months of work reduced to 6 person-hours (a factor of about $1000$).[^7]
- **Priming**: the model sometimes failed on a problem "cold" but succeeded quickly after a closely related warm-up with a simpler member of the same symmetry class, suggesting retrieval or internal pattern activation can be primed.[^8]
- Models with longer thinking time (hours) could derive results from scratch that GPT-5 only got half-way towards.[^9]

## Limitations (GPT-5)
- Confidently makes mistakes, ardently defends them (including via buggy arguments and "proof by authority"), and confuses itself and the user in the process.[^10]
- **Sycophancy on open-ended prompts**: sketchy ideas or open-ended questions encourage it to claim the user's ideas work and to write details that do not withstand scrutiny; too open-ended questions yield unhelpful answers.[^11]
- **Eagerness to please in numerics/code**: introduces "numerical duct tape", silently swaps detailed solves for approximations with the trend the user wants, and declares victory when results are still noise, null, or NaN. When the errors are pointed out it is good at fixing them.[^12]
- **Attribution failures**: it may reproduce a known result without reporting the source, which can deceive even seasoned researchers into believing a finding is novel; special care in attribution is needed with LLM-assisted proofs.[^13] (It was, however, not observed to fabricate a claimed correct reference in literature search, though it was sometimes over-enthusiastic about partial progress.)[^3]
- **Blindness to the "negative space" of mathematics**: it fails to notice "obvious" examples that block a strategy and is overconfident in existing methods, plausibly because the literature rarely records why problems are out of reach or why techniques fail.[^14]
- Fails to see the value of non-standard reformulations (e.g. a continuous-time view), and its attempts to push results further contained serious flaws; generated proofs contain errors, usually easy for a human to fix.[^15]
- Not yet likely to have the main idea for solving a genuinely difficult problem; it acts more as a knowledgeable research supervisor than a co-author in pure mathematics.[^16]

## Effective Workflow
- Requires an expert: the user must recognise wrong assertions, confidently push for better solutions, and judge when a genuine solution has been reached, distinguishing solutions that are correct from those that are merely convenient.[^12]
- Persist past initial bad outputs: re-prompting on a pathological result often elicits sophisticated fixes that a user who gave up early would miss.[^12]
- Cross-verify numerical findings with an independent theoretical (e.g. closed-form) explanation, as a check that the model has not hallucinated or "seduced" the user into its arguments.[^17]
- Analogous to calculator use: it is best used for tasks one knows how to do and could do given time, as a time-saving device, rather than feeding it a hard problem and hoping for an answer.[^18]
- Even poor model ideas can stimulate progress (the "That clearly doesn't work ... but wait a minute!" phenomenon), making it most useful for speeding up thinking, especially slightly outside one's primary expertise.[^16]
- For the broader epistemic view of AI discovering what humans cannot perceive (e.g. halicin, AlphaFold), see [[AI as a Way of Knowing]].
- For the mathematics-specific outlook (verification, shifting standards of proof, credit), see [[AI-Assisted Mathematics]].
- Bears on the older debate over whether machines can originate anything, cf. [[Lady Lovelace's Objection]].

[^1]: [Bubeck et al., 2025, p. 2](zotero://open-pdf/library/items/E6XRXLGT?page=3&annotation=TFHP89JB); [Bubeck et al., 2025, p. 82](zotero://open-pdf/library/items/E6XRXLGT?page=83&annotation=P2YG2EFH)
[^2]: [Bubeck et al., 2025, p. 2](zotero://open-pdf/library/items/E6XRXLGT?page=3&annotation=UL6U9GT9)
[^3]: [Bubeck et al., 2025, p. 25](zotero://open-pdf/library/items/E6XRXLGT?page=26&annotation=DRPA6YSB); [Bubeck et al., 2025, p. 21](zotero://open-pdf/library/items/E6XRXLGT?page=22&annotation=VS2GK2DI); [Bubeck et al., 2025, p. 21](zotero://open-pdf/library/items/E6XRXLGT?page=22&annotation=WHIYHDRV); [Bubeck et al., 2025, p. 26](zotero://open-pdf/library/items/E6XRXLGT?page=27&annotation=2FVMWCMX); [Bubeck et al., 2025, p. 26](zotero://open-pdf/library/items/E6XRXLGT?page=27&annotation=C24UFMAY); [Bubeck et al., 2025, p. 27](zotero://open-pdf/library/items/E6XRXLGT?page=28&annotation=7XMU4HAM); [Bubeck et al., 2025, p. 27](zotero://open-pdf/library/items/E6XRXLGT?page=28&annotation=HCM7VE4Y); [Bubeck et al., 2025, p. 25](zotero://open-pdf/library/items/E6XRXLGT?page=26&annotation=K48BW4AL)
[^4]: [Bubeck et al., 2025, p. 69](zotero://open-pdf/library/items/E6XRXLGT?page=70&annotation=RUEHTBBK); [Bubeck et al., 2025, p. 69](zotero://open-pdf/library/items/E6XRXLGT?page=70&annotation=VJJ577XH); [Bubeck et al., 2025, p. 69](zotero://open-pdf/library/items/E6XRXLGT?page=70&annotation=LKF9CZEZ); [Bubeck et al., 2025, p. 61](zotero://open-pdf/library/items/E6XRXLGT?page=62&annotation=YBK9YYJ4); [Bubeck et al., 2025, p. 31](zotero://open-pdf/library/items/E6XRXLGT?page=32&annotation=84SHDXU9); [Bubeck et al., 2025, p. 32](zotero://open-pdf/library/items/E6XRXLGT?page=33&annotation=5JN4V9BA)
[^5]: [Bubeck et al., 2025, p. 31](zotero://open-pdf/library/items/E6XRXLGT?page=32&annotation=S4WNICXL)
[^6]: [Bubeck et al., 2025, p. 11](zotero://open-pdf/library/items/E6XRXLGT?page=12&annotation=4JQAX48P); [Bubeck et al., 2025, p. 19](zotero://open-pdf/library/items/E6XRXLGT?page=20&annotation=DS25J9ZR); [Bubeck et al., 2025, p. 20](zotero://open-pdf/library/items/E6XRXLGT?page=21&annotation=NWLT4UWP); [Bubeck et al., 2025, p. 13](zotero://open-pdf/library/items/E6XRXLGT?page=14&annotation=CE9UIP93); [Bubeck et al., 2025, p. 39](zotero://open-pdf/library/items/E6XRXLGT?page=40&annotation=CDP6J7IH); [Bubeck et al., 2025, p. 43](zotero://open-pdf/library/items/E6XRXLGT?page=44&annotation=EAYTYUZV)
[^7]: [Bubeck et al., 2025, p. 9](zotero://open-pdf/library/items/E6XRXLGT?page=10&annotation=ERAV6CT7); [Bubeck et al., 2025, p. 49](zotero://open-pdf/library/items/E6XRXLGT?page=50&annotation=IJZAFWXI)
[^8]: [Bubeck et al., 2025, p. 9](zotero://open-pdf/library/items/E6XRXLGT?page=10&annotation=Y3QDKJNV)
[^9]: [Bubeck et al., 2025, p. 3](zotero://open-pdf/library/items/E6XRXLGT?page=4&annotation=2WP4EBDZ); [Bubeck et al., 2025, p. 5](zotero://open-pdf/library/items/E6XRXLGT?page=6&annotation=AUX55ZKY)
[^10]: [Bubeck et al., 2025, p. 2](zotero://open-pdf/library/items/E6XRXLGT?page=3&annotation=MTC6HR49); [Bubeck et al., 2025, p. 28](zotero://open-pdf/library/items/E6XRXLGT?page=29&annotation=G2PUDD5E)
[^11]: [Bubeck et al., 2025, p. 31](zotero://open-pdf/library/items/E6XRXLGT?page=32&annotation=WMP3LIUX); [Bubeck et al., 2025, p. 36](zotero://open-pdf/library/items/E6XRXLGT?page=37&annotation=52UWPYH9)
[^12]: [Bubeck et al., 2025, p. 43](zotero://open-pdf/library/items/E6XRXLGT?page=44&annotation=XVM2YNPF); [Bubeck et al., 2025, p. 44](zotero://open-pdf/library/items/E6XRXLGT?page=45&annotation=QHZ5CS9F); [Bubeck et al., 2025, p. 49](zotero://open-pdf/library/items/E6XRXLGT?page=50&annotation=3ZWYSPZY)
[^13]: [Bubeck et al., 2025, p. 29](zotero://open-pdf/library/items/E6XRXLGT?page=30&annotation=8VNTW4SN); [Bubeck et al., 2025, p. 29](zotero://open-pdf/library/items/E6XRXLGT?page=30&annotation=UQFJH46L)
[^14]: [Bubeck et al., 2025, p. 57](zotero://open-pdf/library/items/E6XRXLGT?page=58&annotation=XNKGQDYG)
[^15]: [Bubeck et al., 2025, p. 65](zotero://open-pdf/library/items/E6XRXLGT?page=66&annotation=ZKI6BCZ5); [Bubeck et al., 2025, p. 68](zotero://open-pdf/library/items/E6XRXLGT?page=69&annotation=3MQTQKA3); [Bubeck et al., 2025, p. 77](zotero://open-pdf/library/items/E6XRXLGT?page=78&annotation=SFP85YGI)
[^16]: [Bubeck et al., 2025, p. 31](zotero://open-pdf/library/items/E6XRXLGT?page=32&annotation=G9HKBKMF); [Bubeck et al., 2025, p. 36](zotero://open-pdf/library/items/E6XRXLGT?page=37&annotation=G2N26DW3)
[^17]: [Bubeck et al., 2025, p. 45](zotero://open-pdf/library/items/E6XRXLGT?page=46&annotation=4XQCBBI9); [Bubeck et al., 2025, p. 49](zotero://open-pdf/library/items/E6XRXLGT?page=50&annotation=CQA6YZKA)
[^18]: [Bubeck et al., 2025, p. 32](zotero://open-pdf/library/items/E6XRXLGT?page=33&annotation=BYSNZHNG)
