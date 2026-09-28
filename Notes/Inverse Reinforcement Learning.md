---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Inverse Reinforcement Learning[^1]
> The inverse of [[Reinforcement Learning|reinforcement learning]]: rather than asking "given a reward signal, what behaviour optimises it?", IRL asks "given observed behaviour, what reward signal, if any, is being optimised?", so that machines infer human values by observing us.

# Properties
- Motivated by human infants, who by 18 months identify others' goals and obstacles and spontaneously help without reward; humans are "the world's experts at mind reading", inferring what others want by age one, before what they think (about four).[^2]
- IRL is *ill-posed*: large families of reward functions are behaviourally indistinguishable, though this ambiguity rarely matters since behaviour is unchanged.[^3]
- Can surpass imperfect demonstrators: if an expert's attempts are imperfect in different ways each time, IRL can infer the intended manoeuvre (e.g. helicopter aerobatics).[^4]
- *Maximum-entropy IRL* (Ziebart et al.) models the expert as noisily rational, more likely to take actions the more reward they bring, and picks the reward maximising the likelihood of the demonstrations while remaining maximally uncertain otherwise:
$$\begin{align}
P(\tau \mid \theta) = \frac{\exp\!\left(\theta^\top \mathbf{f}_\tau\right)}{Z(\theta)}
\end{align}$$
where $\mathbf{f}_\tau$ are trajectory features. It could predict drivers' routes and infer intended destinations from partial routes.[^5]
- Typical IRL requires an expert who can demonstrate; learning from human *preferences* instead lets non-demonstrators teach behaviours they can only recognise (e.g. a simulated backflip), each person imparting their own aesthetic.[^6]
- Extended to cooperation in [[Cooperative Inverse Reinforcement Learning]] and to instructions in [[Inverse Reward Design]].

[^1]: [Christian, 2021, p. 251](zotero://open-pdf/library/items/P27SWKW4?page=251&annotation=SJJQJ6QG); [Christian, 2021, p. 253](zotero://open-pdf/library/items/P27SWKW4?page=253&annotation=P79F7ELQ)
[^2]: [Christian, 2021, p. 249](zotero://open-pdf/library/items/P27SWKW4?page=249&annotation=YXHSYC5D); [Christian, 2021, p. 250](zotero://open-pdf/library/items/P27SWKW4?page=250&annotation=TVAPIUXV); [Christian, 2021, p. 250](zotero://open-pdf/library/items/P27SWKW4?page=250&annotation=PNN9Z845); [Christian, 2021, p. 250](zotero://open-pdf/library/items/P27SWKW4?page=250&annotation=A2AD6D9R)
[^3]: [Christian, 2021, p. 254](zotero://open-pdf/library/items/P27SWKW4?page=254&annotation=H8J2EMT9)
[^4]: [Christian, 2021, p. 257](zotero://open-pdf/library/items/P27SWKW4?page=257&annotation=8DK292YB)
[^5]: [Christian, 2021, p. 258](zotero://open-pdf/library/items/P27SWKW4?page=258&annotation=Y824EQXS); [Christian, 2021, p. 259](zotero://open-pdf/library/items/P27SWKW4?page=259&annotation=YVM278D9)
[^6]: [Christian, 2021, p. 259](zotero://open-pdf/library/items/P27SWKW4?page=259&annotation=JW76HP75); [Christian, 2021, p. 264](zotero://open-pdf/library/items/P27SWKW4?page=264&annotation=KW8MDDCU)
