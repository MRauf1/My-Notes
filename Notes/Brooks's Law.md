---
tags:
  - computer_science
  - software_engineering
---

# Definition
> [!info] Brooks's Law[^1]
> "Adding manpower to a late software project makes it later" (Fred Brooks, *The Mythical Man-Month*, 1975).

# Properties
- **Mechanisms.**
	- *Ramp-up*: new people need time to become productive, and they take time from experienced members who must train them.
	- *Communication overhead*: with $n$ people there are $\binom{n}{2} = \frac{n(n-1)}{2}$ possible communication channels, so coordination cost grows quadratically while added capacity grows only linearly.
	- *Limited divisibility*: some tasks cannot be partitioned. "Nine women can't make a baby in one month."
- **Evidence and caveats.** Brooks himself called it an "outrageous simplification". A system-dynamics simulation found that adding staff late always raised cost but did not always delay delivery. Small, early additions of experienced people can help (Abdel-Hamid, 1988). Empirically, larger teams have lower per-person productivity.
- **Related limits on parallel speedup.** Compare [[Amdahl's Law]], where the serial fraction caps parallel speedup, and [[Work-in-Progress Limit]].
- Pausch got a lifelong mentor in Brooks simply by asking for 30 minutes of his time.[^1] See [[Underestimation of Compliance]].

[^1]: [Pausch, 2008, p. 138](zotero://open-pdf/library/items/8CZDD8BA?page=138&annotation=P2W2XW8T); [p. 138](zotero://open-pdf/library/items/8CZDD8BA?page=138&annotation=TA3CUIE6)
